/*
 * Simple light and temperature sensor reading program
 * Written by Nanik Adnani for the Make U of T Hackathon
 * February 19th 2022
 */


int val;            //used for storing the value of recently read sensors
int tempPin = 1;    //analog pin the centre of the temperature sensor is connected to
int lightPin = 2;   //analog pin the LDR is connected to

void setup()
{
  Serial.begin(9600);   //start writing to serial
}
void loop()
{
  val = analogRead(tempPin);            //read the temperature
  float voltage = ( val/1024.0)*5000;   //translate ADC value to millivolts
  float cel = voltage/10;               //translate millivolts to celcius (formula in datasheet)
  Serial.print("TEMPRATURE = ");        //print temperature
  Serial.print(cel);
  Serial.print("*C");
  Serial.println();
  val = analogRead(lightPin);           //measure intensite of light - no unit conversion, for this project we just measure the relative brightness (0 = dark, 1024 = very bright).
  Serial.print("LIGHT = ");             //print light to serial
  Serial.print(val);
  Serial.println();
  delay(1000);
}
