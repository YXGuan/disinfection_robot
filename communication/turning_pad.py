# IR line follower for 2 base
# actively updating collision avoidance sensor?
# can not trigger too often
# Node Red  Pythohn program at conflict,
# Have to use SSH to terminate the node red first to run python program?
# In practice, this works poorly!


import RPi.GPIO as GPIO
import time
from time import sleep

# black --> 1
# white --> 0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

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


#CONDITIONS
while True:
    GPIO.output(TRIG, True)
    time.sleep(0.00001)                      
    GPIO.output(TRIG, False)
    i=GPIO.input(7)   

    while GPIO.input(ECHO)==0:               
        pulse_start = time.time()              

    while GPIO.input(ECHO)==1:               
        pulse_end = time.time()                

    pulse_duration = pulse_end - pulse_start 

    distance = pulse_duration * 17150        

    distance = round(distance, 2)
    
    if distance < 20: #obstacle
        print("obstacle detected")
        GPIO.output(29,0)
        GPIO.output(31,0)
        GPIO.output(33,0)
        GPIO.output(35,0)
        time.sleep(2)
        

    else:      
        print("Distance:",distance ,"cm")    #- 0.5
        
                      

        
        if i==0:#if white, go forward
            print (" forward  ",i)
            GPIO.output(29,1)
            GPIO.output(31,0)
            GPIO.output(33,0)
            GPIO.output(35,1)
            
        else:# if black, turn right for 1 seconds
            print (" right  ",i)
            GPIO.output(29,0)
            GPIO.output(31,1)
            GPIO.output(33,0)
            GPIO.output(35,1)
            time.sleep(2)
            GPIO.output(29,1)
            GPIO.output(31,0)
            GPIO.output(33,0)
            GPIO.output(35,1)
            time.sleep(2)
        


    time.sleep(0.1)#this is in second


