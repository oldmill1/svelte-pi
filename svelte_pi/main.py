# main.py
import click
from .ui import show_welcome, get_project_name, ask_reset_css, get_parent_directory, show_confirmation, show_summary
from .project_setup import create_sveltekit_project, add_prettier, install_sass
from .file_operations import create_reset_css, update_app_html, create_component


@click.group()
def cli():
    """SvelteKit project launcher with custom defaults"""
    pass


@cli.command()
def create():
    """Create a new SvelteKit project"""
    show_welcome()

    # Step 1: Get project name
    project_name = get_project_name()
    show_confirmation("Project name", project_name)

    # Step 2: Ask about reset.css
    use_reset_css = ask_reset_css()
    reset_status = "Yes" if use_reset_css else "No"
    show_confirmation("Include reset.css", reset_status)

    # Step 3: Get parent directory
    parent_dir = get_parent_directory()
    show_confirmation("Project directory", parent_dir)

    # Step 4: Create the SvelteKit project
    project_path = create_sveltekit_project(project_name, parent_dir)
    if not project_path:
        return

    # Step 5: Add prettier
    if not add_prettier(project_path):
        return

    # Step 6: Install sass-embedded
    if not install_sass(project_path):
        return

    # Step 7: Add reset.css if requested
    if use_reset_css:
        if not create_reset_css(project_path):
            return
        if not update_app_html(project_path):
            return

    show_summary(project_name, use_reset_css, parent_dir)


@cli.command()
@click.argument('component_path')
def component(component_path):
    """Create a new component at the specified path"""
    from rich.console import Console

    console = Console()
    console.print(f"[cyan]Creating component:[/cyan] [bold]{component_path}[/bold]")

    if create_component(component_path):
        console.print(f"[green]✓[/green] Component created successfully")
    else:
        console.print(f"[red]✗[/red] Failed to create component")


# Keep backward compatibility - if no subcommand is given, run create
@click.command()
def main():
    """SvelteKit project launcher with custom defaults (legacy entry point)"""
    create.callback()


if __name__ == "__main__":
    cli()
