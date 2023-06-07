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

data = pd.read_excel('./Data/data.xlsx')
data = data.replace(float('nan'),"")

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
srno = data.shape[0]
num = list(data["Sr.No"])

if(data.shape[0]==0):
    srno=1

totSQFt = 0
new = None

####################################################################################################################################################

#***************************************************************************************************************************************************#


####################################################################################################################################################

def setCustomerName(cust):
    global custName
    custName = cust

####################################################################################################################################################


custName = None
today = date.today()
totSrno = len(list(data["Sr.No"]))
printCount = 0
ratio = dict()


SlidingWindowWidth = 45
SlidingWindowHeight = 40

SilidingDoorWidth = 45
SilidingDoorHeight = 41

FixLouverWidth = 40
FixLouverHeight= 48

PattiLouverWidth = 40
PattiLouverHeight= 48

OpenableWindowWidth = 45
OpenableWindowHeight = 43.5

SlidingfoldingdoorWidth = 45 
SlidingfoldingdoorHeight = 36

CasementWindowWidth = 40
CasementWindowHeight = 48

AluminiumpartitionWidth = 45
AluminiumpartitionHeight = 36

ToughenedpartitionWidth = 45
ToughenedpartitionHeight = 36

ToughenedDoorWidth = 45
ToughenedDoorHeight = 45

CompositepannelWidth = 45
CompositepannelHeight = 36

CurtainwallWidth = 45
CurtainwallHeight = 36

FixWindowWidth = 45
FixWindowHeight = 45

ExhaustFanWindowWidth = 45
ExhaustFanWindowHeight = 49.5
# ["Sliding Window", "Sliding Door", "Fix Louver", "Patti Louver", "Openable Window", "Sliding folding door", "Casement Window", "Aluminium partition", "Toughened partition", "Toughened Door", "Composite pannel", "Curtain wall", "Fix Window"

ratio["Sliding Window"] = [SlidingWindowWidth, SlidingWindowHeight]
ratio["Sliding Door"] = [SilidingDoorWidth, SilidingDoorHeight]
ratio["Fix Louver"] = [FixLouverWidth, FixLouverHeight]
ratio["Patti Louver"] = [PattiLouverWidth, PattiLouverHeight]
ratio["Openable Window"] = [OpenableWindowWidth, OpenableWindowHeight]
ratio["Sliding folding door"] = [SlidingfoldingdoorWidth, SlidingfoldingdoorHeight]
ratio["Casement Window"] = [CasementWindowWidth, CasementWindowHeight]
ratio["Aluminium partition"] = [AluminiumpartitionWidth, AluminiumpartitionHeight]
ratio["Toughened partition"] = [AluminiumpartitionWidth, AluminiumpartitionHeight]
ratio["Toughened Door"] = [AluminiumpartitionWidth, AluminiumpartitionHeight]
ratio["Composite pannel"] = [CompositepannelWidth, CompositepannelHeight]
ratio["Curtain wall"] = [CurtainwallWidth, CurtainwallHeight]
ratio["Fix Window"] = [FixWindowWidth, FixWindowHeight]
ratio["Exhaust Fan Window"] = [ExhaustFanWindowWidth, ExhaustFanWindowHeight]


varName = dict()
varName[1] = "Width"
varName[2] = "Height"
varName[4] = "Type"
varName[5] = "Aluminium Material"
varName[6] = "Glass Thickness"
varName[7] = "Glass Type"
varName[8] = "Hardware Lock"
varName[9] = "Hardware Bearing"
varName[10] = "Rubber Type"
varName[11] = "Rubber Thickness"
varName[12] = "Wool File"
varName[13] = "Aluminium Net"
varName[14] = "Frame Colour"
varName[15] = "Silicon"
# varName[16] = "Screw 6.56"
# varName[17] = "Screw 9.56"
# varName[18] = "Screw 25.6"
# varName[19] = "Screw 32.6"
# varName[20] = "Screw 50.8"
# varName[21] = "Screw 75.1"
varName[22] = "Lower Blade"
varName[23] = "Handle"
varName[24] = "Acrylic Sheet Colour"
varName[25] = "Hardware"
varName[26] = "Composite Sheet Colour"
varName[27] = "Masking Tape Colour"
varName[28] = "ACP Sheet"

totalLevel = 0
endLevel = 0

class PDF(FPDF):
    
    fileName = None
    printDoneFlag = False
    
    def header(self):
        self.set_font('helvetica', 'B', 15)

    def footer(self):
        self.set_y(-17)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(169,169,169)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')
        
        self.set_y(-12)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(169,169,169)
        self.cell(0, 10, "All Images shown are Illustrations, not actual product and not upto scale. Actual product may vary.", align='C')
        
    def insertImage(self,x,design,textLevel):
        
        key = data["windowTypeVar"][x]
        
        self.set_draw_color(0,0,0)
        self.line(design+5, textLevel+5.55, design+5, textLevel+4.7+ratio[key][1])
        
        if(ratio[key][0]<50):
            self.line(design+12.8, textLevel+9.5+ratio[key][1], design+ratio[key][0]+12.5, textLevel+9.5+ratio[key][1])
        else:
            self.line(design+7.8, textLevel+9.5+ratio[key][1], design+ratio[key][0]+7.5, textLevel+9.5+ratio[key][1])
        
        self.set_draw_color(169,169,169)
        self.dashed_line(design+5, textLevel+5.3, design+50, textLevel+5.3)
        self.dashed_line(design+5, textLevel+4.9+ratio[key][1], design+50, textLevel+4.9+ratio[key][1])
        
        if(ratio[key][0]<50):
            self.dashed_line(design+12.8, textLevel+5.2, design+12.8, textLevel+9.5+ratio[key][1])
            self.dashed_line(design+ratio[key][0]+12.5, textLevel+6, design+ratio[key][0]+12.5, textLevel+9.5+ratio[key][1])
        else:    
            self.dashed_line(design+7.8, textLevel+5.2, design+7.8, textLevel+9.5+ratio[key][1])
            self.dashed_line(design+ratio[key][0]+7.5, textLevel+6, design+ratio[key][0]+7.5, textLevel+9.5+ratio[key][1])
        
        if(ratio[key][0]<50):
            self.image('./Images/{}.png'.format(data["windowTypeVar"][x]), x=design + 12.5, y=textLevel+5, w=ratio[key][0], h=ratio[key][1])
        else:            
            self.image('./Images/{}.png'.format(data["windowTypeVar"][x]), x=design + 7.5, y=textLevel+5, w=ratio[key][0], h=ratio[key][1])
        
        strWidth = self.get_string_width(data["Width"][x])
        strHeight = self.get_string_width(data["Height"][x])
        
        self.set_y(textLevel+8.2+ratio[key][1])
        self.set_x(design+(60-strWidth)/2)
        self.set_font('helvetica', '', 6)
        self.set_fill_color(256,256,256)
        self.cell(w=strWidth+4, txt="{}".format(data["Width"][x]), align='C', fill=True)
        
        self.set_y(textLevel+4+(ratio[key][1])/2)
        self.set_x(design+1.7)
        self.set_font('helvetica', '', 6)
        self.set_fill_color(256,256,256)
        self.cell(w=strHeight+4, h=5, txt="{}".format(data["Height"][x]), align='C', fill=True)
        
        
    def printInPDF(self, textLevel, design, specs, cost, quantity, amount, x):
        
        print(x)
        key = data["windowTypeVar"][x]
        
        self.set_y(textLevel)
        self.set_x(15)
        self.set_font('helvetica', '', 6)
        self.cell(w=12,txt="{}".format(x+1), align='C')
        self.insertImage(x,design,textLevel)
        
        if(ratio[key][0]<50):
            self.set_y(textLevel+65)
        else:
            self.set_y(textLevel+55) 
        self.set_x(design)
        self.set_font('helvetica', 'B', 6)
        self.cell(w=65,txt="{}".format(data["windowTypeVar"][x]), align='C')
        
        self.printSpecs(textLevel,specs,x)
        
        self.set_y(textLevel)
        self.set_x(cost)
        self.set_font('helvetica', 'B', 6)
        self.cell(w=20,txt="Rs. {}".format(data["cstAmtInr"][x][1:]), align='C')
        
        self.set_y(textLevel)
        self.set_x(quantity)
        self.set_font('helvetica', '', 6)
        self.cell(w=10,txt="{}".format(data["quantity"][x]), align='C')
        
        self.set_y(textLevel)
        self.set_x(amount)
        self.set_font('helvetica', 'B', 6)
        self.cell(w=28,txt="Rs. {}".format(data["quantAmnt"][x][1:]), align='C')
        
        
    def printSpecs(self, textLevel, specs, x):
        self.set_y(textLevel)
        self.set_x(specs)
        self.set_font('helvetica', 'BI', 7)
        self.set_text_color(118, 175, 93)
        self.cell(w=10,txt="Rate (Rs.): {} Sq.Ft.".format(data["costEntVar"][x]))
        textLevel = textLevel + 4
        self.set_y(textLevel)
        self.set_x(specs)
        self.set_font('helvetica', '', 6)
        self.set_text_color(0,0,0)
        self.cell(w=10,txt="Area: {} Sq.Ft.".format(data["totSqftEntVar"][x]))
        textLevel = textLevel + 4
        self.set_y(textLevel)
        self.set_x(specs)
        for i in varName.keys():
            if(data.iloc[x][i]!="" and data.iloc[x][i]!=0 ):
                self.multi_cell(w=40, h=3.5, txt="{}: {}".format(varName[i], data.iloc[x][i]))
                textLevel = self.get_y()
                self.set_y(textLevel)
                self.set_x(specs)

    def drawLines(self, titleLevelY):
        titleLevelX = 15
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+89)
        titleLevelX = titleLevelX + 12
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+89)
        titleLevelX = titleLevelX + 65
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+89)
        titleLevelX = titleLevelX + 45
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+89)
        titleLevelX = titleLevelX + 20
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+89)
        titleLevelX = titleLevelX + 10
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+89)
        titleLevelX = titleLevelX + 28
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+89)
        self.line(15, titleLevelY+89, 195, titleLevelY+89)
        
    def drawLinesHome(self, titleLevelY, noOfDiv):
        titleLevelX = 15
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+noOfDiv)
        titleLevelX = titleLevelX + 12
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+noOfDiv)
        titleLevelX = titleLevelX + 65
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+noOfDiv)
        titleLevelX = titleLevelX + 45
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+noOfDiv)
        titleLevelX = titleLevelX + 20
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+noOfDiv)
        titleLevelX = titleLevelX + 10
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+noOfDiv)
        titleLevelX = titleLevelX + 28
        self.set_draw_color(169,169,169)
        self.line(titleLevelX, titleLevelY, titleLevelX, titleLevelY+noOfDiv)
        self.line(15, titleLevelY+noOfDiv, 195, titleLevelY+noOfDiv)

    def homePage(self):
        global printCount,totalLevel
        
        self.image('./Images/MGA_1.png', x=20, y=10, w=55, h=35.9)
        self.line(85, 6, 85, 48)
        self.image('./Images/Mapslogo.png', x=95, y=12, w=5, h=7, link="https://www.google.com/maps/place/Madhav+Glass+and+Aluminium/@19.8758195,75.3916281,18.5z/data=!4m5!3m4!1s0x0:0x6466e4a2d6fec24c!8m2!3d19.8759565!4d75.3913081")
        self.image('./Images/PhoneIcon.png', x=95, y=24, w=5, h=5)
        self.image('./Images/EmailIcon.png', x=95, y=35, w=5, h=3.8)

        self.set_y(15)
        self.set_x(102)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="Chikalthana MIDC, Opp Ajantha Pharma, Aurangabad - 431001", link="https://www.google.com/maps/place/Madhav+Glass+and+Aluminium/@19.8758195,75.3916281,18.5z/data=!4m5!3m4!1s0x0:0x6466e4a2d6fec24c!8m2!3d19.8759565!4d75.3913081")

        self.set_y(27)
        self.set_x(102)
        self.cell(w=0,txt="7875115371, 8149440829")

        self.set_y(37)
        self.set_x(102)
        self.cell(w=0,txt="madhavglassandaluminium@gmail.com")

        self.line(15, 52, 195, 52)
        self.dashed_line(15, 53, 195, 53)

        self.set_y(60)
        self.set_x(170)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="Date:")

        self.set_y(60.1)
        self.set_x(179)
        self.set_font('helvetica', '', 9)
        self.cell(w=0,txt="{}/{}/{}".format(today.day,today.month,today.year))

        self.set_y(67)
        self.set_x(140)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="Quotaion Number: ")

        wi = self.get_string_width("Quotaion Number: ")
        
        self.set_y(67)
        self.set_x(140+wi)
        self.set_font('helvetica', '', 9)
        self.cell(w=0,txt="{}".format(data["quotaionNumber"][0]))

        self.set_y(60)
        self.set_x(15)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="To,")

        self.set_y(67)
        self.set_x(15)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="{} ".format(data["custNamVar"][0]))

        self.set_y(70)
        self.set_x(15)
        self.set_font('helvetica', 'B', 8)
        self.multi_cell(w=60, h=3.5,txt="{}".format(data["address"][0]))

        self.ln(h=7)
        titleLevelY = self.get_y()
        titleLevelX = 15

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=12, h=10, txt="Sr.No", fill=True, border=True, align='C')

        titleLevelX = titleLevelX + 12

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=65, h=10, txt="DESIGN", fill=True, border=True, align='C')

        design = titleLevelX
        titleLevelX = titleLevelX + 65

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=45, h=10, txt="SPECIFICATIONS", fill=True, border=True, align='C')

        specs = titleLevelX
        titleLevelX = titleLevelX + 45

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=20, h=10, txt="COST(Rs.)", fill=True, border=True, align='C')

        cost = titleLevelX
        titleLevelX = titleLevelX + 20
        
        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=10, h=10, txt="QTY", fill=True, border=True, align='C')

        quantity = titleLevelX
        titleLevelX = titleLevelX + 10

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=28, h=10, txt="AMOUNT(Rs.)", fill=True, border=True, align='C')

        amount = titleLevelX

        noOfDiv = (280 - titleLevelY)/2
        textLevel = titleLevelY + 15
        
        for i in range(2):
            if(printCount<data[data.columns[0]].count()):
                self.drawLinesHome(titleLevelY,noOfDiv)
                
                printCount+=1
                self.printInPDF(textLevel, design, specs, cost, quantity, amount, i)
                textLevel = textLevel + noOfDiv
                titleLevelY = textLevel - 15
            
        totalLevel = self.get_y()
        
    def newPage(self):
        global printCount, totSrno, totalLevel
        
        titleLevelY = 15
        titleLevelX = 15
        
        self.set_draw_color(0,0,0)

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=12, h=10, txt="Sr.No", fill=True, border=True, align='C')
        
        titleLevelX = titleLevelX + 12
        
        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=65, h=10, txt="DESIGN", fill=True, border=True, align='C')
        
        design = titleLevelX
        titleLevelX = titleLevelX + 65
        
        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=45, h=10, txt="SPECIFICATIONS", fill=True, border=True, align='C')
        
        specs = titleLevelX
        titleLevelX = titleLevelX + 45
        
        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=20, h=10, txt="COST(Rs.)", fill=True, border=True, align='C')
        
        cost = titleLevelX
        titleLevelX = titleLevelX + 20
        
        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=10, h=10, txt="QTY", fill=True, border=True, align='C')
        
        quantity = titleLevelX
        titleLevelX = titleLevelX + 10
        
        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=28, h=10, txt="AMOUNT(Rs.)", fill=True, border=True, align='C')
        
        amount = titleLevelX
        titleLevelX = titleLevelX + 28
        titleLevelY = titleLevelY
        
        for i in range(3):
            if(printCount<data[data.columns[0]].count()):
                if(i==0):
                    self.drawLines(titleLevelY+6)
                    self.printInPDF(titleLevelY + 15, design, specs, cost, quantity, amount, printCount)
                    printCount+=1
                    titleLevelY = titleLevelY+88
                elif(i==1):
                    self.drawLines(titleLevelY+2.5)
                    self.printInPDF(titleLevelY + 15, design, specs, cost, quantity, amount, printCount)
                    printCount+=1
                    titleLevelY = titleLevelY+88
                else:
                    self.drawLines(titleLevelY)
                    self.printInPDF(titleLevelY + 15, design, specs, cost, quantity, amount, printCount)
                    printCount+=1
                    titleLevelY = titleLevelY+88
        
        totalLevel = self.get_y()

    def totalDisplay(self):
        global totalLevel, endLevel
        
        totalLevel = 20
        
        lastRow = data.shape[0] - 1
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        
        temp = data["totQuanSum"][0]
        total = float(temp[1:].replace(",",""))
        disc = 0
        preTax = 0
        cgst = 0
        sgst = 0
        postTax = 0
        inst = 0
        
        wi = self.get_string_width("Total Area: ")
        self.set_y(totalLevel)
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=wi + 2, h=6, txt="Total Area: ", align='L')
        
        tempList = list(data["totSqftEntQuantVar"])
        tempList = [float(i) for i in tempList]
        
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=20, h=6, txt="{} Sq.Ft.".format(round(sum(tempList),2)), align='L')
        
        self.set_y(totalLevel)
        self.set_x(100)
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=45, h=6, txt="Total", fill=True, border=True, align='C')
        
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=10, h=6, txt=" : ", fill=True, border=True, align='C')
        
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=40, h=6, txt="Rs. {}".format(data["totQuanSum"][0][1:]), fill=True, border=True, align='C')
        
        totalLevel = totalLevel + 6
            
        wi = self.get_string_width("Total Windows: ")
        self.set_y(totalLevel)
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=wi, h=6, txt="Total Windows: ", align='L')
        
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=20, h=6, txt="{} Nos".format(round(sum(data["quantity"]),2)), align='L')
        
        if(data["discountFlag"][0]=="True Flag"):
            disc = float(data["discountEntVar"][lastRow])
            discAm = indCurr(round(disc,2))
            
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="Discount", fill=True, border=True, align='C')
            
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
        
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(discAm[1:]), fill=True, border=True, align='C')
        
            totalLevel = totalLevel + 6
        
        preTaxTo = indCurr(round(total - disc,2))
        preTax = total - disc
        
        self.set_y(totalLevel)
        self.set_x(100)
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=45, h=6, txt="Pre-Tax Total", fill=True, border=True, align='C')
        
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=10, h=6, txt=" : ", fill=True, border=True, align='C')
        
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=40, h=6, txt="Rs. {}".format(preTaxTo[1:]), fill=True, border=True, align='C')
        
        totalLevel = totalLevel + 6
        cgst = indCurr(round(preTax*9/100,2))
        sgst = indCurr(round(preTax*9/100,2))
        
        self.set_y(totalLevel)
        self.set_x(100)
        self.set_font('helvetica', '', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=45, h=7, txt="CGST @9%", fill=True, border=True, align='C')
        
        self.set_font('helvetica', '', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
        
        self.set_font('helvetica', '', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=40, h=7, txt="Rs. {}".format(cgst[1:]), fill=True, border=True, align='C')
        
        totalLevel = totalLevel + 6
        
        self.set_y(totalLevel)
        self.set_x(100)
        self.set_font('helvetica', '', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=45, h=7, txt="SGST @9%", fill=True, border=True, align='C')
        
        self.set_font('helvetica', '', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
        
        self.set_font('helvetica', '', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=40, h=7, txt="Rs. {}".format(sgst[1:]), fill=True, border=True, align='C')
    
        totalLevel = totalLevel + 6
        postTaxTo = indCurr(round(preTax + (preTax*18/100),2))
        postTax = (preTax + (preTax*18/100))
        
        self.set_y(totalLevel)
        self.set_x(100)
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=45, h=7, txt="Post-Tax Total", fill=True, border=True, align='C')
        
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
        
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=40, h=7, txt="Rs. {}".format(postTaxTo[1:]), fill=True, border=True, align='C')
        
        totalLevel = totalLevel + 6
        
        if(data["installationFlag"][0]=="True Flag"):
            inst = float(data["instEntVar"][lastRow])
            instAm = indCurr(round(inst,2))
            
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', '', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="Installation Charges", fill=True, border=True, align='C')
            
            self.set_font('helvetica', '', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
        
            self.set_font('helvetica', '', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(instAm[1:]), fill=True, border=True, align='C')
        
            totalLevel = totalLevel + 6
            postTax = postTax + inst
        
        granTot = indCurr(round(postTax,2))
        
        self.set_y(totalLevel)
        self.set_x(100)
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=45, h=7, txt="Grand Total", fill=True, border=True, align='C')
        
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
        
        self.set_font('helvetica', 'B', 7)
        self.set_fill_color(229,233,243)
        self.cell(w=40, h=7, txt="Rs. {}".format(granTot[1:]), fill=True, border=True, align='C')
        
        endLevel = self.get_y() + 15
        
    def pdfEnd(self):
        global endLevel
        
        str1 = "Freight charges are extra and to be mentioned on the day of delivery. Quotation validity is (7) days from the date of issue."
        str2 = "1. PAYMENT"
        str3 = "a. An advance 70% of the amount should be paid once the order is confirmed."
        str4 = "b. 25% of the amount after the material is received on site."
        str5 = "c. Balalnce amount to be paid at the time of handover."
        str6 = "3. WORK SPACE & ELECTRICITY"
        str7 = "a. Adequate storage space and electricity shall be provided on site by the customer."
        str8 = "4. Aperture/Surface where window will be installed should be smooth."
        str9 = "5. At least one coat of paint must be finished before installation."
        str10 = "6. Grills must be painted before installation begins."
        str11 = "7. Scaffolding/Bracing should be provided on site by the customer if required."
        str12 = "8. Measurements are taken as per standard units."
        str13 = "9. Actual cost may vary based on the measurement taken at the time of installation."
        str14 = "Thanking you and assuring you the best of our services all the times."
        str15 = "I have gone through the specifications & Drawings. \nI accept terms and conditions"

        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.set_text_color(255,0,0)
        self.multi_cell(w=180, h=7, txt=str1, align='L')
        
        endLevel = self.get_y() + 10
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.set_text_color(0,0,0)
        self.multi_cell(w=180, h=7, txt=str2, align='L')
        
        endLevel = self.get_y()
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 9)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str3, align='L')
        
        endLevel = self.get_y() 
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 9)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str4, align='L')
        
        endLevel = self.get_y()
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B',9 )
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str5, align='L')
        
        endLevel = self.get_y() + 5
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str6, align='L')
        
        endLevel = self.get_y() 
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B',9 )
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str7, align='L')
        
        endLevel = self.get_y() + 3
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str8, align='L')
        
        endLevel = self.get_y() + 3
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str9, align='L')
        
        endLevel = self.get_y() + 3
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str10, align='L')
        
        
        endLevel = self.get_y() + 3
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str11, align='L')
        
        endLevel = self.get_y() + 3
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str12, align='L')
        
        endLevel = self.get_y() + 3
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str13, align='L')
        
        endLevel = self.get_y() + 3
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str14, align='L')
        
        endLevel = self.get_y() +  40
        print(endLevel)
        if(endLevel>270):
            self.add_page()
            endLevel = 50
            
        self.set_y(endLevel)
        self.set_x(115)
        self.set_font('helvetica', 'B', 9)
        self.set_fill_color(229,233,243)
        # self.set_text_color(255,0,0)
        self.multi_cell(w=85, h=7, txt=str15, align='L')
        
        
    def driverCode(self):
        global printCount
        
        printCount = 0
        self.alias_nb_pages()
        self.set_left_margin(15)
        self.set_right_margin(15)
        self.set_auto_page_break(auto = True, margin = 15)
        self.add_page()
        self.set_y(15)
        self.homePage()

        for i in range(ceil((data.shape[0]-2)/3)):
            self.add_page()
            self.newPage()

        self.add_page()
        self.totalDisplay()
        self.pdfEnd()
        self.output(self.fileName)
        self.printDoneFlag = True

#***************************************************************************************************************************************************#

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

def checkDigits():
    localFlag = True
    for i in str(costEntVar.get()):
        if (i not in digVerify):
            print(i)
            localFlag = False
            return localFlag
            break
    return localFlag

def clearValues():
    global quantity
    
    # Width.set("")
    # Height.set("")
    # windowTypeVar.set("")
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
    # totSqftEntVar.set("")
    # cstAmtInr.set("")
    # costEntVar.set("")
    # discountEntVar.set("")
    # gstEntVar.set("")
    # costTotVar.set("")
    # discTotVar.set("")
    # gstTotVar.set("")
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
        

    data.loc[len(data.index)] = [""]*59
    
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
    data['costEntVar'] = addNewRowData(costEntVar, "costEntVar")
    data['discountEntVar'] = addNewRowData(discountEntVar, "discountEntVar")
    data['gstEntVar'] = addNewRowData(gstEntVar, "gstEntVar")
    data['costTotVar'] = addNewRowData(costTotVar, "costTotVar")
    data['discTotVar'] = addNewRowData(discTotVar, "discTotVar")
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

def afterCalculate():
    global srno, windowTypeVar,	trackVar, aluMatVar, glaThicVar, glaTypVar, hardLocVar, hardBeaVar, rubbTypVar, rubbThicVar, woolFileVar, aluNetVar,	fraColVar, silColVar, screwVar1, screwVar2, screwVar3, screwVar4, screwVar5, screwVar6, lowBladVar, handleVar, acrSheVar, hardwaVar, compSheVar, 	maskTapVar, acpSheVar, totSqftEntVar, costEntVar, profitEntVar, discountEntVar, labourEntVar, gstEntVar, costTotVar, profTotVar, discTotVar, laboTotVar	, gstTotVar, custNamVar, custAddVar, custConVar, address
    
    data['discountEntVar'] = addNewRowData(discountEntVar, "discountEntVar")
    data['instEntVar'] = addNewRowData(instEntVar, "instEntVar")
    data['gstEntVar'] = addNewRowData(gstEntVar, "gstEntVar")
    data['costTotVar'] = addNewRowData(costTotVar, "costTotVar")
    data['discTotVar'] = addNewRowData(discTotVar, "discTotVar")
    data['instTotVar'] = addNewRowData(instTotVar, "instTotVar")
    data['gstTotVar'] = addNewRowData(gstTotVar, "gstTotVar")
    
    data.to_excel('./Data/{}_QuatationData.xlsx'.format(custNamVar.get()), index=False)


#***********************-----------------------------**************************----------------------------**********************------------------

custName = None
today = date.today()
printCount = 0
taxPrintCount = 0
taxLevel = 0
endPrintLevel = 0
amtsum = 0

class PDFInvoice(FPDF):
    
    fileName = None
    printDoneFlag = False
    buyerY = None
    
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, 'TAX INVOICE', align='C')

        self.line(15, 20, 15, 280)
        self.line(195, 20, 195, 280)
        self.line(15, 20, 195, 20)
        self.line(15, 280, 195, 280)
    
    def footer(self):
        self.set_y(-17)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(169,169,169)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')
        
        self.set_y(-12)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(169,169,169)
        self.cell(0, 10, "This is a Computer Generated Invoice.", align='C')

    def drawLines(self, titleLevelY=10):
        
        self.line(105, 20, 105, 65)
        self.line(15, 65, 195, 65)
        self.line(15, 80, 195, 80)
        self.line(15, 95, 195, 95)
        
        for i in range(1,4):
            self.line(15+(60*i), 65, 15+(60*i), 95 )
            
        self.line(15, 96, 195, 96)
      
    def drawLinesInfo(self, printLevel):
        self.line(15, 105, 195, 105)
        self.line(23, 96, 23, printLevel)
        self.line(88, 96, 88, printLevel)
        self.line(108, 96, 107, printLevel)
        self.line(132, 96, 132, printLevel)
        self.line(157, 96, 157, printLevel)
        self.line(167.5, 96, 167.5, printLevel)
       
    def drawLinesTax(self, startTaxLevel, taxLevel):
        self.line(40, startTaxLevel, 40, taxLevel+7)
        self.line(70, startTaxLevel, 70, taxLevel+7)
        self.line(120, startTaxLevel, 120, taxLevel+7)
        self.line(170, startTaxLevel, 170, taxLevel+7)
        self.line(70, startTaxLevel+8, 170, startTaxLevel + 8)
        self.line(90, startTaxLevel+8, 90, taxLevel+7)
        self.line(140, startTaxLevel+8, 140, taxLevel+7)
        self.line(15, startTaxLevel+16, 195, startTaxLevel + 16)
        

    def printTaxInfo(self, taxLevel, x, taxSum):
        global amtsum
        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        
        self.set_y(taxLevel+2)
        self.set_x(15)
        self.set_font('helvetica', '', 8)
        self.cell(w=25,txt="{}".format(data["hsnSacVar"][x]), align='C')

        amt = data["quantAmnt"][x]
        amtD = float(amt[1:].replace(",",""))
        
        if(data["discountFlag"][0]=="True Flag"):
        
            lastRow = data.shape[0] - 1
            disc = float(data["discountEntVar"][lastRow])
            discPerItem = disc/data.shape[0]
            amtD = amtD - discPerItem
            
        amtI = indCurr(round(amtD,2))
        
        amtsum = amtsum + amtD
        
        self.set_y(taxLevel+2)
        self.set_x(40)
        self.set_font('helvetica', '', 8)
        self.cell(w=30,txt="Rs. {}".format(amtI[1:]), align='C')


        self.set_y(taxLevel+2)
        self.set_x(70)
        self.set_font('helvetica', '', 8)
        self.cell(w=20,txt="9%", align='C')
        
        taxC = amtD
        taxC = taxC*9/100
        taxAmt = indCurr(taxC)
        self.set_y(taxLevel+2)
        self.set_x(90)
        self.set_font('helvetica', '', 8)
        self.cell(w=30,txt="Rs. {}".format(taxAmt[1:]), align='C')

        self.set_y(taxLevel+2)
        self.set_x(120)
        self.set_font('helvetica', '', 8)
        self.cell(w=20,txt="9%", align='C')
        
        self.set_y(taxLevel+2)
        self.set_x(140)
        self.set_font('helvetica', '', 8)
        self.cell(w=30,txt="Rs. {}".format(taxAmt[1:]), align='C')
    
        finTax = taxC*2
        finTax = indCurr(finTax)
        self.set_y(taxLevel + 2)
        self.set_x(170)
        self.set_font('helvetica', '', 8)
        self.cell(w=25,txt="Rs. {}".format(finTax[1:]), align='C')
        
        return taxSum + taxC

    def printInfo(self, x, printLevel):
        
        self.set_y(printLevel)
        self.set_x(15.5)
        self.set_font('helvetica', '', 8)
        self.cell(w=7,txt="{}".format(x+1), align="C")
        
        wi = float(data["Width"][x].replace("ft",""))
        he = float(data["Height"][x].replace("ft",""))
        
        area = wi*he
        are = str(round(area,2)) + " Sq Ft."
        
        desc = data["windowTypeVar"][x]
        desc1 = " (" + data["Width"][x] + " x " + data["Height"][x] + " = " + are + ")"

        w = self.get_string_width(desc)

        self.set_y(printLevel)
        self.set_x(24)
        self.set_font('helvetica', 'BI', 8)
        self.cell(w=w+2,txt="{}".format(desc), align="L")
        self.set_font('helvetica', '', 7)
        self.cell(w=77,txt="{}".format(desc1), align="L")
        
        self.set_y(printLevel)
        self.set_x(88)
        self.set_font('helvetica', '', 8)
        self.cell(w=20,txt="{}".format(data["hsnSacVar"][x]), align='C')
        
        amount = data["cstAmtInr"][x]
        rate = data["costEntVar"][x]

        self.set_y(printLevel)
        self.set_x(115)
        self.set_font('helvetica', '', 8)
        self.cell(w=22.5,txt="{}".format(rate), align='L')

        self.set_y(printLevel)
        self.set_x(133)
        self.set_font('helvetica', '', 8)
        self.cell(w=25,txt="Rs. {}".format(amount[1:]), align='L')

        self.set_y(printLevel)
        self.set_x(160)
        self.set_font('helvetica', '', 8)
        self.cell(w=8, txt="{}".format(data["quantity"][x]), align='C')
        
        amt = data["quantAmnt"][x]

        self.set_y(printLevel)
        self.set_x(168)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=22.5,txt="Rs. {}".format(amt[1:]), align='L')
        
    def homePage(self):
        pass
        
        self.set_y(23)
        self.set_x(17.5)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=12,txt="Seller", align='C')        
        
        self.set_y(30)
        self.set_x(17)
        self.set_font('helvetica', 'BI', 8)
        self.cell(w=0,txt="Madhav Glass and Aluminium")
        
        self.set_y(34)
        self.set_x(17)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="Chikalthana MIDC, Opp Ajantha Pharma,", link="https://www.google.com/maps/place/Madhav+Glass+and+Aluminium/@19.8758195,75.3916281,18.5z/data=!4m5!3m4!1s0x0:0x6466e4a2d6fec24c!8m2!3d19.8759565!4d75.3913081")

        self.set_y(38)
        self.set_x(17)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="Aurangabad - 431001", link="https://www.google.com/maps/place/Madhav+Glass+and+Aluminium/@19.8758195,75.3916281,18.5z/data=!4m5!3m4!1s0x0:0x6466e4a2d6fec24c!8m2!3d19.8759565!4d75.3913081")
        
        self.set_y(42)
        self.set_x(17)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="State Name : ")
        
        wi = self.get_string_width("State Name : ")
        
        self.set_y(42)
        self.set_x(17+wi)
        self.set_font('helvetica', 'I', 8)
        self.cell(w=0,txt="Maharashtra, Code : 27")
        
        self.set_y(46)
        self.set_x(17)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="Contact : ")
        
        wi = self.get_string_width("Contact : ")
        
        self.set_y(46)
        self.set_x(17+wi)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="7875115371, 8149440829")
        
        self.set_y(50)
        self.set_x(17)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="Email-ID : ")
        
        wi = self.get_string_width("Email-ID : ")
        
        self.set_y(50)
        self.set_x(17+wi)
        self.set_font('helvetica', 'I', 8)
        self.cell(w=0,txt="madhavglassandaluminium@gmail.com")
        
        self.set_y(54)
        self.set_x(17)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="GST Registration No : ")
        
        wi = self.get_string_width("GST Registration No : ")
        
        self.set_y(54)
        self.set_x(17+wi)
        self.set_font('helvetica', 'I', 8)
        self.cell(w=0,txt="27CURPB8193C1ZC")
    
        self.set_y(58)
        self.set_x(17)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="PAN No : ")
        
        wi = self.get_string_width("PAN No : ")
        
        self.set_y(58)
        self.set_x(17+wi)
        self.set_font('helvetica', 'I', 8)
        self.cell(w=0,txt="CURPB8193C")
        
        self.set_y(23)
        self.set_x(107)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Buyer")
        
        self.set_y(30)
        self.set_x(107)
        self.set_font('helvetica', 'BI', 8)
        self.cell(w=0,txt="{}".format(data["custNamVar"][0]))
        
        self.set_y(34)
        self.set_x(107)
        self.set_font('helvetica', '', 8)
        self.multi_cell(w=70, h=4,txt="{}".format(data["address"][0]))

        self.set_y(self.get_y())
        self.set_x(107)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="Contact : ")

        wi = self.get_string_width("Contact : ")

        self.set_y(self.get_y())
        self.set_x(107+wi)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="{}".format(data["custConVar"][0]))
        
        
        self.set_y(self.get_y()+4)
        self.set_x(107)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="GST Registration No : ")
        
        wi = self.get_string_width("GST Registration No : ")
        
        self.set_y(self.get_y())
        self.set_x(107+wi)
        self.set_font('helvetica', 'I', 8)
        self.cell(w=0,txt="{}".format(data["custGstNumb"][0]))
    
        self.set_y(self.get_y()+4)
        self.set_x(107)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="PAN No : ")
        
        wi = self.get_string_width("PAN No : ")
        
        self.set_y(self.get_y())
        self.set_x(107+wi)
        self.set_font('helvetica', 'I', 8)
        self.cell(w=0,txt="{}".format(data["custPanNumb"][0]))
        
        self.set_y(67)
        self.set_x(17)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Invoice No.")
        
        self.set_y(73)
        self.set_x(17)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="{}".format(data["invoiceNumber"][0]))
        
        self.set_y(67)
        self.set_x(77)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Quotation No.")
        
        self.set_y(73)
        self.set_x(77)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="{}".format(data["quotaionNumber"][0]))
        
        self.set_y(67)
        self.set_x(137)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Date")
        
        self.set_y(73)
        self.set_x(137)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="{}/{}/{}".format(today.day,today.month,today.year))
    
        self.set_y(82)
        self.set_x(17)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Mode/Terms of Payment")
        
        self.set_y(88)
        self.set_x(17)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="{}".format(data["modeTerms"][0]))
        
        self.set_y(82)
        self.set_x(77)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Terms of Delivery")
        
        self.set_y(88)
        self.set_x(77)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="{}".format(data["termsOfDel"][0]))
        
        self.set_y(82)
        self.set_x(137)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Destination")
    
        self.set_y(88)
        self.set_x(137)
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="{}".format(data["destination"][0]))
    
        self.drawLines()
    
    def infosectionTitle(self):
        self.set_y(97.5)
        self.set_x(15.5)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Sr.")        
        
        self.set_y(101.5)
        self.set_x(15.5)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="No.")
        
        self.set_y(99)
        self.set_x(23)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=65,txt="Description of Goods", align='C')

        self.set_y(99)
        self.set_x(88)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=20, txt="HSN/SAC", align='C')

        self.set_y(99)
        self.set_x(110)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=23, txt="Rate/Sq Ft.", align='C')
        
        self.set_y(99)
        self.set_x(133)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=24, txt="Amount", align='C')

        self.set_y(99)
        self.set_x(158)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=10, txt="Qty.", align='C')
    
        self.set_y(99)
        self.set_x(167.5)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=30, txt="Total Amount", align='C')
    
    def infosection(self):
        
        global printCount, taxLevel
        
        printLevel = 108
        self.infosectionTitle()
        nop = ceil(data.shape[0]/15)
        flag = False
        
        for i in range(data.shape[0]):
            if(printLevel<=200):
                printCount+=1
                self.printInfo(i, printLevel)
                printLevel = printLevel + 7
            else:
                flag = True
        
        if(printLevel<=210 and printLevel>=206 and flag==True):
            self.line(15, printLevel, 195, printLevel)
            
        for j in range(nop-1):
            self.set_y(printLevel + 5)
            self.set_x(168)
            self.set_font('helvetica', 'B', 10)
            self.cell(w=22,txt="Continued...", align='L')
            self.drawLinesInfo(printLevel)
            self.add_page()
            self.homePage()
            self.infosectionTitle()        
            printLevel = 108
            for i in range(printCount,data.shape[0]):
                if(printLevel<=190):
                    printCount+=1
                    self.printInfo(i, printLevel)
                    printLevel = printLevel + 7
            if(j!=nop-2):
                self.line(15, printLevel, 195, printLevel)
        
        
        self.set_y(printLevel-4)
        self.set_x(168)
        self.set_font('helvetica', '', 8)
        self.cell(w=22.5,txt="_______________", align='L')
        
        amt = data["totQuanSum"][0]
        self.set_y(printLevel+1)
        self.set_x(168)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=22.5,txt="Rs. {}".format(amt[1:]), align='L')
        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        bill = float(amt[1:].replace(",",""))
        
        lastRow = data.shape[0] - 1
        
        
        
        printLevel = printLevel + 10
        
        if(data["discountFlag"][0]=="True Flag"):
            disc = float(data["discountEntVar"][lastRow])
            bill = bill - disc
            discA = indCurr(round(disc,2))
            
            self.set_y(printLevel)
            self.set_x(60)
            self.set_font('helvetica', 'B', 8)
            self.cell(w=22.5,txt="Discount", align='R')
            
            self.set_y(printLevel)
            self.set_x(168)
            self.set_font('helvetica', 'B', 8)
            self.cell(w=22.5,txt="(-) Rs. {}".format(discA[1:]), align='L')
        
            printLevel = printLevel + 5
        
        cgst = indCurr(bill*9/100)
        
        self.set_y(printLevel)
        self.set_x(60)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=22.5,txt="CGST @9%", align='R')
        
        self.set_y(printLevel)
        self.set_x(168)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=22.5,txt="Rs. {}".format(cgst[1:]), align='L')
    
        printLevel = printLevel + 5
    
        self.set_y(printLevel)
        self.set_x(60)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=22.5,txt="SGST @9%", align='R')
        
        self.set_y(printLevel)
        self.set_x(168)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=22.5,txt="Rs. {}".format(cgst[1:]), align='L')
        
        bill = bill + (bill*18/100)
        
        if(data["installationFlag"][0]=="True Flag"):
            inst = float(data["instEntVar"][lastRow])
            instAm = indCurr(round(inst,2))
            
            printLevel = printLevel + 5
            
            self.set_y(printLevel)
            self.set_x(59)
            self.set_font('helvetica', 'B', 8)
            self.cell(w=22.5,txt="Installation Charges", align='R')
            
            self.set_y(printLevel)
            self.set_x(168)
            self.set_font('helvetica', 'B', 8)
            self.cell(w=22.5,txt="Rs. {}".format(instAm[1:]), align='L')
            
            bill = bill + inst
        printLevel = printLevel + 7
        
       
        
        rou = bill - floor(bill)
        rou = round(rou,2)
        
        if(rou!=0):
        
            self.set_y(printLevel)
            self.set_x(60)
            self.set_font('helvetica', 'B', 8)
            self.cell(w=22,txt="Round Off", align='R')
            
            self.set_y(printLevel)
            self.set_x(168)
            self.set_font('helvetica', 'B', 8)
            self.cell(w=22,txt="(-) Rs. {}".format(rou), align='L')
             
            printLevel = printLevel + 8
        
        bill = bill - rou
        bill = round(bill)
        curr = indCurr(bill)
        
        self.set_y(printLevel)
        self.set_x(60)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=22,txt="Total", align='R')
        
        self.set_y(printLevel)
        self.set_x(168)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=22,txt="Rs. {}".format(curr[1:]), align='L')
        
        printLevel = printLevel + 5
        
        billWords = num2words(bill, lang ='en_IN').title()
        
        self.set_y(printLevel + 3)
        self.set_x(16)
        self.set_font('helvetica', '', 10)
        self.cell(w=22,txt="Amount Chargeable (in words)", align='L')
        
        self.set_y(printLevel + 10)
        self.set_x(16)
        self.set_font('helvetica', 'B', 10)
        self.multi_cell(w=160, h=5,txt="Indian Rupees {} Only".format(billWords), align='L')
        
        self.set_y(printLevel + 3)
        self.set_x(168)
        self.set_font('helvetica', '', 10)
        self.cell(w=22,txt="E. & O.E", align='L')
        
        self.drawLinesInfo(printLevel)
        self.line(15, printLevel, 195, printLevel)
        self.line(15, printLevel + 23, 195, printLevel + 23)
          
    def taxableAmountTitle(self):
        
        taxLevel = 97
        self.set_y(taxLevel+2)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=25,txt="HSN/SAC", align='C')

        self.set_y(taxLevel+2)
        self.set_x(40)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=30,txt="Taxable Value", align='C')

        self.set_y(taxLevel+1)
        self.set_x(70)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=50,txt="Central Tax", align='C')

        self.set_y(taxLevel+8)
        self.set_x(70)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=20,txt="Rate", align='C')
        
        self.set_y(taxLevel+8)
        self.set_x(90)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=30,txt="Amount", align='C')

        self.set_y(taxLevel+1)
        self.set_x(120)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=50,txt="State Tax", align='C')
    
        self.set_y(taxLevel+8)
        self.set_x(120)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=20,txt="Rate", align='C')
        
        self.set_y(taxLevel+8)
        self.set_x(140)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=30,txt="Amount", align='C')
    
        self.set_y(taxLevel)
        self.set_x(170)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=25,txt="Total Tax", align='C')
        
        self.set_y(taxLevel+5)
        self.set_x(170)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=25,txt="Amount", align='C')
    
    def taxableAmount(self):
        
        global taxLevel, taxPrintCount, endPrintLevel, amtsum
        
        taxLevel = 97
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        startTaxLevel = taxLevel - 2
        taxLevel = taxLevel + 15
        taxSum = 0
        nop = ceil(data.shape[0]/18)
        
        self.taxableAmountTitle() 
        
        for i in range(data.shape[0]):
            if(taxLevel<=230):
                taxPrintCount+=1
                taxSum = self.printTaxInfo(taxLevel, i, taxSum)
                taxLevel = taxLevel + 7
                
        
        if(taxLevel<=240 and taxLevel>220):
            self.line(15, taxLevel, 195, taxLevel)
            self.drawLinesTax(startTaxLevel, taxLevel-7)
        
        for j in range(nop-1):
            
            self.set_y(taxLevel + 5)
            self.set_x(168)
            self.set_font('helvetica', 'B', 10)
            self.cell(w=22,txt="Continued...", align='L')
            
            self.add_page()
            self.homePage()
            self.taxableAmountTitle()        
            taxLevel = 108
            for i in range(taxPrintCount,data.shape[0]):
                if(taxLevel<=230):
                    taxPrintCount+=1
                    taxSum = self.printTaxInfo(taxLevel+4, i, taxSum)
                    taxLevel = taxLevel + 7
            if(j!=nop-2):
                self.line(15, taxLevel+3, 195, taxLevel+3)
            self.drawLinesTax(startTaxLevel, taxLevel-4)
        
        taxLevel = taxLevel + 4
        
        amtsu = indCurr(round(amtsum,2))
        
        self.set_y(taxLevel + 2)
        self.set_x(15)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=25,txt="Total  ", align='R')
        
        self.set_y(taxLevel + 2)
        self.set_x(40)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=30  ,txt="Rs. {}".format(amtsu[1:]), align='C')
        
        ta = indCurr(taxSum)
        
        self.set_y(taxLevel + 2)
        self.set_x(90)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=30  ,txt="Rs. {}".format(ta[1:]), align='C')
        
        self.set_y(taxLevel + 2)
        self.set_x(140)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=30  ,txt="Rs. {}".format(ta[1:]), align='C')
        
        finTax = taxSum*2
        finTax=round(finTax,2)
        finTa = indCurr(finTax)
        
        self.set_y(taxLevel + 2)
        self.set_x(170)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=25  ,txt="Rs. {}".format(finTa[1:]), align='C')
        
        billWords = num2words(finTax, lang ='en_IN').title()
        
        self.set_y(taxLevel + 9)
        self.set_x(16)
        self.set_font('helvetica', '', 10)
        self.cell(w=22,txt="Tax Amount (in words)", align='L')
        
        self.set_y(taxLevel + 16)
        self.set_x(16)
        self.set_font('helvetica', 'B', 10)
        self.multi_cell(w=160, h=5,txt="Indian Rupees {} Only".format(billWords), align='L')
        
        self.drawLinesTax(startTaxLevel, taxLevel)
        self.line(15, taxLevel+7, 195, taxLevel+7)
        self.line(15, taxLevel, 195, taxLevel)
        self.line(15, taxLevel + 28, 195, taxLevel + 28)
        
        endPrintLevel = taxLevel
        
    def endPrint(self):
        global endPrintLevel
        
        name = "Madhav Glass & Aluminium"
        bank = "Punjab National Bank"
        account = "0650050015525"
        ifsc = "PUNB0065020"
        
        if(endPrintLevel>200):
            self.add_page()
            self.homePage()
            endPrintLevel = 100
        else:
            endPrintLevel = 225

        self.dashed_line(15, endPrintLevel, 195, endPrintLevel)
        self.line(15, endPrintLevel+28, 195, endPrintLevel+28)
        self.line(15, endPrintLevel+55, 195, endPrintLevel+55)
        self.line(105, endPrintLevel+28, 105, endPrintLevel+55)

        endPrintLevel = endPrintLevel + 2

        self.set_y(endPrintLevel)
        self.set_x(16)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=22,txt="Bank Details", align='L')

        endPrintLevel = endPrintLevel + 7

        self.set_y(endPrintLevel)
        self.set_x(16)
        self.set_font('helvetica', '', 10)
        self.cell(w=22,txt="Recipient Name : ", align='L')

        wi = self.get_string_width("Recipient Name : ")

        self.set_y(endPrintLevel)
        self.set_x(16 + wi)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=22,txt="{}".format(name), align='L')
        
        endPrintLevel = endPrintLevel + 5
        
        self.set_y(endPrintLevel)
        self.set_x(16)
        self.set_font('helvetica', '', 10)
        self.cell(w=22,txt="BANK NAME : ", align='L')
        
        wi = self.get_string_width("BANK NAME : ")
        
        self.set_y(endPrintLevel)
        self.set_x(16+wi)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=22,txt="{}".format(bank), align='L')
        
        endPrintLevel = endPrintLevel + 5
        
        self.set_y(endPrintLevel)
        self.set_x(16)
        self.set_font('helvetica', '', 10)
        self.cell(w=22,txt="Account No : ", align='L')
        
        wi = self.get_string_width("Account No : ")
        
        self.set_y(endPrintLevel)
        self.set_x(16+wi)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=22,txt="{}".format(account), align='L')
        
        endPrintLevel = endPrintLevel + 5
        
        self.set_y(endPrintLevel)
        self.set_x(16)
        self.set_font('helvetica', '', 10)
        self.cell(w=22,txt="IFSC CODE : ", align='L')
        
        wi = self.get_string_width("IFSC CODE : ")
        
        self.set_y(endPrintLevel)
        self.set_x(16+wi)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=22,txt="{}".format(ifsc), align='L')

        endPrintLevel = endPrintLevel + 5
        
        self.set_y(endPrintLevel+22)
        self.set_x(16)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=22,txt="Madhav Glass & Aluminium (Seal and Signature)", align='L')

        self.set_y(endPrintLevel+22)
        self.set_x(106)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=90,txt="Customers Signature  ", align='R')

        # print(endPrintLevel)
        
    def invoiceDriverCode(self):
        # pdfInv = PDFInvoice('P', 'mm', 'A4')
        self.alias_nb_pages()
        self.set_left_margin(15)
        self.set_right_margin(15)
        self.set_auto_page_break(auto = True, margin = 15)
        self.add_page()
        self.set_y(15)

        self.homePage()
        # self.drawLines()
        self.infosection()
        self.add_page()
        self.homePage()
        self.taxableAmount()
        self.endPrint()
        
        self.output(self.fileName)
        self.printDoneFlag = True

#***********************-----------------------------**************************----------------------------**********************------------------

class Invoice:
    
    new = None
    maintab = None
    frame2 = None
    finAmt = None
    data = None
    invNumbVar = tk.StringVar()
    quotNumbVar = tk.StringVar()
    modeTermVar = tk.StringVar()
    termOfDelVar = tk.StringVar()
    destinVar = tk.StringVar()
    custGstVar = tk.StringVar()
    custPanVar = tk.StringVar()
    
    def createNewRow(self):
        row = tk.LabelFrame(self.maintab, borderwidth=2)
        return row
    
    def generateInvoicePDF(self):
        global data
        
        invData = pd.read_excel('./data/WindowDatabaseQuoAndInvoice.xlsx')
        invData = invData.replace(float('nan'),"")
        
        invData.loc[len(invData.index)] = ['']*5
        lastRow = invData.shape[0] - 1
        
        data["invoiceNumber"] = self.invNumbVar.get()
        data["quotaionNumber"] = self.quotNumbVar.get()
        data["modeTerms"] = self.modeTermVar.get()
        data["termsOfDel"] = self.termOfDelVar.get()
        data["destination"] = self.destinVar.get()
        data["custGstNumb"] = self.custGstVar.get()
        data["custPanNumb"] = self.custPanVar.get()
        
        for i in range(data.shape[0]):
            data["hsnSacVar"][i] = self.finAmt[i].get()
    
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["dateAndTime"] = current_time
    
        invData["dateAndTime"][lastRow] = current_time
        invData["custNamVar"][lastRow] = data["custNamVar"][0]
        invData["custConVar"][lastRow] = data["custConVar"][0]
        invData["quotaionNumber"][lastRow] = data["quotaionNumber"][0]
        invData["invoiceNumber"][lastRow] = data["invoiceNumber"][0]
    
        data.to_excel('./Data/{}_QuatationData.xlsx'.format(custNamVar.get()), index=False)
        invData.to_excel('./Data/WindowDatabaseQuoAndInvoice.xlsx', index=False)
        
        self.new.attributes('-topmost',False)
        
        prog = tk.Toplevel()
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width-(screen_width/2.8))/2
        y = ((screen_height/1.5))/2 + 100
        prog.geometry('+%d+%d'%(x,y))
        prog.title('Wait')
        
        labour = ttk.Label(prog, text="PDF is generating might take a minute or two. This window would close automatically once done.", font=("",10,"bold") )
        labour.grid(column=0, row=3, padx=20, pady=20, sticky='W')
        
        files = [('PDF Files', '*.pdf'), ('All Files', '*.*')]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        setCustomerName(custNamVar.get())
        pdfInv = PDFInvoice('P', 'mm', 'A4')
        
        pdfInv.fileName = file.name
        prog.attributes('-topmost',True)
        pdfInv.invoiceDriverCode()
        print("Finished")
        
        if(pdfInv.printDoneFlag==True):
            prog.destroy()
            self.new.attributes('-topmost',True)
    
    def invWindow(self):
        global data
        new = tk.Toplevel()
        new.attributes('-topmost',True)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width-(screen_width/2.8))/2 - 40
        y = ((screen_height/1.5))/2 - 240
        new.geometry('+%d+%d'%(x,y))
        new.title('Invoice')
        self.new = new
        
        custDetails = ttk.Label(self.new, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        
        frame2 = tk.LabelFrame(self.new, borderwidth=2, width=1000, labelwidget=custDetails )
        frame2.grid(column=0, row=0, columnspan=3, padx=5, pady=5, sticky='W')
        self.frame2 = frame2
        
        custNamVar.set(data.iloc[0]["custNamVar"])
        custConVar.set(data.iloc[0]["custConVar"])
        address = data.iloc[0]["address"]
    
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=0, row=2, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=0, row=3, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer GST No.")
        custConLab.grid(column=0, row=4, padx=10, pady=10, sticky='W')
        custConLab = ttk.Label(self.frame2, text="Customer PAN No.")
        custConLab.grid(column=0, row=5, padx=10, pady=10, sticky='W')

        custNamEnt = tk.Entry(self.frame2, textvariable=custNamVar, font=("",9,""), relief="solid", width = 43, state='disabled')
        custNamEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        custAddEnt = tk.Text(self.frame2, font=("",9,""), relief="solid", height=3, width = 43, background="#f0f0f0", foreground="#6d6d6d")
        custAddEnt.grid(column=1,row=2, padx=10, pady=10, sticky='W')
        custAddEnt.insert(1.0, address)
        custAddEnt.config(state=tk.DISABLED)
        custConEnt = tk.Entry(self.frame2, textvariable=custConVar, font=("",9,""), relief="solid", width = 43, state='disabled')
        custConEnt.grid(column=1,row=3, padx=10, pady=10, sticky='W')
        custConEnt = tk.Entry(self.frame2, textvariable=self.custGstVar, font=("",9,""), relief="solid", width = 43)
        custConEnt.grid(column=1,row=4, padx=10, pady=10, sticky='W')
        custConEnt = tk.Entry(self.frame2, textvariable=self.custPanVar, font=("",9,""), relief="solid", width = 43)
        custConEnt.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        
        frame_canvas = tk.Frame(self.new, borderwidth=2)
        frame_canvas.grid(row=2, column=0, columnspan=3, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        frame_canvas.grid_propagate(False)
 
        canvas = tk.Canvas(frame_canvas)
        canvas.grid(row=0, column=0, sticky="news")
 
        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        frame_buttons = tk.LabelFrame(canvas, borderwidth=2,  padx=5)
        canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
        
        cartDetails = ttk.Label(frame_buttons, text="Cart Details", font=("",10,"bold"))
        cartDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
                
        head1 = tk.Label(frame_buttons, text="Sr.No", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head1.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        head2 = tk.Label(frame_buttons, text="Description of Goods", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head2.grid(column=1, row=1, padx=10, pady=10, sticky='W')
        head3 = tk.Label(frame_buttons, text="HSN/SAC", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head3.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        head4 = tk.Label(frame_buttons, text="Rate", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head4.grid(column=3, row=1, padx=10, pady=10, sticky='W')
        head5 = tk.Label(frame_buttons, text="Quantity", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head5.grid(column=4, row=1, padx=10, pady=10, sticky='W')
        head6 = tk.Label(frame_buttons, text="Amount", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head6.grid(column=5, row=1, padx=10, pady=10, sticky='W')
        
            
        row = self.createNewRow()
        row.grid(column=0, row=1, padx=5, pady=5, sticky='W')
        
        i = 0
        
        finA = [1]*data.shape[0]
        self.finAmt = []
        for i in range(data.shape[0]):
            tmp = tk.StringVar()
            self.finAmt.append(tmp)
        
        for i in range(data.shape[0]):
            try:
                finA[i] = data["hsnSacVar"][i]
                self.finAmt[i].set(finA[i])
            except:
                print("Error in Deletion")
        
        for i in range(data[data.columns[0]].count()):
            x=i
            
            head1 = tk.Label(frame_buttons, text=i+1, padx=10)
            head1.grid(column=0, row=i+2, padx=10, pady=10, sticky='W')
            
            desc = data["windowTypeVar"][x] + " (" + data["Width"][x] + " x " + data["Height"][x] + ")"
            head2 = tk.Label(frame_buttons, text=desc, padx=10)
            head2.grid(column=1, row=i+2, padx=10, pady=10, sticky='W')
            
            head3 = tk.Entry(frame_buttons, text=data["hsnSacVar"][x], textvariable=self.finAmt[i], relief="solid",  width = 13)
            head3.grid(column=2, row=i+2, padx=10, pady=10, sticky='W')
            
            rate = data["cstAmtInr"][x]
            head4 = tk.Label(frame_buttons, text=rate, padx=10)
            head4.grid(column=3, row=i+2, padx=10, pady=10, sticky='W')
            
            head5 = tk.Label(frame_buttons, text=data["quantity"][x], padx=10)
            head5.grid(column=4, row=i+2, padx=10, pady=10, sticky='W')
            
            head6 = tk.Label(frame_buttons, text=data["quantAmnt"][x], padx=10)
            head6.grid(column=5, row=i+2, padx=10, pady=10, sticky='W')

        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        finCost = indCurr(finalCost)
        costTotVar.set(finCost)
        
        line = ttk.Label(frame_buttons, text="________________________________________________________________________________________________________________________________________________")
        line.grid(column=0, row=i+3, columnspan=7, padx=10, pady=10, sticky='N')
        
        cost = ttk.Label(frame_buttons, text="Total Cost")
        cost.grid(column=0, row=i+5, padx=10, pady=10, sticky='W')
        
        finAmt = tk.StringVar()
        finAmt.set(indCurr(data.iloc[i]["finalCost"]))
        
        costTot = tk.Entry(frame_buttons, textvariable=finAmt, relief="solid", width = 14, state='disabled')
        costTot.grid(column=3,row=i+5, padx=10, pady=10, sticky='W')
        
        qtyAmt = tk.StringVar()
        qtyAmt.set(data.iloc[i]["totQuanSum"])
    
        qtyCostTot = tk.Entry(frame_buttons, textvariable=qtyAmt, relief="solid", width = 14, state='disabled')
        qtyCostTot.grid(column=5,row=i+5, padx=10, pady=10, sticky='W')
 
        frame_buttons.update_idletasks()
        frame_canvas.config(width=810, height=400)
 
        canvas.config(scrollregion=canvas.bbox("all"))       
        invDetails = ttk.Label(self.new, text="Invoice Details", font=("",10,"bold"))
        invDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        
        frame3 = tk.LabelFrame(self.new, borderwidth=2, labelwidget=invDetails)
        frame3.grid(column=0, row=3, columnspan=10, padx=5, pady=5, sticky='W')
        
        invNumb = tk.Label(frame3, text="Invoice Number")
        invNumb.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        
        #invoiceNumber = data["custNamVar"][0][:3] + "/" + str(today.day) + str(today.month) + "-" + str(today.year) + "/" + str(randint(100, 999))
        #data["invoiceNumber"] = invoiceNumber
        #self.invNumbVar.set(invoiceNumber)
        invNumbEnt = tk.Entry(frame3, textvariable=self.invNumbVar, font=("",9,""), relief="solid", width = 20)
        invNumbEnt.grid(column=1,row=0, padx=10, pady=10, sticky='W')
        
        quoNumb = tk.Label(frame3, text="Enter Quotation Number")
        quoNumb.grid(column=2, row=0, padx=10, pady=10, sticky='W')

        quoNumbEnt = tk.Entry(frame3, textvariable=self.quotNumbVar, font=("",9,""), relief="solid", width = 20)
        quoNumbEnt.grid(column=3,row=0, padx=10, pady=10, sticky='W')
        
        modeTerm = tk.Label(frame3, text="Enter Mode/Terms of Payment")
        modeTerm.grid(column=0, row=1, padx=10, pady=10, sticky='W')

        modeTermEnt = tk.Entry(frame3, textvariable=self.modeTermVar, font=("",9,""), relief="solid", width = 20)
        modeTermEnt.grid(column=1,row=1, padx=10, pady=10, sticky='W')
        
        termOfDel = tk.Label(frame3, text="Enter Terms of Delivery")
        termOfDel.grid(column=2, row=1, padx=10, pady=10, sticky='W')

        termOfDelEnt = tk.Entry(frame3, textvariable=self.termOfDelVar, font=("",9,""), relief="solid", width = 20)
        termOfDelEnt.grid(column=3,row=1, padx=10, pady=10, sticky='W')

        destin = tk.Label(frame3, text="Enter Destination")
        destin.grid(column=0, row=2, padx=10, pady=10, sticky='W')

        destinEnt = tk.Entry(frame3, textvariable=self.destinVar, font=("",9,""), relief="solid", width = 20)
        destinEnt.grid(column=1,row=2, padx=10, pady=10, sticky='W')

        invoice=tk.Button(new, text = 'Generate Invoice PDF', width=20, command = self.generateInvoicePDF)
        invoice.grid(column=0,row=4, padx=10, pady=15, sticky='E')
        
####################################################################################################################################################

class CalculatePage:

    new = None
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

    def generatePDF(self):
        global data, pressedCalcFlag, quotationNumber
        
        quotationNumber = "QUO" + "/" + str(today.day) + str(today.month) + "-" + str(today.year) + "/" + str(randint(100, 999))
        
        data["dateAndTime"] = datetime.now()
        
        if(pressedCalcFlag != True):
            messagebox.showerror("Invalid","Please press calculate button", parent=self.new)
            pressedCalcFlag == False
            return False
        
        self.new.attributes('-topmost',False)
        
        data["quotaionNumber"] = quotationNumber
        
        prog = tk.Toplevel()
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width-(screen_width/2.8))/2
        y = ((screen_height/1.5))/2 + 100
        prog.geometry('+%d+%d'%(x,y))
        prog.title('Wait')
        
        labour = ttk.Label(prog, text="PDF is generating might take a minute or two. This window would close automatically once done.", font=("",10,"bold") )
        labour.grid(column=0, row=3, padx=20, pady=20, sticky='W')
        files = [('PDF Files', '*.pdf'), ('All Files', '*.*')]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        setCustomerName(custNamVar.get())
        pobj = PDF('P', 'mm', 'A4')
        pobj.fileName = file.name
        prog.attributes('-topmost',True)
        pobj.driverCode()
         
        print("Finished")
        
        if(pobj.printDoneFlag==True):
            prog.destroy()
            self.new.attributes('-topmost',True)

    def calculateCost(self):
        global profitAmnt, pressedCalcFlag
        
        data["dateAndTime"] = datetime.now()
        
        pressedCalcFlag = True
        
        if(gstEntVar.get()==""):
            messagebox.showerror("Invalid","Please fill GST percentage", parent=self.new)
            return False
        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')

        totalcost = costTotVar.get()
        totalcost = float(totalcost[1:].replace(",",""))
        
        print(totalcost)
        discountedCost = 0.0
        installationCost = 0.0
        gstCost = 0.0
        
        if(discountEntVar.get() != "" and instEntVar.get() != ""):
            data["discountFlag"][0] = "True Flag"
            data["installationFlag"][0] = "True Flag"
            
            discountedCost = totalcost - float(discountEntVar.get())
            gstCost = discountedCost + (discountedCost*18/100)
            installationCost = gstCost + float(instEntVar.get())
            
            discTotVar.set(indCurr(discountedCost))
            instTotVar.set(indCurr(installationCost))
            gstTotVar.set(indCurr(gstCost))
            
        else:
            data["discountFlag"][0] = "False Flag"
            data["installationFlag"][0] = "False Flag"
            
            gstCost = totalcost + (totalcost*18/100)
            gstTotVar.set(indCurr(gstCost))
        
            if(discountEntVar.get() != ""):
                data["discountFlag"][0] = "True Flag"
                discountedCost = totalcost - float(discountEntVar.get())
                gstCost = discountedCost + (discountedCost*18/100)
                discTotVar.set(indCurr(discountedCost))
                gstTotVar.set(indCurr(gstCost))
            else:
                discTotVar.set("")
                data["discountFlag"][0] = "False Flag"
                
            if(instEntVar.get() != ""):
                data["installationFlag"][0] = "True Flag"
                gstCost = totalcost + (totalcost*18/100)
                installationCost = gstCost + float(instEntVar.get())
                instTotVar.set(indCurr(installationCost))
                gstTotVar.set(indCurr(gstCost))
            else:
                instTotVar.set("")
                data["installationFlag"][0] = "False Flag"
            
        print(totalcost, discountedCost, installationCost)
        afterCalculate()
    
    def callInvoice(self):
        global pressedCalcFlag
        
        if(pressedCalcFlag != True):
            messagebox.showerror("Invalid","Please press calculate button", parent=self.new)
            pressedCalcFlag == False
            return False
        
        self.new.destroy()
        obj = Invoice()
        obj.invWindow()
    
    def costPage(self):
        
        new = tk.Toplevel()
        new.attributes('-topmost',True)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width-(screen_width/2.8))/2 + 30
        y = ((screen_height/1.5))/2
        new.geometry('+%d+%d'%(x,y))
        new.title('Calculation')
        self.new = new
        
        totSqftEntVar.set(totSQFt)
        
        entLab = ttk.Label(new, text="Enter Values")
        entLab.grid(column=1, row=0, padx=10, pady=10, sticky='W')
        totLab = ttk.Label(new, text="Total")
        totLab.grid(column=3, row=0, padx=10, pady=10, sticky='W')
        
        discount = ttk.Label(new, text="Enter Discount Amount")
        discount.grid(column=0, row=4, padx=10, pady=10, sticky='W')
        install = ttk.Label(new, text="Enter Installation Charges")
        install.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        gst = ttk.Label(new, text="GST (In Percentage)")
        gst.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        
        gstEntVar.set(18)
        
        self.discountEnt = tk.Entry(new, textvariable=discountEntVar, relief="solid", width = 16)
        self.discountEnt.grid(column=1,row=4, padx=10, pady=10, sticky='W')
        self.instEnt = tk.Entry(new, textvariable=instEntVar, relief="solid", width = 16)
        self.instEnt.grid(column=1,row=6, padx=10, pady=10, sticky='W')
        self.gstEnt = tk.Entry(new, textvariable=gstEntVar, relief="solid", width = 16)
        self.gstEnt.grid(column=1,row=5, padx=10, pady=10, sticky='W')
        
        cost = ttk.Label(new, text="Total Cost")
        cost.grid(column=0, row=2, padx=10, pady=10, sticky='W')

        discount = ttk.Label(new, text="Cost After Discount")
        discount.grid(column=2, row=4, padx=10, pady=10, sticky='W')
        install = ttk.Label(new, text="Cost with Installation Charges")
        install.grid(column=2, row=6, padx=10, pady=10, sticky='W')
        gst = ttk.Label(new, text="Final bill amout with GST")
        gst.grid(column=2, row=5, padx=10, pady=10, sticky='W')
    
        costTotVar.set(data["totQuanSum"][0])

        self.costTot = tk.Entry(new, textvariable=costTotVar, relief="solid", width = 16, state='disabled')
        self.costTot.grid(column=3,row=2, padx=10, pady=10, sticky='W')
        
        self.discTot = tk.Entry(new, textvariable=discTotVar, relief="solid", width = 16, state='disabled')
        self.discTot.grid(column=3,row=4, padx=10, pady=10, sticky='W')
        self.instTot = tk.Entry(new, textvariable=instTotVar, relief="solid", width = 16, state='disabled')
        self.instTot.grid(column=3,row=6, padx=10, pady=10, sticky='W')
        self.gstTot = tk.Entry(new, textvariable=gstTotVar, relief="solid", width = 16, state='disabled')
        self.gstTot.grid(column=3,row=5, padx=10, pady=10, sticky='W')

        calculate=tk.Button(new, text = 'Calculate', width=20, command = self.calculateCost)
        calculate.grid(column=0,row=7, columnspan=2, padx=10, pady=15, sticky='W')
        
        genPdf=tk.Button(new, text = 'Generate PDF', width=20, command = self.generatePDF)
        genPdf.grid(column=1,row=7, columnspan=2, padx=10, pady=15, sticky='N')
    
        invoice=tk.Button(new, text = 'Invoice Page', width=20, command = self.callInvoice)
        invoice.grid(column=2,row=7, columnspan=2, padx=10, pady=15, sticky='E')
    
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
        data = data.reset_index()
        data = data.drop('index', 1)
        self.addMorePage()
    
    def nextItem(self):
        
        if(calcQuantFlag==False):
            messagebox.showerror("Invalid","Please calculate quantity values by clicking on Calculate(Quantity) Button", parent=self.new)
            return False
        
        data.to_excel('./Data/{}_QuatationData.xlsx'.format(custNamVar.get()), index=False)
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
        
        self.new.grab_release()
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
    
    
    def calcQuant(self):
        
        global calcQuantFlag
        
        qTemp = []
        for i in range(data[data.columns[0]].count()):
            qTemp.append(int(float(self.qt[i].get())))
        
        data["quantity"] = qTemp
        for i in range(data[data.columns[0]].count()):
            if(data["quantity"][i]==""):
                messagebox.showerror("Invalid","Please fill quantities of every item.", parent=self.new)
                return False
        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        tList = []
        
        suum = 0
        area = 0
        totArea = 0
        for i in range(data[data.columns[0]].count()):
            amt = float(data.iloc[i]["cstAmtInr"][1:].replace(",",""))
            temp = qTemp[i] * amt
            wi = float(data["Width"][i].replace("ft",""))
            he = float(data["Height"][i].replace("ft",""))
            area = wi*he
            data["totSqftEntVar"][i] = area
            totArea = area * qTemp[i]
            suum = suum + temp
            tList.append(indCurr(temp))
            data["totSqftEntQuantVar"][i] = totArea
            
        
        data["totQuanSum"] = indCurr(suum)
        data["quantAmnt"] = tList
        self.new.destroy()
        self.addMorePage()
        
        calcQuantFlag=True
    
    def addMorePage(self):
        global srno
        
        new = tk.Toplevel()
        new.attributes('-topmost',True)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width-(screen_width/2.5))/2 - 30
        y = (screen_height-(screen_height/2.5))/2 - 150
        new.geometry('+%d+%d'%(x,y))
        new.title('Cart')
        self.new = new
        
        custDetails = ttk.Label(self.new, text="Customer Details", font=("",10,"bold"))
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        
        frame2 = tk.LabelFrame(self.new, borderwidth=2, width=1000, labelwidget=custDetails )
        frame2.grid(column=0, row=0, columnspan=3, padx=5, pady=5, sticky='W')
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
        
        frame_canvas = tk.Frame(self.new, borderwidth=2)
        frame_canvas.grid(row=2, column=0, columnspan=3, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        frame_canvas.grid_propagate(False)
 
        canvas = tk.Canvas(frame_canvas)
        canvas.grid(row=0, column=0, sticky="news")
 
        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        frame_buttons = tk.LabelFrame(canvas, borderwidth=2,  padx=5)
        canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
        
        cartDetails = ttk.Label(frame_buttons, text="Cart Details", font=("",10,"bold"))
        cartDetails.grid(column=0, row=0, padx=10, pady=10, sticky='W')
                
        head1 = tk.Label(frame_buttons, text="Sr.No", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head1.grid(column=0, row=1, padx=10, pady=10, sticky='W')
        head2 = tk.Label(frame_buttons, text="Window Type", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head2.grid(column=1, row=1, padx=10, pady=10, sticky='W')
        head3 = tk.Label(frame_buttons, text="Width", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head3.grid(column=2, row=1, padx=10, pady=10, sticky='W')
        head4 = tk.Label(frame_buttons, text="Height", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head4.grid(column=3, row=1, padx=10, pady=10, sticky='W')
        head5 = tk.Label(frame_buttons, text="Cost", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head5.grid(column=4, row=1, padx=10, pady=10, sticky='W')
        head6 = tk.Label(frame_buttons, text="Quantity", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head6.grid(column=5, row=1, padx=10, pady=10, sticky='W')
        head7 = tk.Label(frame_buttons, text="Amount", font=("",10,"bold"), background="#f0f0f0", relief = tk.GROOVE, padx=10, pady=5)
        head7.grid(column=6, row=1, padx=10, pady=10, sticky='W')
            
        row = self.createNewRow()
        row.grid(column=0, row=1, padx=5, pady=5, sticky='W')
        
        i = 0
        
        qty = [1]*srno
        self.qt = []
        for i in range(data.shape[0]):
            tmp = tk.StringVar()
            self.qt.append(tmp)
        
        for i in range(data.shape[0]):
            try:
                qty[i] = data["quantity"][i]
                self.qt[i].set(qty[i])
            except:
                print("Error in Deletion")
        
        for i in range(data[data.columns[0]].count()):
            head1 = tk.Label(frame_buttons, text=i+1, padx=10)
            head1.grid(column=0, row=i+2, padx=10, pady=10, sticky='W')
            head2 = tk.Label(frame_buttons, text=data.iloc[i]["windowTypeVar"], padx=10)
            head2.grid(column=1, row=i+2, padx=10, pady=10, sticky='W')
            head3 = tk.Label(frame_buttons, text=data.iloc[i]["Width"], padx=10)
            head3.grid(column=2, row=i+2, padx=10, pady=10, sticky='W')
            head4 = tk.Label(frame_buttons, text=data.iloc[i]["Height"], padx=10)
            head4.grid(column=3, row=i+2, padx=10, pady=10, sticky='W')
            head5 = tk.Label(frame_buttons, text=data.iloc[i]["cstAmtInr"], padx=10)
            head5.grid(column=4, row=i+2, padx=10, pady=10, sticky='W')
            quantity = tk.Entry(frame_buttons, textvariable=self.qt[i], relief="solid", width = 12)
            quantity.grid(column=5,row=i+2, padx=10, pady=10, sticky='W')
            head6 = tk.Label(frame_buttons, text=data.iloc[i]["quantAmnt"], padx=10)
            head6.grid(column=6, row=i+2, padx=10, pady=10, sticky='W')
            delete=tk.Button(frame_buttons, text = 'X', font=("",10,"bold"), width=2, fg='red', command=lambda num=data.iloc[i]["Sr.No"] : self.deleteRow(num))
            delete.grid(column=7,row=i+2, padx=10, pady=10, sticky='W')

        
        indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        finCost = indCurr(finalCost)
        costTotVar.set(finCost)
        
        line = ttk.Label(frame_buttons, text="________________________________________________________________________________________________________________________________________________")
        line.grid(column=0, row=i+3, columnspan=7, padx=10, pady=10, sticky='N')
        
        cost = ttk.Label(frame_buttons, text="Total Cost")
        cost.grid(column=0, row=i+5, padx=10, pady=10, sticky='W')
        
        finAmt = tk.StringVar()
        finAmt.set(indCurr(data.iloc[i]["finalCost"]))
        
        costTot = tk.Entry(frame_buttons, textvariable=finAmt, relief="solid", width = 14, state='disabled')
        costTot.grid(column=4,row=i+5, padx=10, pady=10, sticky='W')
        
        qtyAmt = tk.StringVar()
        qtyAmt.set(data.iloc[i]["totQuanSum"])
    
        qtyCostTot = tk.Entry(frame_buttons, textvariable=qtyAmt, relief="solid", width = 14, state='disabled')
        qtyCostTot.grid(column=6,row=i+5, padx=10, pady=10, sticky='W')
 
        frame_buttons.update_idletasks()
        frame_canvas.config(width=810, height=400)
 
        canvas.config(scrollregion=canvas.bbox("all"))
        
        addButt=tk.Button(self.new, text = 'Add More Items', font=("",10,"bold"), width=24, command = self.addNewItem)
        addButt.grid(column=0,row=3, padx=10, pady=15, sticky='W')

        calc=tk.Button(self.new, text = 'Calculate(Quantity)', font=("",10,"bold"), width=24, command = self.calcQuant)
        calc.grid(column=1,row=3, padx=10, pady=15, sticky='N')
        
        nextButt=tk.Button(self.new, text = 'Next', font=("",10,"bold"), width=24, command = self.nextItem)
        nextButt.grid(column=2,row=3, padx=10, pady=15, sticky='E')

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
    y = (screen_height/2) - (app_height/2) - 200
    new.geometry('+%d+%d'%(x,y))
    
    totSQFt = float(Width.get()) * float(Height.get())
    totSQFt = round(totSQFt,2)    
    
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
        clearValues()
        obj = FixLouver(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Patti Louver"):
        new.title("Patti Louver")
        clearValues()
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
    
    elif(selectWinDrop.get() == "Aluminium partition"):
        new.title("Aluminium partition")
        clearValues()
        obj = AluminiumPartition(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Toughened partition"):
        new.title("Toughened partition")
        clearValues()
        obj = ToughenedPartition(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Toughened Door"):
        new.title("Toughened Door")
        clearValues()
        obj = ToughenedDoor(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Composite pannel"):
        new.title("Composite pannel")
        clearValues()
        obj = CompositePanel(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()
    
    elif(selectWinDrop.get() == "Curtain wall"):
        new.title("Curtain wall")
        clearValues()
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
        
    elif(selectWinDrop.get() == "Exhaust Fan Window"):
        new.title("Exhaust Fan Window")
        clearValues()
        obj = ExhaustFanWindow(new)
        obj.frameCreate()
        obj.variableTitles()
        obj.variables()

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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
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
 
        canvas.config(scrollregion=(0,0,700,685))
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
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
        canvas.config(scrollregion=(0,0,700,650))

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
    
        image = Image.open("./Images/Sliding Door.png")
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
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
        canvas.config(scrollregion=(0,0,700,530))

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
    
        image = Image.open("./Images/Fix Louver.png")
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
            
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
        canvas.config(scrollregion=(0,0,700,530))
        

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
    
        image = Image.open("./Images/Patti Louver.png")
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
            
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
        canvas.config(scrollregion=(0,0,700,690))

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
    
        image = Image.open("./Images/Openable Window.png")
        resize_image = image.resize((600, 400))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        imgLab = tk.Label(self.frame1, image=img)
        imgLab.image = img
        imgLab.grid(column=2, row=1, rowspan=15)
        selectWinLabel = ttk.Label(self.frame1, text=selectWinDrop.get(), font=("",20,"bold"))
        selectWinLabel.grid(column=2, row=16)
        selectWinLabel = ttk.Label(self.frame1, text="(This is an Illustration, not actual product)", font=("",10,""))
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
            
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
        canvas.config(scrollregion=(0,0,700,690))       

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
    
        image = Image.open("./Images/Sliding folding door.png")
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
            
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
        canvas.config(scrollregion=(0,0,700,695))

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
    
        image = Image.open("./Images/Casement Window.png")
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
            
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
        canvas.config(scrollregion=(0,0,700,530))
        

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
    
        image = Image.open("./Images/Aluminium partition.png")
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
            
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
        canvas.config(scrollregion=(0,0,700,530))

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
    
        image = Image.open("./Images/Toughened partition.png")
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
            
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
        canvas.config(scrollregion=(0,0,700,530))
        

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
    
        image = Image.open("./Images/Toughened Door.png")
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
            
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
        canvas.config(scrollregion=(0,0,700,530))
        

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
    
        image = Image.open("./Images/Composite pannel.png")
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
            
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
        canvas.config(scrollregion=(0,0,700,530))
        
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
    
        image = Image.open("./Images/Curtain wall.png")
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
            
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
        canvas.config(scrollregion=(0,0,700,650))

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
    
        image = Image.open("./Images/Fix Window.png")
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

class ExhaustFanWindow:
    
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
        
        localFlag = checkDigits()
        if(costEntVar.get() == ""):
            messagebox.showerror("Invalid","Please fill in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        if(not costEntVar.get().isdigit() and localFlag==False):
            messagebox.showerror("Invalid","Please enter numbers in the cost field.", parent=self.new)
            calculateFlag = False
            return False
        else:
            indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
            cstAmt = float(totSQFt)*float(costEntVar.get())
            self.cstAmtInr.set(indCurr(cstAmt))
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
        canvas.config(scrollregion=(0,0,700,590))

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
    
        image = Image.open("./Images/Exhaust Fan Window.png")
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
        typeLabel = ttk.Label(self.frame1, text="Type")
        typeLabel.grid(column=0, row=5, padx=10, pady=10, sticky='W')
        aluMaterial = ttk.Label(self.frame1, text="Aluminium Material")
        aluMaterial.grid(column=0, row=6, padx=10, pady=10, sticky='W')
        glaThick = ttk.Label(self.frame1, text="Glass Thickness")
        glaThick.grid(column=0, row=7, padx=10, pady=10, sticky='W')
        glaType = ttk.Label(self.frame1, text="Glass Type")
        glaType.grid(column=0, row=8, padx=10, pady=10, sticky='W')
        hard = ttk.Label(self.frame1, text="Hardware")
        hard.grid(column=0, row=9, padx=10, pady=10, sticky='W')
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
        
        hardwa = tk.Entry(self.frame1, textvariable=hardwaVar, width=33, relief="solid")
        hardwa.grid(column=1,row=9, padx=10, pady=10, sticky='W')
        
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
windDetails = ttk.Label(root, text="Enter Window Details", font=("",10,"bold"))
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
cartButt=tk.Button(root, text=' Cart ', font=("",10,"bold"), command=obj.addMorePage, image=cartImg, compound=tk.RIGHT)
cartButt.grid(column=1,row=0, padx=10, pady=15, sticky='NE')

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
custConEnt = tk.Entry(frame0, textvariable=custConVar, font=("",10,""), relief="solid", width = 21)
custConEnt.grid(column=1,row=3, padx=10, pady=10, sticky='W')

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

# obj = Invoice()
# invoice=tk.Button(new, text = 'Invoice Page', width=20, command = obj.invWindow)
# invoice.grid(column=1,row=1, columnspan=2, padx=10, pady=15, sticky='E')

m = tk.Menu(root)
root.config(menu=m)
file_menu = tk.Menu(m, tearoff=False)
m.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Open from file", command=open_file1)

root.mainloop()