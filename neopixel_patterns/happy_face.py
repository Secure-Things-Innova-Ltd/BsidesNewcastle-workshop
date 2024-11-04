import machine
import neopixel
import time

# Setup for an 8x8 NeoPixel matrix
num_pixels = 64
pin = machine.Pin(0)  # Replace '0' with the correct GPIO pin number used for your setup
np = neopixel.NeoPixel(pin, num_pixels)

# Happy face pattern (rows from bottom to top)
happy_face = [
    0b00111100,
    0b01000010,
    0b10011001,
    0b10100101,
    0b10000001,
    0b10100101,
    0b10000001,
    0b01111110
]

# Function to display the happy face on the matrix
def display_pattern(pattern):
    for row in range(8):
        for col in range(8):
            pixel_index = row * 8 + col
            if (pattern[row] >> (7 - col)) & 1:
                np[pixel_index] = (0, 50, 0)  # Green color (R, G, B)
            else:
                np[pixel_index] = (0, 0, 0)  # Turn off the LED
    np.write()

try:
    # Display the happy face
    display_pattern(happy_face)
    time.sleep(5)  # Keep the pattern for 5 seconds

except KeyboardInterrupt:
    # Turn off all LEDs when Ctrl+C is pressed
    for i in range(num_pixels):
        np[i] = (0, 0, 0)
    np.write()
    print("\nProgram stopped safely.")
