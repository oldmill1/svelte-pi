# file_templates.py

RESET_CSS_CONTENT = """/* src/lib/styles/reset.css - reset.css */
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


def get_svelte_component_template(component_name):
    """Generate Svelte component template with component name"""
    return f"""<script lang="ts">
  import styles from './{component_name}.module.scss';
  // Component logic here
</script>

<div class={{styles.container}}>
  <h1>{component_name}</h1>
</div>
"""


def get_scss_module_template():
    """Generate SCSS module template"""
    return """.container {
  // Styles for the component
}
"""
