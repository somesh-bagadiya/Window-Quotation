# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:31:03 2022

@author: DarkLegacy
"""


from fpdf import FPDF
from datetime import date
# from datetime import datetime
from num2words import num2words
from babel.numbers import format_currency
import pandas as pd
from math import floor
from math import ceil

data = pd.read_excel('./data/Somesh Bagadiya_QuatationData.xlsx')
data = data.replace(float('nan'),"")

# data = None
custName = None
# Returns the current local date
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
        # self.line(105, 70, 195, 70)
        
        #------------------------------------------------------------------

        self.line(15, 80, 195, 80)
        self.line(15, 95, 195, 95)
        
        for i in range(1,4):
            self.line(15+(60*i), 65, 15+(60*i), 95 )
            
        self.line(15, 96, 195, 96)
      
    def drawLinesInfo(self, printLevel):
        self.line(15, 105, 195, 105)
        self.line(23, 96, 23, printLevel)
        self.line(88, 96, 88, printLevel)
        self.line(115, 96, 115, printLevel)
        self.line(145, 96, 145, printLevel)
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
        # self.line(167.5, 96, 167.5, taxLevel)
        

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

        desc = data["windowTypeVar"][x] + " (" + data["Width"][x] + " x " + data["Height"][x] + ")"

        self.set_y(printLevel)
        self.set_x(24)
        self.set_font('helvetica', '', 8)
        self.cell(w=77,txt="{}".format(desc), align="L")
        

        self.set_y(printLevel)
        self.set_x(88)
        self.set_font('helvetica', '', 8)
        self.cell(w=22.5,txt="{}".format(data["hsnSacVar"][x]), align='L')
        
        rate = data["cstAmtInr"][x]

        self.set_y(printLevel)
        self.set_x(115)
        self.set_font('helvetica', '', 8)
        self.cell(w=22.5,txt="Rs. {}".format(rate[1:]), align='L')

        self.set_y(printLevel)
        self.set_x(145)
        self.set_font('helvetica', '', 8)
        self.cell(w=22.5,txt="{}".format(data["quantity"][x]), align='C')
        
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
        self.cell(w=0,txt="1234567890")
        
        #------------------------------------------------------------------------------------------------------------------------------------
        
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
        # self.multi_cell(w=60, h=5,txt="asdfad sfadfa")

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
        
        
        # self.buyerY = self.get_y() + 5
    
        #------------------------------------------------------------------------------------------------------------------------------------
        
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
    
        #------------------------------------------------------------------------------------------------------------------------------------
        
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
        self.set_y(97)
        self.set_x(15.5)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Sr.")        
        
        self.set_y(101)
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
        self.cell(w=27,txt="HSN/SAC", align='C')

        self.set_y(99)
        self.set_x(115)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=30,txt="Rate", align='C')

        self.set_y(99)
        self.set_x(145)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=22.5,txt="Quantity", align='C')
    
        self.set_y(99)
        self.set_x(167.5)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=27.5,txt="Amount", align='C')
    
    def infosection(self):
        
        global printCount, taxLevel
        

        # printLevel = self.get_y() + 9
        printLevel = 108
        # print(printLevel)
        
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
        # print(printLevel)
        # taxLevel = printLevel + 18
        
        
        self.line(15, printLevel, 195, printLevel)
        self.line(15, printLevel + 23, 195, printLevel + 23)
          
    def taxableAmountTitle(self):
        taxLevel = 97
        
        # indCurr = lambda x : format_currency(x, 'INR', locale='en_IN').replace(u'\xa0', u' ')
        # startTaxLevel = taxLevel - 2
        
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
        
        # for i in range(data.shape[0]):
        #     taxPrintCount+=1
        #     taxSum = self.printTaxInfo(taxLevel, i, taxSum)
        #     taxLevel = taxLevel + 7
            
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
        
        # self.drawLinesTax(startTaxLevel, taxLevel-7)
        
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
        
        # self.drawLinesTax(startTaxLevel, taxLevel)
        
    def endPrint(self):
        global endPrintLevel
        
        name = "Madhav Glass & Aluminium"
        bank = "Punjab National Bank"
        account = "0650050015525"
        ifsc = "PUNB0065020"
        
        # print(endPrintLevel)
        
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

pdfInv = PDFInvoice('P', 'mm', 'A4')
pdfInv.invoiceDriverCode()
# pdfInv.alias_nb_pages()
# pdfInv.set_left_margin(15)
# pdfInv.set_right_margin(15)
# pdfInv.set_auto_page_break(auto = True, margin = 15)
# pdfInv.add_page()
# pdfInv.set_y(15)

# pdfInv.homePage()
# # pdfInv.drawLines()
# pdfInv.infosection()
# pdfInv.add_page()
# pdfInv.homePage()
# pdfInv.taxableAmount()
# pdfInv.endPrint()

pdfInv.output('Invoice1.pdf')


# Scroll