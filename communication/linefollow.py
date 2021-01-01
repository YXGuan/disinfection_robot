# IR line follower for 2 base

import RPi.GPIO as GPIO
import time
from time import sleep

# black --> 1
# white --> 0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#IR SENSOR INPUTS

GPIO.setup(7, GPIO.IN)	#i                            
GPIO.setup(11,GPIO.IN)	#j
GPIO.setup(13,GPIO.IN)	#k
GPIO.setup(15,GPIO.IN)	#l
#GPIO.setup(33,GPIO.IN)	#m

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
        
    i=GPIO.input(7)                         
    j=GPIO.input(11)
    k=GPIO.input(13)
    l=GPIO.input(15)

    if i==0 and j==0 and k==0 and l==1:
                           
        print ("sharp right",i,j,k,l )
        GPIO.output(29,0)
        GPIO.output(31,1)
        GPIO.output(33,0)
        GPIO.output(35,1)
        
    elif i==0 and j==0 and k==1 and l==1 :

        print (" right  ",i,j,k,l)
        GPIO.output(29,0)
        GPIO.output(31,1)
        GPIO.output(33,0)
        GPIO.output(35,0)
        
    elif i==1 and j==1 and k==0 and l==0 :

        print (" left  ",i,j,k,l)
        GPIO.output(29,0)
        GPIO.output(31,0)
        GPIO.output(33,1)
        GPIO.output(35,0)
        
    elif i==1 and j==0 and k==0 and l==0 :

        print (" sharp left  ",i,j,k,l)
        GPIO.output(29,1)
        GPIO.output(31,0)
        GPIO.output(33,1)
        GPIO.output(35,0)

    elif i==0 and j==1 and k==1 and l==0 :

        print (" forward  ",i,j,k,l)
        GPIO.output(29,1)
        GPIO.output(31,0)
        GPIO.output(33,0)
        GPIO.output(35,1)
        
    elif i==1 and j==1 and k==1 and l==1 :

        print (" stop  ",i,j,k,l)
        GPIO.output(29,0)
        GPIO.output(31,0)
        GPIO.output(33,0)
        GPIO.output(35,0)
        
    else :
        print(i,j,k,l,"")
        print ("other case")
        
        GPIO.output(29,0)
        GPIO.output(31,0)
        GPIO.output(33,0)
        GPIO.output(35,0)

    time.sleep(0.1)#this is in second

