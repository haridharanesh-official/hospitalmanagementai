
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(1000);
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://<flask-ip>:5000/vitals");
    http.addHeader("Content-Type", "application/json");

    String payload = "{\"patient_id\": \"bed1\", \"heart_rate\": 78, \"spo2\": 91, \"temperature\": 100.5, \"alcohol_level\": 0.02}";
    http.POST(payload);
    http.end();
  }
  delay(15000);
}
