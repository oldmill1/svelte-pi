# ui.py
from rich.console import Console
from rich.prompt import Prompt, Confirm

console = Console()


def show_welcome():
    """Display the welcome banner"""
    console.print()
    console.print("✨ [light_blue1]SvelteKit Launcher[/light_blue1] [grey85]v1.0.0[/grey85]")
    console.print("[light_sky_blue2]“A long time ago in a repo far, far away...”[/light_sky_blue2]")
    console.print("[pale_green1]Let’s set the project in motion.[/pale_green1]")
    console.print()


def get_project_name():
    """Get the project name from user"""
    while True:
        project_name = Prompt.ask(
            "[light_steel_blue1]What’s the name of your project?[/light_steel_blue1]",
            console=console
        )

        if project_name.strip():
            console.print(f"[pale_green1]✓ Project name set: {project_name}[/pale_green1]")
            return project_name.strip()
        else:
            console.print("[light_goldenrod1]Please enter a valid project name.[/light_goldenrod1]")


def ask_reset_css():
    """Ask if user wants to include reset.css"""
    return Confirm.ask(
        "[powder_blue]Do you want to include reset.css?[/powder_blue]",
        default=True,
        console=console
    )


def get_parent_directory():
    """Get the parent directory where the project should be created"""
    import os
    default_dir = os.path.expanduser("~/dev")

    parent_dir = Prompt.ask(
        "[light_salmon1]Where should the project be created?[/light_salmon1]",
        default=default_dir,
        console=console
    )

    console.print(f"[khaki1]Directory set: {parent_dir}[/khaki1]")
    return os.path.expanduser(parent_dir)


def show_confirmation(label, value):
    """Show a confirmation checkmark for user choices"""
    console.print(f"[pale_green1]✓ {label}: [bold]{value}[/bold][/pale_green1]")


def show_summary(project_name, use_reset_css, parent_dir):
    """Show final summary of choices"""
    console.print()
    console.print("[light_goldenrod1]✨ Setup complete![/light_goldenrod1]")
    reset_status = "Yes" if use_reset_css else "No"
    console.print(f"[grey89]Project: {project_name}, Reset CSS: {reset_status}, Directory: {parent_dir}[/grey89]")
    console.print("[light_sea_green]All ready to launch.[/light_sea_green]")
