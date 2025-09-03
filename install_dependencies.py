#!/usr/bin/env python3
"""
Installation script for web scraping dependencies.
Run this script to install all required packages.
"""

import subprocess
import sys

def install_package(package):
    """Install a package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError:
        print(f"✗ Failed to install {package}")
        return False

def main():
    """Install all required dependencies."""
    print("Installing web scraping dependencies...")
    print("=" * 50)
    
    packages = [
        "beautifulsoup4==4.12.2",
        "lxml==4.9.3",
        "requests==2.31.0"
    ]
    
    success_count = 0
    for package in packages:
        if install_package(package):
            success_count += 1
    
    print("=" * 50)
    if success_count == len(packages):
        print("✓ All dependencies installed successfully!")
        print("You can now run: python3 webscraping.py")
    else:
        print(f"✗ Only {success_count}/{len(packages)} packages installed successfully.")
        print("Please check the error messages above and try again.")

if __name__ == "__main__":
    main()
