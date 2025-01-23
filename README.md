# J0hanz Gitpod Template

[![GitHub last commit](https://img.shields.io/github/last-commit/j0hanz/j0hanz-gitpod-template)](https://github.com/j0hanz/j0hanz-gitpod-template/commits/main) [![GitHub repo size](https://img.shields.io/github/repo-size/j0hanz/j0hanz-gitpod-template)](https://github.com/j0hanz/j0hanz-gitpod-template)

---

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/j0hanz/j0hanz-gitpod-template)

A pre-configured development environment for **Python**, **Django**, **Node.js**, **MongoDB**, **PostgreSQL**, **AWS** and **Heroku**. Equipped with essential tools, linters, formatters, and VS Code extensions to enhance your workflow.

---

## Features

- **Python**: `3.12` & `3.13` via `pyenv`
- **Node.js**: `20.18.1` via `nvm`
- **MongoDB Shell**: `mongosh`
- **PostgreSQL**: `16`
- **Heroku CLI**
- **AWS CLI**
- **VS Code Extensions**: Python, Django, and more
- **Linters & Formatters**: `djlint`, `ruff`
- **Custom Scripts**: Initialization and repository info display

---

## Getting Started

### Prerequisites

- Create a [Gitpod Account](https://www.gitpod.io/)
- Access the [repository](https://github.com/j0hanz/j0hanz-gitpod-template)

### Setup

1. **Use This Template**: Click "Use this template" on the repository page to create a new repository.
2. **Open in Gitpod**: Click the button below to open in Gitpod:

   [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/j0hanz/j0hanz-gitpod-template)

3. **Initialize the Workspace**: The workspace builds and initializes automatically.
4. **Start Coding**: Begin coding immediately with the pre-configured environment.

### Deployment to Heroku

#### Web Interface

1. **Create a Heroku Account**: Sign up for [Heroku](https://signup.heroku.com/).
2. **Prepare Your Application**: Push your code to GitHub and commit all changes.
3. **Create a New Heroku Application**:
   - Log in to Heroku and create a new app.
   - Choose a unique name and region.
4. **Set Environment Variables**: Add required environment variables under "Config Vars" in your app's settings.
5. **Deploy Your Application**:
   - Connect to your GitHub repository in the "Deploy" tab.
   - Choose the branch to deploy and click "Deploy Branch".
6. **Verify Deployment**: Open the provided URL to ensure your application is running.

#### CLI Interface

1. **Login to Heroku**: Ensure you are logged in:

   ```sh
   heroku login
   ```

2. **Create a New Heroku App**: Create a new app:

   ```sh
   heroku create <your-app-name>
   ```

3. **Deploy to Heroku**: Push your code:

   ```sh
   git push heroku main
   ```

4. **Open Your App**: Open your deployed app:

   ```sh
   heroku open
   ```

5. **Manage Your App**: Use the Heroku CLI for management:

   ```sh
   heroku logs --tail
   heroku ps:scale web=1
   ```

---

## Environment Details

### Python Setup

- **Versions**: 3.12 (default) and 3.13
- **Global Tools**: `bandit`, `coverage`, `djlint`, `ruff`, `pytest`, `mypy`, `isort`, `pylint`, and more
- **Aliases**: `python` → Python 3.12, `pip` → Corresponding pip version

### Node.js Setup

- **Version**: 20.18.1
- **Global Tools**: `npm`, `pnpm`, `yarn`, `typescript`, `eslint`, `prettier`, `node-gyp`

### PostgreSQL Setup

- **Version**: PostgreSQL 16
- **Scripts**: Start: `~/.pg_ctl/bin/pg_start`, Stop: `~/.pg_ctl/bin/pg_stop`

### MongoDB Shell

- **Installed**: `mongosh`

### VS Code Extensions

- **Python**: [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- **Linters**: [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff), [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- **Markdown**: [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- **Utilities**: [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme), [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense)

---

## Linters & Formatters

### **Djlint**: Django Template Linter

- **Config**: In `pyproject.toml`
- **Usage**:
  - Lint: `djlint /path/to/templates`
  - Reformat: `djlint --reformat /path/to/templates`
- [Documentation](https://www.djlint.com/docs/getting-started/)

### **Ruff**: Fast Python Linter

- **Config**: In `pyproject.toml`
- **Usage**:
  - Check: `ruff check path/to/file.py`
  - Fix: `ruff check path/to/file.py --fix`
  - Format: `ruff format path/to/file.py`
- [Documentation](https://docs.astral.sh/ruff/)

---

## Custom Scripts

- **Initialization Script**: Automates dependency installation and environment setup
- **Repo Info Display**: Provides repository and branch details, last commit info, and user metadata

---

## Git Ignore

Key exclusions:

- **Python**: `__pycache__/`, `.pytest_cache`, `db.sqlite3`
- **Node.js**: `node_modules/`
- **Environment**: `.env`, `env.py`

---

This template is your all-in-one solution for efficient, robust development. Start building without worrying about setup.

**Happy Coding!**
