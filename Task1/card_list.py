import serial

serialPort = serial.Serial(port = "COM3", baudrate = 9600,
                            bytesize = 8, timeout = 2, stopbits = serial.STOPBITS_ONE)

serialPort.open()
serialString = ""

while(1):

    if (serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        print(serialString.decode('Ascii'))
