
import RPi.GPIO as GPIO
import time
import sensor_module

MOTOR_PIN_A = 17
MOTOR_PIN_B = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN_A, GPIO.OUT)
GPIO.setup(MOTOR_PIN_B, GPIO.OUT)

def move_forward():
    GPIO.output(MOTOR_PIN_A, GPIO.HIGH)
    GPIO.output(MOTOR_PIN_B, GPIO.LOW)
    time.sleep(1) 
def move_backward():
    GPIO.output(MOTOR_PIN_A, GPIO.LOW)
    GPIO.output(MOTOR_PIN_B, GPIO.HIGH)
    time.sleep(1)

while True:
    if sensor_module.is_leak_detected():
        move_backward()
        time.sleep(2)
    else:
        move_forward()
        time.sleep(2)
