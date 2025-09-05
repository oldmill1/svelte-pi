# file_operations.py
from pathlib import Path
from rich.console import Console
from file_templates import RESET_CSS_CONTENT

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
