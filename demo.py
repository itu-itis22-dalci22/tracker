from RpiMotorLib import RpiMotorLib

direction_pin = 21      # nemma 17
step_pin = 19           # nemma 17
mode_pins = 29, 31, 33  # nemma 17

steps = 200
steptype = "Full"
stepdelay = 0.005
verbose = False
initialdelay = 0.05

print("A4988Nema Test")
a4988_nema = RpiMotorLib.A4988Nema(direction_pin, step_pin, mode_pins, "A4988")

while True:
  for clockwise in [True, False]:
     a4988_nema.motor_go(clockwise, steptype, steps, stepdelay, verbose, initialdelay)
