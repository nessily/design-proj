
#include <Arduino_LSM6DS3.h>
#include <Firebase_Arduino_WiFiNINA.h>
#include <OneWire.h>
#include <DallasTemperature.h>
 
#define FIREBASE_HOST "turtles-ee1ed-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "d4XCbBblU5oNmk7rZwcOYEXONk0ZqrUyLrBUuuVy"
#define WIFI_SSID "BABABUIH"
#define WIFI_PASSWORD "OllieEmmy"
 
FirebaseData firebaseData;
 
String path = "/Arduino";


// Arduino digital pin 7
#define ONE_WIRE_BUS 7
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);



 void setup(void)
{
  Serial.begin(9600);
  sensors.begin();

 Serial.print("Connecting to WiFi…");
 int status = WL_IDLE_STATUS;
 while (status != WL_CONNECTED) {
 status = WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
 Serial.print(".");
 delay(300);
 }
 Serial.print(" IP: ");
 Serial.println(WiFi.localIP());
 Serial.println();
 
 Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH, WIFI_SSID, WIFI_PASSWORD);
 Firebase.reconnectWiFi(true);
}
void loop(void){ 
  float x, y;
  sensors.requestTemperatures();
  x = sensors.getTempFByIndex(0);
  y = sensors.getTempCByIndex(0);
  Serial.print("Degrees Celsius: ");
  Serial.print(y); 
  Serial.print(" - Degrees Fahrenheit: ");
  Serial.println(x); 
  delay(2000);
 
 // Send temps to Firebase with specific paths
 if (Firebase.setFloat(firebaseData, path + "/Temp/F", x)) {
 Serial.println(firebaseData.dataPath() + " = " + x);
 }
 if (Firebase.setFloat(firebaseData, path + "/Temp/C", y)) {
 Serial.println(firebaseData.dataPath() + " = " + y);
 } 
 
 else {
 Serial.println("Error: " + firebaseData.errorReason());
 }
 
 Serial.println();
 delay(1000);
 }
