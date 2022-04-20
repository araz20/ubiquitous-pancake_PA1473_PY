#!/usr/bin/env pybricks-micropython
import sys
import __init__

# from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase


# Per-run-variables
left_motor_port = Port.A
right_motor_port = Port.D
front_sensor_port = Port.S3
parking_light_port = Port.S1
turn_light_port = Port.S4
obstacle_sensor = UltrasonicSensor(Port.S4)
#Robot
ev3 = EV3Brick()
left_motor= Motor(Port.C, positive_direction=Direction.CONTERCLOCKWISE, geros=[12,20])
rigth_motor= Motor(Port.B, positive_direction=Direction.CONTERCLOCKWISE, geros=[12,20])
robot = DriveBase(left_motor, rigth_motor, wheel_diameter=56, axle_track=118)
# Sensors
front_sensor = UltrasonicSensor(front_sensor_port)
parking_light = ColorSensor(parking_light_port) # Sensor som kollar efter banan
# color sensor.
line_sensor = ColorSensor(Port.S3)
# Sensors
front_sensor = UltrasonicSensor(Port.S3)
left_light = ColorSensor(Port.S1) # Sensor som kollar efter banan
right_light = ColorSensor(Port.S4) # Sensor som känner av om vi ska parkera

# Constants
BLACK = 9
WHITE = 85
THRESHOLD_RIGHT = 30
THRESHOLD_LEFT = 40
DRIVE_SPEED = 50
GAIN = 1.2
PARKING_TIME = 1000 * 5 # milliseconds
COLLISION_DISTANCE = 0 
turn_rate = 0

def park():
    parked = False
    while not parked:
        parked = True # När parkeringsanimationen är klar
    return False


def drive(turn_rate: int):
    robot.drive(DRIVE_SPEED, turn_rate)
    wait(10)

def main():
    while True:
        colliding = bool(front_sensor.distance() < COLLISION_DISTANCE) # Ändra tröskelvärde
        parking = bool(0 < right_light.reflection() < 1) # Ändra tröskelvärden

        if colliding: # Stanna temporärt
                robot.stop()
        elif parking: # Parkera
                parking = park()
        else: # Följ linjen som vanligt
            reflection = 0
            deviation = 0
            turn_rate = 0
            while obstacle_sensor.distance() > 300:
             wait(10)
        return True
if __name__ == '__main__':
    sys.exit(main())
