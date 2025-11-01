#!/usr/bin/env bash
# Build script for frontend on Render

echo "Installing dependencies..."
npm install

echo "Building production bundle..."
npm run build

echo "Build complete!"
