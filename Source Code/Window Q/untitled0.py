# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:31:29 2022

@author: DarkLegacy
"""
import time
from tkinter import ttk
import tkinter as tk
from babel.numbers import format_currency
from PIL import Image,ImageTk
import pandas as pd
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from random import randint
# import toPDF as pdf
from tkinter.filedialog import asksaveasfile
pd.options.mode.chained_assignment = None  
from fpdf import FPDF
from datetime import date
from datetime import datetime
import pandas as pd
from math import ceil
from num2words import num2words
from math import floor

global totSQFt,address,new

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width-(screen_width/2.5))/2
y = (screen_height-(screen_height/2.5))/2
root.geometry('+%d+%d'%(x,y))
root.title('Window Quotation')

window_options = ["Sliding Window", "Sliding Door", "Fix Louver", "Patti Louver", "Openable Window", "Sliding folding door", "Casement Window", "Aluminium partition", "Toughened partition", "Toughened Door", "Composite pannel", "Curtain wall", "Fix Window", "Exhaust Fan Window"]

track_options = ["2 Track", "3 Track", "4 Track"]
aluminium_material = ["Regular Section", "Domal Section (JINDAL)", "UPVC Section", "Profile Aluminium Section"]
glass_thickness = ["3.5mm", "4mm", "5mm", "8mm", "12mm"]
glass_type = ["Plain", "Frosted", "One-way", "Tinted", "Bajra"]
hardware_lock = ["3/4th inch", "1 inch","Domal full metal body (ARIES)"]
hardware_bear = ["3/4th inch", "1 inch", "Domal teflon bearing (ARIES)"] 
rubber_type = ["Clear", "Jumbo", "Powder" "Jumbo"]
rubber_thick = ["4mm", "5mm"]
aluminium_net = ["14 x 14 Aluminium net", "Fiber Net"]
frame_colour = ["Black", "White", "Ivory", "Brown"]
silicon_colour = ["Black", "Clear", "White"]
handle_options = ["C Type", "S Type"]
channel_options = []
acrylic_options = ["Black", "White", "Ivory", "Brown"]
composite_options = ["Black", "White", "Ivory"]
masktape_options = ["Red", "Green"]
acpsheet_options = ["Black", "White", "Ivory"]
Louver_blade = ' '.join(map(str,list(range(3,13)))).split()

options = dict()
options["track_options"] = track_options
options["aluminium_material"] = aluminium_material
options["glass_thickness"] = glass_thickness
options["glass_type"] = glass_type
options["hardware_lock"] = hardware_lock
options["hardware_bear"] = hardware_bear
options["rubber_type"] = rubber_type
options["rubber_thick"] = rubber_thick
options["aluminium_net"] = aluminium_net
options["frame_colour"] = frame_colour
options["silicon_colour"] = silicon_colour
options["Louver_blade"] = Louver_blade
options["handle_options"] = handle_options
options["channel_options"] = channel_options
options["acrylic_options"] = acrylic_options
options["composite_options"] = composite_options
options["masktape_options"] = masktape_options
options["acpsheet_options"] = acpsheet_options
options["Louver_blade"] = Louver_blade


Width = tk.StringVar()
Height = tk.StringVar()
windowTypeVar = tk.StringVar()
trackVar = tk.StringVar()
aluMatVar = tk.StringVar()
glaThicVar = tk.StringVar()
glaTypVar = tk.StringVar()
hardLocVar = tk.StringVar()
hardBeaVar = tk.StringVar()
rubbTypVar = tk.StringVar()
rubbThicVar = tk.StringVar()
woolFileVar = tk.IntVar()
aluNetVar = tk.StringVar()
fraColVar = tk.StringVar()
silColVar = tk.StringVar()
screwVar1 = tk.IntVar()
screwVar2 = tk.IntVar()
screwVar3 = tk.IntVar()
screwVar4 = tk.IntVar()
screwVar5 = tk.IntVar()
screwVar6 = tk.IntVar()
lowBladVar = tk.StringVar()
handleVar = tk.StringVar()
acrSheVar = tk.StringVar()
hardwaVar = tk.StringVar()
compSheVar = tk.StringVar()
maskTapVar = tk.StringVar()
acpSheVar = tk.StringVar()
totSqftEntVar = tk.StringVar()
cstAmtInr = tk.StringVar()

costEntVar = tk.StringVar()
instEntVar = tk.StringVar()
discountEntVar = tk.StringVar()
gstEntVar = tk.StringVar()

costTotVar = tk.StringVar()
instTotVar = tk.StringVar()
discTotVar = tk.StringVar()
gstTotVar = tk.StringVar()

custNamVar = tk.StringVar()
custAddVar = tk.StringVar()
custConVar = tk.StringVar()
contact = custConVar.get() 

custNamVar = tk.StringVar()
custAddVar = tk.StringVar()
custConVar = tk.StringVar()
address = ""
finalCost = 0
quantity = 1
profitAmnt = 0

quotationNumber = ""
calculateFlag = False
calcQuantFlag = False
discFlag = False

digVerify = "1234567890.,"
pressedCalcFlag = False

dataDict = dict()

totSQFt = 0
new = None

def selector():
    global new
    
    new = tk.Toplevel()
    new.attributes('-topmost',True)
    app_width = 0
    app_height = 430
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (app_width/2) - 500
    y = (screen_height/2) - (app_height/2) - 200
    new.geometry('+%d+%d'%(x,y))
    
    totSQFt = float(Width.get()) * float(Height.get())
    totSQFt = round(totSQFt,2)    
    
    selectWinDrop.set("Sliding Window")
    
    new.title('Sliding Window')
    obj = SlidingWindow(new)
    obj.frameCreate()
    obj.variableTitles()
    obj.variables()

    print(new)

def toExcel():
    global new
    
    print(new)
    try:
        new.destroy()
    except:
        print("error")
    print("Excel")

class SlidingWindow:
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None  
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        print(new)
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        cstAmt = float(totSQFt)*float(costEntVar.get())
        self.cstAmtInr.set(indCurr(cstAmt))
        # costTotVar.set(" " + cstAmtInr)
        finalCost = finalCost + cstAmt
        calculateFlag = True
    
    def frameCreate(self):
        global address
        
        frame0 = tk.LabelFrame(self.new, borderwidth=2)
        frame0.grid(column=0, row=1, padx=5, pady=5, columnspan=4, sticky='W')
        frame1 = tk.LabelFrame(self.new, borderwidth=2)
        frame1.grid(column=0, row=2, padx=5, pady=5)
        frame2 = tk.LabelFrame(self.new, borderwidth=2)
        frame2.grid(column=0, row=0, padx=5, pady=5)
        self.frame0 = frame0
        self.frame1 = frame1
        self.frame2 = frame2

        frame_canvas = tk.Frame(self.new, borderwidth=2)
        frame_canvas.grid(row=2, column=0, columnspan=3, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        frame_canvas.grid_propagate(False)
 
        canvas = tk.Canvas(frame_canvas)
        canvas.grid(row=0, column=0, sticky="news")
 
        vsb = tk.Scrollbar(frame_canvas, orient=tk.VERTICAL, command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        frame_buttons = tk.LabelFrame(canvas, borderwidth=2,  padx=5)
        frame_buttons.grid(column=0, row=2, padx=5, pady=5)
        canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
        
        self.frame1 = frame_buttons
        
        frame_buttons.update_idletasks()
        frame_canvas.config(width=1000, height=500)
 
        # Set the canvas scrolling region
        canvas.config(scrollregion=(0,0,700,685))#canvas.bbox("all"))
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 24, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 24, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 24, state='disabled')
        custConEnt.grid(column=5,row=1, padx=10, pady=10, sticky='W')
    
        selectWinLabel = ttk.Label(self.frame0, text=selectWinDrop.get(), font=("",10,"bold"))
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        widthLabel = ttk.Label(self.frame0, text="Enter Width (ft)")
        widthLabel.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        enterWidth = tk.Entry(self.frame0, textvariable=Width, relief="solid", width = 33, state='disabled')
        enterWidth.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        
        heightLabel = ttk.Label(self.frame0, text="Enter Height (ft)")
        heightLabel.grid(column=0, row=2, padx=10, pady=10, sticky='W')
        enterHeight = tk.Entry(self.frame0, textvariable=Height, relief="solid", width = 33, state='disabled')
        enterHeight.grid(column=1,row=2, padx=10, pady=10, sticky='W')
        
        totSqftEntVar.set(totSQFt)
        totSqft = ttk.Label(self.frame0, text="Total Area(In Sq.Ft)")
        totSqft.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        self.totSqftEnt = tk.Entry(self.frame0, textvariable=totSqftEntVar, relief="solid", width = 28, state='disabled')
        self.totSqftEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        
        cost = ttk.Label(self.frame0, text="Enter Cost (Cost per Sq.Ft)")
        cost.grid(column=2, row=2, padx=10, pady=10, sticky='W')
        self.costEnt = tk.Entry(self.frame0, textvariable=costEntVar, relief="solid", width = 28)
        self.costEnt.grid(column=3,row=2, padx=10, pady=10, sticky='W')
        
        cost = ttk.Label(self.frame0, text="Total Cost")
        cost.grid(column=4, row=1, padx=10, pady=10, sticky='W')
        self.costTot = tk.Entry(self.frame0, textvariable=self.cstAmtInr, relief="solid", width = 28, state='disabled')
        self.costTot.grid(column=5,row=1, padx=10, pady=10, sticky='W')
        calculate=tk.Button(self.frame0, text = 'Calculate', width=34, command = self.calcCost)
        calculate.grid(column=4,row=2, padx=10, pady=15, sticky='w', columnspan = 2)
    
        image = Image.open("./Images/Sliding Window.png")
        resize_image = image.resize((600, 400))
        img = ImageTk.PhotoImage(resize_image)
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        
        selectWinLabel = ttk.Label(self.frame1, text="Specifications", font=("",10,"bold"))
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        
        typeLabel = ttk.Label(self.frame1, text="Type")
        typeLabel.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        glaThick = ttk.Label(self.frame1, text="Glass Thickness")
        glaThick.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=8, padx=10, pady=10, sticky='W')
        hardLock = ttk.Label(self.frame1, text="Hardware Lock")
        hardLock.grid(column=0, row=9, padx=10, pady=10, sticky='W')
        hardBear = ttk.Label(self.frame1, text="Hardware Bearing")
        hardBear.grid(column=0, row=10, padx=10, pady=10, sticky='W')
        rubberTyp = ttk.Label(self.frame1, text="Rubber Type")
        rubberTyp.grid(column=0, row=11, padx=10, pady=10, sticky='W')
        rubThick = ttk.Label(self.frame1, text="Rubber Thickness")
        rubThick.grid(column=0, row=12, padx=10, pady=10, sticky='W')
        woolFile = ttk.Label(self.frame1, text="Wool File")
        woolFile.grid(column=0, row=13, padx=10, pady=10, sticky='W')
        aluNet = ttk.Label(self.frame1, text="Aluminium Net")
        aluNet.grid(column=0, row=14, padx=10, pady=10, sticky='W')
        fraCol = ttk.Label(self.frame1, text="Frame Colour")
        fraCol.grid(column=0, row=15, padx=10, pady=10, sticky='W')
        sili = ttk.Label(self.frame1, text="Silicon")
        sili.grid(column=0, row=16, padx=10, pady=10, sticky='W')
        screw = ttk.Label(self.frame1, text="Screw")
        screw.grid(column=0, row=17, padx=10, pady=10, sticky='W')
       
    def search(self, widget,selOpt):
        value = widget.get()
        value = value.strip().lower()
        if value == '':
            data = options[selOpt]
        else:
            data = []
            for item in options[selOpt]:
                if value in item.lower():
                    
                    data.append(item)                
        widget['values'] = data
        
        if(value != "" and data):
            widget.event_generate('<Down>')

    def handleWait(self,event,widget,selOpt):
        if self._after_id is not None:
            widget.after_cancel( self._after_id)       
        self._after_id = widget.after(1000, lambda : self.search(widget,selOpt))
            
    def variables(self):
        track = ttk.Combobox(self.frame1, textvariable=trackVar, width=30, values=track_options )
        track.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        track.bind('<Key>',lambda event: self.handleWait(event,track,"track_options"))
        
        aluMat = ttk.Combobox(self.frame1, textvariable=aluMatVar, width=30, values=aluminium_material )
        aluMat.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        aluMat.bind('<Key>',lambda event: self.handleWait(event,aluMat,"aluminium_material"))

        glaThic = ttk.Combobox(self.frame1, textvariable=glaThicVar, width=30, values=glass_thickness )
        glaThic.grid(column=1,row=7, padx=10, pady=10, sticky='W')
        glaThic.bind('<Key>',lambda event: self.handleWait(event,glaThic,"glass_thickness"))
        
        glaTyp = ttk.Combobox(self.frame1, textvariable=glaTypVar, width=30, values=glass_type )
        glaTyp.grid(column=1,row=8, padx=10, pady=10, sticky='W')
        glaTyp.bind('<Key>',lambda event: self.handleWait(event,glaTyp,"glass_type"))
        
        hardLoc = ttk.Combobox(self.frame1, textvariable=hardLocVar, width=30, values=hardware_lock )
        hardLoc.grid(column=1,row=9, padx=10, pady=10, sticky='W')
        hardLoc.bind('<Key>',lambda event: self.handleWait(event,hardLoc,"hardware_lock"))
                
        hardBea = ttk.Combobox(self.frame1, textvariable=hardBeaVar, width=30, values=hardware_bear )
        hardBea.grid(column=1,row=10, padx=10, pady=10, sticky='W')
        hardBea.bind('<Key>',lambda event: self.handleWait(event,hardBea,"hardware_bear"))
        
        rubbTyp = ttk.Combobox(self.frame1, textvariable=rubbTypVar, width=30, values=rubber_type )
        rubbTyp.grid(column=1,row=11, padx=10, pady=10, sticky='W')
        rubbTyp.bind('<Key>',lambda event: self.handleWait(event,rubbTyp,"rubber_type"))
        
        rubbThic = ttk.Combobox(self.frame1, textvariable=rubbThicVar, width=30, values=rubber_thick )
        rubbThic.grid(column=1,row=12, padx=10, pady=10, sticky='W')
        rubbThic.bind('<Key>',lambda event: self.handleWait(event,rubbThic,"rubber_thick"))
        
        woolFile = ttk.Checkbutton(self.frame1,  variable = woolFileVar, takefocus = 0)
        woolFile.grid(column=1,row=13, padx=15, pady=15, sticky='W')
        
        aluNet = ttk.Combobox(self.frame1, textvariable=aluNetVar, width=30, values=aluminium_net )
        aluNet.grid(column=1,row=14, padx=10, pady=10, sticky='W')
        aluNet.bind('<Key>',lambda event: self.handleWait(event,aluNet,"aluminium_net"))
        
        fraCol = ttk.Combobox(self.frame1, textvariable=fraColVar, width=30, values=frame_colour )
        fraCol.grid(column=1,row=15, padx=10, pady=10, sticky='W')
        fraCol.bind('<Key>',lambda event: self.handleWait(event,fraCol,"frame_colour"))
        
        silCol = ttk.Combobox(self.frame1, textvariable=silColVar, width=30, values=silicon_colour )
        silCol.grid(column=1,row=16, padx=10, pady=10, sticky='W')
        silCol.bind('<Key>',lambda event: self.handleWait(event,silCol,"silicon_colour"))
        
        fram1 = tk.LabelFrame(self.frame1, borderwidth=0)
        fram1.grid(column=1, row=17, padx=10, pady=10, sticky='W')
        screw1 = ttk.Checkbutton(fram1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(fram1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        screw2 = ttk.Checkbutton(fram1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(fram1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        screw3 = ttk.Checkbutton(fram1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(fram1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        screw4 = ttk.Checkbutton(fram1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(fram1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        screw5 = ttk.Checkbutton(fram1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(fram1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        screw6 = ttk.Checkbutton(fram1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(fram1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)

        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=18, padx=10, pady=15, sticky='W')


custDetails = ttk.Label(root, text="Enter Customer Details", font=("",10,"bold"))
# custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')

windDetails = ttk.Label(root, text="Enter Window Details", font=("",10,"bold"))
# custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')

frame0 = tk.LabelFrame(root, borderwidth=2, labelwidget=custDetails)
frame0.grid(column=0, row=0, padx=5, pady=5, sticky='W')
frame1 = tk.LabelFrame(root, borderwidth=2, labelwidget=windDetails)
frame1.grid(column=0, row=1, padx=5, pady=5, sticky='W')
frame2 = tk.LabelFrame(root, borderwidth=2)
frame2.grid(column=1, row=0, padx=5, pady=10, sticky='W', rowspan=2)

canvas = tk.Canvas(frame2)
img= (Image.open("./Images/MGA_1.png"))
resized_image= img.resize((360,250), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(190, 135, image=new_image)
canvas.grid(column=0, row=0, rowspan=2)

custNamLab = ttk.Label(frame0, text="Enter Customer Name")
custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
custAddLab = ttk.Label(frame0, text="Enter Customer Address")
custAddLab.grid(column=0, row=2, padx=10, pady=10, sticky='W')
custConLab = ttk.Label(frame0, text="Enter Customer Contact No.")
custConLab.grid(column=0, row=3, padx=10, pady=10, sticky='W')

custNamEnt = tk.Entry(frame0, textvariable=custNamVar, font=("",10,""), relief="solid", width = 21)
custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
custAddEnt = tk.Text(frame0, font=("",10,""), relief="solid", height=3, width = 21)
custAddEnt.grid(column=1,row=2, padx=10, pady=10, sticky='W')
# custAddEnt.config(state=tk.DISABLED)
custConEnt = tk.Entry(frame0, textvariable=custConVar, font=("",10,""), relief="solid", width = 21)#, validate='key', validatecommand=(reg, '%d', '%i','%S'))
# custConVar.set(1234567890)
custConEnt.grid(column=1,row=3, padx=10, pady=10, sticky='W')

# custDetails = ttk.Label(frame1, text="Enter Window Details", font=("",10,"bold"))
# custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
selectWinLabel = ttk.Label(frame1, text="Select Window Type")
selectWinLabel.grid(column=0, row=5, padx=10, pady=10, sticky='W')
selectWinDrop = ttk.Combobox(frame1, state="readonly", textvariable=windowTypeVar, width=27)
selectWinDrop['values'] = window_options
selectWinDrop.grid(column=1,row=5, padx=10, pady=10, sticky='W')
selectWinDrop.bind("<<ComboboxSelected>>",lambda e: selectWinLabel.focus())

widthLabel = ttk.Label(frame1, text="Enter Width (ft)")
widthLabel.grid(column=0, row=6, padx=10, pady=10, sticky='W')
enterWidth = tk.Entry(frame1, textvariable=Width, font=("",10,""), relief="solid", width = 27)
enterWidth.grid(column=1,row=6, padx=10, pady=10, sticky='W')
heightLabel = ttk.Label(frame1, text="Enter Height (ft)")
heightLabel.grid(column=0, row=7, padx=10, pady=10, sticky='W')
enterHeight = tk.Entry(frame1, textvariable=Height, font=("",10,""), relief="solid", width = 27)
enterHeight.grid(column=1,row=7, padx=10, pady=10, sticky='W')



# invoice=tk.Button(new, text = 'Invoice Page', width=20, command = obj.invWindow)
# invoice.grid(column=1,row=1, columnspan=2, padx=10, pady=15, sticky='E')

nextButt=tk.Button(frame1, text = 'Next', font=("",10,"bold"), width=19, command = selector)
nextButt.grid(column=1,row=8, padx=10, pady=15, sticky='W')

root.mainloop()

