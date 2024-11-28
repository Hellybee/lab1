#define ENA 7
#define IN1 8
#define IN2 9

#define ENCODER_B_A 6
#define ENCODER_B_B 5

byte encoderBLast;
bool encoderBDir = true;
int encoderBCount = 0;

void ISR_encoderB() {
  byte encoderBA = digitalRead(ENCODER_B_A);
  if (encoderBLast == LOW && encoderBA == HIGH) {
    byte encoderBB = digitalRead(ENCODER_B_B);
    if (encoderBB == LOW) {
      encoderBDir = true;
    } else if (encoderBB == HIGH) {
      encoderBDir = false;
    }
  }
  encoderBLast = encoderBA;
  if (encoderBDir) {
    encoderBCount++;
  } else {
    encoderBCount--;
  }
}

void setup() {
  Serial.begin(9600);
  
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  pinMode(ENCODER_B_A, INPUT);
  pinMode(ENCODER_B_B, INPUT);
  
  attachInterrupt(digitalPinToInterrupt(ENCODER_B_A), ISR_encoderB, CHANGE);
}

unsigned long lastTime = 0;
bool logging = false;

void loop() {
  
  if (Serial.available()) {
    char cmd = Serial.read();
    if (cmd == 'f') {
      Serial.println("forward");
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      analogWrite(ENA, 125);
      logging = true;
    } if (cmd == 'b') {
      Serial.println("backward");
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      analogWrite(ENA, 125);
      logging = true;
    } else if (cmd == 's') {
      Serial.println("stop");
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      analogWrite(ENA, 0);
      logging = false;
    } 
  }

  unsigned long currTime = millis();
  if (logging && (currTime - lastTime > 100)) {
    Serial.print("encoderB = ");
    Serial.print(encoderBCount);
    Serial.println();
    lastTime = currTime;
  }
}
