import time
import board
import busio
import adafruit_tcs34725
import neopixel

# Define specific I2C pins for the sensor
scl_pin = board.IO40
sda_pin = board.IO38

# Create I2C bus using specified SCL and SDA pins
i2c = busio.I2C(scl_pin, sda_pin)

# Create sensor object with the new I2C bus
sensor = adafruit_tcs34725.TCS34725(i2c)

# Define NeoPixel pin and number of pixels
pixel_pin = board.IO12
num_pixels = 1  # Assuming you have 1 NeoPixel

# Create NeoPixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

# Main loop reading color and printing it every second.
while True:
    # Obtain RGB values as bytes
    r, g, b = sensor.color_rgb_bytes  # This already provides RGB in 0-255 format

    # Print RGB values in the format "R,G,B"
    print("RGB color: {0},{1},{2}".format(r, g, b))

    # Set NeoPixel to the color read from the sensor
    pixels.fill((r, g, b))

    # Optional: Read the color temperature and lux of the sensor too
    temp = sensor.color_temperature
    lux = sensor.lux
    print("Temperature: {0}K Lux: {1}\n".format(temp, lux))

    time.sleep(1.0)
