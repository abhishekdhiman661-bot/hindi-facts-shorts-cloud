#!/usr/bin/env python3
"""
Cloud Render Worker for Clip #2:
Puffco x BenDaDonnn: Hash Butler in Tuxedo & Big Hits!
Runs on GitHub Actions Ubuntu Runner (100% Cloud Compute).
"""

import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_VIDEO = os.path.join(SCRIPT_DIR, "final_puffco_clip2.mp4")
RAW_CLIP = os.path.join(SCRIPT_DIR, "raw_clip2.mp4")
ASS_FILE = os.path.join(SCRIPT_DIR, "captions2.ass")

TWITCH_VOD_URL = "https://www.twitch.tv/videos/2933247628"
START_TIME = "01:15:12"
END_TIME = "01:15:54"

def main():
    print("🚀 [Cloud] Starting Clip #2 Render: Hash Butler & Big Hits...")
    
    # 1. Download section directly on Cloud
    print(f"📥 Downloading Twitch VOD section: {START_TIME} to {END_TIME}...")
    dl_cmd = [
        "yt-dlp",
        "--download-sections", f"*{START_TIME}-{END_TIME}",
        "-f", "bestvideo+bestaudio/best",
        "--merge-output-format", "mp4",
        "-o", RAW_CLIP,
        TWITCH_VOD_URL
    ]
    subprocess.run(dl_cmd, check=True)
    print(f"✅ Download complete: {RAW_CLIP}")

    # 2. Generate timed word-by-word kinetic ASS subtitles
    print("📝 Generating Kinetic ASS Subtitles for Clip #2...")
    lines = [
        (0.5, 3.2, [("STEVEN,", 0.5, 1.2), ("WHAT IS", 1.2, 1.9), ("YOU DOING?", 1.9, 3.2)]),
        (3.5, 6.2, [("TAKING THIS HIT,", 3.5, 4.5), ("WHAT", 4.5, 5.0), ("YOU MEAN?", 5.0, 6.2)]),
        (6.5, 9.8, [("YOU S'POSED", 6.5, 7.5), ("TO BE ON THAT", 7.5, 8.8), ("OTHER ONE!", 8.8, 9.8)]),
        (10.0, 13.5, [("WE TRYING", 10.0, 11.0), ("DIFFERENT SH*T...", 11.0, 12.2), ("MORE TERPS!", 12.2, 13.5)]),
        (14.0, 17.5, [("THIS IS", 14.0, 14.8), ("SAME THING,", 14.8, 15.8), ("JUST SMALLER!", 15.8, 17.5)]),
        (18.0, 21.5, [("OH YEAH,", 18.0, 19.0), ("HIT THAT...", 19.0, 20.2), ("YOU SEE THAT?!", 20.2, 21.5)]),
        (22.0, 25.5, [("OOH!!", 22.0, 23.2), ("*COUGHS*", 23.2, 24.5), ("OH WOW! 💨", 24.5, 25.5)]),
        (26.0, 29.5, [("YEAH BRO,", 26.0, 27.0), ("THIS SH*T", 27.0, 28.0), ("IS FIRE!", 28.0, 29.5)]),
        (30.0, 34.0, [("THAT HIT", 30.0, 31.0), ("WAS A LITTLE", 31.0, 32.2), ("CRUCIAL! 💀", 32.2, 34.0)]),
        (34.5, 38.5, [("LADIES,", 34.5, 35.5), ("YOU KNOW", 35.5, 36.5), ("WHAT TIME IT IS?", 36.5, 38.5)]),
        (38.8, 41.5, [("IT'S", 38.8, 39.4), ("SHOT", 39.4, 40.2), ("O'CLOCK!! 🥂", 40.2, 41.5)])
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
Style: TopHook,DejaVu Sans,50,{WHITE},&H000000FF,{OUTLINE},&H90000000,-1,0,0,0,100,100,2,0,4,8,0,8,60,60,250,1
Style: SubHook,DejaVu Sans,38,{GREEN},&H000000FF,{OUTLINE},&H90000000,-1,0,0,0,100,100,2,0,4,6,0,8,60,60,330,1
Style: MainSub,DejaVu Sans,72,{WHITE},&H000000FF,{OUTLINE},&H80000000,-1,0,0,0,100,100,1,0,1,6,3,2,60,60,320,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 1,0:00:00.00,0:00:42.00,TopHook,,0,0,0,,{{\\an8\\bord6\\shad0}}🔥 BEN DADONNN x PUFFCO 🔥
Dialogue: 1,0:00:00.00,0:00:42.00,SubHook,,0,0,0,,{{\\an8\\bord5\\shad0}}🤵 HASH BUTLER IN TUXEDO SERVES A HIT! 💨
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
    print("🎬 Rendering final 9:16 Vertical MP4 on Cloud...")
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
