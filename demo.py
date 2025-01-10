import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import signal
import sys

# Pin configuration
direction_pin = 21      # GPIO pin for direction control
step_pin = 19           # GPIO pin for stepping
mode_pins = (29, 31, 33)  # GPIO pins for microstepping mode

# Motor parameters
steps = 200             # Number of steps per movement
steptype = "Half"       # Step type: "Full", "Half", "1/4", "1/8", "1/16"
stepdelay = 0.005       # Delay between steps
verbose = False         # Verbose output
initialdelay = 0.05     # Initial delay before movement starts

# Initialize the A4988 stepper motor driver
a4988_nema = RpiMotorLib.A4988Nema(direction_pin, step_pin, mode_pins, "A4988")

# Function to handle cleanup on exit
def cleanup(signal, frame):
    print("\nExiting gracefully...")
    GPIO.cleanup()  # Release GPIO resources
    sys.exit(0)

# Attach signal handler for graceful exit
signal.signal(signal.SIGINT, cleanup)

# Main program
if __name__ == "__main__":
    print("Testing motor...")

    # Test loop to verify functionality (rotates 5 times in both directions)
    for i in range(5):  # Change the range to test more/less
        print(f"Cycle {i + 1} - Clockwise")
        a4988_nema.motor_go(True, steptype, steps, stepdelay, verbose, initialdelay)
        
        print(f"Cycle {i + 1} - Counterclockwise")
        a4988_nema.motor_go(False, steptype, steps, stepdelay, verbose, initialdelay)
    
    print("Test completed. Starting infinite loop...")

    # Infinite loop for continuous operation
    while True:
        for clockwise in [True, False]:
            direction = "Clockwise" if clockwise else "Counterclockwise"
            print(f"Rotating {direction}...")
            a4988_nema.motor_go(clockwise, steptype, steps, stepdelay, verbose, initialdelay)
