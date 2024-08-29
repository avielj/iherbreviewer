#!/bin/bash

# Check for OS type
OS_TYPE=$(uname)

# Function to install prerequisites on macOS
install_mac() {
    echo "Installing prerequisites on macOS..."

    # Install Python
    brew install python

    # Install Google Chrome
    brew install --cask google-chrome

    # Install ChromeDriver
    brew install chromedriver

    # Install required Python packages
    pip install -r requirements.txt
}

# Function to install prerequisites on Linux
install_linux() {
    echo "Installing prerequisites on Linux..."

    # Install Python
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip

    # Install Google Chrome
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb
    sudo apt-get install -f

    # Install ChromeDriver
    sudo apt-get install -y chromedriver

    # Install required Python packages
    pip3 install -r requirements.txt
}

# Function to install prerequisites on Windows
install_windows() {
    echo "Please manually install the following prerequisites on Windows:"
    echo "1. Python: https://www.python.org/downloads/"
    echo "2. Google Chrome: https://www.google.com/chrome/"
    echo "3. ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads"
    echo "4. Required Python packages: pip install -r requirements.txt"
}

# Determine OS type and call the appropriate function
case "$OS_TYPE" in
    "Darwin")
        install_mac
        ;;
    "Linux")
        install_linux
        ;;
    *)
        echo "Unsupported OS type: $OS_TYPE"
        echo "For Windows, please follow the manual installation instructions."
        install_windows
        ;;
esac
