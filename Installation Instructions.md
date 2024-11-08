# Installation Instructions

This guide will help you set up your environment to run the code provided for the **“Intro to Electronics with NeoPixel and Pico”** workshop.

## Step 1: Install MicroPython on Your Raspberry Pi Pico
1. **Download MicroPython**:
   - Visit the [MicroPython download page](https://micropython.org/download/rp2-pico/) and download the latest firmware for the Raspberry Pi Pico.
2. **Flash MicroPython onto Your Pico**:
   - Connect your Raspberry Pi Pico to your computer while holding down the BOOTSEL button.
   - The Pico should appear as a USB drive on your computer.
   - Drag and drop the downloaded `.uf2` firmware file onto the Pico drive. It will reboot automatically and be ready with MicroPython.

## Step 2: Set Up Your Development Environment
1. **Install Thonny IDE**:
   - Download and install [Thonny IDE](https://thonny.org/), a beginner-friendly Python IDE.
2. **Connect to Your Pico**:
   - Open Thonny IDE.
   - Go to **Run** > **Select Interpreter**, choose **MicroPython (Raspberry Pi Pico)**, and select the appropriate port.
3. **Test Your Setup**:
   - Enter a simple `print("Hello, Pico!")` command in Thonny’s editor and run it to ensure the connection works.

## Step 3: Install Required Libraries
1. **neopixel Library**:
   - The `neopixel` library is typically included in the standard MicroPython firmware. To confirm, run the following command in Thonny:
     ```python
     import neopixel
     ```

## Step 4: Run the Workshop Code
1. **Upload Code**:
   - Copy the provided Python code for the 😊 face (`happy_face.py`) and 😞 face (`sad_face.py`) to your Pico.
   - Save one of the files as `main.py` if you want it to run automatically on boot.

2. **Run the Code**:
   - Run the code in Thonny or reset the Pico to see the selected pattern displayed on your NeoPixel matrix.

