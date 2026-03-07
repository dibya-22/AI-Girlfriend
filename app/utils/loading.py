import time

def loading_animation(stop_event):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    i = 0
    while not stop_event.is_set():
        print(f"\r{frames[i % len(frames)]} Loading...", end="", flush=True)
        i += 1
        time.sleep(0.1)
    print("\r" + " " * 20 + "\r", end="", flush=True)