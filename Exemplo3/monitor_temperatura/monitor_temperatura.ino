void setup() {
  Serial.begin(115200);
}

void loop() {
  float temperatura = analogRead(A0)*0.0488;
  if(Serial.available() > 0){
    char comando = Serial.read();
    if(comando == 't'){
      Serial.println(temperatura);
    }
  }
}
