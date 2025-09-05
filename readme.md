# svelte-pi

A powerful CLI tool to quickly scaffold SvelteKit projects and manage components with your preferred setup and
conventions.

## Features

- 🚀 **Project Scaffolding**: Create SvelteKit projects with TypeScript, Yarn, and Prettier pre-configured
- 🎨 **Optional Reset CSS**: Modern CSS reset with clean defaults
- 📦 **Sass Support**: Automatic sass-embedded installation
- 🧩 **Component Generation**: Create organized components following best practices
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

### `svelte-pi component <path>`

Creates a new component with proper file structure and naming conventions.

**Arguments:**

- `<path>` - Component path relative to `src/lib/components/`

**What it creates:**

- `ComponentName.svelte` - Main component file
- `ComponentName.module.scss` - Component-specific styles

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
# Create authentication components
svelte-pi component features/auth/login
svelte-pi component features/auth/signup

# Create UI components
svelte-pi component ui/button
svelte-pi component ui/modal

# Create layout components
svelte-pi component layout/header
svelte-pi component layout/sidebar
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
├── ComponentName.svelte        # Main component
└── ComponentName.module.scss   # Scoped styles
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
- **Rich**: Beautiful terminal formatting
- **Python 3.9+**: Modern Python features

### Project Structure

```
svelte-pi/
├── svelte_pi/              # Main package
│   ├── main.py             # CLI commands and orchestration
│   ├── ui.py               # User interface and prompts
│   ├── project_setup.py    # SvelteKit project creation
│   ├── file_operations.py  # File and component operations
│   └── file_templates.py   # Content templates
├── setup.py                # Package configuration
└── requirements.txt        # Dependencies
```

## Roadmap

- [ ] Component content templates (boilerplate code)
- [ ] Page/route creation (`svelte-pi page`)
- [ ] Custom component types (with props, stores, etc.)
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