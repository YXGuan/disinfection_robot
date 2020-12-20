char t;

// Motor A connections
int enA = 6;
int in1 = 2;
int in2 = 3;
// Motor B connections
int enB = 7;
int in3 = 4;
int in4 = 5;


void setup() {

  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  if (Serial.available() > 0) {
    t = Serial.read();
    Stop(); //initialize with motors stoped
    //Change pin mode only if new command is different from previous.
    //Serial.println(command);
    switch (t) {
      case '1':
        forward();
        break;
      case '2':
        back();
        break;
      case '3':
        left();
        break;
      case '4':
        right();
        break;
      case '5':
        Stop();
        break;
    }
  }
}

void forward() {           //move forward(all motors rotate in forward direction)
  digitalWrite (enA, HIGH);
  digitalWrite (enB, HIGH);

  digitalWrite (in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite (in3, LOW);
  digitalWrite(in4, HIGH);
  delay(1000);
}

void back() {     //move reverse (all motors rotate in reverse direction)
  // Turn off motors - Initial state
  digitalWrite (enA, HIGH);
  digitalWrite (enB, HIGH);
  digitalWrite (in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite (in3, HIGH);
  digitalWrite(in4, LOW);
  delay(2000);
}

void left() {     //turn right (left side motors rotate in forward direction, right side motors doesn't rotate)
  digitalWrite (enA, HIGH);
  digitalWrite (enB, HIGH);
  digitalWrite (in2, HIGH);
  digitalWrite(in1, LOW);
  digitalWrite (in4, LOW);
  digitalWrite(in3, HIGH);
  delay(1000);

}

void right() {     //turn left (right side motors rotate in forward direction, left side motors doesn't rotate)
  digitalWrite (enA, HIGH);
  digitalWrite (enB, HIGH);
  digitalWrite (in2, LOW);
  digitalWrite(in1, HIGH);
  digitalWrite (in4, HIGH);
  digitalWrite(in3, LOW);
  delay(1000);

}

void Stop() {     //STOP (all motors stop)
  digitalWrite (enA, LOW);
  digitalWrite (enB, LOW);
}
