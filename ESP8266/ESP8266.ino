#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>

// colocar o SSID do Wi-Fi
const char* ssid = "";
// colocar a senha 
const char* password = "";

ESP8266WebServer server(80);

const int led = 2;
const int relayPin = 0;

void acender() {
 digitalWrite(led, 0);
 digitalWrite(relayPin, LOW);
 server.send(200, "text/plain", "O led foi ligado!");
}

void apagar() {
 digitalWrite(led, 1);
 digitalWrite(relayPin, HIGH);
 server.send(200, "text/plain", "O Led foi desligado!");
}

void handleNotFound(){
 digitalWrite(led, 1);
 String message = "File Not Found\n\n";
 message += "URI: ";
 message += server.uri();
 message += "\nMethod: ";
 message += (server.method() == HTTP_GET)?"GET":"POST";
 message += "\nArguments: ";
 message += server.args();
 message += "\n";
 for (uint8_t i=0; i<server.args(); i++){
   message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
 }
 server.send(404, "text/plain", message);
 digitalWrite(led, 0);
}

void setup(void){
 pinMode(led, OUTPUT);
 pinMode(relayPin, OUTPUT);
 digitalWrite(relayPin, LOW);  // Define o relé como desligado no início
 digitalWrite(led, 1);
 Serial.begin(115200);
 WiFi.begin(ssid, password);
 Serial.println("");


 // Wait for connection
 while (WiFi.status() != WL_CONNECTED) {
   delay(500);
   Serial.print(".");
 }
 Serial.println("");
 Serial.print("Conectado a ");
 Serial.println(ssid);
 Serial.print("endereço de IP: ");
 Serial.println(WiFi.localIP());


 if (MDNS.begin("esp8266")) {
   Serial.println("Resposta MDNS iniciada");
 }


 server.on("/", handleRoot);
 server.on("/acender", acender);
 server.on("/apagar", apagar);



 server.on("/inline", [](){
   server.send(200, "text/plain", "isso funciona também");
 });

 server.onNotFound(handleNotFound);

 server.begin();
 Serial.println("servidor HTTP iniciado");
}

void loop(void){
 server.handleClient();
}