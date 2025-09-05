# project_setup.py
import subprocess
from pathlib import Path
from rich.console import Console

console = Console()


def create_sveltekit_project(project_name, parent_dir):
    """Create a new SvelteKit project with custom defaults"""
    project_path = Path(parent_dir) / project_name

    console.print(f"[cyan]Creating SvelteKit project in {project_path}...[/cyan]")

    try:
        cmd = [
            "npx", "sv", "create", project_name,
            "--template", "minimal",
            "--types", "ts",
            "--install", "yarn",
            "--no-add-ons"
        ]

        console.print(f"[dim]Running command: {' '.join(cmd)}[/dim]")
        console.print(f"[dim]Working directory: {parent_dir}[/dim]")

        # Use Popen to send "y" to npx prompt
        process = subprocess.Popen(
            cmd,
            cwd=parent_dir,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Send "y" to confirm npx package installation
        stdout, stderr = process.communicate(input="y\n", timeout=120)

        if process.returncode == 0:
            console.print(f"[green]✓[/green] SvelteKit project created successfully")
            return project_path
        else:
            console.print(f"[red]Error creating SvelteKit project:[/red]")
            console.print(f"[red]Exit code: {process.returncode}[/red]")
            console.print(f"[red]Stdout: {stdout}[/red]")
            console.print(f"[red]Stderr: {stderr}[/red]")
            return None

    except subprocess.TimeoutExpired:
        console.print(f"[red]Error: Command timed out after 2 minutes[/red]")
        process.kill()
        return None
    except Exception as e:
        console.print(f"[red]Unexpected error: {str(e)}[/red]")
        return None


def add_prettier(project_path):
    """Add prettier to the project"""
    console.print(f"[cyan]Adding prettier...[/cyan]")

    try:
        cmd = ["npx", "sv", "add", "prettier", "--no-install"]

        result = subprocess.run(
            cmd,
            cwd=project_path,
            capture_output=True,
            text=True,
            check=True
        )

        console.print(f"[green]✓[/green] Prettier added successfully")
        return True

    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error adding prettier:[/red]")
        console.print(f"[red]{e.stderr}[/red]")
        return False


def install_sass(project_path):
    """Install sass-embedded"""
    console.print(f"[cyan]Installing sass-embedded...[/cyan]")

    try:
        cmd = ["yarn", "add", "-D", "sass-embedded"]

        result = subprocess.run(
            cmd,
            cwd=project_path,
            capture_output=True,
            text=True,
            check=True
        )

        console.print(f"[green]✓[/green] sass-embedded installed successfully")
        return True

    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error installing sass-embedded:[/red]")
        console.print(f"[red]{e.stderr}[/red]")
        return False
