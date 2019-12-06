#define TAMANHO 10
float historico[TAMANHO];

float temperatura;
unsigned long tempoInicial;

float leituraSimples(){
  float media = 0;
  for(int i = 0; i < 5; i++){
    media += analogRead(A0)*0.0488;     
  }
  media /= 5;
  Serial.println(media);
  return media;
}

void insereLeitura(float novaLeitura){
  for(int i = 1; i < TAMANHO; i++){
      historico[i-1] = historico[i];
//      Serial.print(historico[i-1]);
//      Serial.print(" ");
  }
//  Serial.println("");
  historico[TAMANHO-1] = novaLeitura;
}

void lerHistorico(){
  for(int i = 0; i < TAMANHO; i++){
    Serial.print(historico[i]);
    Serial.print(" ");
  }
  Serial.println(" ");
}

void setup() {
  tempoInicial = millis();
  Serial.begin(115200);
}

void loop() {
  unsigned long tempoAtual = millis();  
  if(tempoAtual - tempoInicial > 2000){
    temperatura = leituraSimples();
    insereLeitura(temperatura);
    tempoInicial = millis();
  }
  
  if(Serial.available() > 0) {
    char comando = Serial.read();
    if (comando == 's'){
      leituraSimples();
    }

    if (comando == 'h'){
      lerHistorico();
    }  
  }
}
