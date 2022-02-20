import serial
from datetime import datetime

serialPort = serial.Serial(port = "COM7", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE) # this sets the connection to the arduino
serialPort.close() # this helped us reduce errors 
serialPort.open() # we had to open the port to access the data that was being submitted

serialString = ""                           # Used to hold data coming over UART
with open('test.txt', 'a') as file:

    while(1):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        # Wait until there is data waiting in the serial buffer
        if(serialPort.in_waiting > 0):

            # Read data out of the buffer until a carraige return / new line is found
            serialString = serialPort.readline()

            # Print the contents of the serial data
            print(serialString.decode('Ascii')+ "Current Time =", current_time)

            # Tell the device connected over the serial port that we recevied the data!
            # The b at the beginning is used to indicate bytes!
            serialPort.write(b"Thank you for sending data \r\n")