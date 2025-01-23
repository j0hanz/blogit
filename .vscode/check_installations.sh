#!/bin/bash

# Function to check installation
check_installation() {
    if command -v "$1" &> /dev/null; then
        "$1" --version
    else
        echo "$2 is not installed"
    fi
}

# List of tools to check
tools=("python" "pip" "node" "npm" "psql" "mongosh" "heroku")
names=("Python" "pip" "Node.js" "npm" "PostgreSQL" "MongoDB" "Heroku CLI")

# Checking software installations
for i in "${!tools[@]}"; do
    check_installation "${tools[$i]}" "${names[$i]}"
done
