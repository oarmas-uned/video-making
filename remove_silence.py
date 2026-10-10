import subprocess
import re
import sys

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    print("Detecting silence...")
    cmd = ["ffmpeg", "-i", input_file, "-af", "silencedetect=noise=-30dB:d=0.3", "-f", "null", "-"]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)
    
    silences = []
    start = None
    for line in res.stderr.split("\n"):
        if "silence_start" in line:
            start = float(line.split("silence_start: ")[1].split()[0])
        if "silence_end" in line:
            end = float(line.split("silence_end: ")[1].split()[0])
            if start is not None:
                silences.append((start, end))
                start = None
            
    print(f"Found {len(silences)} silences.")
    
    cmd_dur = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", input_file]
    dur_res = subprocess.run(cmd_dur, stdout=subprocess.PIPE, text=True)
    duration = float(dur_res.stdout.strip())
    
    keeps = []
    last = 0
    margin = 0.1
    for s_start, s_end in silences:
        # add margin so it doesn't sound too abrupt
        keep_end = s_start + margin
        if keep_end > last:
            keeps.append((last, keep_end))
        last = s_end - margin
        
    if last < duration:
        keeps.append((last, duration))
        
    if not keeps:
        keeps.append((0, duration))
        
    print(f"Keeping {len(keeps)} segments...")
    
    filter_complex = ""
    for i, (start_t, end_t) in enumerate(keeps):
        filter_complex += f"[0:v]trim=start={start_t}:end={end_t},setpts=PTS-STARTPTS[v{i}]; "
        filter_complex += f"[0:a]atrim=start={start_t}:end={end_t},asetpts=PTS-STARTPTS[a{i}]; "
        
    for i in range(len(keeps)):
        filter_complex += f"[v{i}][a{i}]"
        
    filter_complex += f"concat=n={len(keeps)}:v=1:a=1[vout][aout]"
    
    print("Cutting video...")
    cut_cmd = [
        "ffmpeg", "-y", "-i", input_file, 
        "-filter_complex", filter_complex, 
        "-map", "[vout]", "-map", "[aout]",
        output_file
    ]
    subprocess.run(cut_cmd, check=True)
    print("Done!")

if __name__ == "__main__":
    main()
