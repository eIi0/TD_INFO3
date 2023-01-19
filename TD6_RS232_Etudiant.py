# -*- coding:Latin-1 -*-
import serial
import serial.tools.list_ports
from  tkinter import *
from tkinter import ttk

def OpenPort():
    global ser
    global LClose
    portName = selected_port.get()
    ser = serial.Serial(portName[0:5])
    LClose.configure(bg = "yellow",text = 'Port Opened'+portName )

def ListPort():
    global Cport
    global LInfo
    listePorts = serial.tools.list_ports.comports()
    CPort['values'] = listePorts
    
def ClosePort():
    global LClose
    ser.close()
    LClose.configure(bg = "red",text = 'Port Closed' )

def ReadDataPort():
    global LData,LDataStr
    data = ser.readline()
    bindata = []
    hexdata = []
    for i in range(len(data)):
        bindata.append(data[i])
        hexdata.append(hex(data[i]))
    LData.configure(text = str(bindata))
    LDataStr.configure(text=str(data))
    LDataHexa.configure(text=str(hexdata))

def WriteData():
    ser.write(value)
    
    

#interface graphique
ser = serial.Serial()

fen1 = Tk()
fen1.geometry('600x400')
fen1.title("Centrale Meteo")
#label 
LPort = Label(fen1,text='Ports:')
LPort.grid(row=2,sticky=E)

#bouton liste port
BListePorts = Button(fen1,text = 'List Ports',command = ListPort)
BListePorts.grid(row=3,sticky=E)

#combo box
selected_port = StringVar()
CPort = ttk.Combobox(fen1, textvariable=selected_port)
CPort['state'] = 'readonly'
CPort.grid(row=4,sticky = E)

#button ouverture
BOpenPort = Button(fen1,text = 'Open Port',command= OpenPort)
BOpenPort.grid(row = 5,sticky = E)

#Label fermeture 
LClose = Label(fen1,text = 'Port Closed',bg = 'red')
LClose.grid(row = 1,column = 2,sticky = E)

#button fermeture
BClosePort = Button(fen1,text='Close Ports',command = ClosePort)
BClosePort.grid(row = 6,sticky=E)

# LInfo = Label(fen1,text='',bg = 'white')
# LInfo.grid(row = 7,column = 1,columnspan = 8)

#Button receive
BReceive  =Button(fen1,text='read data',command = ReadDataPort)
BReceive.grid(row=7,sticky = E)
#Label Data
LData = Label(fen1,bg = 'yellow')
LData.grid(row = 8,column=1,sticky = W)
LDataStr = Label(fen1,bg = 'gray')
LDataStr.grid(row = 9,column=1,sticky = W)
LDataHexa = Label(fen1,bg = 'cyan')
LDataHexa.grid(row = 10,column=1,sticky = W)
#Button emit
BWrite = Button(fen1,text= 'Write Data',command = WriteData)
BWrite.grid(row = 11,column = 2)

#Entrer pour le texte a envoyer
value = StringVar() 
value.set("Texte")
entree = Entry(fen1, width=30)
entree.grid(row = 11,column = 1)
fen1.mainloop()




