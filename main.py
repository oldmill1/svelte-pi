# main.py
import click
from ui import show_welcome, get_project_name, ask_reset_css, get_parent_directory, show_confirmation, show_summary
from svelte_creator import create_sveltekit_project, add_prettier, install_sass


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

    # TODO: Add reset.css creation in next step

    show_summary(project_name, use_reset_css, parent_dir)


if __name__ == "__main__":
    main()
