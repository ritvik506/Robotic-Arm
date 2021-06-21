from getkey import getkey
import RPi.GPIO as GPIO
import time

left_right = 0
up_down = 0

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

servo_base = GPIO.PWM(18, 50)
servo_arm = GPIO.PWM(3, 50)

servo_arm.start(0)
servo_base.start(0)

key = getkey()
while key != 'q':
    key = getkey()
    if key == 'w':  # Conveys to Arm Servo
        up_down -= 1
    elif key == 's':  # Conveys to Arm Servo
        up_down += 1
    elif key == 'a':  # Conveys to Base Servo
        left_right -= 1
    elif key == 'd':  # Conveys to Base Servo
        left_right += 1
    servo_base.ChangeDutyCycle(1.5+(left_right/9))
    servo_arm.ChangeDutyCycle(1.5+(up_down/9))
    time.sleep(0.005)

servo_arm.stop()
servo_base.stop()
GPIO.cleanup()
print("Motion Stopped")
