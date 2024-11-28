int in1 = 8;  
int in2 = 9;
int ena = 7;

int sen1 = 5;
int sen2 = 6;
void setup() {
 
  Serial.begin(9600);
  pinMode(ena, 1);
  pinMode(in1, 1);
  pinMode(in2, 1);

  
  analogWrite(ena, 0);  // 초기화
  delay(5000);   
  Serial.println("--Encoder_motor--");
}

void loop() {
  unsigned long millisTime = millis();
  Serial.print("millisTime : ");
  Serial.println(millisTime);

  int v1 = millisTime%10;
  int v2 = (millisTime/10)%10;
  int v3 = (millisTime/100)%10; 
  int v4 =  (millisTime/1000)%10;
  

  Serial.print(v4);
  Serial.print(" : ");
  Serial.print(v3);
  Serial.print(" : ");  
  Serial.print(v2);
  Serial.print(" : ");  
  Serial.println(v1);
  
//  Serial.println("Fir------------------");
//  digitalWrite(in1, LOW);
//  digitalWrite(in2, LOW);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(ena, 60);
//  for(int i =0; i<255; i+=10){
//    analogWrite(ena, i);
//    Serial.print("속도 : ");
//    Serial.println(i);
//    delay(1000);
//  }
 // analogWrite(ena, 0);
 
}
