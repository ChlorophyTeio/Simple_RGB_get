# Simple RGB Get

## Introduction
Simple_RGB_get is a Python script for the OpenMV IDE that allows you to capture RGB color values from a specific pixel location on the camera sensor. It provides a simple way to monitor and retrieve color information in real-time.

## Requirements
- OpenMV IDE: Make sure you have the OpenMV IDE installed on your computer. You can download it from the official OpenMV website.

## Getting Started
1. Clone or download the Simple_RGB_get.py script to your local machine.
2. Open the OpenMV IDE.
3. Connect your OpenMV camera to your computer using a USB cable.
4. In the OpenMV IDE, click on "Open Script" and select the Simple_RGB_get.py file.
5. Once the script is loaded, click on the "Run" button or press Ctrl+R to execute the script on your OpenMV camera.

## Usage
1. After running the script, you will see the camera feed in the OpenMV IDE window.
2. The script will continuously capture images from the camera sensor.
3. Every 5 seconds, it will print the RGB color values of the pixel at coordinates (160, 120) in the console.
4. Additionally, a white crosshair will be drawn on the camera feed at the specified pixel location.

## Customization
- You can modify the pixel coordinates by changing the values in the `get_pixel()` function call.
- Adjust the time interval for color capture by modifying the value in the `if current_time - prev_time >= 5:` condition.

## Troubleshooting
- Make sure you have correctly set up the OpenMV IDE and connected your OpenMV camera to your computer.
- If you encounter any issues or errors, refer to the OpenMV documentation or community forums for assistance.
