# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 00:07:04 2021

@author: DarkLegacy
"""

from tkinter import ttk
import tkinter as tk
from babel.numbers import format_currency
from PIL import Image,ImageTk
import pandas as pd
from tkinter.filedialog import askopenfile
from tkinter import messagebox

####################################################################################################################################################

data = pd.read_excel('./Data/data.xlsx')
data = data.replace(float('nan'),"")

####################################################################################################################################################

root = tk.Tk()
app_width = 305
app_height = 180
# root.geometry("303x180")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (app_width/2) - 220
y = (screen_height/2) - (app_height/2) - 100
root.geometry('+%d+%d'%(x,y))
# root.resizable(False, False)
root.title('Window Quotation')

####################################################################################################################################################

window_options = ["Sliding Window", "Sliding Door", "Fix Louver", "Patti Louver", "Openable Window", "Sliding folding door", "Casement Window", "Aluminum partition", "Toughened partition", "Toughened Door", "Composite pannel", "Curtain wall", "Fix Window"]

track_options = ["2 Track", "3 Track", "4 Track"]
aluminium_material = ["Regular Section", "Dumal Section", "UPVC Section", "Profile Aluminum Section"]
glass_thickness = ["3.5mm", "4mm", "5mm", "8mm", "12mm"]
glass_type = ["Plain", "Frosted", "One-way", "Tinted", "Bajra"]
hardware_lock = ["3/4th inch", "1 inch"]
hardware_bear = ["3/4th inch", "1 inch"] 
rubber_type = ["Clear", "Jumbo", "Powder" "Jumbo"]
rubber_thick = ["4mm", "5mm"]
aluminium_net = ["3ft bundle" ,"4ft bundle","5ft bundle"]
frame_colour = ["Black", "White", "Ivory", "Brown"]
silicon_colour = ["Black", "Clear", "White"]
handle_options = ["C Type", "S Type"]
channel_options = []
acrylic_options = ["Black", "White", "Ivory", "Brown"]
composite_options = ["Black", "White", "Ivory"]
masktape_options = ["Red", "Green"]
acpsheet_options = ["Black", "White", "Ivory"]
Louver_blade = ' '.join(map(str,list(range(3,13)))).split()

####################################################################################################################################################

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

####################################################################################################################################################

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
profitEntVar = tk.StringVar()
discountEntVar = tk.StringVar()
labourEntVar = tk.StringVar()
gstEntVar = tk.StringVar()
costTotVar = tk.StringVar()
profTotVar = tk.StringVar()
discTotVar = tk.StringVar()
laboTotVar = tk.StringVar()
gstTotVar = tk.StringVar()
custNamVar = tk.StringVar()
custAddVar = tk.StringVar()
custConVar = tk.StringVar()
address = ""
finalCost = 0
quantity = 1
profitAmnt = 0

calculateFlag = False
# s = tk.IntVar()

dataDict = dict()
srno = 1 
num = list(data["Sr.No"])
if(len(num)!=0):
    srno = num[-1]

####################################################################################################################################################

totSQFt = 0
new = None

####################################################################################################################################################

def open_file1():
    global data,root,srno,finalCost
    
    filename = askopenfile(title="Open a File", filetype=(("xlxs files", ".*xlsx"), ("All Files", "*.")))
    data = pd.read_excel(filename.name)
    data = data.replace(float('nan'),"")
    num = list(data["Sr.No"])
    if(len(num)!=0):
        srno = num[-1] + 1
        
    temp = list(data["finalCost"])
    finalCost = temp[-1] 
        
    obj = Cart()
    obj.addMorePage()

####################################################################################################################################################

def clearValues():
    global quantity
    
    Width.set("")
    Height.set("")
    windowTypeVar.set("")
    trackVar.set("")
    aluMatVar.set("")
    glaThicVar.set("")
    glaTypVar.set("")
    hardLocVar.set("")
    hardBeaVar.set("")
    rubbTypVar.set("")
    rubbThicVar.set("")
    woolFileVar.set(0)
    aluNetVar.set("")
    fraColVar.set("")
    silColVar.set("")
    screwVar1.set(0)
    screwVar2.set(0)
    screwVar3.set(0)
    screwVar4.set(0)
    screwVar5.set(0)
    screwVar6.set(0)
    lowBladVar.set("")
    handleVar.set("")
    acrSheVar.set("")
    hardwaVar.set("")
    compSheVar.set("")
    maskTapVar.set("")
    acpSheVar.set("")
    totSqftEntVar.set("")
    cstAmtInr.set("")
    costEntVar.set("")
    profitEntVar.set("")
    discountEntVar.set("")
    labourEntVar.set("")
    gstEntVar.set("")
    # costTotVar.set("")
    profTotVar.set("")
    discTotVar.set("")
    laboTotVar.set("")
    gstTotVar.set("")
    quantity = 1

def addNewRowData(obj,objStr):
    temp = obj.get()
    lst = data[objStr].to_list()
    lst[-1] = temp
    return lst

def toExcel():
    global srno, windowTypeVar,	trackVar, aluMatVar, glaThicVar, glaTypVar, hardLocVar, hardBeaVar, rubbTypVar, rubbThicVar, woolFileVar, aluNetVar,	fraColVar, silColVar, screwVar1, screwVar2, screwVar3, screwVar4, screwVar5, screwVar6, lowBladVar, handleVar, acrSheVar, hardwaVar, compSheVar, 	maskTapVar, acpSheVar, totSqftEntVar, costEntVar, profitEntVar, discountEntVar, labourEntVar, gstEntVar, costTotVar, profTotVar, discTotVar, laboTotVar	, gstTotVar, custNamVar, custAddVar, custConVar, address, new, calculateFlag

    if(calculateFlag == True):
        calculateFlag = False
    else:
        messagebox.showerror("Invalid","Please fill in the cost field and click on the calculate button.", parent=new)
        return
        

    data.loc[len(data.index)] = [""]*49
    
    listSrno= data['Sr.No'].to_list()
    listSrno[-1] = srno
    data['Sr.No'] = listSrno
    srno+=1
    
    wd = addNewRowData(Width, "Width")
    wd[-1] = wd[-1] + " ft"
    data['Width'] = wd
    ht = addNewRowData(Height, "Height")
    ht[-1] = ht[-1] + " ft"
    data['Height'] = ht
    data['windowTypeVar'] = addNewRowData(windowTypeVar, "windowTypeVar")
    data['trackVar'] = addNewRowData(trackVar, "trackVar")
    data['aluMatVar'] = addNewRowData(aluMatVar, "aluMatVar")
    data['glaThicVar'] = addNewRowData(glaThicVar, "glaThicVar")
    data['glaTypVar'] = addNewRowData(glaTypVar, "glaTypVar")
    data['hardLocVar'] = addNewRowData(hardLocVar, "hardLocVar")
    data['hardBeaVar'] = addNewRowData(hardBeaVar, "hardBeaVar")
    data['rubbTypVar'] = addNewRowData(rubbTypVar, "rubbTypVar")
    data['rubbThicVar'] = addNewRowData(rubbThicVar, "rubbThicVar") 
    data['woolFileVar'] = addNewRowData(woolFileVar, "woolFileVar")
    data['aluNetVar'] = addNewRowData(aluNetVar, "aluNetVar")
    data['fraColVar'] = addNewRowData(fraColVar, "fraColVar")
    data['silColVar'] = addNewRowData(silColVar, "silColVar")
    data['screwVar1'] = addNewRowData(screwVar1, "screwVar1")
    data['screwVar2'] = addNewRowData(screwVar2, "screwVar2")
    data['screwVar3'] = addNewRowData(screwVar3, "screwVar3")
    data['screwVar4'] = addNewRowData(screwVar4, "screwVar4")
    data['screwVar5'] = addNewRowData(screwVar5, "screwVar5")
    data['screwVar6'] = addNewRowData(screwVar6, "screwVar6")
    data['lowBladVar'] = addNewRowData(lowBladVar, "lowBladVar")
    data['handleVar'] = addNewRowData(handleVar, "handleVar")
    data['acrSheVar'] = addNewRowData(acrSheVar, "acrSheVar")
    data['hardwaVar'] = addNewRowData(hardwaVar, "hardwaVar")
    data['compSheVar'] = addNewRowData(compSheVar, "compSheVar")
    data['maskTapVar'] = addNewRowData(maskTapVar, "maskTapVar")
    data['acpSheVar'] = addNewRowData(acpSheVar, "acpSheVar")
    data['totSqftEntVar'] = addNewRowData(totSqftEntVar, "totSqftEntVar")
    data['cstAmtInr'] = addNewRowData(cstAmtInr, "cstAmtInr")
    data['costEntVar'] = addNewRowData(costEntVar, "windowTypeVar")
    data['profitEntVar'] = addNewRowData(profitEntVar, "profitEntVar")
    data['discountEntVar'] = addNewRowData(discountEntVar, "discountEntVar")
    data['labourEntVar'] = addNewRowData(labourEntVar, "labourEntVar")
    data['gstEntVar'] = addNewRowData(gstEntVar, "gstEntVar")
    data['costTotVar'] = addNewRowData(costTotVar, "costTotVar")
    data['profTotVar'] = addNewRowData(profTotVar, "profTotVar")
    data['discTotVar'] = addNewRowData(discTotVar, "discTotVar")
    data['laboTotVar'] = addNewRowData(laboTotVar, "laboTotVar")
    data['gstTotVar'] = addNewRowData(gstTotVar, "gstTotVar")
    data['custNamVar'] = addNewRowData(custNamVar, "custNamVar")
    data['custAddVar'] = addNewRowData(custAddVar, "custAddVar")
    data['custConVar'] = addNewRowData(custConVar, "custConVar")
    
    listAdd = data['address'].to_list()
    listAdd[-1] = address
    data['address'] = listAdd
    
    
    listAdd = data['quantity'].to_list()
    listAdd[-1] = quantity
    data['quantity'] = listAdd
    
    listFinCost = data['finalCost'].to_list()
    listFinCost[-1] = finalCost
    data['finalCost'] = listFinCost

    data.to_excel('./Data/{}_QuatationData.xlsx'.format(custNamVar.get()), index=False)
    
    obj = Cart()
    new.destroy()
    obj.addMorePage()
    clearValues()

def afterCalculate():
    global srno, windowTypeVar,	trackVar, aluMatVar, glaThicVar, glaTypVar, hardLocVar, hardBeaVar, rubbTypVar, rubbThicVar, woolFileVar, aluNetVar,	fraColVar, silColVar, screwVar1, screwVar2, screwVar3, screwVar4, screwVar5, screwVar6, lowBladVar, handleVar, acrSheVar, hardwaVar, compSheVar, 	maskTapVar, acpSheVar, totSqftEntVar, costEntVar, profitEntVar, discountEntVar, labourEntVar, gstEntVar, costTotVar, profTotVar, discTotVar, laboTotVar	, gstTotVar, custNamVar, custAddVar, custConVar, address
    
    data['totSqftEntVar'] = addNewRowData(totSqftEntVar, "totSqftEntVar")
    data['costEntVar'] = addNewRowData(costEntVar, "windowTypeVar")
    data['profitEntVar'] = addNewRowData(profitEntVar, "profitEntVar")
    data['discountEntVar'] = addNewRowData(discountEntVar, "discountEntVar")
    data['labourEntVar'] = addNewRowData(labourEntVar, "labourEntVar")
    data['gstEntVar'] = addNewRowData(gstEntVar, "gstEntVar")
    data['costTotVar'] = addNewRowData(costTotVar, "costTotVar")
    data['profTotVar'] = addNewRowData(profTotVar, "profTotVar")
    data['discTotVar'] = addNewRowData(discTotVar, "discTotVar")
    data['laboTotVar'] = addNewRowData(laboTotVar, "laboTotVar")
    data['gstTotVar'] = addNewRowData(gstTotVar, "gstTotVar")
    
    data.to_excel('./Data/{}_QuatationData.xlsx'.format(custNamVar.get()), index=False)

####################################################################################################################################################

def selector():
    global totSQFt,address,new
    
    contact = custConVar.get() 
    
    if(contact.isdigit() and len(contact)>7 and len(contact)<=10 ):
        pass
    else:
        messagebox.showerror("Invalid","Please enter a valid Contact Number")
        return False

    if(Width.get()=="" or Height.get()==""):
        messagebox.showerror("Invalid","Please enter Width and Height")
        return False
    
    address = custAddEnt.get("1.0","end-1c")
    
    new = tk.Toplevel()
    new.attributes('-topmost',True)
    app_width = 0
    app_height = 430
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (app_width/2) - 500
    y = (screen_height/2) - (app_height/2) - 300
    new.geometry('+%d+%d'%(x,y))
    
    totSQFt = int(Width.get()) * int(Height.get())
        
    
    if(selectWinDrop.get() == "Sliding Window"):
        new.title('Sliding Window')
        obj = SlidingWindow(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Sliding Door"):
        new.title("Sliding Door")
        obj = SlidingDoor(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Fix Louver"):
        new.title("Fix Louver")
        obj = FixLouver(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Patti Louver"):
        new.title("Patti Louver")
        obj = PattiLouver(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Openable Window"):
        new.title("Openable Window")
        obj = OpenableWindow(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Sliding folding door"):
        new.title("Sliding folding door")
        obj = SlidingFoldingDoor(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Casement Window"):
        new.title("Casement Window")
        obj = CasementWindow(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Aluminum partition"):
        new.title("Aluminum partition")
        obj = AluminiumPartition(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Toughened partition"):
        new.title("Toughened partition")
        obj = ToughenedPartition(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Toughened Door"):
        new.title("Toughened Door")
        obj = ToughenedDoor(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Composite pannel"):
        new.title("Composite pannel")
        obj = CompositePanel(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Curtain wall"):
        new.title("Curtain wall")
        obj = CurtainWall(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Fix Window"):
        new.title("Fix Window")
        obj = FixWindow(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()

####################################################################################################################################################

class CalculatePage:

    costEnt = None    
    profitEnt = None
    discountEnt = None 
    labourEnt = None
    gstEnt = None
    totSqftEnt = None
    costTot = None
    profTot = None
    discTot = None
    laboTot = None
    gstTot = None

    def calculateCost(self):
        global profitAmnt
        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        
        cstAmt = finalCost
    
        labAmt = cstAmt + (cstAmt*int(labourEntVar.get())/100)
        labAmtInr = indCurr(labAmt)
        laboTotVar.set(labAmtInr)
    
        prftAmt = labAmt + (labAmt*int(profitEntVar.get())/100)
        profitAmnt = prftAmt
        prftAmtInr = indCurr(prftAmt)
        profTotVar.set(prftAmtInr)
    
        if(discountEntVar.get() != ""):
            discAmt = prftAmt - (prftAmt*int(discountEntVar.get())/100)
            discAmtInr = indCurr(discAmt)
            discTotVar.set(discAmtInr)     
            
            gstAmt = discAmt + (discAmt*int(labourEntVar.get())/100)
            gstAmtInr = indCurr(gstAmt)
            gstTotVar.set(gstAmtInr)
            
        else:
            discTotVar.set("")
            gstAmt = prftAmt + (prftAmt*int(labourEntVar.get())/100)
            gstAmtInr = indCurr(gstAmt)
            gstTotVar.set(gstAmtInr)
            
        afterCalculate()
    
    def costPage(self):
        global finalCost
        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        
        new = tk.Toplevel()
        new.attributes('-topmost',True)
        app_width = 0
        app_height = 430
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (app_width/2) - 50
        y = (screen_height/2) - (app_height/2) - 100
        new.geometry('+%d+%d'%(x,y))
        
        totSqftEntVar.set(totSQFt)
        
        entLab = ttk.Label(new, text="Enter Values")
        entLab.grid(column=1, row=0, padx=10, pady=10, sticky='W')
        totLab = ttk.Label(new, text="Total")
        totLab.grid(column=3, row=0, padx=10, pady=10, sticky='W')
        
        # totSqft = ttk.Label(new, text="Total Area(In Sq.Ft)")
        # totSqft.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        # cost = ttk.Label(new, text="Enter Cost (Cost per Sq.Ft)")
        # cost.grid(column=0, row=2, padx=10, pady=10, sticky='W')
        labour = ttk.Label(new, text="Enter Labour Charges (In Percentage)")
        labour.grid(column=0, row=3, padx=10, pady=10, sticky='W')
        profit = ttk.Label(new, text="Enter Profit (In Percentage)")
        profit.grid(column=0, row=4, padx=10, pady=10, sticky='W')
        discount = ttk.Label(new, text="Enter Discount (In Percentage)")
        discount.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        gst = ttk.Label(new, text="GST (In Percentage)")
        gst.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        
        # self.costEnt = tk.Entry(new, textvariable=costEntVar, relief="solid", width = 16)
        # self.costEnt.grid(column=1,row=2, padx=10, pady=10, sticky='W')
        self.labourEnt = tk.Entry(new, textvariable=labourEntVar, relief="solid", width = 16)
        self.labourEnt.grid(column=1,row=3, padx=10, pady=10, sticky='W')
        self.profitEnt = tk.Entry(new, textvariable=profitEntVar, relief="solid", width = 16)
        self.profitEnt.grid(column=1,row=4, padx=10, pady=10, sticky='W')
        self.discountEnt = tk.Entry(new, textvariable=discountEntVar, relief="solid", width = 16)
        self.discountEnt.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        self.gstEnt = tk.Entry(new, textvariable=gstEntVar, relief="solid", width = 16)
        self.gstEnt.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        
        cost = ttk.Label(new, text="Total Cost")
        cost.grid(column=0, row=2, padx=10, pady=10, sticky='W')
        labour = ttk.Label(new, text="Cost with Labour Charges")
        labour.grid(column=2, row=3, padx=10, pady=10, sticky='W')
        profit = ttk.Label(new, text="Cost with Profit")
        profit.grid(column=2, row=4, padx=10, pady=10, sticky='W')
        discount = ttk.Label(new, text="Cost After Discount")
        discount.grid(column=2, row=5, padx=10, pady=10, sticky='W')
        gst = ttk.Label(new, text="Final bill amout with GST")
        gst.grid(column=2, row=6, padx=10, pady=10, sticky='W')
    
        finCost = indCurr(finalCost)
        costTotVar.set(finCost)
        # self.totSqftEnt = tk.Entry(new, textvariable=totSqftEntVar, relief="solid", width = 16, state='disabled')
        # self.totSqftEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        self.costTot = tk.Entry(new, textvariable=costTotVar, relief="solid", width = 16, state='disabled')
        self.costTot.grid(column=3,row=2, padx=10, pady=10, sticky='W')
        self.laboTot = tk.Entry(new, textvariable=laboTotVar, relief="solid", width = 16, state='disabled')
        self.laboTot.grid(column=3,row=3, padx=10, pady=10, sticky='W')
        self.profTot = tk.Entry(new, textvariable=profTotVar, relief="solid", width = 16, state='disabled')
        self.profTot.grid(column=3,row=4, padx=10, pady=10, sticky='W')
        self.discTot = tk.Entry(new, textvariable=discTotVar, relief="solid", width = 16, state='disabled')
        self.discTot.grid(column=3,row=5, padx=10, pady=10, sticky='W')
        self.gstTot = tk.Entry(new, textvariable=gstTotVar, relief="solid", width = 16, state='disabled')
        self.gstTot.grid(column=3,row=6, padx=10, pady=10, sticky='W')

        calculate=tk.Button(new, text = 'Calculate', width=17, command = self.calculateCost)
        calculate.grid(column=1,row=7, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################

class Cart:
    
    new = None
    maintab = None
    frame2 = None
    qtyFlag = False
    qt = None
    
    def createNewRow(self):
        row = tk.LabelFrame(self.maintab, borderwidth=2)
        return row
    
    def deleteRow(self,num):
        global data, srno
        data.drop(data.index[data['Sr.No'] == num], inplace=True)
        self.new.destroy()
        srno-=1
        self.addMorePage()
    
    def nextItem(self):
        
        self.new.destroy()
        
        frame0 = tk.LabelFrame(root, borderwidth=2)
        frame0.grid(column=0, row=0, padx=5, pady=5, sticky='W')
        frame1 = tk.LabelFrame(root, borderwidth=2)
        frame1.grid(column=0, row=1, padx=5, pady=5, sticky='W')
        frame2 = tk.LabelFrame(root, borderwidth=2)
        frame2.grid(column=1, row=0, padx=5, pady=10, sticky='W', rowspan=2)

        canvas = tk.Canvas(frame2)
        img= (Image.open("./Images/MGA_1.png"))
        resized_image= img.resize((360,250), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        canvas.create_image(190, 135, image=new_image)
        canvas.grid(column=2, row=3)

        custNamVar.set(data.iloc[0]["custNamVar"])
        custConVar.set(data.iloc[0]["custConVar"])
        address = data.iloc[0]["address"]

        custDetails = ttk.Label(frame0, text="Enter Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        custNamLab = ttk.Label(frame0, text="Enter Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(frame0, text="Enter Customer Address")
        custAddLab.grid(column=0, row=2, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(frame0, text="Enter Customer Contact No.")
        custConLab.grid(column=0, row=3, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(frame0, textvariable=custNamVar, font=("",10,""), relief="solid", width = 21, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(frame0, font=("",10,""), relief="solid", height=3, width = 21, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=1,row=2, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custConEnt = tk.Entry(frame0, textvariable=custConVar, font=("",10,""), relief="solid", width = 21, state='disabled')
        custConEnt.grid(column=1,row=3, padx=10, pady=10, sticky='W')

        custDetails = ttk.Label(frame1, text="Enter Window Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        selectWinLabel = ttk.Label(frame1, text="Select Window Type")
        selectWinLabel.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        selectWinDrop = ttk.Combobox(frame1, state="disabled", textvariable=windowTypeVar, width=23)
        selectWinDrop['values'] = window_options
        selectWinDrop.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        selectWinDrop.bind("<<ComboboxSelected>>",lambda e: selectWinLabel.focus())
        nextButt=tk.Button(frame1, text = 'Next', font=("",10,"bold"), width=19, command = selector)
        nextButt.grid(column=1,row=8, padx=10, pady=15, sticky='W')

        widthLabel = ttk.Label(frame1, text="Enter Width (ft)")
        widthLabel.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        enterWidth = tk.Entry(frame1, textvariable=Width, font=("",10,""), relief="solid", width = 23, state='disabled')
        enterWidth.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        heightLabel = ttk.Label(frame1, text="Enter Height (ft)")
        heightLabel.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        enterHeight = tk.Entry(frame1, textvariable=Height, font=("",10,""), relief="solid", width = 23, state='disabled')
        enterHeight.grid(column=1,row=7, padx=10, pady=10, sticky='W')
    
        obj = CalculatePage()
        obj.costPage()
    
        root.mainloop()
    
    
    def addNewItem(self):
        self.new.destroy()
        
        frame0 = tk.LabelFrame(root, borderwidth=2)
        frame0.grid(column=0, row=0, padx=5, pady=5, sticky='W')
        frame1 = tk.LabelFrame(root, borderwidth=2)
        frame1.grid(column=0, row=1, padx=5, pady=5, sticky='W')
        frame2 = tk.LabelFrame(root, borderwidth=2)
        frame2.grid(column=1, row=0, padx=5, pady=10, sticky='W', rowspan=2)

        canvas = tk.Canvas(frame2)
        img= (Image.open("./Images/MGA_1.png"))
        resized_image= img.resize((360,250), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        canvas.create_image(190, 135, image=new_image)
        canvas.grid(column=2, row=3)

        custDetails = ttk.Label(frame0, text="Enter Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        custNamLab = ttk.Label(frame0, text="Enter Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(frame0, text="Enter Customer Address")
        custAddLab.grid(column=0, row=2, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(frame0, text="Enter Customer Contact No.")
        custConLab.grid(column=0, row=3, padx=10, pady=10, sticky='W')

        custNamVar.set(data.iloc[0]["custNamVar"])
        custConVar.set(data.iloc[0]["custConVar"])
        address = data.iloc[0]["address"]

        custNamEnt = tk.Entry(frame0, textvariable=custNamVar, font=("",10,""), relief="solid", width = 21, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(frame0, font=("",10,""), relief="solid", height=3, width = 21, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=1,row=2, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(frame0, textvariable=custConVar, font=("",10,""), relief="solid", width = 21, state='disabled')
        custConEnt.grid(column=1,row=3, padx=10, pady=10, sticky='W')

        custDetails = ttk.Label(frame1, text="Enter Window Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        selectWinLabel = ttk.Label(frame1, text="Select Window Type")
        selectWinLabel.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        selectWinDrop = ttk.Combobox(frame1, state="readonly", textvariable=windowTypeVar, width=23 )
        selectWinDrop['values'] = window_options
        selectWinDrop.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        selectWinDrop.bind("<<ComboboxSelected>>",lambda e: selectWinLabel.focus())
        nextButt=tk.Button(frame1, text = 'Next', font=("",10,"bold"), width=19, command = selector)
        nextButt.grid(column=1,row=8, padx=10, pady=15, sticky='W')

        widthLabel = ttk.Label(frame1, text="Enter Width (ft)")
        widthLabel.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        enterWidth = tk.Entry(frame1, textvariable=Width, font=("",10,""), relief="solid", width = 23)
        enterWidth.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        heightLabel = ttk.Label(frame1, text="Enter Height (ft)")
        heightLabel.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        enterHeight = tk.Entry(frame1, textvariable=Height, font=("",10,""), relief="solid", width = 23)
        enterHeight.grid(column=1,row=7, padx=10, pady=10, sticky='W')

        root.mainloop()
        
    def callback(self,event):
        # # head5 = tk.Label(self.maintab, text=data.iloc[i]["finalCost"], padx=10)
        # # head5.grid(column=4, row=i+1, padx=10, pady=10, sticky='W')
        
        # cost = data.iloc[i]["finalCost"]
        # amnt = cost * qty.get()
        # print(cost,qty.get())
        # # head5 = tk.Label(self.maintab, text=amnt, padx=10)
        # # head5.grid(column=7, row=i+1, padx=10, pady=10, sticky='W')
    
        self.qtyFlag = True
    
    def calcQuant(self):
        # print("In Quant")
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        tList = []
        qTemp = []
        suum = 0
        for i in range(srno-1):
            amt = float(data.iloc[i]["cstAmtInr"][1:].replace(",",""))
            temp = int(self.qt[i].get()) * amt
            suum = suum + temp
            tList.append(indCurr(temp))
            qTemp.append(self.qt[i].get())
            
        data["quantity"] = qTemp
        data["totQuanSum"] = indCurr(suum)
        data["quantAmnt"] = tList
        self.new.destroy()
        self.addMorePage()
        
    
    def addMorePage(self):
        global srno
        
        new = tk.Toplevel()
        new.attributes('-topmost',True)
        app_width = 0
        app_height = 430
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (app_width/2) - 270
        y = (screen_height/2) - (app_height/2) - 100
        new.geometry('+%d+%d'%(x,y))
        new.title('Cart')
        self.new = new
        
        custDetails = ttk.Label(self.new, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        
        frame2 = tk.LabelFrame(self.new, borderwidth=2, width=1000, labelwidget=custDetails )
        frame2.grid(column=0, row=0, columnspan=3, padx=5, pady=5, sticky='W')
        # frame2.grid_propagate(0)
        self.frame2 = frame2
        
        custNamVar.set(data.iloc[0]["custNamVar"])
        custConVar.set(data.iloc[0]["custConVar"])
        address = data.iloc[0]["address"]
    
        custDetails = ttk.Label(self.frame2, text="", font=("",10,"bold"))
        custDetails.grid(column=1, row=0, padx=8, pady=10, sticky='W')
        custDetails = ttk.Label(self.frame2, text="", font=("",10,"bold"))
        custDetails.grid(column=2, row=0, padx=8, pady=10, sticky='W')
        custDetails = ttk.Label(self.frame2, text="", font=("",10,"bold"))
        custDetails.grid(column=3, row=0, padx=8, pady=10, sticky='W')
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=0, row=2, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=0, row=3, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 43, state='disabled')
        custNamEnt.grid(column=5,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 43, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=5,row=2, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 43, state='disabled')
        custConEnt.grid(column=5,row=3, padx=10, pady=10, sticky='W')
        
        cartDetails = ttk.Label(self.new, text="Cart Details", font=("",10,"bold"))
        cartDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        maintab =  tk.LabelFrame(self.new, borderwidth=2, labelwidget=cartDetails)
        maintab.grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky='W')
        self.maintab = maintab
        
        head1 = tk.Label(self.maintab, text="Sr.No", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head1.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        head2 = tk.Label(self.maintab, text="Window Type", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head2.grid(column=1, row=0, padx=10, pady=10, sticky='W')
        head3 = tk.Label(self.maintab, text="Width", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head3.grid(column=2, row=0, padx=10, pady=10, sticky='W')
        head4 = tk.Label(self.maintab, text="Height", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head4.grid(column=3, row=0, padx=10, pady=10, sticky='W')
        head5 = tk.Label(self.maintab, text="Cost", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head5.grid(column=4, row=0, padx=10, pady=10, sticky='W')
        head6 = tk.Label(self.maintab, text="Quantity", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head6.grid(column=5, row=0, padx=10, pady=10, sticky='W')
        head7 = tk.Label(self.maintab, text="Amount", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head7.grid(column=6, row=0, padx=10, pady=10, sticky='W')
            
        row = self.createNewRow()
        row.grid(column=0, row=0, padx=5, pady=5, sticky='W')
        
        i = 0
        
        qty = [1]*srno
        self.qt = []
        for i in range(srno-1):
            tmp = tk.StringVar()
            self.qt.append(tmp)
        
        for i in range(srno-1):
            qty[i] = data.iloc[i]["quantity"]
            self.qt[i].set(qty[i])
        
        for i in range(srno-1):
            head1 = tk.Label(self.maintab, text=data.iloc[i]["Sr.No"], padx=10)
            head1.grid(column=0, row=i+1, padx=10, pady=10, sticky='W')
            head2 = tk.Label(self.maintab, text=data.iloc[i]["windowTypeVar"], padx=10)
            head2.grid(column=1, row=i+1, padx=10, pady=10, sticky='W')
            head3 = tk.Label(self.maintab, text=data.iloc[i]["Width"], padx=10)
            head3.grid(column=2, row=i+1, padx=10, pady=10, sticky='W')
            head4 = tk.Label(self.maintab, text=data.iloc[i]["Height"], padx=10)
            head4.grid(column=3, row=i+1, padx=10, pady=10, sticky='W')
            head5 = tk.Label(self.maintab, text=data.iloc[i]["cstAmtInr"], padx=10)
            head5.grid(column=4, row=i+1, padx=10, pady=10, sticky='W')
            quantity = tk.Entry(self.maintab, textvariable=self.qt[i], relief="solid", width = 12)
            quantity.grid(column=5,row=i+1, padx=10, pady=10, sticky='W')
            head6 = tk.Label(self.maintab, text=data.iloc[i]["quantAmnt"], padx=10)
            head6.grid(column=6, row=i+1, padx=10, pady=10, sticky='W')
            delete=tk.Button(self.maintab, text = 'X', font=("",10,"bold"), width=2, fg='red', command=lambda num=data.iloc[i]["Sr.No"] : self.deleteRow(num))
            delete.grid(column=7,row=i+1, padx=10, pady=10, sticky='W')

        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        finCost = indCurr(finalCost)
        costTotVar.set(finCost)
        line = ttk.Label(self.maintab, text="_____________________________________________________________________________________________________________________________________________")
        line.grid(column=0, row=i+2, columnspan=7, padx=10, pady=10, sticky='N')
        cost = ttk.Label(self.maintab, text="Total Cost")
        cost.grid(column=0, row=i+3, padx=10, pady=10, sticky='W')
        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        finAmt = tk.StringVar()
        finAmt.set(indCurr(data.iloc[i]["finalCost"]))
        
        costTot = tk.Entry(self.maintab, textvariable=finAmt, relief="solid", width = 14, state='disabled')
        costTot.grid(column=4,row=i+3, padx=10, pady=10, sticky='W')
        
        qtyAmt = tk.StringVar()
        qtyAmt.set(data.iloc[i]["totQuanSum"])
    
        qtyCostTot = tk.Entry(self.maintab, textvariable=qtyAmt, relief="solid", width = 14, state='disabled')
        qtyCostTot.grid(column=6,row=i+3, padx=10, pady=10, sticky='W')
        
        addButt=tk.Button(self.new, text = 'Add More Items', font=("",10,"bold"), width=24, command = self.addNewItem)
        addButt.grid(column=0,row=3, padx=10, pady=15, sticky='W')

        calc=tk.Button(self.new, text = 'Calculate(Quantity)', font=("",10,"bold"), width=24, command = self.calcQuant)
        calc.grid(column=1,row=3, padx=10, pady=15, sticky='N')
        
        nextButt=tk.Button(self.new, text = 'Next', font=("",10,"bold"), width=24, command = self.nextItem)
        nextButt.grid(column=2,row=3, padx=10, pady=15, sticky='E')
    
####################################################################################################################################################

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
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
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

####################################################################################################################################################    

class SlidingDoor:
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
        frame2.grid(column=0, row=0, padx=5, pady=5, sticky='W')
        self.frame0 = frame0
        self.frame1 = frame1
        self.frame2 = frame2
    
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 23, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 24, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 23, state='disabled')
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Sliding Door.png")
        resize_image = image.resize((580, 500))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
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
    
####################################################################################################################################################

class FixLouver:
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
    
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 23, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 24, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 23, state='disabled')
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Fix Louver.png")
        resize_image = image.resize((580, 500))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        glaMaterial = ttk.Label(self.frame1, text="Glass Material")
        glaMaterial.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        lowBlade = ttk.Label(self.frame1, text="Louver Blade")
        lowBlade.grid(column=0, row=8, padx=10, pady=10, sticky='W')  
        fraCol = ttk.Label(self.frame1, text="Frame Colour")
        fraCol.grid(column=0, row=9, padx=10, pady=10, sticky='W')
        sili = ttk.Label(self.frame1, text="Silicon")
        sili.grid(column=0, row=10, padx=10, pady=10, sticky='W')
        screw = ttk.Label(self.frame1, text="Screw")
        screw.grid(column=0, row=11, padx=10, pady=10, sticky='W')
        
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
        
        aluMat = ttk.Combobox(self.frame1, textvariable=aluMatVar, width=30, values=aluminium_material )
        aluMat.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        aluMat.bind('<Key>',lambda event: self.handleWait(event,aluMat,"aluminium_material"))
        
        glaThic = ttk.Combobox(self.frame1, textvariable=glaThicVar, width=30, values=glass_thickness )
        glaThic.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        glaThic.bind('<Key>',lambda event: self.handleWait(event,glaThic,"glass_thickness"))
        
        glaTyp = ttk.Combobox(self.frame1, textvariable=glaTypVar, width=30, values=glass_type )
        glaTyp.grid(column=1,row=7, padx=10, pady=10, sticky='W')
        glaTyp.bind('<Key>',lambda event: self.handleWait(event,glaTyp,"glass_type"))

        lowBlad = ttk.Combobox(self.frame1, textvariable=lowBladVar, width=30, values=Louver_blade )
        lowBlad.grid(column=1,row=8, padx=10, pady=10, sticky='W')
        lowBlad.bind('<Key>',lambda event: self.handleWait(event,lowBlad,"Louver_blade"))
        
        fraCol = ttk.Combobox(self.frame1, textvariable=fraColVar, width=30, values=frame_colour )
        fraCol.grid(column=1,row=9, padx=10, pady=10, sticky='W')
        fraCol.bind('<Key>',lambda event: self.handleWait(event,fraCol,"frame_colour"))
        
        silCol = ttk.Combobox(self.frame1, textvariable=silColVar, width=30, values=silicon_colour )
        silCol.grid(column=1,row=10, padx=10, pady=10, sticky='W')
        silCol.bind('<Key>',lambda event: self.handleWait(event,silCol,"silicon_colour"))
        
        frame1 = tk.LabelFrame(self.frame1, borderwidth=0)
        frame1.grid(column=1, row=11, padx=10, pady=10, sticky='W')
        
        screw1 = ttk.Checkbutton(frame1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(frame1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        
        screw2 = ttk.Checkbutton(frame1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(frame1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        
        screw3 = ttk.Checkbutton(frame1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(frame1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        
        screw4 = ttk.Checkbutton(frame1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(frame1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        
        screw5 = ttk.Checkbutton(frame1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(frame1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        
        screw6 = ttk.Checkbutton(frame1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(frame1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)
    
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=18, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################
     
class PattiLouver:
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
    
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 23, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 24, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 23, state='disabled')
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Patti Louver.png")
        resize_image = image.resize((580, 500))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        glaMaterial = ttk.Label(self.frame1, text="Glass Material")
        glaMaterial.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        lowBlade = ttk.Label(self.frame1, text="Louver Blade")
        lowBlade.grid(column=0, row=8, padx=10, pady=10, sticky='W')  
        fraCol = ttk.Label(self.frame1, text="Frame Colour")
        fraCol.grid(column=0, row=9, padx=10, pady=10, sticky='W')
        sili = ttk.Label(self.frame1, text="Silicon")
        sili.grid(column=0, row=10, padx=10, pady=10, sticky='W')
        screw = ttk.Label(self.frame1, text="Screw")
        screw.grid(column=0, row=11, padx=10, pady=10, sticky='W')
        
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
        
        aluMat = ttk.Combobox(self.frame1, textvariable=aluMatVar, width=30, values=aluminium_material )
        aluMat.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        aluMat.bind('<Key>',lambda event: self.handleWait(event,aluMat,"aluminium_material"))
        
        glaThic = ttk.Combobox(self.frame1, textvariable=glaThicVar, width=30, values=glass_thickness )
        glaThic.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        glaThic.bind('<Key>',lambda event: self.handleWait(event,glaThic,"glass_thickness"))
        
        glaTyp = ttk.Combobox(self.frame1, textvariable=glaTypVar, width=30, values=glass_type )
        glaTyp.grid(column=1,row=7, padx=10, pady=10, sticky='W')
        glaTyp.bind('<Key>',lambda event: self.handleWait(event,glaTyp,"glass_type"))

        lowBlad = ttk.Combobox(self.frame1, textvariable=lowBladVar, width=30, values=Louver_blade )
        lowBlad.grid(column=1,row=8, padx=10, pady=10, sticky='W')
        lowBlad.bind('<Key>',lambda event: self.handleWait(event,lowBlad,"Louver_blade"))
        
        fraCol = ttk.Combobox(self.frame1, textvariable=fraColVar, width=30, values=frame_colour )
        fraCol.grid(column=1,row=9, padx=10, pady=10, sticky='W')
        fraCol.bind('<Key>',lambda event: self.handleWait(event,fraCol,"frame_colour"))
        
        silCol = ttk.Combobox(self.frame1, textvariable=silColVar, width=30, values=silicon_colour )
        silCol.grid(column=1,row=10, padx=10, pady=10, sticky='W')
        silCol.bind('<Key>',lambda event: self.handleWait(event,silCol,"silicon_colour"))
        
        frame1 = tk.LabelFrame(self.frame1, borderwidth=0)
        frame1.grid(column=1, row=11, padx=10, pady=10, sticky='W')
        
        screw1 = ttk.Checkbutton(frame1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(frame1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        
        screw2 = ttk.Checkbutton(frame1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(frame1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        
        screw3 = ttk.Checkbutton(frame1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(frame1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        
        screw4 = ttk.Checkbutton(frame1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(frame1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        
        screw5 = ttk.Checkbutton(frame1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(frame1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        
        screw6 = ttk.Checkbutton(frame1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(frame1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)
        
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=18, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################
        
class OpenableWindow:
    
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 25, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 24, state='disabled')
        custConEnt.grid(column=5,row=1, padx=10, pady=10, sticky='W')
    
        selectWinLabel = ttk.Label(self.frame0, text=selectWinDrop.get(), font=("",10,"bold"))
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        widthLabel = ttk.Label(self.frame0, text="Enter Width (ft)")
        widthLabel.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        enterWidth = tk.Entry(self.frame0, textvariable=Width, relief="solid", width = 32, state='disabled')
        enterWidth.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        
        heightLabel = ttk.Label(self.frame0, text="Enter Height (ft)")
        heightLabel.grid(column=0, row=2, padx=10, pady=10, sticky='W')
        enterHeight = tk.Entry(self.frame0, textvariable=Height, relief="solid", width = 32, state='disabled')
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Openable Window.png")
        resize_image = image.resize((610, 500))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        typeLabel = ttk.Label(self.frame1, text="Type")
        typeLabel.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        glaMaterial = ttk.Label(self.frame1, text="Glass Material")
        glaMaterial.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=8, padx=10, pady=10, sticky='W')
        hardLock = ttk.Label(self.frame1, text="Hardware Lock")
        hardLock.grid(column=0, row=9, padx=10, pady=10, sticky='W')
        hardBear = ttk.Label(self.frame1, text="Hardware Bearing")
        hardBear.grid(column=0, row=10, padx=10, pady=10, sticky='W')
        rubber = ttk.Label(self.frame1, text="Rubber")
        rubber.grid(column=0, row=11, padx=10, pady=10, sticky='W')
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
        handle = ttk.Label(self.frame1, text="Handle")
        handle.grid(column=0, row=17, padx=10, pady=10, sticky='W')  
        screw = ttk.Label(self.frame1, text="Screw")
        screw.grid(column=0, row=18, padx=10, pady=10, sticky='W')
        
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
        
        handle = ttk.Combobox(self.frame1, textvariable=handleVar, width=30, values=handle_options )
        handle.grid(column=1,row=17, padx=10, pady=10, sticky='W')
        handle.bind('<Key>',lambda event: self.handleWait(event,handle,"handle_options"))
        
        frame1 = tk.LabelFrame(self.frame1, borderwidth=0)
        frame1.grid(column=1, row=18, padx=10, pady=10, sticky='W')
        
        screw1 = ttk.Checkbutton(frame1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(frame1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        
        screw2 = ttk.Checkbutton(frame1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(frame1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        
        screw3 = ttk.Checkbutton(frame1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(frame1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        
        screw4 = ttk.Checkbutton(frame1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(frame1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        
        screw5 = ttk.Checkbutton(frame1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(frame1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        
        screw6 = ttk.Checkbutton(frame1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(frame1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)
        
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=19, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################

class SlidingFoldingDoor:
    
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None

    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
    
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 25, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 25, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 25, state='disabled')
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Sliding folding door 1.png")
        resize_image = image.resize((625, 500))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        typeLabel = ttk.Label(self.frame1, text="Type")
        typeLabel.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        glaMaterial = ttk.Label(self.frame1, text="Glass Material")
        glaMaterial.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=8, padx=10, pady=10, sticky='W')
        hardLock = ttk.Label(self.frame1, text="Hardware Lock")
        hardLock.grid(column=0, row=9, padx=10, pady=10, sticky='W')
        hardBear = ttk.Label(self.frame1, text="Hardware Bearing")
        hardBear.grid(column=0, row=10, padx=10, pady=10, sticky='W')
        rubber = ttk.Label(self.frame1, text="Rubber")
        rubber.grid(column=0, row=11, padx=10, pady=10, sticky='W')
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
        channel = ttk.Label(self.frame1, text="Channel")
        channel.grid(column=0, row=17, padx=10, pady=10, sticky='W') 
        screw = ttk.Label(self.frame1, text="Screw")
        screw.grid(column=0, row=18, padx=10, pady=10, sticky='W')
         
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
        
        handle = ttk.Combobox(self.frame1, textvariable=handleVar, width=30, values=channel_options )
        handle.grid(column=1,row=17, padx=10, pady=10, sticky='W')
        handle.bind('<Key>',lambda event: self.handleWait(event,handle,"channel_options"))
        
        frame1 = tk.LabelFrame(self.frame1, borderwidth=0)
        frame1.grid(column=1, row=18, padx=10, pady=10, sticky='W')
        
        screw1 = ttk.Checkbutton(frame1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(frame1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        
        screw2 = ttk.Checkbutton(frame1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(frame1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        
        screw3 = ttk.Checkbutton(frame1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(frame1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        
        screw4 = ttk.Checkbutton(frame1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(frame1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        
        screw5 = ttk.Checkbutton(frame1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(frame1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        
        screw6 = ttk.Checkbutton(frame1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(frame1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)
        
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=19, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################
        
class CasementWindow:
    
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None

    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
    
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 25, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 24, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 25, state='disabled')
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Casement Window.png")
        resize_image = image.resize((620, 500))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        typeLabel = ttk.Label(self.frame1, text="Type")
        typeLabel.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        glaMaterial = ttk.Label(self.frame1, text="Glass Material")
        glaMaterial.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=8, padx=10, pady=10, sticky='W')
        hardLock = ttk.Label(self.frame1, text="Hardware Lock")
        hardLock.grid(column=0, row=9, padx=10, pady=10, sticky='W')
        hardBear = ttk.Label(self.frame1, text="Hardware Bearing")
        hardBear.grid(column=0, row=10, padx=10, pady=10, sticky='W')
        rubber = ttk.Label(self.frame1, text="Rubber")
        rubber.grid(column=0, row=11, padx=10, pady=10, sticky='W')
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
        handle = ttk.Label(self.frame1, text="Handle")
        handle.grid(column=0, row=17, padx=10, pady=10, sticky='W')  
        screw = ttk.Label(self.frame1, text="Screw")
        screw.grid(column=0, row=18, padx=10, pady=10, sticky='W')
        
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
        
        handle = ttk.Combobox(self.frame1, textvariable=handleVar, width=30, values=handle_options )
        handle.grid(column=1,row=17, padx=10, pady=10, sticky='W')
        handle.bind('<Key>',lambda event: self.handleWait(event,handle,"handle_options"))
        
        frame1 = tk.LabelFrame(self.frame1, borderwidth=0)
        frame1.grid(column=1, row=18, padx=10, pady=10, sticky='W')
        
        screw1 = ttk.Checkbutton(frame1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(frame1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        
        screw2 = ttk.Checkbutton(frame1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(frame1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        
        screw3 = ttk.Checkbutton(frame1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(frame1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        
        screw4 = ttk.Checkbutton(frame1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(frame1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        
        screw5 = ttk.Checkbutton(frame1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(frame1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        
        screw6 = ttk.Checkbutton(frame1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(frame1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)
        
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=19, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################
     
class AluminiumPartition:
    
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
    
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 25, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 25, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 25, state='disabled')
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Aluminum partition.png")
        resize_image = image.resize((620, 450))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        glaMaterial = ttk.Label(self.frame1, text="Glass Material")
        glaMaterial.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        acrShee = ttk.Label(self.frame1, text="Acrylic Sheet Colour")
        acrShee.grid(column=0, row=8, padx=10, pady=10, sticky='W')
        fraCol = ttk.Label(self.frame1, text="Frame Colour")
        fraCol.grid(column=0, row=9, padx=10, pady=10, sticky='W')
        hard = ttk.Label(self.frame1, text="Hardware")
        hard.grid(column=0, row=10, padx=10, pady=10, sticky='W')  
        screw = ttk.Label(self.frame1, text="Screw")
        screw.grid(column=0, row=11, padx=10, pady=10, sticky='W')
        
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
        aluMat = ttk.Combobox(self.frame1, textvariable=aluMatVar, width=30, values=aluminium_material )
        aluMat.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        aluMat.bind('<Key>',lambda event: self.handleWait(event,aluMat,"aluminium_material"))
        
        glaThic = ttk.Combobox(self.frame1, textvariable=glaThicVar, width=30, values=glass_thickness )
        glaThic.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        glaThic.bind('<Key>',lambda event: self.handleWait(event,glaThic,"glass_thickness"))
        
        glaTyp = ttk.Combobox(self.frame1, textvariable=glaTypVar, width=30, values=glass_type )
        glaTyp.grid(column=1,row=7, padx=10, pady=10, sticky='W')
        glaTyp.bind('<Key>',lambda event: self.handleWait(event,glaTyp,"glass_type"))
        
        acrShe = ttk.Combobox(self.frame1, textvariable=acrSheVar, width=30, values=acrylic_options )
        acrShe.grid(column=1,row=8, padx=10, pady=10, sticky='W')
        acrShe.bind('<Key>',lambda event: self.handleWait(event,acrShe,"acrylic_options"))
        
        fraCol = ttk.Combobox(self.frame1, textvariable=fraColVar, width=30, values=frame_colour )
        fraCol.grid(column=1,row=9, padx=10, pady=10, sticky='W')
        fraCol.bind('<Key>',lambda event: self.handleWait(event,fraCol,"frame_colour"))
        
        hardwa = tk.Entry(self.frame1, textvariable=hardwaVar, width=33, relief="solid")
        hardwa.grid(column=1,row=10, padx=10, pady=10, sticky='W')
        
        frame1 = tk.LabelFrame(self.frame1, borderwidth=0)
        frame1.grid(column=1, row=11, padx=10, pady=10, sticky='W')
        
        screw1 = ttk.Checkbutton(frame1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(frame1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        
        screw2 = ttk.Checkbutton(frame1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(frame1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        
        screw3 = ttk.Checkbutton(frame1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(frame1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        
        screw4 = ttk.Checkbutton(frame1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(frame1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        
        screw5 = ttk.Checkbutton(frame1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(frame1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        
        screw6 = ttk.Checkbutton(frame1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(frame1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)
        
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=18, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################
        
class ToughenedPartition:
    
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
    
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 25, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 26, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 25, state='disabled')
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Toughened partition.png")
        resize_image = image.resize((630, 500))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        glaMaterial = ttk.Label(self.frame1, text="Glass Material")
        glaMaterial.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        fraCol = ttk.Label(self.frame1, text="Frame Colour")
        fraCol.grid(column=0, row=8, padx=10, pady=10, sticky='W')
        hard = ttk.Label(self.frame1, text="Hardware")
        hard.grid(column=0, row=9, padx=10, pady=10, sticky='W') 
        screw = ttk.Label(self.frame1, text="Screw")
        screw.grid(column=0, row=10, padx=10, pady=10, sticky='W')
        
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
        aluMat = ttk.Combobox(self.frame1, textvariable=aluMatVar, width=30, values=aluminium_material )
        aluMat.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        aluMat.bind('<Key>',lambda event: self.handleWait(event,aluMat,"aluminium_material"))
        
        glaThic = ttk.Combobox(self.frame1, textvariable=glaThicVar, width=30, values=glass_thickness )
        glaThic.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        glaThic.bind('<Key>',lambda event: self.handleWait(event,glaThic,"glass_thickness"))
        
        glaTyp = ttk.Combobox(self.frame1, textvariable=glaTypVar, width=30, values=glass_type )
        glaTyp.grid(column=1,row=7, padx=10, pady=10, sticky='W')
        glaTyp.bind('<Key>',lambda event: self.handleWait(event,glaTyp,"glass_type"))

        fraCol = ttk.Combobox(self.frame1, textvariable=fraColVar, width=30, values=frame_colour )
        fraCol.grid(column=1,row=8, padx=10, pady=10, sticky='W')
        fraCol.bind('<Key>',lambda event: self.handleWait(event,fraCol,"frame_colour"))
        
        hardwa = tk.Entry(self.frame1, textvariable=hardwaVar, width=33, relief="solid")
        hardwa.grid(column=1,row=9, padx=10, pady=10, sticky='W')
        
        frame1 = tk.LabelFrame(self.frame1, borderwidth=0)
        frame1.grid(column=1, row=10, padx=10, pady=10, sticky='W')
        
        screw1 = ttk.Checkbutton(frame1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(frame1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        
        screw2 = ttk.Checkbutton(frame1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(frame1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        
        screw3 = ttk.Checkbutton(frame1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(frame1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        
        screw4 = ttk.Checkbutton(frame1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(frame1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        
        screw5 = ttk.Checkbutton(frame1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(frame1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        
        screw6 = ttk.Checkbutton(frame1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(frame1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)
        
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=18, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################

class ToughenedDoor:
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Toughened Door.png")
        resize_image = image.resize((603, 500))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        glaMaterial = ttk.Label(self.frame1, text="Glass Material")
        glaMaterial.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        fraCol = ttk.Label(self.frame1, text="Frame Colour")
        fraCol.grid(column=0, row=8, padx=10, pady=10, sticky='W')
        hard = ttk.Label(self.frame1, text="Hardware")
        hard.grid(column=0, row=9, padx=10, pady=10, sticky='W') 
        screw = ttk.Label(self.frame1, text="Screw")
        screw.grid(column=0, row=10, padx=10, pady=10, sticky='W')
        
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
        aluMat = ttk.Combobox(self.frame1, textvariable=aluMatVar, width=30, values=aluminium_material )
        aluMat.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        aluMat.bind('<Key>',lambda event: self.handleWait(event,aluMat,"aluminium_material"))
        
        glaThic = ttk.Combobox(self.frame1, textvariable=glaThicVar, width=30, values=glass_thickness )
        glaThic.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        glaThic.bind('<Key>',lambda event: self.handleWait(event,glaThic,"glass_thickness"))
        
        glaTyp = ttk.Combobox(self.frame1, textvariable=glaTypVar, width=30, values=glass_type )
        glaTyp.grid(column=1,row=7, padx=10, pady=10, sticky='W')
        glaTyp.bind('<Key>',lambda event: self.handleWait(event,glaTyp,"glass_type"))

        fraCol = ttk.Combobox(self.frame1, textvariable=fraColVar, width=30, values=frame_colour )
        fraCol.grid(column=1,row=8, padx=10, pady=10, sticky='W')
        fraCol.bind('<Key>',lambda event: self.handleWait(event,fraCol,"frame_colour"))
        
        hardwa = tk.Entry(self.frame1, textvariable=hardwaVar, width=33, relief="solid")
        hardwa.grid(column=1,row=9, padx=10, pady=10, sticky='W')
        
        frame1 = tk.LabelFrame(self.frame1, borderwidth=0)
        frame1.grid(column=1, row=10, padx=10, pady=10, sticky='W')
        
        screw1 = ttk.Checkbutton(frame1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(frame1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        
        screw2 = ttk.Checkbutton(frame1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(frame1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        
        screw3 = ttk.Checkbutton(frame1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(frame1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        
        screw4 = ttk.Checkbutton(frame1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(frame1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        
        screw5 = ttk.Checkbutton(frame1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(frame1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        
        screw6 = ttk.Checkbutton(frame1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(frame1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)
        
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=18, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################
        
class CompositePanel:
    
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
    
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 25, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 25, background="#f0f0f0", foreground="#6d6d6d")
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Composite pannel.png")
        resize_image = image.resize((610, 500))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        compShee = ttk.Label(self.frame1, text="Composite Sheet")
        compShee.grid(column=0, row=6, padx=10, pady=10, sticky='W')      
        fraCol = ttk.Label(self.frame1, text="Frame Colour")
        fraCol.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        sili = ttk.Label(self.frame1, text="Silicon")
        sili.grid(column=0, row=8, padx=10, pady=10, sticky='W')
        maskTape = ttk.Label(self.frame1, text="Masking Tape")
        maskTape.grid(column=0, row=9, padx=10, pady=10, sticky='W') 
        screw = ttk.Label(self.frame1, text="Screw")
        screw.grid(column=0, row=10, padx=10, pady=10, sticky='W')
    
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
        aluMat = ttk.Combobox(self.frame1, textvariable=aluMatVar, width=30, values=aluminium_material )
        aluMat.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        aluMat.bind('<Key>',lambda event: self.handleWait(event,aluMat,"aluminium_material"))
        
        compShe = ttk.Combobox(self.frame1, textvariable=compSheVar, width=30, values=composite_options )
        compShe.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        compShe.bind('<Key>',lambda event: self.handleWait(event,compShe,"composite_options"))
        
        fraCol = ttk.Combobox(self.frame1, textvariable=fraColVar, width=30, values=frame_colour )
        fraCol.grid(column=1,row=7, padx=10, pady=10, sticky='W')
        fraCol.bind('<Key>',lambda event: self.handleWait(event,fraCol,"frame_colour"))
        
        silCol = ttk.Combobox(self.frame1, textvariable=silColVar, width=30, values=silicon_colour )
        silCol.grid(column=1,row=8, padx=10, pady=10, sticky='W')
        silCol.bind('<Key>',lambda event: self.handleWait(event,silCol,"silicon_colour"))
        
        maskTap = ttk.Combobox(self.frame1, textvariable=maskTapVar, width=30, values=masktape_options )
        maskTap.grid(column=1,row=9, padx=10, pady=10, sticky='W')
        maskTap.bind('<Key>',lambda event: self.handleWait(event,maskTap,"masktape_options"))
        
        frame1 = tk.LabelFrame(self.frame1, borderwidth=0)
        frame1.grid(column=1, row=10, padx=10, pady=10, sticky='W')
        
        screw1 = ttk.Checkbutton(frame1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(frame1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        
        screw2 = ttk.Checkbutton(frame1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(frame1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        
        screw3 = ttk.Checkbutton(frame1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(frame1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        
        screw4 = ttk.Checkbutton(frame1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(frame1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        
        screw5 = ttk.Checkbutton(frame1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(frame1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        
        screw6 = ttk.Checkbutton(frame1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(frame1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)
        
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=18, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################

class CurtainWall:
    
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
    
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 23, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 24, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 23, state='disabled')
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Curtain wall.png")
        resize_image = image.resize((630, 450))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
        glaMaterial = ttk.Label(self.frame1, text="Glass Material")
        glaMaterial.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        acpSheet = ttk.Label(self.frame1, text="ACP Sheet")
        acpSheet.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        
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
        glaThic = ttk.Combobox(self.frame1, textvariable=glaThicVar, width=30, values=glass_thickness )
        glaThic.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        glaThic.bind('<Key>',lambda event: self.handleWait(event,glaThic,"glass_thickness"))
        
        glaTyp = ttk.Combobox(self.frame1, textvariable=glaTypVar, width=30, values=glass_type )
        glaTyp.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        glaTyp.bind('<Key>',lambda event: self.handleWait(event,glaTyp,"glass_type"))
        
        acpShe = ttk.Combobox(self.frame1, textvariable=acpSheVar, width=30, values=acpsheet_options )
        acpShe.grid(column=1,row=7, padx=10, pady=10, sticky='W')
        acpShe.bind('<Key>',lambda event: self.handleWait(event,glaTyp,"acpsheet_options"))
        
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=18, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################
        
class FixWindow:
    
    new = None
    _after_id = None
    frame1 = None
    frame2 = None
    frame0 = None
    cstAmtInr = None
    
    def __init__(self, new):
        global cstAmtInr
        self.new = new
        self.cstAmtInr = cstAmtInr
    
    def calcCost(self):
        global finalCost, calculateFlag
        
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        elif(not costEntVar.get().isdigit()):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = int(totSQFt)*int(costEntVar.get())
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
    
        custDetails = ttk.Label(self.frame2, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",10,""), relief="solid", width = 23, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",10,""), relief="solid", height=3, width = 24, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",10,""), relief="solid", width = 23, state='disabled')
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
    
        image = Image.open("C:/Users/DarkLegacy/Documents/Window Q/Images/Fix Window.png")
        resize_image = image.resize((580, 500))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, Not actual product)", font=("",10,""))
        selectWinLabel.grid(column=2, row=17)
    
    def variableTitles(self):
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
        
        frame1 = tk.LabelFrame(self.frame1, borderwidth=0)
        frame1.grid(column=1, row=17, padx=10, pady=10, sticky='W')
        
        screw1 = ttk.Checkbutton(frame1,  variable = screwVar1, takefocus = 0)
        screw1.grid(column=0,row=0, sticky='N', padx=5, pady=5)
        screwLab1 = ttk.Label(frame1, text="6.56")
        screwLab1.grid(column=0, row=1, sticky='N', padx=5, pady=5)
        
        screw2 = ttk.Checkbutton(frame1,  variable = screwVar2, takefocus = 0)
        screw2.grid(column=1,row=0, sticky='N', padx=5, pady=5)
        screwLab2 = ttk.Label(frame1, text="9.56")
        screwLab2.grid(column=1, row=1, sticky='N', padx=5, pady=5)
        
        screw3 = ttk.Checkbutton(frame1,  variable = screwVar3, takefocus = 0)
        screw3.grid(column=2,row=0, sticky='N', padx=5, pady=5)
        screwLab3 = ttk.Label(frame1, text="25.6")
        screwLab3.grid(column=2, row=1, sticky='N', padx=5, pady=5)
        
        screw4 = ttk.Checkbutton(frame1,  variable = screwVar4, takefocus = 0)
        screw4.grid(column=3,row=0, sticky='N', padx=5, pady=5)
        screwLab4 = ttk.Label(frame1, text="32.6")
        screwLab4.grid(column=3, row=1, sticky='N', padx=5, pady=5)
        
        screw5 = ttk.Checkbutton(frame1,  variable = screwVar5, takefocus = 0)
        screw5.grid(column=4,row=0, sticky='N', padx=5, pady=5)
        screwLab5 = ttk.Label(frame1, text="50.8")
        screwLab5.grid(column=4, row=1, sticky='N', padx=5, pady=5)
        
        screw6 = ttk.Checkbutton(frame1,  variable = screwVar6, takefocus = 0)
        screw6.grid(column=5,row=0, sticky='N', padx=5, pady=5)
        screwLab6 = ttk.Label(frame1, text="75.10")
        screwLab6.grid(column=5, row=1, sticky='N', padx=5, pady=5)
        
        nextButt=tk.Button(self.frame1, text = 'Next', font=("",10,"bold"), width=24, command = toExcel)
        nextButt.grid(column=1,row=18, padx=10, pady=15, sticky='W')
    
####################################################################################################################################################        

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

obj = Cart()
cart= Image.open("./Images/CartIcon.png")
carImg = cart.resize((20,17), Image.ANTIALIAS)
cartImg= ImageTk.PhotoImage(carImg)
nextButt=tk.Button(root, text=' Cart ', font=("",10,"bold"), command=obj.addMorePage, image=cartImg, compound=tk.RIGHT)
nextButt.grid(column=1,row=0, padx=10, pady=15, sticky='NE')

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
custConEnt.grid(column=1,row=3, padx=10, pady=10, sticky='W')

# custDetails = ttk.Label(frame1, text="Enter Window Details", font=("",10,"bold"))
# custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
selectWinLabel = ttk.Label(frame1, text="Select Window Type")
selectWinLabel.grid(column=0, row=5, padx=10, pady=10, sticky='W')
selectWinDrop = ttk.Combobox(frame1, state="readonly", textvariable=windowTypeVar, width=27)
selectWinDrop['values'] = window_options
selectWinDrop.grid(column=1,row=5, padx=10, pady=10, sticky='W')
selectWinDrop.bind("<<ComboboxSelected>>",lambda e: selectWinLabel.focus())
nextButt=tk.Button(frame1, text = 'Next', font=("",10,"bold"), width=19, command = selector)
nextButt.grid(column=1,row=8, padx=10, pady=15, sticky='W')

widthLabel = ttk.Label(frame1, text="Enter Width (ft)")
widthLabel.grid(column=0, row=6, padx=10, pady=10, sticky='W')
enterWidth = tk.Entry(frame1, textvariable=Width, font=("",10,""), relief="solid", width = 27)
enterWidth.grid(column=1,row=6, padx=10, pady=10, sticky='W')
heightLabel = ttk.Label(frame1, text="Enter Height (ft)")
heightLabel.grid(column=0, row=7, padx=10, pady=10, sticky='W')
enterHeight = tk.Entry(frame1, textvariable=Height, font=("",10,""), relief="solid", width = 27)
enterHeight.grid(column=1,row=7, padx=10, pady=10, sticky='W')

m = tk.Menu(root)
root.config(menu=m)
file_menu = tk.Menu(m, tearoff=False)
m.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Open from file", command=open_file1)

root.mainloop()

# Louver