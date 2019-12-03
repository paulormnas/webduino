#define LED 8
bool statusLED = false;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, statusLED);
}

void loop() {
  if(Serial.available() > 0){
    digitalWrite(LED, !statusLED);
    statusLED = !statusLED;
    char byteChegando = Serial.read();

    if(statusLED)
      Serial.println("O LED está ligado");
    else
      Serial.println("O LED está desligado");
  }
}
