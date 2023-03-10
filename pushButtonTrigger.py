import board
from alertDriver import AlertSystem
import digitalio




# Configure the internal GPIO connected to the LED as a digital output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
# Configure the internal GPIO connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set the internal resistor to pull-up
# Print a message on the serial console
print('Hello! My LED is controlled by the button.')
# Loop so the code runs continuously
while True:
    led.value = not button.value # if the button is pressed

    if not button.value:
        AlertSystem()
