#!/usr/bin/env python3
"""
Cloud Render Worker for Puffco x BenDaDonnn GTA 6 Twitch Clip.
Runs on GitHub Actions Ubuntu Runner (100% Cloud Compute).
"""

import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_VIDEO = os.path.join(SCRIPT_DIR, "final_puffco_short.mp4")
RAW_CLIP = os.path.join(SCRIPT_DIR, "raw_clip.mp4")
ASS_FILE = os.path.join(SCRIPT_DIR, "captions.ass")

TWITCH_VOD_URL = "https://www.twitch.tv/videos/2933247628"
START_TIME = "00:15:30"
DURATION = "52"

def main():
    print("🚀 [Cloud] Starting Puffco x BenDaDonnn Cloud Render Pipeline...")
    
    # 1. Download precise segment from Twitch using yt-dlp on GitHub Cloud
    print(f"📥 Downloading Twitch VOD section: {START_TIME} for {DURATION}s...")
    dl_cmd = [
        "yt-dlp",
        "--download-sections", f"*{START_TIME}-00:16:22",
        "-f", "bestvideo+bestaudio/best",
        "--merge-output-format", "mp4",
        "-o", RAW_CLIP,
        TWITCH_VOD_URL
    ]
    subprocess.run(dl_cmd, check=True)
    print(f"✅ Download complete: {RAW_CLIP}")

    # 2. Generate timed word-by-word kinetic ASS subtitles
    print("📝 Generating Kinetic ASS Subtitles...")
    lines = [
        (0.5, 3.8, [("WHAT", 0.5, 0.9), ("I DO", 0.9, 1.3), ("KNOW IS", 1.3, 1.8), ("I GOT", 1.8, 2.3), ("PUFFCO!", 2.3, 3.8)]),
        (4.0, 7.5, [("THEY", 4.0, 4.4), ("S'POSED TO", 4.4, 5.0), ("PUFFCO", 5.0, 5.8), ("YOUR HEAD", 5.8, 6.5), ("OFF!", 6.5, 7.5)]),
        (8.0, 11.2, [("ALL TYPES", 8.0, 8.8), ("OF GIZMOS", 8.8, 9.6), ("& GADGETS!", 9.6, 11.2)]),
        (11.5, 14.5, [("THIS", 11.5, 12.0), ("IS FROM", 12.0, 12.7), ("THE FUTURE!", 12.7, 14.5)]),
        (14.8, 18.2, [("HOW THEY", 14.8, 15.5), ("ROLL OUT", 15.5, 16.2), ("THE ALIENS...", 16.2, 18.2)]),
        (18.5, 21.5, [("THIS WHAT", 18.5, 19.2), ("THEY BE", 19.2, 20.0), ("SMOKING!", 20.0, 21.5)]),
        (22.0, 25.5, [("PEEP THIS,", 22.0, 23.0), ("ONE OF THEY", 23.0, 24.0), ("CONCOCTIONS!", 24.0, 25.5)]),
        (26.0, 29.5, [("PUT THE", 26.0, 26.8), ("WAX IN HERE...", 26.8, 28.2), ("BOOM!", 28.2, 29.5)]),
        (30.0, 33.5, [("THEN YOU", 30.0, 30.8), ("HIT THAT", 30.8, 31.8), ("MUTHAF**KA!", 31.8, 33.5)]),
        (34.0, 38.0, [("YOU GOTTA", 34.0, 34.8), ("HAVE", 34.8, 35.5), ("CLEAR LUNGS!", 35.5, 38.0)]),
        (38.5, 42.5, [("AS SOON", 38.5, 39.2), ("AS YOU", 39.2, 40.0), ("HIT THIS...", 40.0, 42.5)]),
        (42.5, 47.0, [("I'M TALKIN'", 42.5, 43.5), ("LIGHTS", 43.5, 44.8), ("OUT! 💀", 44.8, 47.0)])
    ]

    def fmt_time(t):
        h = int(t // 3600)
        m = int((t % 3600) // 60)
        s = t - h * 3600 - m * 60
        return f"{h}:{m:02d}:{s:05.2f}"

    PLAY_W, PLAY_H = 1080, 1920
    WHITE = "&H00FFFFFF&"
    YELLOW = "&H0000FFFF&"
    GREEN = "&H0033FF00&"
    OUTLINE = "&H00000000&"

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {PLAY_W}
PlayResY: {PLAY_H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TopHook,DejaVu Sans,52,{WHITE},&H000000FF,{OUTLINE},&H90000000,-1,0,0,0,100,100,2,0,4,8,0,8,60,60,250,1
Style: SubHook,DejaVu Sans,40,{GREEN},&H000000FF,{OUTLINE},&H90000000,-1,0,0,0,100,100,2,0,4,6,0,8,60,60,330,1
Style: MainSub,DejaVu Sans,72,{WHITE},&H000000FF,{OUTLINE},&H80000000,-1,0,0,0,100,100,1,0,1,6,3,2,60,60,320,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 1,0:00:00.00,0:00:52.00,TopHook,,0,0,0,,{{\\an8\\bord6\\shad0}}🔥 BEN DADONNN x PUFFCO 🔥
Dialogue: 1,0:00:00.00,0:00:52.00,SubHook,,0,0,0,,{{\\an8\\bord5\\shad0}}🛸 \\"THIS IS FROM THE FUTURE!\\" 💨
"""

    events = []
    for line_start, line_end, words in lines:
        for idx, (word, w_start, w_end) in enumerate(words):
            parts = []
            for j, (w_text, _, _) in enumerate(words):
                if j == idx:
                    parts.append(f"{{\\c{YELLOW}}}{w_text}{{\\c{WHITE}}}")
                else:
                    parts.append(w_text)
            line_text = " ".join(parts)
            events.append(f"Dialogue: 2,{fmt_time(w_start)},{fmt_time(w_end)},MainSub,,0,0,0,,{line_text}")

    with open(ASS_FILE, "w") as f:
        f.write(header + "\n".join(events) + "\n")
    print(f"✅ Generated {len(events)} subtitle events in {ASS_FILE}")

    # 3. Render 9:16 Vertical Short with FFmpeg
    print("🎬 Rendering final 9:16 Vertical MP4...")
    filter_complex = (
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5[bg];"
        "[0:v]scale=1080:608[fg];"
        "[bg][fg]overlay=0:(H-h)/2[comp];"
        f"[comp]ass={ASS_FILE}[out]"
    )

    ff_cmd = [
        "ffmpeg", "-y",
        "-i", RAW_CLIP,
        "-filter_complex", filter_complex,
        "-map", "[out]",
        "-map", "0:a",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "20",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        OUTPUT_VIDEO
    ]
    subprocess.run(ff_cmd, check=True)
    print(f"🎉 Final Cloud Render Complete: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    main()
