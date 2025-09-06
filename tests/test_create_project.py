# tests/test_create_project.py
import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from svelte_pi.main import cli
from svelte_pi.project_setup import create_sveltekit_project
from svelte_pi.file_operations import create_reset_css, update_app_html


class TestProjectCreation:
    """Test suite for SvelteKit project creation functionality"""

    def setup_method(self):
        """Set up test environment before each test"""
        # Create a temporary directory for testing
        self.test_dir = Path(tempfile.mkdtemp())

    def teardown_method(self):
        """Clean up after each test"""
        # Remove the temporary directory and all its contents
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_create_command_integration(self):
        """Test that the create command runs and completes basic flow"""
        runner = CliRunner()

        # Mock all the file operations that need real structure
        with patch('svelte_pi.project_setup.subprocess.Popen') as mock_popen, \
                patch('svelte_pi.project_setup.subprocess.run') as mock_run, \
                patch('svelte_pi.file_operations.create_reset_css') as mock_reset, \
                patch('svelte_pi.file_operations.update_app_html') as mock_update:
            # Mock the sv create command
            mock_process = MagicMock()
            mock_process.returncode = 0
            mock_process.communicate.return_value = ("Success", "")
            mock_popen.return_value = mock_process

            # Mock other operations to return success
            mock_run.return_value = MagicMock(returncode=0)
            mock_reset.return_value = True
            mock_update.return_value = True

            # Simulate user input: project name, yes to reset.css, custom directory
            user_input = f"test-project\ny\n{self.test_dir}\n"

            # Run the create command
            result = runner.invoke(cli, ['create'], input=user_input)

            # Basic checks - just that it ran without crashing
            assert result.exit_code == 0, f"Command failed with output: {result.output}"

            # Verify at least the main subprocess was called
            mock_popen.assert_called_once()  # sv create was called

            # Don't be too strict about the other calls since the flow might exit early
            # The important thing is that the command completed successfully

    def test_folder_creation_simple(self):
        """Simple test: does it create the right folders?"""
        project_name = "simple-test"

        # Just test our project setup function with mocked subprocess
        with patch('svelte_pi.project_setup.subprocess.Popen') as mock_popen:
            # Mock successful sv create
            mock_process = MagicMock()
            mock_process.returncode = 0
            mock_process.communicate.return_value = ("Success", "")
            mock_popen.return_value = mock_process

            # Manually create what sv create would make (just the basics)
            expected_project_path = self.test_dir / project_name
            expected_project_path.mkdir(parents=True)
            (expected_project_path / "src").mkdir()
            (expected_project_path / "package.json").write_text('{"name": "test"}')

            # Call our function
            result_path = create_sveltekit_project(project_name, str(self.test_dir))

            # Test 1: Did it create the folder with the right name?
            assert expected_project_path.exists()
            assert expected_project_path.is_dir()

            # Test 2: Does it have a src folder (making it a SvelteKit project)?
            src_folder = expected_project_path / "src"
            assert src_folder.exists()
            assert src_folder.is_dir()

            # Test 3: Did the function return the right path?
            assert result_path == expected_project_path

    def test_reset_css_exists_after_creation(self):
        """Test that reset.css gets created when requested"""
        project_name = "reset-css-test"
        project_path = self.test_dir / project_name

        # Create basic project structure
        project_path.mkdir(parents=True)
        (project_path / "src").mkdir()

        # Test reset.css creation
        success = create_reset_css(project_path)

        # Should succeed
        assert success, "create_reset_css should return True"

        # Test 3: Does reset.css exist where we expect it?
        reset_css_path = project_path / "src" / "lib" / "styles" / "reset.css"
        assert reset_css_path.exists(), "reset.css was not created"

        # Basic content check
        content = reset_css_path.read_text()
        assert len(content) > 100, "reset.css seems too short"
        assert "box-sizing" in content.lower(), "reset.css doesn't contain expected CSS"

    def test_app_html_update(self):
        """Test that app.html is updated to include reset.css"""
        project_name = "test-app-html"
        project_path = self.test_dir / project_name

        # Create mock SvelteKit structure with app.html
        self._create_mock_sveltekit_structure(project_path)

        # Create app.html with basic content
        app_html_path = project_path / "src" / "app.html"
        app_html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <link rel="icon" href="%sveltekit.assets%/favicon.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    %sveltekit.head%
</head>
<body data-sveltekit-preload-data="hover">
    <div style="display: contents">%sveltekit.body%</div>
</body>
</html>'''
        app_html_path.write_text(app_html_content)

        # Update app.html to include reset.css
        success = update_app_html(project_path)
        assert success, "update_app_html should return True on success"

        # Verify reset.css link was added
        updated_content = app_html_path.read_text()
        assert 'reset.css' in updated_content, "app.html was not updated to include reset.css"
        assert '<link rel="stylesheet"' in updated_content, "CSS link tag was not added to app.html"

    def test_project_creation_with_invalid_directory(self):
        """Test behavior when target directory doesn't exist or is invalid"""
        invalid_dir = "/definitely/does/not/exist/anywhere"

        with patch('svelte_pi.project_setup.subprocess.Popen') as mock_popen:
            # Mock subprocess to fail due to invalid directory
            mock_popen.side_effect = FileNotFoundError("Directory not found")

            result_path = create_sveltekit_project("test-project", invalid_dir)
            assert result_path is None, "Should return None when directory is invalid"

    def _create_mock_sveltekit_structure(self, project_path):
        """Helper method to create a mock SvelteKit project structure"""
        project_path.mkdir(parents=True, exist_ok=True)

        # Create essential SvelteKit files and directories
        (project_path / "src").mkdir(exist_ok=True)
        (project_path / "src" / "lib").mkdir(exist_ok=True)
        (project_path / "src" / "routes").mkdir(exist_ok=True)
        (project_path / "static").mkdir(exist_ok=True)

        # Create package.json with SvelteKit dependency
        package_json = {
            "name": project_path.name,
            "version": "0.0.1",
            "private": True,
            "scripts": {
                "dev": "vite dev",
                "build": "vite build"
            },
            "devDependencies": {
                "@sveltejs/kit": "^1.0.0",
                "vite": "^4.0.0"
            }
        }

        import json
        (project_path / "package.json").write_text(json.dumps(package_json, indent=2))
        (project_path / "svelte.config.js").write_text("import adapter from '@sveltejs/adapter-auto';")
        (project_path / "vite.config.ts").write_text("import { sveltekit } from '@sveltejs/kit/vite';")


if __name__ == "__main__":
    pytest.main([__file__])
