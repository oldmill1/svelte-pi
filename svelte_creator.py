# svelte_creator.py
import subprocess
import os
from pathlib import Path
from rich.console import Console

console = Console()


def create_sveltekit_project(project_name, parent_dir):
    """Create a new SvelteKit project with custom defaults"""
    project_path = Path(parent_dir) / project_name

    console.print(f"[cyan]Creating SvelteKit project in {project_path}...[/cyan]")

    try:
        # Create the SvelteKit project with our defaults
        cmd = [
            "npx", "sv", "create", project_name,
            "--template", "minimal",
            "--types", "ts",
            "--install", "yarn",
            "--no-add-ons"
        ]

        # Run in the parent directory
        result = subprocess.run(
            cmd,
            cwd=parent_dir,
            capture_output=True,
            text=True,
            check=True
        )

        console.print(f"[green]✓[/green] SvelteKit project created successfully")
        return project_path

    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error creating SvelteKit project:[/red]")
        console.print(f"[red]{e.stderr}[/red]")
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
