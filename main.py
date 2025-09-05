# main.py
import click
from ui import show_welcome, get_project_name, ask_reset_css, show_confirmation, show_summary


@click.command()
def main():
    """SvelteKit project launcher with custom defaults"""
    show_welcome()

    # Step 1: Get project name
    project_name = get_project_name()
    show_confirmation("Project name", project_name)

    # Step 2: Ask about reset.css
    use_reset_css = ask_reset_css()
    reset_status = "Yes" if use_reset_css else "No"
    show_confirmation("Include reset.css", reset_status)

    # TODO: Add SvelteKit creation logic in next step

    show_summary(project_name, use_reset_css)


if __name__ == "__main__":
    main()
