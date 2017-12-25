#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Adafruit_NeoPixel.h>
 
const char* ssid = "<your ssid>";
const char* password = "<your password>";

#define DIM 16
#define MEDIUM 3
#define BRIGHT 1

#define NP_BRIGHTNESS DIM  //  DIM MEDIUM or BRIGHT

#define PIN 0
#define PIXELS 16

Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXELS, PIN, NEO_GRB + NEO_KHZ800);

long last_colour = 0;

void setup () {

  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
 
  Serial.begin(74880);
  Serial.print("\rConnecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
 
}

uint32_t component(uint32_t color, uint32_t mask, int i) {
  return ((color & mask) / i);
}

uint32_t brightness(uint32_t color, int i) {
  return (component(color, 0xff0000, i<<16) << 16)
       | (component(color, 0x00ff00, i<<8) << 8)
       |  component(color, 0x0000ff, i);
}

void updateColour(uint32_t payload_colour) {
  uint32_t np_colour = brightness(payload_colour, NP_BRIGHTNESS);
  for (int i=0; i < PIXELS; i++) {
    strip.setPixelColor(i, np_colour);
  }
  strip.show();
}

void loop() {
 
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    HTTPClient http;
 
    http.begin("http://api.thingspeak.com/channels/1417/field/2/last.txt");
    int httpCode = http.GET();

    if (httpCode > 0) {
 
      String payload = http.getString();

      if (payload.length() == 7) {
        char str[7];
        memcpy(str, &payload[1], 6);
        str[6] = '\0';
        long payload_colour = strtol(str, NULL, 16);
        if ((payload_colour != 0) and (payload_colour != last_colour)) {
          if(payload_colour == 16753920) {
            payload_colour = 15562758; // gamma correction for Orange
          }
          updateColour(payload_colour);
          last_colour = payload_colour;               
          Serial.print("Changing colour to: ");
        }
      } else {
        Serial.print("Bad colour: ");
      }
      Serial.println(payload);
    }
    http.end();   // Close connection
 
  }
 
  delay(2000);
 
}
