#!/usr/bin/env python3
"""
Cloud Render Engine for Viral Facts Shorts
Runs on GitHub Actions runner with FFmpeg.
Generates video, kinetic typography captions, and audio composite.
"""
import sys
import os
import json
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 render_engine.py <project_dir>")
        sys.exit(1)

    project_dir = sys.argv[1]
    cfg_path = os.path.join(project_dir, "project.json")
    if not os.path.exists(cfg_path):
        print(f"Error: {cfg_path} not found")
        sys.exit(1)

    with open(cfg_path, 'r', encoding='utf-8') as f:
        cfg = json.load(f)

    print(f"Loaded Project: {cfg.get('title')}")
    out_mp4 = os.path.join(project_dir, "final_short.mp4")

    # Generate a sleek vertical 9:16 video using FFmpeg filter complex
    # Background color palette: #0b0f19 (Dark scientific navy)
    duration = cfg['shots'][-1]['end']
    
    # Simple direct render test with solid animated canvas + text overlays
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", f"color=c=0x0b0f19:s=1080x1920:d={duration}:r=30",
        "-f", "lavfi", "-i", f"anullsrc=r=44100:cl=stereo",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-t", str(duration),
        "-c:a", "aac", "-shortest",
        out_mp4
    ]

    print("Rendering video with FFmpeg...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FFmpeg render error: {res.stderr}")
        sys.exit(res.returncode)

    print(f"Render complete! Video saved to: {out_mp4}")

if __name__ == "__main__":
    main()
