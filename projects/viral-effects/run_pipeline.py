#!/usr/bin/env python3
"""
Master Pipeline: 51 Claude Video Effects + Roman Hindi Animated Typography
1. Executes fx.py with plan.json (Mediapipe selfie segmentation + Yunet face tracking)
2. Generates animated Roman Hindi ASS captions
3. Merges effects and kinetic typography into 1080x1920 final master MP4
"""

import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_VIDEO = os.path.join(SCRIPT_DIR, "raw_input.mp4")
PLAN_FILE = os.path.join(SCRIPT_DIR, "plan.json")
EFFECTS_OUT = os.path.join(SCRIPT_DIR, "effects_intermediate.mp4")
FINAL_OUT = os.path.join(SCRIPT_DIR, "final_master_reel.mp4")
ASS_FILE = os.path.join(SCRIPT_DIR, "captions.ass")

def format_ts(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:01d}:{m:02d}:{s:05.2f}"

def main():
    print("🚀 STEP 1: Rendering 51 Claude Video Effects (AI Segmentation & Face Tracking)...")
    fx_cmd = [
        sys.executable,
        os.path.join(SCRIPT_DIR, "scripts", "fx.py"),
        "--plan", PLAN_FILE,
        INPUT_VIDEO,
        EFFECTS_OUT
    ]
    print("Running:", " ".join(fx_cmd))
    subprocess.check_call(fx_cmd)
    print(f"✅ Effects step done: {EFFECTS_OUT}")

    print("🚀 STEP 2: Generating Roman Hindi Kinetic Subtitles...")
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

    highlight_yellow = "&H0000FFFF"
    highlight_green  = "&H0033FF00"
    white_color      = "&H00FFFFFF"

    ass_header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TopBadge,DejaVu Sans,44,{white_color},&H000000FF,&H00000000,&HB0000000,-1,0,0,0,100,100,2,0,4,8,0,8,60,60,180,1
Style: TypographyPop,DejaVu Sans,72,{white_color},&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,1,0,1,6,3,2,60,60,460,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = [
        "Dialogue: 1,0:00:00.00,0:01:06.66,TopBadge,,0,0,0,,{\\an8\\bord5\\shad0}🔥 10 ADS VS 10 IDEAS 🔥"
    ]

    for seg_start, seg_end, words in segments:
        dur = seg_end - seg_start
        per_w = dur / len(words)
        for idx, w in enumerate(words):
            w_start = seg_start + (idx * per_w)
            w_end   = seg_start + ((idx + 1) * per_w)
            s_str = format_ts(w_start)
            e_str = format_ts(w_end)
            parts = []
            for j, word_item in enumerate(words):
                if j == idx:
                    col = highlight_yellow if (idx % 2 == 0) else highlight_green
                    parts.append(f"{{\\c{col}\\b1\\fscx118\\fscy118\\t(0,100,\\fscx100\\fscy100)}}{word_item}{{\\rTypographyPop}}")
                else:
                    parts.append(f"{{\\c{white_color}\\b1}}{word_item}")
            line = " ".join(parts)
            events.append(f"Dialogue: 0,{s_str},{e_str},TypographyPop,,0,0,0,,{line}")

    with open(ASS_FILE, "w", encoding="utf-8") as f:
        f.write(ass_header + "\n".join(events))
    print(f"✅ Generated {len(events)} ASS events")

    print("🚀 STEP 3: Burning Subtitles & Final 1080x1920 Export...")
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-i", EFFECTS_OUT,
        "-vf", f"subtitles='{ASS_FILE}'",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "copy",
        FINAL_OUT
    ]
    print("Running:", " ".join(ffmpeg_cmd))
    subprocess.check_call(ffmpeg_cmd)
    print(f"🎉 MASTER REEL RENDERED SUCCESSFULLY: {FINAL_OUT}")

if __name__ == "__main__":
    main()
