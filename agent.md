# Video Making Pipeline Context & Architecture

This document serves as the system architecture and knowledge base for the `video-making` repository. It outlines the AI-driven, zero-editing video generation pipeline we built using Google Antigravity / HyperFrames.

## Pipeline Architecture

The goal of this pipeline is to take a raw, unedited "talking head" recording and automatically package it into a high-retention, kinetic typography-driven Short/Reel (similar to high-end competitor videos) with **zero manual video editing**.

### Core Technologies
- **HyperFrames (`npx hyperframes`)**: HTML/CSS/GSAP-based video rendering engine. Used to composite web-based graphic cards over a background video layer, capturing it in a headless Chromium instance to an `.mp4`.
- **FFmpeg & Python**: Used for silence removal, audio extraction, and final re-encoding.
- **Whisper (via HyperFrames)**: Local transcription engine for converting speech to timed text.

### The 5-Step Automated Workflow
1. **Silence Removal (`remove_silence.py`)**
   - **Input:** Raw video (`Untitled_Scene...mp4`)
   - **Process:** Runs `ffmpeg silencedetect` to find pauses and dead air, generates a dynamic trim script, and concats the clips.
   - **Output:** `input_cut.mp4`

2. **Metadata & Audio Extraction**
   - **Process:** Extracts `audio.mp3` and `metadata.json` (resolution, fps, duration) using `ffprobe` and `ffmpeg`.

3. **Transcription (`npx hyperframes transcribe`)**
   - **Process:** Uses `small.en` Whisper model locally to transcribe `audio.mp3` into a word-level timestamped array.
   - **Output:** `videos/my-reel/transcript.json`

4. **Composition Generation (`build_composition_v2.py`)**
   - **Process:** Python script that chunks the transcript into 15 high-density takeaway cards.
   - **Design System:**
     - **Layout:** "Inverted Stack" (9:16 portrait) — Speaker video locked to the bottom 44%, graphics dominate the top 56%.
     - **Style:** "Geom" — Aggressive color clashing (chartreuse green, hot pink, black) and bold uppercase typography (Inter Black).
     - **Animation:** Kinetic `scale-pop` with `back.out(1.6)` easing for punchy, instant cuts (GSAP).
   - **Output:** `public/index.html` (the master GSAP timeline) and `public/cards/*.html` (the individual visual overlays).

5. **Headless GPU Render (`npx hyperframes render`)**
   - **Process:** Chrome headless renders the DOM over the re-encoded `input-video.mp4`.
   - **Config:** Runs with `PRODUCER_BROWSER_GPU_MODE=hardware` for acceleration.
   - **Output:** `output_v2_real.mp4`

## Important Commands

**Re-run the Python generator (if you tweak text/animations):**
```bash
python build_composition_v2.py
```

**Re-render the final MP4:**
```bash
cd videos/my-reel
export PRODUCER_BROWSER_GPU_MODE=hardware
npx hyperframes render . -c public/index.html --output output_v2_real.mp4
```

## System Requirements
- Node.js v22+
- FFmpeg
- Ubuntu/Linux dependencies for Puppeteer/Headless Chrome (libnss3, libatk, libgbm, etc.)

## Easy Render Script
To avoid missing the GPU configuration on a new device, simply run:
```bash
bash render.sh
```
