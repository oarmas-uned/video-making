#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting HyperFrames Render Pipeline..."

# 1. Force hardware GPU acceleration for headless Chrome
# This is critical for fast, page-side shader transitions and overall capture speed.
export PRODUCER_BROWSER_GPU_MODE=hardware
echo "✅ Set PRODUCER_BROWSER_GPU_MODE=hardware"

# 2. Run the composition builder script
echo "✅ Generating GSAP layouts and cards..."
python3 build_composition_v2.py

# 3. Enter the project directory and render
cd videos/my-reel
echo "✅ Running HyperFrames render..."
npx hyperframes render . -c public/index.html --output output_final.mp4

echo "🎉 Render complete! Output saved to videos/my-reel/output_final.mp4"
