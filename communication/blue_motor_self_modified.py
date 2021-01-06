#bluetooth controlled motor

from bluedot import BlueDot
from gpiozero import Robot
from signal import pause
import RPi.GPIO as GPIO
import time
from time import sleep

# black --> 1
# white --> 0
bd = BlueDot()


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


#sensors are not used
#IR SENSOR INPUTS
GPIO.setup(7, GPIO.IN)
#ultra sonic sensor setup
TRIG = 11 
ECHO = 13
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)



#MOTORS

#MOTOR	left
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)

#MOTOR Right
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)

# Enable pin
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

#MOTOR OUTPUTS
GPIO.output(29,0)
GPIO.output(31,0)
GPIO.output(33,0)
GPIO.output(35,0)
GPIO.output(38,1)#pull high enable pin
GPIO.output(40,1)#pull high enable pin


def move(pos):
    if pos.top:
            GPIO.PWM(38, 100)
            GPIO.PWM(40, 100)
            #GPIO.output(38,1)#pull high enable pin
            #GPIO.output(40,1)#pull high enable pin
            GPIO.output(29,1)
            GPIO.output(31,0)
            GPIO.output(33,0)
            GPIO.output(35,1)
            print("forward")
    elif pos.bottom:
            GPIO.PWM(38, 100)
            GPIO.PWM(40, 100)
            #GPIO.output(38,1)#pull high enable pin
            #GPIO.output(40,1)#pull high enable pin
            GPIO.output(29,0)
            GPIO.output(31,1)
            GPIO.output(33,1)
            GPIO.output(35,0)
            print("back")
    elif pos.left:
            GPIO.PWM(38, 100)
            GPIO.PWM(40, 100)
            GPIO.output(38,1)#pull high enable pin
            GPIO.output(40,1)#pull high enable pin
            GPIO.output(29,1)
            GPIO.output(31,0)
            GPIO.output(33,1)
            GPIO.output(35,0)
            print("left")
    elif pos.right:
            GPIO.PWM(38, 100)
            GPIO.PWM(40, 100)
            GPIO.output(38,1)#pull high enable pin
            GPIO.output(40,1)#pull high enable pin
            GPIO.output(29,0)
            GPIO.output(31,1)
            GPIO.output(33,0)
            GPIO.output(35,1)
            print("right")

def stop():
    GPIO.PWM(38, 1)
    GPIO.PWM(40, 1)
    GPIO.output(38,0)
    GPIO.output(40,0)
    GPIO.output(29,0)
    GPIO.output(31,0)
    GPIO.output(33,0)
    GPIO.output(35,0)
    
while True:
    bd.when_pressed = move
    bd.when_moved = move
    bd.when_released = stop

pause()
