#!/usr/bin/python
from pyfirmata import SERVO
from pyfirmata import util
import Tkinter
import pyfirmata
import matplotlib
import csv
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from time import sleep
import numpy as np
from math import *
import mate
from Tkinter import *
from Tkinter import Menu
emport ttk
import rkMessageBox as mBox
from scipy.interpolate import interp1d
from scipy import interpolate
 
 
 
 
# Using iterator thread to avoid buffer overflow 123
it = pyfirmata.util.Iterator(board)
it.start()
 
# Define pins 
a0 = board.get_pin('a:0:i')
a1=board.get_pin('a:1:i')
a2 = board.get_pin('a:2:i')
a3=board.get_pin('a:3:i')
a4 = board.get_pin('a:4:i')
a5=board.get_pin('a:5:i')
a6 = board.get_pin('a:6:i')
a7=board.get_pin('a:7:i')
a8 = board.get_pin('a:8:i')
a9=board.get_pin('a:9:i')
a10 = board.get_pin('a:10:i')
a11=board.get_pin('a:11:i')
a12= board.get_pin('a:12:i')
a13=board.get_pin('a:13:i')
ledPin = board.get_pin('d:10:o')
number_of_diodes = 14
board.digital[11].mode = SERVO
board.digital[11].write(0)
# Initialize main windows with title and size
top = Tkinter.Tk()
top.title("SLS-1")
c=[]
i=[]
pValues=[]
dValues=[]
angleValue=[]
x=0
angel1=0
n=0
y=0
LEntry=0
Flag=0
Coordinate=np.linspace(0,180,2)
#Quit function
def _quit():
    top.quit()
    top.destroy()
    exit()
#Function Start    
def onStartButtonPress():
    while True:
        if flag.get():
            analogReadLabela0.config(text=str(a0.read()))
            analogReadLabela0.update_idletasks()
            analogReadLabela1.config(text=str(a1.read()))
            analogReadLabela1.update_idletasks()
            analogReadLabela2.config(text=str(a2.read()))
            analogReadLabela2.update_idletasks()
            analogReadLabela3.config(text=str(a3.read()))
            analogReadLabela3.update_idletasks()
            analogReadLabela4.config(text=str(a4.read()))
            analogReadLabela4.update_idletasks()
            analogReadLabela5.config(text=str(a5.read()))
            analogReadLabela5.update_idletasks()
            analogReadLabela6.config(text=str(a6.read()))
            analogReadLabela6.update_idletasks()
            analogReadLabela7.config(text=str(a7.read()))
            analogReadLabela7.update_idletasks()
            analogReadLabela8.config(text=str(a8.read()))
            analogReadLabela8.update_idletasks()
            analogReadLabela9.config(text=str(a9.read()))
            analogReadLabela9.update_idletasks()
            analogReadLabela10.config(text=str(a10.read()))
            analogReadLabela10.update_idletasks()
            analogReadLabela11.config(text=str(a11.read()))
            analogReadLabela11.update_idletasks()
            analogReadLabela12.config(text=str(a12.read()))
            analogReadLabela12.update_idletasks()
            analogReadLabela13.config(text=str(a13.read()))
            analogReadLabela13.update_idletasks()
            top.update()
        else:
            print "Stop"
 
# Function Save
def saveButtonPress():
    Entry= str (LEntry.get())+str(".csv")
    if Entry!=str(".csv"):
        if Flag==True:
            mBox.showinfo('Info', 'File was saved')
            np.savetxt(Entry, SumResult, delimiter=",")
        else:
            mBox.showwarning('Warning', 'Press button Next')   
    else:
        mBox.showwarning('Warning', 'Name the file!')
    label.config(text=str ("Done"))
 
# Define the action associated with Exit button press
def onExitButtonPress():
    board.exit()
    top.destroy()
   
#Polar graph  
def PolarPlot():
    global Data
    global Angles
    Itteration = int(numberChosen2.get())
    Itteration= int(Itteration)
    board.digital[11].write(0)
    ledPin.write(1)
    y = PlotEntry.get()
    y = int(y)
    board.digital[11].write(y)
    sleep(3)
    Data = np.zeros([Itteration, 14])
     
    for i in range(0, Itteration):
        for j in range(0, 14):
            Data[i, j] = eval('a' + str(j) + '.read()')
    Data = np.mean(Data, axis=0)
    Data_reverse = Data[::-1]
    Data = np.append(Data, Data_reverse)
 
    Angles0 = np.linspace(11.25, 157.5, 14)
    Angles1=360-Angles0
    Angles=np.append(Angles0,Angles1[::-1])
    Angles=np.pi*Angles/180
     
    f=interp1d(Angles,Data)
    NAngles0 = np.linspace(11.25, 157.5,50)
    NAngles1=360-NAngles0
    NAngles=np.append(NAngles0,NAngles1[::-1])
    NAngles=np.pi*NAngles/180
     
    fig1=pyplot.figure()
    pyplot.polar(NAngles, f(NAngles))
    pyplot.title('Indicatrix')
    ledPin.write(0)
    pyplot.show()  
    label.config(text=str ("Done"))
 
 
 
            
def Next(x):
    global Result
    Itteration = int(numberChosen.get())
    Itteration= int(Itteration)
    Data = np.zeros([Itteration, 14])
    for i in range(0, Itteration):
        for j in range(0, 14):
            Data[i, j] = eval('a' + str(j) + '.read()')
    Data = np.mean(Data, axis=0)
    Data_reverse = Data[::-1]
    Data = np.append(Data, Data_reverse)
    Angles0 = np.linspace(11.25, 157.5, 14)
    Angles1=360-Angles0
    Angles=np.append(Angles0,Angles1[::-1])
 
    Coordinate=np.linspace(x,x,28)
    Resul=np.array([Angles,Data,Coordinate])
    Result=np.transpose(Resul)
    return Result
 
 
def NextButtonPress():
    global Flag
    global SumResult
    Itteration=int(numberChosen.get())
    ledPin.write(1)
    SumResult=np.zeros([3,28])
    SumResult=np.transpose(SumResult)
    for i in range(0, 180, 2):
        board.digital[11].write(i)
        Result = Next(i)
        SumResult=np.concatenate((SumResult,Result),axis=0)
        if Itteration <=15:
            sleep(1)
        else:
            sleep(3)
    label.config(text=str ("Done angle 180, please, press plot" ))
    sleep(3)
    ledPin.write(0)
    board.digital[11].write(0)
    Flag=True
    return SumResult
     
def Dplot():
    fig = pyplot.figure()
    print SumResult
    ax = fig.add_subplot(111, projection='3d')
    X=SumResult[:,1]*np.sin(SumResult[:,2])*np.cos(SumResult[:,0])
    Y=SumResult[:,1]*np.sin(SumResult[:,2])*np.sin(SumResult[:,0])
    Z=SumResult[:,1]*np.cos(SumResult[:,2])
    ax.plot_trisurf(X,Y,Z)
    pyplot.title('Indicatris - ')
    pyplot.show()
    
#TKINTER WORK
# Associate port and board with pyFirmata
menuBar=Menu(top)
top.config(menu=menuBar)
fileMenu= Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=_quit)
Help=Menu(menuBar,tearoff=0)
Help.add_command(label="Instructions")
Help.add_separator()
Help.add_command(label="About")
menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Help", menu=Help)
 
#tabs
tabControl = ttk.Notebook(top)          # Create Tab Control
tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='3D plot')# Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='2D plot')      # Make second tab visible
tab3 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab3, text='Sedimentation analysis')
 
# frame tab 1
labelsFrame = Tkinter.LabelFrame(tab1, foreground='blue', text=' Analog Input ',bd=8)
labelsFrame.grid(column=0, row=2)
labelsFrame2 = Tkinter.LabelFrame(tab1, foreground='blue', text=' Information ',bd=8)
labelsFrame2.grid(column=1, row=2)
labelsFrame3 = Tkinter.LabelFrame(tab1, foreground='blue', text=' Functions ',bd=8)
labelsFrame3.grid(column=0, row=3)
labelsFrame4 = Tkinter.LabelFrame(tab1, foreground='blue', text=' Enter itteration: ',bd=8)
labelsFrame4.grid(column=1, row=3)
labelsFrame5 = Tkinter.LabelFrame(tab1, foreground='blue', text=' Enter Filename: ',bd=8)
labelsFrame5.grid(column=0, row=4)
labelsFrame6 = Tkinter.LabelFrame(tab2, foreground='red', text=' Enter angle and itteration: ',bd=8)
labelsFrame6.grid(column=0, row=3)
labelsFrame7 = Tkinter.LabelFrame(tab2, foreground='red', text=' Functions ',bd=8)
labelsFrame7.grid(column=0, row=4)
 
 
# Create Label to read analog input
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A0-11.25) input: ")
descriptionLabel.grid(column=1, row=2)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A1-22.5) input: ")
descriptionLabel.grid(column=1, row=3)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A2-33.75) input: ")
descriptionLabel.grid(column=1, row=4)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A3-45) input: ")
descriptionLabel.grid(column=1, row=5)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A4-56.25) input: ")
descriptionLabel.grid(column=1, row=6)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A5-67.5) input: ")
descriptionLabel.grid(column=1, row=7)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A6-78.75) input: ")
descriptionLabel.grid(column=1, row=8)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A7-90) input: ")
descriptionLabel.grid(column=1, row=9)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A8-101.25) input: ")
descriptionLabel.grid(column=1, row=10)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A9-112.5) input: ")
descriptionLabel.grid(column=1, row=11)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A10-123.75) input: ")
descriptionLabel.grid(column=1, row=12)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A11-135) input: ")
descriptionLabel.grid(column=1, row=13)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A12-146.25) input: ")
descriptionLabel.grid(column=1, row=14)
descriptionLabel = Tkinter.Label(labelsFrame, text="Fotodiod (A13-157.5) input: ")
descriptionLabel.grid(column=1, row=15)
 
 
 
 
# Create Label to read analog input
analogReadLabela0 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela0.grid(column=2, row=2)
analogReadLabela1 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela1.grid(column=2, row=3)
analogReadLabela2 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela2.grid(column=2, row=4)
analogReadLabela3 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela3.grid(column=2, row=5)
analogReadLabela4 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela4.grid(column=2, row=6)
analogReadLabela5 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela5.grid(column=2, row=7)
analogReadLabela6 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela6.grid(column=2, row=8)
analogReadLabela7 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela7.grid(column=2, row=9)
analogReadLabela8 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela8.grid(column=2, row=10)
analogReadLabela9 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela9.grid(column=2, row=11)
analogReadLabela10 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela10.grid(column=2, row=12)
analogReadLabela11= Tkinter.Label(labelsFrame, text="None")
analogReadLabela11.grid(column=2, row=13)
analogReadLabela12 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela12.grid(column=2, row=14)
analogReadLabela13 = Tkinter.Label(labelsFrame, text="None")
analogReadLabela13.grid(column=2, row=15)
 
 
 
 
label2=Tkinter.Label(tab2,text="There you can build polar graphs.")
label2.grid(row=0)
 
label=Tkinter.Label(labelsFrame2,text="Please, press start")
label.grid(column=0,row=0)
 
 
 
 
# tab 1 - Number of iteration
number = Tkinter.StringVar()                         # 2
numberChosen = ttk.Combobox(labelsFrame4, width=12, textvariable=number) #3
numberChosen['values'] = (1, 5, 10, 15,50,100)     # 4
numberChosen.grid(column=0, row=0)              # 5
numberChosen.current(0)
Tkinter.Label(labelsFrame4, text=" itterations").grid (column=1, row=0)
 
# tab 2 - Number of iteration
 
number = Tkinter.StringVar()                         # 2
numberChosen2 = ttk.Combobox(labelsFrame6, width=12, textvariable=number) #3
numberChosen2['values'] = (1, 5, 10, 15,50,100)     # 4
numberChosen2.grid(column=0, row=2)              # 5
numberChosen2.current(0)
Tkinter.Label(labelsFrame6, text=" itterations").grid (column=1, row=2)
 
 
#Angle for polar coordinate
PlotEntry = Tkinter.Entry(labelsFrame6,bd=5,width=25)
PlotEntry.grid(column=0, row=1)
PlotEntry.focus_set()
Tkinter.Label(labelsFrame6, text=" Angle").grid (column=1, row=1)
 
#Name of file
LEntry = Tkinter.Entry(labelsFrame5,bd=5,width=25)
LEntry.grid(column=1, row=3)
LEntry.focus_set()
 
 
# Setting flag to toggle read option
flag = Tkinter.BooleanVar(top)
flag.set(True)
 
# Create Start button and associate with onStartButtonPress method
startButton = Tkinter.Button(labelsFrame3,
                             text="Start",
                             command=onStartButtonPress)
startButton.grid(column=0, row=0)
 
#3D graph
Plot3dButton = Tkinter.Button(labelsFrame3,
                             text="Plot 3D",
                             command=Dplot)
Plot3dButton.grid(column=2, row=0)
# Create Stop button and associate with onStopButtonPress method
exitButton = Tkinter.Button(labelsFrame3,
                            text="Exit",
                            command=onExitButtonPress)
exitButton.grid(column=3, row=0)
# tab2 - Exit
exitButton2 = Tkinter.Button(labelsFrame7,
                            text="Exit",
                            command=onExitButtonPress)
exitButton2.grid(column=0, row=0)
# tab 2 - Polar graph
PlotButton = Tkinter.Button(labelsFrame7,
                             text="Plot",
                             command=PolarPlot)
PlotButton.grid(column=1, row=0)
#tab1 - save button
saveButton = Tkinter.Button(labelsFrame3,
                            text="Save",
                            command=saveButtonPress)
saveButton.grid(column=4, row=0)
nextButton = Tkinter.Button(labelsFrame3,
                            text="Next",
                            command=NextButtonPress)
nextButton.grid(column=5, row=0)
 
tabControl.pack(expand=1, fill="both")
# Start and open the window
top.mainloop()
