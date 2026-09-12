import sys
import time
import subprocess
import numpy as np
import pyaudio

# --- AUDIO CONFIGURATION ---
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 22050
CHUNK = 512

# === HARD MODE THRESHOLDS ===
MIN_VOLUME_RMS = 0.1200  # Floor limit (ignores talking)
MAX_VOLUME_RMS = 0.9500  # Ceiling limit (hardware max)
EXPONENT       = 6.0     # Steepness curve

current_rms = 0.0
dzen_process = None

def get_screen_dimensions():
    try:
        cmd = "xrandr | grep '*' | awk '{print $1}'"
        res = subprocess.check_output(cmd, shell=True).decode().strip().split('\n')[0]
        w, h = res.split('x')
        return int(w), int(h)
    except Exception:
        return 1920, 1080

SCREEN_W, SCREEN_H = get_screen_dimensions()

def set_dzen_cover(cover_ratio):
    """Updates the black dzen2 overlay width cleanly."""
    global dzen_process
    
    cover_w = int(SCREEN_W * cover_ratio)
    x_pos = SCREEN_W - cover_w
    
    if dzen_process is not None:
        dzen_process.terminate()
        dzen_process = None

    if cover_w > 10:
        cmd = f"dzen2 -x {x_pos} -y 0 -w {cover_w} -h {SCREEN_H} -bg black -fg black -e ''"
        dzen_process = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def audio_callback(in_data, frame_count, time_info, status):
    global current_rms
    
    audio_data = np.frombuffer(in_data, dtype=np.int16)
    float_data = audio_data.astype(np.float32) / 32768.0
    current_rms = float(np.sqrt(np.mean(float_data**2)))
    return (in_data, pyaudio.paContinue)

def main():
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
        stream_callback=audio_callback
    )

    print("=== DUAL-DIRECTION ULTRA-SMOOTH SCREAM OVERLAY ACTIVE ===")
    print(f"[*] Screen Resolution: {SCREEN_W}x{SCREEN_H}")
    print("[*] Screen opens smoothly when screaming AND glides back slowly when quiet.")
    print("Press Ctrl+C to exit.\n")

    stream.start_stream()
    time.sleep(0.3)

    smoothed_ratio = 1.0  # Start 100% blacked out
    last_applied_step = -1.0

    try:
        while stream.is_active():
            if current_rms > MIN_VOLUME_RMS:
                norm_vol = (current_rms - MIN_VOLUME_RMS) / (MAX_VOLUME_RMS - MIN_VOLUME_RMS)
                norm_vol = np.clip(norm_vol, 0.0, 1.0)
                
                visibility_factor = np.power(norm_vol, EXPONENT)
                target_ratio = 1.0 - visibility_factor
            else:
                target_ratio = 1.0  # Target full blackout when quiet

            # --- DUAL-DIRECTION SMOOTHING (BOTH SIDES SMOOTH) ---
            if target_ratio < smoothed_ratio:
                # SCREAMING / UNCOVERING: Smooth fluid opening (Lower = smoother/slower)
                alpha = 0.08
            else:
                # QUIET / COVERING: Slow cinematic return to black
                alpha = 0.012

            smoothed_ratio = (alpha * target_ratio) + ((1.0 - alpha) * smoothed_ratio)

            # High 0.5% quantization steps (200) for ultra-smooth gliding
            current_step = round(smoothed_ratio * 200) / 200.0

            if current_step != last_applied_step:
                set_dzen_cover(current_step)
                last_applied_step = current_step

            visible_pct = int((1.0 - current_step) * 100)
            sys.stdout.write(f"\rRMS: {current_rms:.4f} | Desktop Visibility: {visible_pct}%   ")
            sys.stdout.flush()
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\n[+] Exiting and restoring full desktop view...")
    finally:
        if dzen_process is not None:
            dzen_process.terminate()
        subprocess.run("pkill dzen2", shell=True, stderr=subprocess.DEVNULL)
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
