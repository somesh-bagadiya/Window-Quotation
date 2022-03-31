# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 23:58:17 2022

@author: DarkLegacy
"""

from fpdf import FPDF
from datetime import date
import pandas as pd
from math import ceil



####################################################################################################################################################

def setCustomerName(cust):
    global custName
    custName = cust

####################################################################################################################################################


data = pd.read_excel('./data/_QuatationData.xlsx')
data = data.replace(float('nan'),"")

# data = None
custName = None
# Returns the current local date
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

AluminumpartitionWidth = 45
AluminumpartitionHeight = 36

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

# ["Sliding Window", "Sliding Door", "Fix Louver", "Patti Louver", "Openable Window", "Sliding folding door", "Casement Window", "Aluminum partition", "Toughened partition", "Toughened Door", "Composite pannel", "Curtain wall", "Fix Window"

ratio["Sliding Window"] = [SlidingWindowWidth, SlidingWindowHeight]
ratio["Sliding Door"] = [SilidingDoorWidth, SilidingDoorHeight]
ratio["Fix Louver"] = [FixLouverWidth, FixLouverHeight]
ratio["Patti Louver"] = [PattiLouverWidth, PattiLouverHeight]
ratio["Openable Window"] = [OpenableWindowWidth, OpenableWindowHeight]
ratio["Sliding folding door"] = [SlidingfoldingdoorWidth, SlidingfoldingdoorHeight]
ratio["Casement Window"] = [CasementWindowWidth, CasementWindowHeight]
ratio["Aluminum partition"] = [AluminumpartitionWidth, AluminumpartitionHeight]
ratio["Toughened partition"] = [AluminumpartitionWidth, AluminumpartitionHeight]
ratio["Toughened Door"] = [AluminumpartitionWidth, AluminumpartitionHeight]
ratio["Composite pannel"] = [CompositepannelWidth, CompositepannelHeight]
ratio["Curtain wall"] = [CurtainwallWidth, CurtainwallHeight]
ratio["Fix Window"] = [FixWindowWidth, FixWindowHeight]


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
        # self.line(design+60, textLevel+5.5, design+60, textLevel+4.7+ratio[key][1])
        
        if(ratio[key][0]<50):
            # self.line(design+12.8, textLevel+0.5, design+12.8+ratio[key][0], textLevel+0.5)
            self.line(design+12.8, textLevel+9.5+ratio[key][1], design+ratio[key][0]+12.5, textLevel+9.5+ratio[key][1])
        else:
            # self.line(design+7.8, textLevel+0.5, design+ratio[key][0]+7.5, textLevel+0.5)
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
        
        # print(x)
        
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
        
        # self.set_y(textLevel-0.5)
        # self.set_x(design+(60-strWidth)/2)
        # self.set_font('helvetica', '', 6)
        # self.set_fill_color(256,256,256)
        # self.cell(w=strWidth+4, txt="{}".format(data["Width"][x]), align='C', fill=True)
        
        
    def printInPDF(self, textLevel, design, specs, cost, quantity, amount, x):
        
        print(x)
        key = data["windowTypeVar"][x]
        
        self.set_y(textLevel)
        self.set_x(15)
        self.set_font('helvetica', '', 6)
        self.cell(w=12,txt="{}".format(x+1), align='C')
        
        self.insertImage(x,design,textLevel)
        # self.image('./Images/{}.png'.format(data["windowTypeVar"][x]), x=design + 7.5, y=textLevel+5, w = ratio[key][1], h=ratio[key][0])
        if(ratio[key][0]<50):
            self.set_y(textLevel+65)
        else:
            self.set_y(textLevel+55) 
        self.set_x(design)
        self.set_font('helvetica', 'B', 6)
        self.cell(w=65,txt="{}".format(data["windowTypeVar"][x]), align='C')
        
        self.printSpecs(textLevel,specs,x)
        
        if(data["discountFlag"][0]=="True Flag"):
            self.set_y(textLevel)
            self.set_x(cost)
            self.set_font('helvetica', 'B', 6)
            self.cell(w=20,txt="Rs. {}".format(data["costWithLabProfAndDisc"][x][1:]), align='C')
            
            self.set_y(textLevel)
            self.set_x(quantity)
            self.set_font('helvetica', '', 6)
            self.cell(w=10,txt="{}".format(data["quantity"][x]), align='C')
            
            self.set_y(textLevel)
            self.set_x(amount)
            self.set_font('helvetica', 'B', 6)
            self.cell(w=28,txt="Rs. {}".format(data["quantCostWithLabProfAndDisc"][x][1:]), align='C')
        else:
            self.set_y(textLevel)
            self.set_x(cost)
            self.set_font('helvetica', 'B', 6)
            self.cell(w=20,txt="Rs. {}".format(data["costWithLabAndProf"][x][1:]), align='C')
            
            self.set_y(textLevel)
            self.set_x(quantity)
            self.set_font('helvetica', '', 6)
            self.cell(w=10,txt="{}".format(data["quantity"][x]), align='C')
            
            self.set_y(textLevel)
            self.set_x(amount)
            self.set_font('helvetica', 'B', 6)
            self.cell(w=28,txt="Rs. {}".format(data["quantCostWithLabAndProf"][x][1:]), align='C')
        
    def printSpecs(self, textLevel, specs, x):
        self.set_y(textLevel)
        self.set_x(specs)
        self.set_font('helvetica', '', 6)
        # width = self.get_string_width(varName[i])
        self.cell(w=10,txt=" Area: {} Sq.Ft.".format(data["totSqftEntVar"][x]))
        textLevel = textLevel + 4
        self.set_y(textLevel)
        self.set_x(specs)
        for i in varName.keys():
            width = self.get_string_width(varName[i])
            if(data.iloc[x][i]!="" and data.iloc[x][i]!=0 ):
                self.cell(w=width,txt=" {}: {}".format(varName[i], data.iloc[x][i]))
                textLevel = textLevel + 4
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

        self.dashed_line(15, 52, 195, 52)

        self.set_y(60)
        self.set_x(170)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="Date:")

        self.set_y(60.1)
        self.set_x(179)
        self.set_font('helvetica', '', 9)
        self.cell(w=0,txt="{}/{}/{}".format(today.day,today.month,today.year))

        self.set_y(60.1)
        self.set_x(15)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="To,")

        self.set_y(67.1)
        self.set_x(15)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="{} ".format(data["custNamVar"][0]))

        self.set_y(69.5)
        self.set_x(15)
        self.set_font('helvetica', 'B', 8)
        self.multi_cell(w=60, h=5,txt="{}".format(data["address"][0]))
        # self.multi_cell(w=60, h=5,txt="asdfad sfadfa")

        self.set_y(self.get_y()+2.5)
        self.set_x(15)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="{}".format(data["custConVar"][0]))

        self.ln(h=7)
        titleLevelY = self.get_y()
        titleLevelX = 15

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=12, h=10, txt="Sr.No", fill=True, border=True, align='C')
        # self.line(titleLevelX, titleLevelY, titleLevelX, 280)

        titleLevelX = titleLevelX + 12

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=65, h=10, txt="DESIGN", fill=True, border=True, align='C')
        # self.line(titleLevelX, titleLevelY, titleLevelX, 280)

        design = titleLevelX
        titleLevelX = titleLevelX + 65

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=45, h=10, txt="SPECIFICATIONS", fill=True, border=True, align='C')
        # self.line(titleLevelX, titleLevelY, titleLevelX, 280)

        specs = titleLevelX
        titleLevelX = titleLevelX + 45

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=20, h=10, txt="COST(Rs.)", fill=True, border=True, align='C')
        # self.line(titleLevelX, titleLevelY, titleLevelX, 280)

        cost = titleLevelX
        titleLevelX = titleLevelX + 20
        
        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=10, h=10, txt="QTY", fill=True, border=True, align='C')
        # self.line(titleLevelX, titleLevelY, titleLevelX, 280)

        quantity = titleLevelX
        titleLevelX = titleLevelX + 10

        self.set_y(titleLevelY)
        self.set_x(titleLevelX)
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(229,233,243)
        self.cell(w=28, h=10, txt="AMOUNT(Rs.)", fill=True, border=True, align='C')
        # self.line(titleLevelX, titleLevelY, titleLevelX, 280)

        amount = titleLevelX

        noOfDiv = (280 - titleLevelY)/2
        # self.line(15, titleLevelY + noOfDiv, 195, titleLevelY + noOfDiv)

        textLevel = titleLevelY + 15
        
        for i in range(2):#len(list(data["Sr.No"]))):
            if(printCount<data[data.columns[0]].count()):
                self.drawLinesHome(titleLevelY,noOfDiv)
                # print(titleLevelY,noOfDiv-2)
                printCount+=1
                self.printInPDF(textLevel, design, specs, cost, quantity, amount, i)
                textLevel = textLevel + noOfDiv
                titleLevelY = textLevel - 15
            
        totalLevel = self.get_y()
        # self.line(15, 280, 195, 280)
        # self.line(195, titleLevelY, 195, 280)
        
    
        
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
        
        # noOfDiv = (267 - 10)/3
        # self.line(15, titleLevelY + 67.5, 195, titleLevelY + 67.5)
        # self.line(15, titleLevelY + noOfDiv + noOfDiv + 10, 195, titleLevelY + noOfDiv + noOfDiv + 10)
        
        titleLevelY = titleLevelY
        
        for i in range(3):
            if(printCount<data[data.columns[0]].count()):
                if(i==0):
                    # printCount+=1
                    self.drawLines(titleLevelY+6)
                    self.printInPDF(titleLevelY + 15, design, specs, cost, quantity, amount, printCount)
                    printCount+=1
                    titleLevelY = titleLevelY+88
                elif(i==1):
                    # printCount+=1
                    self.drawLines(titleLevelY+2.5)
                    self.printInPDF(titleLevelY + 15, design, specs, cost, quantity, amount, printCount)
                    printCount+=1
                    titleLevelY = titleLevelY+88
                else:
                    # printCount+=1
                    self.drawLines(titleLevelY)
                    self.printInPDF(titleLevelY + 15, design, specs, cost, quantity, amount, printCount)
                    printCount+=1
                    titleLevelY = titleLevelY+88

        # print(self.get_y())
        totalLevel = self.get_y()

    def totalDisplay(self):
        global totalLevel, endLevel
        
        subTot = 0
        cgst = 0
        sgst = 0
        granTot = 0
        
        
        totalLevel = totalLevel + 78
        print(totalLevel)
        
        if(totalLevel <= 80):
            totalLevel = totalLevel + 10
        elif(totalLevel <= 100):
            totalLevel = totalLevel + 10
        elif(totalLevel <= 190):
            totalLevel = totalLevel + 10
        elif(totalLevel > 230):
            self.add_page()
            totalLevel = 15
        
        print(totalLevel)
        
        if(data["discountFlag"][0]=="True Flag"):
            
            for i in range(len(data["quantCostWithLabProfAndDisc"])):
                subTot = subTot + float(data["quantCostWithLabProfAndDisc"][i][1:].replace(",",""))
            
            subTot = round(subTot,2)
            disc = list(data["discountEntVar"])
            discAmt = (subTot*disc[-1]/100)
            discTot = subTot - discAmt
            cgst = round((discTot*9/100),2)
            sgst = round((discTot*9/100),2)
            granTot = round(discTot + sgst + cgst,2)
            
            wi = self.get_string_width("Total Area: ")
            self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=wi + 2, h=7, txt="Total Area: ", align='L')
            
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=20, h=7, txt="{} Sq.Ft.".format(round(sum(data["totSqftEntVar"]),2)), align='L')
            
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="Sub Total", fill=True, border=True, align='C')
            
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
            
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(subTot), fill=True, border=True, align='C')
            
            totalLevel = totalLevel + 7
            
            wi = self.get_string_width("Total Windows: ")
            self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=wi, h=7, txt="Total Windows: ", align='L')
            
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=20, h=7, txt="{} Nos".format(round(sum(data["quantity"]),2)), align='L')
            
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="Discount @{}%".format(disc[-1]), fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(round(discAmt,2)), fill=True, border=True, align='C')
            
            totalLevel = totalLevel + 7
            
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="CGST @9%", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(cgst), fill=True, border=True, align='C')
            
            totalLevel = totalLevel + 7
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="SGST @9%", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(sgst), fill=True, border=True, align='C')
            
            totalLevel = totalLevel + 7
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="Grand Total", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(granTot), fill=True, border=True, align='C')
            
        else:
            
            for i in range(len(data["quantCostWithLabAndProf"])):
                subTot = subTot + float(data["quantCostWithLabAndProf"][i][1:].replace(",",""))
            
            subTot = round(subTot,2)
            cgst = round((subTot*9/100),2)
            sgst = round((subTot*9/100),2)
            granTot = round(subTot + sgst + cgst,2)
        
            wi = self.get_string_width("Total Area: ")
            self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=wi + 2, h=7, txt="Total Area: ", align='L')
            
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=20, h=7, txt="{} Sq.Ft.".format(round(sum(data["totSqftEntVar"]),2)), align='L')
            
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="Sub Total", fill=True, border=True, align='C')
            
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
            
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(subTot), fill=True, border=True, align='C')
            
            totalLevel = totalLevel + 7
            
            wi = self.get_string_width("Total Windows: ")
            self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=wi, h=7, txt="Total Windows: ", align='L')
            
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=20, h=7, txt="{} Nos".format(round(sum(data["quantity"]),2)), align='L')
            
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="CGST @9%", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(cgst), fill=True, border=True, align='C')
            
            totalLevel = totalLevel + 7
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="SGST @9%", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(sgst), fill=True, border=True, align='C')
            
            totalLevel = totalLevel + 7
            self.set_y(totalLevel)
            self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=45, h=7, txt="Grand Total", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align='C')
            
            # self.set_y(totalLevel)
            # self.set_x(100)
            self.set_font('helvetica', 'B', 7)
            self.set_fill_color(229,233,243)
            self.cell(w=40, h=7, txt="Rs. {}".format(granTot), fill=True, border=True, align='C')
        
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
        str8 = "4. WARRANTY"
        str9 = "a. Profile warranty for de-colourisation is 10 yrs."
        str10 = "b. Hardware (Rollers and locking system) warranty is for 5 yrs."
        str11 = "Thanking you and assuring you the best of our services all the times."
        str12 = "I have gone through the specifications & Drawings. \nI accept terms and conditions"

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
        
        endLevel = self.get_y() + 5
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str8, align='L')
        
        endLevel = self.get_y()
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B',9 )
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str9, align='L')
        
        endLevel = self.get_y() 
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B',9 )
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str10, align='L')
        
        endLevel = self.get_y() + 5
        
        self.set_y(endLevel)
        self.set_x(15)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(229,233,243)
        self.multi_cell(w=180, h=7, txt=str11, align='L')
        
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
        self.multi_cell(w=85, h=7, txt=str12, align='L')
        
        
    def driverCode(self):
        # pdf = PDF('P', 'mm', 'A4')
        self.alias_nb_pages()
        self.set_left_margin(15)
        self.set_right_margin(15)
        self.set_auto_page_break(auto = True, margin = 15)
        self.add_page()
        self.set_y(15)
        self.homePage()
                   

        for i in range(ceil((totSrno-2)/3)):
            self.add_page()
            self.newPage()

        self.totalDisplay()
        self.pdfEnd()

        self.output(self.fileName)#'./Data/{} Quotation.pdf'.format(data["custNamVar"][0]))
        # self.output('./Output/{} Quotation.pdf'.format(data["custNamVar"][0]))
        self.printDoneFlag = True
        
pdf = PDF('P', 'mm', 'A4')
pdf.alias_nb_pages()
pdf.set_left_margin(15)
pdf.set_right_margin(15)
pdf.set_auto_page_break(auto = True, margin = 15)
pdf.add_page()
pdf.set_y(15)
pdf.homePage()
           

for i in range(ceil((totSrno-2)/3)):
    pdf.add_page()
    pdf.newPage()

pdf.totalDisplay()
pdf.pdfEnd()

pdf.output('pdf_4.pdf')