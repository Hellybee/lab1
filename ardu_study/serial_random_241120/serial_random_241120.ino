void setup() {
  // 시리얼 통신 시작, 보드 속도는 9600
  Serial.begin(9600);
}

void loop() {
  // 0에서 100까지의 랜덤 숫자 생성
  int randomValue = random(0, 101);  // 0 ~ 100 사이의 랜덤 숫자

  // 랜덤 숫자를 시리얼 포트를 통해 전송
  Serial.println(randomValue);
  // 1초 대기
  delay(1000);  // 1초 간격으로 전송
}
