# ui.py
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text

console = Console()


def show_welcome():
    """Display the welcome banner"""
    welcome_text = Text()
    welcome_text.append("Welcome to the ", style="white")
    welcome_text.append("SvelteKit Launcher!", style="bold cyan")
    welcome_text.append(" (v1.0.0)", style="dim white")

    console.print(Panel(welcome_text, style="cyan", padding=(1, 2)))
    console.print()


def get_project_name():
    """Get the project name from user"""
    while True:
        project_name = Prompt.ask(
            "[cyan]What's the name of your project?[/cyan]",
            console=console
        )

        if project_name.strip():
            return project_name.strip()
        else:
            console.print("[red]Please enter a valid project name[/red]")


def ask_reset_css():
    """Ask if user wants to include reset.css"""
    return Confirm.ask(
        "[cyan]Do you want to include reset.css?[/cyan]",
        default=True,
        console=console
    )


def show_confirmation(label, value):
    """Show a confirmation checkmark for user choices"""
    console.print(f"[green]✓[/green] {label}: [bold]{value}[/bold]")


def show_summary(project_name, use_reset_css):
    """Show final summary of choices"""
    console.print()
    console.print("[yellow]Setup complete! (More features coming in next steps)[/yellow]")
    reset_status = "Yes" if use_reset_css else "No"
    console.print(f"[dim]Project: {project_name}, Reset CSS: {reset_status}[/dim]")
