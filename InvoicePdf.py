# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:31:03 2022

@author: DarkLegacy
"""


from fpdf import FPDF
from datetime import date
import pandas as pd
# from math import ceil

data = pd.read_excel('./data/_QuatationData.xlsx')
data = data.replace(float('nan'),"")

# data = None
custName = None
# Returns the current local date
today = date.today()
totSrno = len(list(data["Sr.No"]))
printCount = 0

ratio = dict()

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
        self.line(15, 105, 195, 105)
        
        
        self.line(23, 96, 23, 280)
        
        
        self.line(100, 96, 100, 280)
        self.line(122.5, 96, 122.5, 280)
        self.line(145, 96, 145, 280)
        self.line(167.5, 96, 167.5, 280)
        # self.line(100, 96, 100, 280)
            
        # self.line(15, self.buyerY, 105, self.buyerY)
        

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
        self.set_font('helvetica', '', 8)
        self.cell(w=0,txt="Email-ID : ")
        
        wi = self.get_string_width("Email-ID : ")
        
        self.set_y(self.get_y())
        self.set_x(107+wi)
        self.set_font('helvetica', 'I', 8)
        self.cell(w=0,txt="madhavglassandaluminium@gmail.com")
        
        self.set_y(self.get_y()+4)
        self.set_x(107)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="GST Registration No : ")
        
        wi = self.get_string_width("GST Registration No : ")
        
        self.set_y(self.get_y())
        self.set_x(107+wi)
        self.set_font('helvetica', 'I', 8)
        self.cell(w=0,txt="27CURPB8193C1ZC")
    
        self.set_y(self.get_y()+4)
        self.set_x(107)
        self.set_font('helvetica', 'B', 8)
        self.cell(w=0,txt="PAN No : ")
        
        wi = self.get_string_width("PAN No : ")
        
        self.set_y(self.get_y())
        self.set_x(107+wi)
        self.set_font('helvetica', 'I', 8)
        self.cell(w=0,txt="1234567890")
        
        
        # self.buyerY = self.get_y() + 5
    
        #------------------------------------------------------------------------------------------------------------------------------------
        
        self.set_y(66)
        self.set_x(17)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Invoice No.")
        
        self.set_y(66)
        self.set_x(77)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Quotation No.")
        
        self.set_y(66)
        self.set_x(137)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Date")
        
    
        #------------------------------------------------------------------------------------------------------------------------------------
        
        self.set_y(81)
        self.set_x(17)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Mode/Terms of Payment")
        
        self.set_y(81)
        self.set_x(77)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Terms of Delivery")
        
        self.set_y(81)
        self.set_x(137)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=0,txt="Destination")
    
    
    def infosection(self):
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
        self.cell(w=77,txt="Description of Goods", align='C')

        self.set_y(99)
        self.set_x(100)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=22.5,txt="HSN/SAC", align='C')

        self.set_y(99)
        self.set_x(122.5)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=22.5,txt="Quantity", align='C')

        self.set_y(99)
        self.set_x(145)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=22.5,txt="Rate", align='C')
    
        self.set_y(99)
        self.set_x(167.5)
        self.set_font('helvetica', 'B', 10)
        self.cell(w=27.5,txt="Amount", align='C')


pdfInv = PDFInvoice('P', 'mm', 'A4')
pdfInv.alias_nb_pages()
pdfInv.set_left_margin(15)
pdfInv.set_right_margin(15)
pdfInv.set_auto_page_break(auto = True, margin = 15)
pdfInv.add_page()
pdfInv.set_y(15)

pdfInv.homePage()
pdfInv.drawLines()
pdfInv.infosection()

pdfInv.output('Invoice.pdf')



# invoice no
# quotation nu
# Mode/Terms of Payment
# Terms of Delivery
# Destination
# Date


# Decimal Issue on cost field 1st page
# Decimal width and height
## Remove Labour Charges and Profit from last page
## remove contat nummber Qoutation 
## Chagne order summary