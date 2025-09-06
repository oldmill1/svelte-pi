# svelte-pi

Quickly scaffold SvelteKit projects

## Features

- 🚀 **Project Scaffolding**: Create SvelteKit projects with TypeScript, Yarn, and Prettier pre-configured
- 🎨 **Optional Reset CSS**: Modern CSS reset with clean defaults
- 📦 **Sass Support**: Automatic sass-embedded installation
- 🧩 **Component Generation**: Create organized components with boilerplate templates
- ✨ **Interactive Wizard**: Component creation with guided prompts
- 🎯 **Smart Validation**: Ensures you're in the right directory before creating components
- ⚡ **Global CLI**: Use from anywhere in your terminal

## Installation

```bash
pip install -e .
```

After installation, the `svelte-pi` command will be available globally.

## Commands

### `svelte-pi create`

Creates a new SvelteKit project with opinionated defaults.

**Interactive prompts:**

- Project name
- Include reset.css (Y/n)
- Parent directory (default: ~/dev)

**What it does:**

1. Creates SvelteKit project with minimal template
2. Configures TypeScript and Yarn
3. Adds Prettier for code formatting
4. Installs sass-embedded for SCSS support
5. Optionally adds modern CSS reset

**Example:**

```bash
svelte-pi create
```

### `svelte-pi component [path]`

Creates a new component with proper file structure, naming conventions, and boilerplate templates.

**Two modes:**

1. **Direct mode**: Provide the path directly
2. **Interactive wizard**: Omit the path to launch the guided wizard

**What it creates:**

- `ComponentName.svelte` - Main component file with TypeScript and SCSS import
- `ComponentName.module.scss` - Component-specific styles with container class

**Component Templates:**

**ComponentName.svelte:**

```svelte
<script lang="ts">
  import styles from './ComponentName.module.scss';
  // Component logic here
</script>

<div class={styles.container}>
  <h1>ComponentName</h1>
</div>
```

**ComponentName.module.scss:**

```scss
.container {
  // Styles for the component
}
```

**Component Organization:**

```
src/lib/components/
├── features/           # Feature-specific components
│   ├── auth/
│   ├── chat/
│   └── trips/
├── layout/            # Layout components
│   └── MainLayout/
├── shared/            # Shared/common components
└── ui/               # Reusable UI components
    ├── ErrorBanner/
    └── TypingIndicator/
```

**Examples:**

```bash
# Direct mode
svelte-pi component features/auth/login
svelte-pi component ui/button
svelte-pi component layout/header

# Interactive wizard mode
svelte-pi component
# ✨ Welcome to Component Creation Wizard
# Name of component (including path): features/auth/signup
```

**Validation:**
The component command validates that you're in a SvelteKit project by checking:

- `package.json` exists with `@sveltejs/kit` dependency
- `src/` directory exists

## Project Structure

When you create a new SvelteKit project, `svelte-pi` generates this structure:

```
my-project/
├── src/
│   ├── lib/
│   │   ├── components/        # Component organization
│   │   └── styles/           # Global styles
│   │       └── reset.css     # Optional CSS reset
│   ├── routes/               # SvelteKit routes
│   ├── app.html              # HTML template
│   └── app.d.ts              # TypeScript declarations
├── static/                   # Static assets
├── package.json              # Dependencies with Yarn
├── tsconfig.json             # TypeScript config
├── svelte.config.js          # SvelteKit config
└── vite.config.ts            # Vite config
```

## Component Conventions

### Naming

- **Directories**: lowercase with hyphens (`auth-form`, `user-profile`)
- **Files**: PascalCase (`AuthForm.svelte`, `UserProfile.svelte`)

### Organization

- **`features/`**: Business logic components (`features/auth/login`)
- **`ui/`**: Reusable interface components (`ui/button`, `ui/modal`)
- **`layout/`**: Page structure components (`layout/header`, `layout/sidebar`)
- **`shared/`**: Common utility components

### File Structure

Each component gets its own directory with:

```
ComponentName/
├── ComponentName.svelte        # Main component with TypeScript and styles import
└── ComponentName.module.scss   # Scoped SCSS styles
```

### Usage Examples

**Created components work immediately:**

```bash
(.venv) ➜  abc svelte-pi component

✨ Welcome to Component Creation Wizard

Name of component (including path): user/profile
Creating component: user/profile
Created: src/lib/components/user/profile/Profile.svelte
Created: src/lib/components/user/profile/Profile.module.scss
✓ Component created successfully
```

**Generated file structure:**

```
src/lib/components/
└── user/
    └── profile/
        ├── Profile.svelte
        └── Profile.module.scss
```

## Help

```bash
# See all available commands
svelte-pi --help

# Get help for specific commands
svelte-pi create --help
svelte-pi component --help
```

## Development

This tool is built with:

- **Click**: Command-line interface framework
- **Rich**: Beautiful terminal formatting and interactive prompts
- **Python 3.9+**: Modern Python features

### Project Structure

```
svelte-pi/
├── svelte_pi/              # Main package
│   ├── main.py             # CLI commands and orchestration
│   ├── ui.py               # User interface and prompts
│   ├── project_setup.py    # SvelteKit project creation
│   ├── file_operations.py  # File and component operations
│   └── file_templates.py   # Content templates (CSS reset, component boilerplate)
├── tests/                  # Comprehensive test suite
│   └── test_create_project.py
├── setup.py                # Package configuration
└── requirements.txt        # Dependencies
```

### Testing

Run the test suite:

```bash
pytest
```

The project includes 5 tests covering:

- Full CLI integration with mocked subprocess calls
- Project directory creation
- Reset CSS functionality
- App.html updates
- Error handling

## Current Status ✅

**Fully functional features:**

- ✅ Complete project scaffolding with all dependencies
- ✅ Interactive component wizard with Rich UI
- ✅ Component templates with TypeScript and SCSS boilerplate
- ✅ Global CLI installation and usage
- ✅ Comprehensive test coverage
- ✅ SvelteKit project validation
- ✅ Automatic directory structure creation

## Roadmap

- [ ] Page/route creation (`svelte-pi page`)
- [ ] Different component types (with props, stores, etc.)
- [ ] Configuration file support (`.svelte-pi.yml`)
- [ ] Git initialization
- [ ] VS Code workspace setup
- [ ] Additional CSS framework options (Tailwind, etc.)

## License

MIT License

Copyright (c) 2025 Ankur Taxali

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.