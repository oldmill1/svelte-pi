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


def create_reset_css(project_path):
    """Create the reset.css file"""
    console.print(f"[cyan]Creating reset.css...[/cyan]")

    reset_css_content = """/* src/lib/styles/reset.css - reset.css */
/* Modern CSS Reset */

/* Box sizing rules */
*,
*::before,
*::after {
    box-sizing: border-box;
}

/* Remove default margin and padding */
* {
    margin: 0;
    padding: 0;
}

/* Remove list styles on ul, ol elements with a list role, which suggests default styling will be removed */
ul[role='list'],
ol[role='list'] {
    list-style: none;
}

/* Set core root defaults */
html {
    scroll-behavior: smooth;
}

/* Set core body defaults */
body {
    min-height: 100vh;
    text-rendering: optimizeSpeed;
    line-height: 1.5;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* A elements that don't have a class get default styles */
a:not([class]) {
    text-decoration-skip-ink: auto;
}

/* Make images easier to work with */
img,
picture,
svg {
    max-width: 100%;
    height: auto;
    display: block;
}

/* Inherit fonts for inputs and buttons */
input,
button,
textarea,
select {
    font: inherit;
}

/* Remove all animations, transitions and smooth scroll for people that prefer not to see them */
@media (prefers-reduced-motion: reduce) {
    html {
        scroll-behavior: auto;
    }

    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}

/* Remove button styling */
button {
    background: none;
    border: none;
    cursor: pointer;
}

/* Remove focus outline for mouse users but keep for keyboard users */
button:focus:not(:focus-visible) {
    outline: none;
}

/* Ensure tables collapse borders by default */
table {
    border-collapse: collapse;
    border-spacing: 0;
}

/* Remove default fieldset and legend styling */
fieldset {
    border: none;
}

legend {
    display: table;
}

/* Improve text rendering */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    line-height: 1.2;
}

/* Remove default styles from address */
address {
    font-style: normal;
}
"""

    try:
        # Create styles directory
        styles_dir = project_path / "src" / "lib" / "styles"
        styles_dir.mkdir(parents=True, exist_ok=True)

        # Write reset.css file
        reset_css_path = styles_dir / "reset.css"
        reset_css_path.write_text(reset_css_content)

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
