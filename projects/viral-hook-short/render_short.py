#!/usr/bin/env python3
"""
Cloud Render Worker for Vertical Viral Shorts.
Runs on GitHub Actions Ubuntu Runner:
1. Roman Hindi (Hinglish) Kinetic Typography with word-by-word pop-in animation.
2. Animated Concept Overlay Stickers (Ad variations vs angles, warnings, badges).
3. Vibrant Electric Yellow & Neon Green highlights with scale pop.
4. Top Hook Banner Badge.
5. High quality 1080x1920 vertical encode.
"""

import os
import sys
import subprocess

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
    print("🎬 Starting Cloud Render Pipeline: Roman Hindi + Typography Overlays...")
    print(f"Input: {INPUT_VIDEO}")
    print(f"Output: {OUTPUT_VIDEO}")

    if not os.path.exists(INPUT_VIDEO):
        print(f"Error: {INPUT_VIDEO} does not exist!")
        sys.exit(1)

    # Roman Hindi (Hinglish) Word Timings with Pacing
    segments = [
        (0.00, 2.10, ["EK", "PRODUCT", "KE", "10", "ADS"]),
        (2.10, 5.40, ["PAR", "KYA", "10", "ALAG", "IDEAS", "HAIN?"]),
        (5.80, 8.50, ["MAAN", "LO", "TUM", "EK"]),
        (8.50, 10.50, ["T-SHIRT", "BRAND", "CHALA", "RAHE", "HO"]),
        (10.60, 14.20, ["PEHLA", "AD:", "HAMARI", "T-SHIRT", "COMFORTABLE"]),
        (14.80, 17.80, ["DOOSRE", "MEIN:", "NAYE", "MODEL", "KE", "SATH"]),
        (18.00, 20.80, ["TEESRE", "MEIN:", "BACKGROUND", "BADAL", "DIYA"]),
        (21.20, 24.50, ["CHAUTHE", "MEIN:", "TEXT", "BADAL", "DIYA"]),
        (25.20, 27.80, ["YE", "10", "ALAG", "ADS", "ZAROOR", "HAIN"]),
        (27.80, 31.20, ["LEKIN", "KYA", "YE", "ALAG", "IDEAS", "HAIN?"]),
        (31.40, 34.80, ["BILKUL", "NAHI!", "YE", "SIRF", "VARIATIONS", "HAIN"]),
        (35.00, 38.80, ["CREATIVE", "ANGLE", "TEST", "KARNA", "ALAG", "HAI"]),
        (39.00, 41.50, ["ANGLE", "CHANGE", "TAB", "HOTA", "HAI"]),
        (41.50, 44.80, ["JAB", "PEHLE", "MEIN:", "COMFORT"]),
        (44.80, 47.50, ["DOOSRE", "MEIN:", "UNIQUE", "DESIGN"]),
        (47.50, 51.00, ["TEESRE", "MEIN:", "DURABILITY", "YA", "PRICE"]),
        (51.00, 55.20, ["ISLIYE", "JAB", "BHI", "CREATIVE", "BANAO"]),
        (55.20, 58.50, ["SIRF", "SURFACE", "VARIATION", "MAT", "BANAO"]),
        (58.50, 62.50, ["ALAG", "MARKETING", "ANGLES", "TEST", "KARO"]),
        (62.50, 66.66, ["TABHI", "AAPKE", "ADS", "SCALE", "HONGE!"])
    ]

    highlight_yellow = "&H0000FFFF"  # Electric Yellow
    highlight_green  = "&H0033FF00"  # Neon Green
    white_color      = "&H00FFFFFF"  # Crisp White

    ass_header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TopHook,DejaVu Sans,44,{white_color},&H000000FF,&H00000000,&HB0000000,-1,0,0,0,100,100,2,0,4,8,0,8,60,60,180,1
Style: OverlaySticker,DejaVu Sans,40,{highlight_yellow},&H000000FF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,4,7,0,8,60,60,260,1
Style: TypographyPop,DejaVu Sans,72,{white_color},&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,1,0,1,6,3,2,60,60,460,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    events = []

    # 1. Top Persistent Hook Header
    events.append("Dialogue: 1,0:00:00.00,0:01:06.66,TopHook,,0,0,0,,{\\an8\\bord5\\shad0}🔥 10 ADS VS 10 IDEAS 🔥")

    # 2. Key Dynamic Overlays & Visual Hook Badges
    events.append("Dialogue: 2,0:00:10.60,0:00:14.20,OverlaySticker,,0,0,0,,{\\an8\\t(0,140,\\fscx100\\fscy100)\\fscx120\\fscy120\\c&H0033FF00&}👕 AD #1: COMFORT ANGLE")
    events.append("Dialogue: 2,0:00:14.80,0:00:17.80,OverlaySticker,,0,0,0,,{\\an8\\t(0,140,\\fscx100\\fscy100)\\fscx120\\fscy120\\c&H0000FFFF&}🔄 AD #2: NEW MODEL VARIATION")
    events.append("Dialogue: 2,0:00:18.00,0:00:20.80,OverlaySticker,,0,0,0,,{\\an8\\t(0,140,\\fscx100\\fscy100)\\fscx120\\fscy120\\c&H00FF9900&}🖼️ AD #3: BACKGROUND CHANGE")
    events.append("Dialogue: 2,0:00:21.20,0:00:24.50,OverlaySticker,,0,0,0,,{\\an8\\t(0,140,\\fscx100\\fscy100)\\fscx120\\fscy120\\c&H000088FF&}✍️ AD #4: COPY / TEXT CHANGE")
    events.append("Dialogue: 2,0:00:27.80,0:00:34.80,OverlaySticker,,0,0,0,,{\\an8\\t(0,140,\\fscx100\\fscy100)\\fscx120\\fscy120\\c&H000000FF&\\1c&H000000FF&\\3c&H00FFFFFF&}⚠️ VARIATION ≠ NEW ANGLE ⚠️")
    events.append("Dialogue: 2,0:00:41.50,0:00:51.00,OverlaySticker,,0,0,0,,{\\an8\\t(0,140,\\fscx100\\fscy100)\\fscx120\\fscy120\\c&H0000FFFF&}💡 ANGLE 1: COMFORT | ANGLE 2: DESIGN")
    events.append("Dialogue: 2,0:00:58.50,0:01:06.66,OverlaySticker,,0,0,0,,{\\an8\\t(0,140,\\fscx100\\fscy100)\\fscx120\\fscy120\\c&H0033FF00&}🚀 TEST NEW ANGLES TO SCALE! 🚀")

    # 3. Roman Hindi (Hinglish) Animated Typography with Pop-In Transform
    for seg_start, seg_end, words in segments:
        duration = seg_end - seg_start
        per_word_dur = duration / len(words)

        for active_idx, w in enumerate(words):
            w_start = seg_start + (active_idx * per_word_dur)
            w_end   = seg_start + ((active_idx + 1) * per_word_dur)
            start_str = format_ts(w_start)
            end_str   = format_ts(w_end)

            # Build line with animated highlight on active word
            parts = []
            for j, word_item in enumerate(words):
                if j == active_idx:
                    # Alternating Yellow & Green highlights for intense visual engagement
                    h_color = highlight_yellow if (active_idx % 2 == 0) else highlight_green
                    # Pop scale from 118% to 100%
                    parts.append(f"{{\\c{h_color}\\b1\\fscx118\\fscy118\\t(0,100,\\fscx100\\fscy100)}}{word_item}{{\\rTypographyPop}}")
                else:
                    parts.append(f"{{\\c{white_color}\\b1}}{word_item}")

            rendered_line = " ".join(parts)
            events.append(f"Dialogue: 0,{start_str},{end_str},TypographyPop,,0,0,0,,{rendered_line}")

    with open(ASS_FILE, "w", encoding="utf-8") as f:
        f.write(ass_header + "\n".join(events))
    print(f"✅ Generated {len(events)} ASS animation events in {ASS_FILE}")

    # 4. FFmpeg High Bitrate Render
    print("🎬 Rendering final short with animated typography & overlays...")
    vf_chain = f"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,subtitles='{ASS_FILE}'"

    cmd = [
        "ffmpeg", "-y",
        "-i", INPUT_VIDEO,
        "-vf", vf_chain,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        OUTPUT_VIDEO
    ]

    print("Executing:", " ".join(cmd))
    subprocess.check_call(cmd)
    print(f"🎉 RENDER COMPLETE: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    main()
