#!/usr/bin/env python3
"""
Cloud Render Worker for Vertical Viral Shorts.
Runs on GitHub Actions Ubuntu Runner:
1. Fast Whisper transcription with word timestamps (Hindi/Hinglish).
2. Generates dynamic Hormozi kinetic typography with Electric Yellow word highlights.
3. Top Hook Banner Badge.
4. High quality 1080x1920 vertical encode.
"""

import os
import sys
import subprocess
from faster_whisper import WhisperModel

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_VIDEO = os.path.join(SCRIPT_DIR, "raw_input.mp4")
OUTPUT_VIDEO = os.path.join(SCRIPT_DIR, "final_viral_short.mp4")
ASS_FILE = os.path.join(SCRIPT_DIR, "captions.ass")

def format_ts(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:01d}:{m:02d}:{s:05.2f}"

def main():
    print(f"🎬 Starting Cloud Render Pipeline...")
    print(f"Input: {INPUT_VIDEO}")
    print(f"Output: {OUTPUT_VIDEO}")

    if not os.path.exists(INPUT_VIDEO):
        print(f"Error: {INPUT_VIDEO} does not exist!")
        sys.exit(1)

    # 1. Transcribe
    print("1/3 🎙️ Running Whisper speech transcription...")
    model = WhisperModel("small", device="cpu", compute_type="default")
    segments, info = model.transcribe(INPUT_VIDEO, language="hi", word_timestamps=True)
    segments = list(segments)
    print(f"Detected language: {info.language} ({info.language_probability:.2f}), Segments: {len(segments)}")

    # 2. Build ASS Subtitles with Hormozi Highlights & Top Hook Badge
    print("2/3 ✍️ Generating Kinetic ASS Subtitles...")
    highlight_color = "&H0000FFFF" # Electric Yellow in BGR hex
    primary_color = "&H00FFFFFF"   # Bright White

    ass_header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,DejaVu Sans,66,{primary_color},&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,1,0,1,6,3,2,60,60,460,1
Style: HookBadge,DejaVu Sans,44,&H00FFFFFF,&H000000FF,&H00000000,&HB0000000,-1,0,0,0,100,100,2,0,4,8,0,8,60,60,190,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = []
    # Persistent Hook Header at the top
    events.append("Dialogue: 1,0:00:00.00,0:01:08.00,HookBadge,,0,0,0,,{\\an8\\bord4\\shad0\\fscx105\\fscy105}🔥 10 ADS VS 10 IDEAS 🔥")

    # Word-by-word active highlight
    for seg in segments:
        words = seg.words if seg.words else []
        if not words:
            events.append(f"Dialogue: 0,{format_ts(seg.start)},{format_ts(seg.end)},Default,,0,0,0,,{seg.text.strip()}")
            continue

        chunk_size = 3
        for i in range(0, len(words), chunk_size):
            chunk = words[i:i + chunk_size]
            for active_idx, w in enumerate(chunk):
                w_start = format_ts(w.start)
                w_end = format_ts(w.end)
                parts = []
                for j, other in enumerate(chunk):
                    clean_w = other.word.strip()
                    if j == active_idx:
                        parts.append(f"{{\\c{highlight_color}\\b1\\fscx112\\fscy112}}{clean_w}{{\\rDefault}}")
                    else:
                        parts.append(clean_w)
                line = " ".join(parts)
                events.append(f"Dialogue: 0,{w_start},{w_end},Default,,0,0,0,,{line}")

    with open(ASS_FILE, "w", encoding="utf-8") as f:
        f.write(ass_header + "\n".join(events))
    print(f"✅ Generated {len(events)} subtitle events in {ASS_FILE}")

    # 3. FFmpeg Render
    print("3/3 🎬 Encoding final short with FFmpeg...")
    vf_filters = [
        "scale=1080:1920:force_original_aspect_ratio=increase",
        "crop=1080:1920",
        f"subtitles='{ASS_FILE}'"
    ]
    vf_str = ",".join(vf_filters)

    cmd = [
        "ffmpeg", "-y",
        "-i", INPUT_VIDEO,
        "-vf", vf_str,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        OUTPUT_VIDEO
    ]

    print("Running:", " ".join(cmd))
    subprocess.check_call(cmd)
    print(f"🎉 RENDER SUCCESSFUL! File saved at: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    main()
