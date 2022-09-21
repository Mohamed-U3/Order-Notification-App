from base64 import encode
from tkinter import *
from tkinter import messagebox
import serial.tools.list_ports

#Create the main window of the app
WindowFrame = Tk()

#change app Text title
WindowFrame.title("Orders Notification App")

#set dimintions
WindowFrame.geometry("600x400")

#Writing age label
the_text = Label(WindowFrame, text="Click on the Button of the required table to be notified"
                    ,height=2,font=("Arial",12))
the_text.pack() #Place the text into the main window

def turn_led_on():
    serialInst.write('H'.encode())
def turn_led_off():
    serialInst.write('L'.encode())

# create Buttons
btn1 = Button(WindowFrame, text="Turn LED on",
                width=10, height=2,bg="#e92e63",fg="white",borderwidth=2,command=turn_led_on).pack()
btn2 = Button(WindowFrame, text="Turn LED off",
                width=10, height=2,bg="#e92e63",fg="white",borderwidth=2,command=turn_led_off).pack()

while True:
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()

    portList = []

    # passing through all the ports that is connected to the computer
    for port in ports:
        portList.append(str(port))
    # automatic Select Arduino if found
    for x in range(0,len(portList)):
        if "Arduino Uno" in portList[x]:
            portvar = portList[x].split(' ', 1)[0]
            print("\nComputer selected")
            print(portList[x])
    
    # check if Computer Select port or not
    try:
        portvar
    except NameError: # If not selected
        print("Computer did not select port\n")
        print("The available Ports are :")
        # passing through all the ports that is connected to the computer then printing them
        for port in portList:
            print(port)
        #input selected port
        val = input("\nselect port: COM")
        #user select one of the existed port then printing the selected one
        for x in range(0,len(portList)):
            if portList[x].startswith("COM" + str(val)):
                portvar = "COM" + str(val)
                print("\nYou selected")
                print(portList[x])
    else:   #If Selected Then initializing serial port
        serialInst.baudrate = 9600
        serialInst.port = portvar
        serialInst.open()
        break

    # insure user Selected the port manually
    try:
        portvar
    except NameError:
        print("You selected non existing Port it Seems")
    else:   #initializing serial port
        serialInst.baudrate = 9600
        serialInst.port = portvar
        serialInst.open()
        break

#Run App for Infinty time
WindowFrame.mainloop()