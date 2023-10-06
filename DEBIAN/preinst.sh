#!/bin/bash
set -e
# Install dependencies
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

echo "Installing Dependencies..."
apt-get update 
apt-get install -y python3
echo "Dependencies installed..."

# Copy your Python script and files to the appropriate location
echo "copying the files to appropiate location..."
cp -r ../../vps/* /usr/local/bin/vps
echo "Copied Successfully..."
# Set permissions and ownership

echo "Setting Permissions..."
chmod +x /usr/local/bin/vps.py
chown root:root /usr/local/bin/vps.py
echo "Done..."
echo "Successfully installed the package!!!"
