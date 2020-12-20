//It is a left side wall follower.

#include <AFMotor.h>
#include <SR04.h>

AF_DCMotor motor3(3, MOTOR34_64KHZ); // Define motor #3, 64KHz pwm
AF_DCMotor motor4(4, MOTOR34_64KHZ); // Define motor #4, 64KHz pwm

int WF_LEFT_US_SENSOR_TRIG = 18;
int WF_LEFT_US_SENSOR_ECHO = 17;
int WF_FRONT_US_SENSOR_TRIG = 16;
int WF_FRONT_US_SENSOR_ECHO = 15;

int NO_OBSTACLE = 0;
int OBSTACLE = 1;

int WF_DISTANCE = 12;
int WF_FRONT_DISTANCE = 16;

SR04 wf_sr04_left = SR04(WF_LEFT_US_SENSOR_ECHO,WF_LEFT_US_SENSOR_TRIG);
SR04 wf_sr04_front = SR04(WF_FRONT_US_SENSOR_ECHO,WF_FRONT_US_SENSOR_TRIG);

int WF_Left = 0;
int WF_Front = 0;

int WF_Left_Status = 0;
int WF_Front_Status = 0;

//Obstacle in Left: Keep Following: PID values
float WF_Kp = 30;
float WF_Ki = 0.003;
float WF_Kd = 8;

//Obstacle in Front: Take a turn: PID values
float MY_Kp_Front = 40;
float MY_Ki_Front = 0; 
float MY_Kd_Front = 20; 

float WF_Error = 0;
int WF_Correction = 0;
float WF_Integral = 0;
float WF_Derivative = 0;
float WF_LastError = 0;

float MY_Error_Front = 0;
float MY_Correction_F = 0;
float MY_Integral_Front = 0;
float MY_Derivative_Front = 0;
float MY_LastError_Front = 0;

int WF_LeftTurnSpeed = 0;
int WF_RightTurnSpeed = 0;

//Here 0 stands for true and 1 stands for false
int rightTurnBegin = 0;
int leftTurnBegin = 0;
int straightLineBegin = 0;



void setup() {
  // put your setup code here, to run once:
  delay(5000);
}

void loop() {
  // put your main code here, to run repeatedly:

beginning:

    WF_Front_Status = WF_GET_FRONT_US_STATUS();

    if(WF_Front_Status == OBSTACLE) {

        //Initialize WALL only once, just in the beginning of right turn
        if (rightTurnBegin == 0)
          WF_INITIALIZE_WALL();

        WF_CONTINUE_WALL_FRONT();

        //Make the right turn flag false, until the next time there arises a right turn
        rightTurnBegin = 1;
        straightLineBegin = 0;

        goto beginning;
    }

    //When a the robot starts following the straight line (until there is a obstacle), initialize the flag to true.
    rightTurnBegin = 0;

    WF_Left = wf_sr04_left.Distance();
    WF_Error = WF_Left - WF_DISTANCE;
    WF_Integral = (WF_Error + WF_Integral);
    WF_Derivative = (WF_Error - WF_LastError);

    WF_Correction = WF_Kp * WF_Error + WF_Kd * WF_Derivative + WF_Ki * WF_Integral;

    //if WF_Error is less than 10, means the robot is following the wall correctly, keep continuing
    if (WF_Error < 10) {

      //Initialize the wall, just in the beginning of straight line
      if (straightLineBegin == 0)
        WF_INITIALIZE_WALL();

      if(WF_Correction > 127 && WF_Correction > 0)
        WF_Correction = 127;

      if(WF_Correction < -127 && WF_Correction < 0)
        WF_Correction = -127;

      WF_LeftTurnSpeed = 128 - WF_Correction;
      WF_RightTurnSpeed = 128 + WF_Correction;

      leftTurnBegin = 0;
      straightLineBegin = 1;

    } else {
      
      //if WF_Error is greater than 10, means the robot has to take left turn

      //Initialize the wall and wall front, just in the beginning of left turn
      if (leftTurnBegin == 0) {
        WF_INITIALIZE_WALL();
        WF_INITIALIZE_WALL_FRONT();
      }

      //PID for left turn
      int speed = 2.5 * WF_Error + 8 * WF_Derivative;

      if (speed > 127 && speed > 0)
        speed = 127;

      if (speed < -127 && speed < 0)
        speed = -127;

      WF_LeftTurnSpeed = 128 - (speed);
      WF_RightTurnSpeed = 128 + (speed);

      leftTurnBegin = 1;
      straightLineBegin = 0;

    }

    motor3.setSpeed(WF_LeftTurnSpeed);
    motor3.run(FORWARD);
    motor4.setSpeed(WF_RightTurnSpeed);
    motor4.run(FORWARD);


    WF_LastError = WF_Error;
    WF_INITIALIZE_WALL_FRONT();

}


void WF_INITIALIZE_WALL(void) {
  WF_Integral = 0;
  WF_Derivative = 0;
  WF_LastError = 0;
}

void WF_INITIALIZE_WALL_FRONT(void) {
  MY_Integral_Front = 0;
  MY_Derivative_Front = 0;
  MY_LastError_Front = 0;
}


//When there is an obstacle in front, take a right turn with the PID parameters declared in the beginning of the program.

void WF_CONTINUE_WALL_FRONT(void) {

        WF_Front = wf_sr04_front.Distance();
        MY_Error_Front = (WF_Front - WF_FRONT_DISTANCE);
        MY_Integral_Front = (MY_Error_Front + MY_Integral_Front);
        MY_Derivative_Front = (MY_Error_Front - MY_LastError_Front);

        MY_Correction_F = MY_Kp_Front * MY_Error_Front + MY_Kd_Front * MY_Derivative_Front + MY_Ki_Front * MY_Integral_Front;

        if(MY_Correction_F > 127 && MY_Correction_F > 0)
          MY_Correction_F = 127;

        if(MY_Correction_F < -127 && MY_Correction_F < 0)
          MY_Correction_F = -127;

        WF_LeftTurnSpeed = 128 - MY_Correction_F;
        WF_RightTurnSpeed = 128 + MY_Correction_F;

        motor3.setSpeed(WF_LeftTurnSpeed);
        motor3.run(FORWARD);
        motor4.setSpeed(WF_RightTurnSpeed);
        motor4.run(FORWARD);

        MY_LastError_Front = MY_Error_Front;

}


int WF_GET_LEFT_US_STATUS(void) {
     if(wf_sr04_left.Distance() < WF_DISTANCE)
       return OBSTACLE;
     else
      return NO_OBSTACLE;
}

int WF_GET_FRONT_US_STATUS(void) {
     if(wf_sr04_front.Distance() < WF_FRONT_DISTANCE)
       return OBSTACLE;
     else
       return NO_OBSTACLE;
}
