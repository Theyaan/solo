# ArkStandalone (Solo)

A lightweight, ultra-fast kiosk-mode GUI application launcher for ArkOS/DarkOS and similar retro handheld operating systems.

ArkStandalone (via the `solo` command) allows you to run standard Linux desktop applications (like web browsers, media players, or file managers) directly on the framebuffer without the massive overhead of a full Desktop Environment like XFCE.

## Features
- **Ultra-Lightweight**: Bypasses heavy desktop environments. Uses `openbox` to perfectly maximize your app without borders.
- **Built-in Mouse Emulation**: Automatically translates your device's joysticks and buttons into mouse movements and clicks.
- **On-Screen Keyboard**: Fully supports `onboard` for typing, mapped directly to your console's **FN** button for instant toggling.
- **Panic Quit Combo**: Hold **Start + Select** at any time to instantly kill the app and safely drop back into EmulationStation.
- **Global Command**: Launch apps from anywhere using the simple `solo` command.

## Installation

1. Clone or download this repository to `/roms/tools/solo/`.
2. Run the automated install script to install dependencies, set permissions, and create the global `solo` command:
   ```bash
   cd /roms/tools/solo
   chmod +x install.sh
   ./install.sh
   ```

## Usage

Simply pass the command of the GUI application you want to run to `solo`:

```bash
solo "vlc"
solo "falkon"
solo "thunar"
```

You can use this directly in the terminal, or place it inside a `.sh` file in your `/roms/ports/` directory to launch apps directly from EmulationStation!

## Controls
- **Left/Right Joysticks**: Move Mouse
- **L2 / R2**: Left Click / Right Click
- **L1 / R1**: Scroll Up / Scroll Down
- **D-Pad**: Arrow Keys
- **A / B / X / Y**: Space / Backspace / Tab / Super (Windows) Key
- **Select / Start**: Escape / Enter
- **FN (Center/Menu button)**: Toggles the On-Screen Keyboard
- **Start + Select (Hold)**: Force Quit app and return to EmulationStation

**The mouse emulation is highly inspired(basically a copy) by sjsltech’s xfce Desktop environment mouse emulation so huge thanks to him.**
