#!/bin/sh

python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.template_name)"

# This script is used to setup the workspace environment for the Gitpod template.
# It installs Python dependencies and checks for software installations.
# It also displays a final message with the status of the setup process.

# Set delay so user can see the initial message before the setup process starts
sleep 5

echo -n "🚀 Preparing workspace environment"
for i in $(seq 1 20); do
    sleep 0.75
    echo -n "."
done
echo

python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"

# Update and upgrade system packages
if ! sudo apt-get update -y && sudo apt-get full-upgrade -y; then
    echo "❌ Failed to update and upgrade system packages."
    exit 1
fi

# Function to check installation with limited output
check_installation() {
    if command -v "$1" >/dev/null 2>&1; then
        version=$("$1" --version | head -n 1)
        echo "✅ $2 is installed ($version)"
    else
        echo "❌ $2 is not installed"
    fi
}

# Function to install Python dependencies with limited output
install_requirements() {
    python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
    echo -n "🔄 Installing dependencies"
    for i in $(seq 1 4); do
        sleep 0.75
        echo -n "."
    done
    echo
    if [ -f "requirements.txt" ]; then
        if pip install -r requirements.txt; then
            echo "✅ Dependencies installed successfully."
        else
            echo "❌ Failed to install dependencies."
            return 1
        fi
    else
        echo "⚠️ requirements.txt not found. Skipping installation."
    fi
}

# Install Python dependencies
if ! install_requirements; then
    echo "❌ Setup failed during dependency installation."
    exit 1
fi

pip list

# Check versions of dependencies
if ! command -v pip-review >/dev/null 2>&1; then
    pip install pip-review
fi
pip-review

# Check for installations of software tools
tools=("python" "pip" "node" "npm" "psql" "mongosh" "heroku" "docker" "aws" "git")
names=("Python" "pip" "Node.js" "npm" "PostgreSQL" "MongoDB" "Heroku CLI" "Docker" "AWS CLI" "Git")
python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
echo -n "🔍 Checking software installations"
for i in $(seq 1 4); do
    sleep 0.75
    echo -n "."
done
echo
for i in "${!tools[@]}"; do
    check_installation "${tools[$i]}" "${names[$i]}" || echo "⚠️ ${names[$i]} not installed or not found."
done

# Final message with setup status
if [ $? -eq 0 ]; then
    python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
    echo "✅ Setup complete! You are ready to start coding."
    echo ""
else
    python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
    echo "❌ Setup failed! Please check the logs and retry."
fi
