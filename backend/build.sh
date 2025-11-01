#!/usr/bin/env bash
# Build script for Render

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Initializing database..."
python -m app.init_db

echo "Build complete!"
