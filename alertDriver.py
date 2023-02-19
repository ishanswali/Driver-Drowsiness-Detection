
# Import libraries needed for blinking the LED
import board
import digitalio
import pwmio
import time
# Configure the internal GPIO connected to the LED as a digital output

def AlertSystem():
    led = digitalio.DigitalInOut(board.GP16)
    led.direction = digitalio.Direction.OUTPUT

    buzzer_pin = board.GP2


    # Initialize the buzzer as a digital output
    buzzer = digitalio.DigitalInOut(buzzer_pin)
    buzzer.direction = digitalio.Direction.OUTPUT

    # Define the duration of each buzzer state (in seconds)
    buzz_duration = 0.1

    # Define the number of times to turn the buzzer on and off
    buzz_count = 10

    # Loop to turn the buzzer on and off

    # Define the pins connected to the motor
    motor_pin1 = board.GP4
    motor_pin2 = board.GP5

    # Initialize the motor pins as digital outputs
    motor1 = digitalio.DigitalInOut(motor_pin1)
    motor1.direction = digitalio.Direction.OUTPUT
    motor2 = digitalio.DigitalInOut(motor_pin2)
    motor2.direction = digitalio.Direction.OUTPUT

    # Define the frequency and duty cycle for the PWM signal
    motor_pwm_frequency = 1000  # in Hertz
    motor_pwm_duty_cycle = 0.5  # between 0 (off) and 1 (full speed)

    # Print a message on the serial console
    print('Hello! My LED is blinking now.')
    # Loop so the code runs continuously


    # Set the duration of the timer in seconds
    timer_duration = 180

    # Get the current time in seconds since the epoch
    start_time = time.time()

    # Create a loop that runs until the timer duration has elapsed
    while time.time() - start_time < timer_duration:
        # Perform any desired actions here
        # ...

        # Check the elapsed time since the start of the timer
        elapsed_time = time.time() - start_time

        # Calculate the time remaining until the end of the timer
        time_remaining = timer_duration - elapsed_time

        # Do something with the time remaining (e.g. display it)
        print(f"Time remaining: {time_remaining:.2f} seconds")



        # Do any other desired actions here
        # ...
        led.value = True  # Turn on the LED
        time.sleep(0.15)  # wait 0.5 seconds
        led.value = False  # Turn off the LED
        time.sleep(0.15)  # wait 0.5 seconds
        # Initialize the PWM signal to control the motor speed
        motor_pwm = pwmio.PWMOut(motor_pin2, frequency=motor_pwm_frequency, duty_cycle=0)

        # Define the duration to run the motor (in seconds)
        motor_run_duration = 5.0

        # Turn the motor on
        motor1.value = True

        # Start the PWM signal to control the motor speed
        motor_pwm.duty_cycle = int(motor_pwm_duty_cycle * 65535)

        # Wait for the motor to run for the specified duration
        time.sleep(motor_run_duration)

        # Turn the motor off
        motor1.value = False

        # Stop the PWM signal
        motor_pwm.duty_cycle = 0
        for i in range(buzz_count):
            # Turn the buzzer on
            buzzer.value = True

            # Wait for the buzzer to buzz
            time.sleep(buzz_duration)

            # Turn the buzzer off
            buzzer.value = False

            # Wait for a short pause
            time.sleep(buzz_duration)

        # Pause the loop for a short time to avoid excessive CPU usage
        time.sleep(0.01)


import machine
import time

# set up the LED on GP17

# set up the UART object
uart = machine.UART(0, baudrate=9600)

while True:
    if uart.any():
        command = uart.read().decode().strip()
        AlertSystem()
