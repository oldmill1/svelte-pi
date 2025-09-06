# file_operations.py
from pathlib import Path
from rich.console import Console
from .file_templates import RESET_CSS_CONTENT, get_svelte_component_template, get_scss_module_template

console = Console()


def create_reset_css(project_path):
    """Create the reset.css file"""
    console.print(f"[cyan]Creating reset.css...[/cyan]")

    try:
        # Create styles directory
        styles_dir = project_path / "src" / "lib" / "styles"
        styles_dir.mkdir(parents=True, exist_ok=True)

        # Write reset.css file
        reset_css_path = styles_dir / "reset.css"
        reset_css_path.write_text(RESET_CSS_CONTENT)

        console.print(f"[green]✓[/green] reset.css created successfully")
        return True

    except Exception as e:
        console.print(f"[red]Error creating reset.css:[/red]")
        console.print(f"[red]{str(e)}[/red]")
        return False


def update_app_html(project_path):
    """Update app.html to include reset.css"""
    console.print(f"[cyan]Updating app.html to include reset.css...[/cyan]")

    try:
        app_html_path = project_path / "src" / "app.html"

        # Read current content
        current_content = app_html_path.read_text()

        # Add reset.css link after the viewport meta tag
        updated_content = current_content.replace(
            '<meta name="viewport" content="width=device-width, initial-scale=1" />',
            '<meta name="viewport" content="width=device-width, initial-scale=1" />\n\t<link rel="stylesheet" href="/src/lib/styles/reset.css" />'
        )

        # Write updated content
        app_html_path.write_text(updated_content)

        console.print(f"[green]✓[/green] app.html updated successfully")
        return True

    except Exception as e:
        console.print(f"[red]Error updating app.html:[/red]")
        console.print(f"[red]{str(e)}[/red]")
        return False


def create_component(component_path):
    """Create a new component with .svelte and .module.scss files"""
    try:
        # Get current working directory
        current_dir = Path.cwd()

        # Check if we're in a SvelteKit project
        if not is_sveltekit_project(current_dir):
            console.print(f"[red]Error: Not in a SvelteKit project directory[/red]")
            console.print(f"[yellow]Make sure you're in a directory that contains:[/yellow]")
            console.print(f"[yellow]  - package.json with '@sveltejs/kit' dependency[/yellow]")
            console.print(f"[yellow]  - src/ directory[/yellow]")
            return False

        # Extract component name from path (last part)
        component_name = component_path.split('/')[-1]
        component_name_capitalized = component_name.capitalize()

        # Build the full component directory path
        full_component_path = current_dir / "src" / "lib" / "components" / component_path

        # Create the component directory
        full_component_path.mkdir(parents=True, exist_ok=True)

        # Create the .svelte file
        svelte_file = full_component_path / f"{component_name_capitalized}.svelte"
        svelte_content = get_svelte_component_template(component_name_capitalized)
        svelte_file.write_text(svelte_content)

        # Create the .module.scss file
        scss_file = full_component_path / f"{component_name_capitalized}.module.scss"
        scss_content = get_scss_module_template()
        scss_file.write_text(scss_content)

        console.print(f"[dim]Created: {svelte_file.relative_to(current_dir)}[/dim]")
        console.print(f"[dim]Created: {scss_file.relative_to(current_dir)}[/dim]")

        return True

    except Exception as e:
        console.print(f"[red]Error creating component:[/red]")
        console.print(f"[red]{str(e)}[/red]")
        return False


def is_sveltekit_project(directory):
    """Check if the current directory is a SvelteKit project"""
    try:
        # Check for package.json
        package_json = directory / "package.json"
        if not package_json.exists():
            return False

        # Check if package.json contains SvelteKit dependency
        import json
        with open(package_json, 'r') as f:
            package_data = json.load(f)

        # Check dependencies and devDependencies for SvelteKit
        dependencies = package_data.get('dependencies', {})
        dev_dependencies = package_data.get('devDependencies', {})

        has_sveltekit = '@sveltejs/kit' in dependencies or '@sveltejs/kit' in dev_dependencies

        # Check for src directory
        src_dir = directory / "src"
        has_src = src_dir.exists() and src_dir.is_dir()

        return has_sveltekit and has_src

    except Exception:
        return False
