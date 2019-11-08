
def bpm():

    import serial
    import matplotlib.pyplot as plt
    #from drawnow import *
    import atexit
    import cv2
    import time

    values = []
    bpmlist = []
    plt.ion()
    cnt=0

    serialArduino = serial.Serial('COM3', 9600)

    def plotValues():
        plt.title('Serial value from Arduino')
        plt.grid(True)
        plt.ylabel('Values')
        plt.plot(values, 'rx-', label='values')
        plt.legend(loc='upper right')

    def doAtExit():
        serialArduino.close()
        print("Close serial")
        print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

    #atexit.register(doAtExit)

    print("Open = " + str(serialArduino.isOpen()))


    for i in range(0,26):
        values.append(0)

    start_time = time.time()
    while True:
        while (serialArduino.inWaiting()==0):
            pass
        valueRead = serialArduino.readline(500)
        bpm = valueRead.decode()[5:8]
        try:
            current_time = time.time()
            if current_time - start_time >10:
                break
            valueInInt = int(bpm)
            print(valueInInt)
            if valueInInt <= 120:
                if valueInInt >= 0:
                    bpmlist.append(valueInInt)
                    values.append(valueInInt)
                    values.pop(0)
                    #drawnow(plotValues)
                else:
                    print("negative number")
            else:
                print("too large")
                bpmlist.append(valueInInt)
        except ValueError:
            print("")


    return bpmlist
