#!/bin/bash
# install.sh for Solo (ArkStandalone)

echo "Installing dependencies..."
sudo apt update
sudo apt install -y openbox onboard xdotool python3-evdev dbus-x11 x11-xserver-utils

echo "Setting permissions..."
chmod +x solo
chmod +x kiosk-mouse-daemon.py

echo "Creating global shortcut..."
sudo ln -sf "$(pwd)/solo" /usr/local/bin/solo

echo "Installation complete!"
echo "You can now run apps using the 'solo' command. For example: solo \"vlc\""
