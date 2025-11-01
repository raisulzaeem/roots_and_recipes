#!/usr/bin/env bash
# Build script for Render

# Disable Poetry auto-detection
export RENDER_RUNTIME_PYTHON_MANAGER=pip

# Change to backend directory
cd "$(dirname "$0")"

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Initializing database..."
python -m app.init_db

echo "Build complete!"
