#include <DHT.h>

#define pinoDHT 23
#define pinoN 22
#define pinoP 34
#define pinoK 35
#define modeloDHT DHT22
#define pinoLDR 25
#define pinoRele 15

// LDR Configs
const float GAMMA = 0.7;
const float RL10 = 50;

DHT dht(pinoDHT, modeloDHT);

bool estadoRele = false;

void setup() {
    Serial.begin(115200);
    pinMode(pinoN, INPUT_PULLUP);
    pinMode(pinoP, INPUT_PULLUP);
    pinMode(pinoK, INPUT_PULLUP);
    pinMode(pinoLDR, INPUT);
    pinMode(pinoRele, OUTPUT);
    digitalWrite(pinoRele, LOW); // Garante que o relé comece desligado
    Serial.println("Iniciando sensores...");
    dht.begin();
}

float verificaPH(){
    float ph = 0;
    float lux = analogRead(pinoLDR);
    Serial.print("Valor Lux Analog: ");
    Serial.println(lux);

    if(lux > 4000) {
        ph = 0;
    } else if(lux > 3950) {
        ph = 1;
    } else if(lux > 3800) {
        ph = 2;
    } else if(lux > 3700) {
        ph = 3;
    } else if(lux > 3500) {
        ph = 4;
    } else if(lux > 2900) {
        ph = 5;
    } else if(lux > 2500) {
        ph = 5.5;
    } else if(lux > 2000) {
        ph = 6;
    } else if(lux > 500) {
        ph = 7;
    } else if(lux > 400) {
        ph = 8;
    } else if(lux > 300) {
        ph = 9;
    } else if(lux > 200) {
        ph = 10;
    } else if(lux > 150) {
        ph = 11;
    } else if(lux > 70) {
        ph = 12;
    } else if(lux > 50) {
        ph = 13;
    } else {
        ph = 14;
    }

    return ph;
}

int verificaNPK() {
    bool N = false;
    bool P = false;
    bool K = false;
    int pH = 0;

    //VERIFICA OS NUMEROS DE NPK
    int valorN = digitalRead(pinoN);
    int valorP = digitalRead(pinoP);
    int valorK = digitalRead(pinoK);

    String message = "";

    if(valorN == HIGH) {
        N = true;
        Serial.println("Nitrogenio: Adequado");
    }else{
        Serial.println("Nitrogenio: Baixo");
        N = false;
    }

    if(valorP == HIGH) {
        P = true;
        Serial.println("Fosforo: Adequado");
    } else {
        Serial.println("Fosforo: Baixo");
        P = false;
    }

    if(valorK == HIGH) {
        K = true;
        Serial.println("Potassio: Adequado");
    } else {
        Serial.println("Potassio: Baixo");
        K = false;
    }

    //Verifica para café qual a necessidade de NPK
    //NPK IDEAL PARA CAFÉ: 4-14-8
    if(N == true && P == true && K == true) {
        message = "NPK Adequado";
        pH = 6.0; // pH ideal para café
    } else if(N == false && P == false && K == false) {
        message = "NPK Muito Baixo, adubar imediatamente na proporção 4-14-8";
        pH = 0; // pH muito baixo
    } else if(N == false && P == false) {
        pH = 3; // pH muito baixo
        message = "N e P Baixo, adubar imediatamente na proporção 4-14-8";
    } else if(N == false && K == false) {
        pH = 4; // pH baixo
        message = "N e K Baixo, adubar imediatamente na proporção 4-14-8";
    } else if(P == false && K == false) {
        pH = 5; // pH baixo
        message = "P e K Baixo, adubar imediatamente na proporção 4-14-8";
    } else if(N == false) {
        pH = 5.5; // pH um pouco baixo
        message = "N Baixo, adubar imediatamente na proporção 4-12-7";
    } else if(P == false) {
        pH = 5.5; // pH um pouco baixo
        message = "P Baixo, adubar imediatamente na proporção 3-14-6";
    } else if(K == false) {
        pH = 5.5; // pH um pouco baixo
        message = "K Baixo, adubar imediatamente na proporção 3-10-8";
    }

    Serial.println(message);
    return pH;
}

void setRele(){
    if(estadoRele) {
        digitalWrite(pinoRele, HIGH);
        Serial.println("Bomba de irrigação ligada.");
    } else {
        digitalWrite(pinoRele, LOW);
        Serial.println("Bomba de irrigação desligada.");
    }
}

void verificaUmidade(){
    //Verifica a umidade do solo
    float umidade_solo = dht.readHumidity();

    if(isnan(umidade_solo)) {
        Serial.println("Falha ao ler do sensor DHT!");
        return;
    }

    Serial.print("Umidade: ");
    Serial.print(umidade_solo);

    if(umidade_solo < 40) {
        Serial.println(" - Solo Seco");
        Serial.println("Ativando a bomba de irrigação");
        estadoRele = true;
    } else if(umidade_solo >= 40 && umidade_solo < 60) {
        Serial.println(" - Solo Ideal");
        estadoRele = false;
    } else {
        Serial.println(" - Solo Encharcado");
        estadoRele = false;
    }

    setRele();
}

void loop() {

    int pH_NPK = verificaNPK();

    Serial.print("pH do solo estimado a partir da definição dos botões de NPK: ");
    Serial.println(pH_NPK);

    float ph = verificaPH(); // Lê o valor do sensor de LDR como se fosse um sensor de PH
    Serial.print("pH do solo estimado a partir do sensor LDR: ");
    Serial.println(ph);

    //ESCRITA MANUAL POR CONTA DE NÃO TER UM SENSOR DE PH
    int ldrNewValue = map(pH_NPK, 0, 9, 0, 3000);
    analogWrite(pinoLDR, ldrNewValue);

    ph = verificaPH(); // Lê o valor do sensor de LDR como se fosse um sensor de PH
    Serial.print("pH do solo LDR atualizado a partir da definição dos botões de NPK: ");
    Serial.println(ph);

    verificaUmidade();

    delay(2000);
}