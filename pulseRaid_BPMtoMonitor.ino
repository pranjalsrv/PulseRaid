


#define USE_ARDUINO_INTERRUPTS true   
#include <PulseSensorPlayground.h>     

//  Variables
const int PulseWire = 0;      
const int LED13 = 13;          
int Threshold = 400;           
                               
PulseSensorPlayground pulseSensor;  


void setup() {   

  Serial.begin(9600);          // For Serial Monitor

  
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);       
  pulseSensor.setThreshold(Threshold);   
 
   if (pulseSensor.begin()) {
    Serial.println(" pulseSensor Object created");   
  }
}



void loop() {

 int myBPM = pulseSensor.getBeatsPerMinute(); 
                                               

if (pulseSensor.sawStartOfBeat()) {             
 Serial.print("BPM: ");                        
 Serial.println(myBPM);        
}

  delay(10);                    

}

  
