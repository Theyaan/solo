import evdev, os, threading, time, glob
from evdev import ecodes

os.environ["DISPLAY"] = ":0"
try:
    os.environ["XAUTHORITY"] = "/home/ark/.Xauthority"
except:
    pass

# Find input devices (try event2 and event3 typically used for gamepad/buttons)
devices = [evdev.InputDevice(path) for path in glob.glob('/dev/input/event*')]
state = {"lx": 0, "ly": 0, "rx": 0, "ry": 0, "select": False, "start": False}

def move_loop():
    while True:
        mx, my = 0, 0
        if abs(state["lx"]) > 500 or abs(state["ly"]) > 500:
            mx += int(state["lx"] * 0.5); my += int(state["ly"] * 0.5)
        if abs(state["rx"]) > 500 or abs(state["ry"]) > 500:
            mx += int(state["rx"] * 0.24); my += int(state["ry"] * 0.24)
        if mx != 0 or my != 0:
            os.system(f"xdotool mousemove_relative -- {int(mx/100)} {int(my/100)}")
        time.sleep(0.01)

threading.Thread(target=move_loop, daemon=True).start()

def process_events(device):
    try:
        for event in device.read_loop():
            if event.type == ecodes.EV_KEY:
                # Toggle onboard keyboard on FN button or similar (706=Mode, 316=Mode, etc)
                # Some RK devices use specific codes. We cover the common ones.
                if event.code in [16, 706, 316, 707, 708] and event.value == 1:
                    os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.ToggleVisible")
                
                # Mouse Buttons
                elif event.code == 312: # L2 -> Left click
                    os.system("xdotool mousedown 1") if event.value == 1 else os.system("xdotool mouseup 1")
                elif event.code == 313: # R2 -> Right click
                    os.system("xdotool mousedown 3") if event.value == 1 else os.system("xdotool mouseup 3")
                
                # Mouse Wheel (Scroll)
                elif event.code == 310 and event.value == 1: # L1
                    os.system("xdotool click 4")
                elif event.code == 311 and event.value == 1: # R1
                    os.system("xdotool click 5")

                # System Keys (Start / Select Combo for Exit)
                elif event.code in [704, 12]:
                    state["select"] = (event.value == 1)
                    if event.value == 1: os.system("xdotool key Escape")
                elif event.code in [705, 13]:
                    state["start"] = (event.value == 1)
                    if event.value == 1: os.system("xdotool key Return")
                
                if state.get("select") and state.get("start"):
                    os.system("xdotool getactivewindow windowkill")

                # D-Pad to Arrow Keys
                elif event.value == 1: # Only trigger on press
                    if event.code == 544: os.system("xdotool key Up")
                    elif event.code == 545: os.system("xdotool key Down")
                    elif event.code == 546: os.system("xdotool key Left")
                    elif event.code == 547: os.system("xdotool key Right")
                    
                    # ABXY Face Buttons
                    elif event.code == 305: os.system("xdotool key space")     # A
                    elif event.code == 304: os.system("xdotool key BackSpace") # B
                    elif event.code == 307: os.system("xdotool key Tab")       # X
                    elif event.code == 308: os.system("xdotool key Super_L")   # Y

            elif event.type == ecodes.EV_ABS:
                if event.code == 0: state["lx"] = event.value
                elif event.code == 1: state["ly"] = event.value
                elif event.code == 3: state["rx"] = event.value
                elif event.code == 4: state["ry"] = event.value
    except Exception as e:
        pass

for dev in devices:
    threading.Thread(target=process_events, args=(dev,), daemon=True).start()

# Keep main thread alive
while True:
    time.sleep(1)
