# Commuter_Science
  This entire project was created to find a simple and cheap way to collect data about your city as you drive around it. 

**CarSensorssss.ino**
---
This file was created to read data from the light & temperator sensors and print it to serial. 

**serial reader.py**
---
This file was created to collect the data from the serial and send it to a text file. Due to some errors while testing, we found the easiest way to send the findings to a text file was to redirect the standard output to a text file using the command `python "serial reader.py" > output.txt`.

**data_parser.py**
---
This file was created to parse the collected data and create an csv file that we could use to analyze and come to conclusions. 
