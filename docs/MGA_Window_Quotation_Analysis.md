# MGA Window Quotation Application - GROUND TRUTH DOCUMENT

> **⚠️ CRITICAL: This document serves as the AUTHORITATIVE GROUND TRUTH for all future development of the MGA Window Quotation Application. Every detail in this document is verified against the actual legacy production code.**

---

## 📋 DOCUMENT RULES & GUIDELINES

### 🔒 **IMMUTABLE PRINCIPLES**
1. **LEGACY CODE IS KING**: The file `MGA Window Quotaion.py` is the source of truth. When in doubt, refer to legacy behavior.
2. **EXACT REPLICATION**: All calculations, validations, workflows, and UI behaviors must match the legacy code EXACTLY.
3. **NO ASSUMPTIONS**: If something is not explicitly documented here, verify against the legacy code before implementing.
4. **VERSION CONTROL**: This document MUST be updated when any legacy behavior is discovered or clarified.

### 🛡️ **DEVELOPMENT RULES**
1. **Before making ANY change**: Cross-reference with this document
2. **Before adding ANY feature**: Verify it exists in legacy code
3. **Before modifying calculations**: Confirm exact formulas against legacy
4. **Before changing validations**: Match exact error messages from legacy
5. **Before altering workflows**: Trace complete user journeys in legacy

### 📝 **DOCUMENTATION STANDARDS**
- **Code References**: Always include exact line numbers and method names from legacy
- **Exact Values**: Use exact strings, numbers, and formulas from legacy code
- **Complete Workflows**: Document every step, validation, and state change
- **Error Messages**: Include exact error message text from legacy
- **File Paths**: Use exact relative paths as in legacy

---

## 🏗️ APPLICATION OVERVIEW

**Legacy File**: `MGA Window Quotaion.py` (5,832 lines)  
**Application Type**: Desktop Python application using tkinter  
**Purpose**: Generate window/door quotations and invoices for MGA Windows  
**Database**: Excel-based data storage and retrieval  

---

## 🎯 COMPLETE PRODUCT CATALOG

The application supports exactly **14 product types** as defined in legacy code:

| Product Type | Legacy Class | Image File | Specifications |
|--------------|--------------|------------|----------------|
| Sliding Window | `SlidingWindow` | `Sliding Window.png` | 13 specifications |
| Sliding Door | `SlidingDoor` | `Sliding Door.png` | 13 specifications |
| Fix Louver | `FixLouver` | `Fix Louver.png` | 14 specifications (includes Louver Blade) |
| Patti Louver | `PattiLouver` | `Patti Louver.png` | 14 specifications (includes Louver Blade) |
| Openable Window | `OpenableWindow` | `Openable Window.png` | 15 specifications (includes Handle) |
| Sliding Folding Door | `SlidingFoldingDoor` | `Sliding folding door.png` | 15 specifications (includes Handle) |
| Casement Window | `CasementWindow` | `Casement Window.png` | 15 specifications (includes Handle) |
| Aluminium Partition | `AluminiumPartition` | `Aluminium partition.png` | 12 specifications |
| Toughened Partition | `ToughenedPartition` | `Toughened partition.png` | 11 specifications |
| Toughened Door | `ToughenedDoor` | `Toughened Door.png` | 13 specifications |
| Composite Panel | `CompositePanel` | `Composite pannel.png` | 17 specifications (includes ACP Sheet) |
| Curtain Wall | `CurtainWall` | `Curtain wall.png` | 16 specifications (includes Comp Sheet) |
| Fix Window | `FixWindow` | `Fix Window.png` | 12 specifications |
| Exhaust Fan Window | `ExhaustFanWindow` | `Exhaust Fan Window.png` | 12 specifications |

---

## 💳 COST CALCULATION SYSTEM

### 🧮 **EXACT CALCULATION FORMULAS**

#### **Basic Cost Calculation**
```python
# From legacy calculateCost() methods
total_sqft = width * height
cost_per_sqft = float(costEntVar.get())
total_cost = total_sqft * cost_per_sqft
```

#### **GST Calculation (Fixed at 18%)**
```python
# From legacy CalculatePage.calculateCost()
if discountEntVar.get() != "" and instEntVar.get() != "":
    discountedCost = totalcost - float(discountEntVar.get())
    gstCost = discountedCost + (discountedCost * 18 / 100)  # GST always 18%
    installationCost = gstCost + float(instEntVar.get())
else:
    gstCost = totalcost + (totalcost * 18 / 100)
    if discountEntVar.get() != "":
        discountedCost = totalcost - float(discountEntVar.get())
        gstCost = discountedCost + (discountedCost * 18 / 100)
    if instEntVar.get() != "":
        installationCost = gstCost + float(instEntVar.get())
```

#### **Invoice GST Breakdown (CGST + SGST)**
```python
# From legacy PDFInvoice.infosection()
cgst = bill * 9 / 100  # CGST @9%
sgst = bill * 9 / 100  # SGST @9% (same as CGST)
total_gst = cgst + sgst  # = 18% total
```

#### **Currency Formatting**
```python
# Exact function from legacy
indCurr = lambda x: format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")
```

---

## 🔍 VALIDATION SYSTEM

### 📋 **INPUT VALIDATION RULES**

#### **Digital Input Validation**
```python
# From legacy checkDigits() function - Line 117
def digVerify(self, value):
    if value.isdigit() or value == "":
        return True
    else:
        return False
```

#### **Required Field Validations**
```python
# Width/Height validation - exact error messages from legacy
if Width.get() == "":
    messagebox.showerror("Invalid", "Please fill in the width field.", parent=new)
    return False

if Height.get() == "":
    messagebox.showerror("Invalid", "Please fill in the height field.", parent=new)
    return False

if not digVerify(Width.get()):
    messagebox.showerror("Invalid", "Please enter numbers in the width field.", parent=new)
    return False

if not digVerify(Height.get()):
    messagebox.showerror("Invalid", "Please enter numbers in the height field.", parent=new)
    return False
```

#### **Cost Field Validation**
```python
# From legacy cost calculation methods
if costEntVar.get() == "":
    messagebox.showerror("Invalid", "Please fill in the cost field.", parent=new)
    return False

if not digVerify(costEntVar.get()):
    messagebox.showerror("Invalid", "Please enter numbers in the cost field.", parent=new)
    return False
```

#### **GST Validation**
```python
# From CalculatePage.calculateCost()
if gstEntVar.get() == "":
    messagebox.showerror("Invalid", "Please fill GST percentage", parent=self.new)
    return False
```

#### **Calculate Button Validation**
```python
# From Cart.nextItem() and Invoice.invWindow()
if pressedCalcFlag != True:
    messagebox.showerror("Invalid", "Please press calculate button", parent=self.new)
    return False
```

#### **Cart Quantity Validation**
```python
# From Cart.nextItem()
if calcQuantFlag != True:
    messagebox.showerror("Invalid", "Please calculate quantity values by clicking on Calculate(Quantity) Button", parent=new)
    return False
```

---

## 📁 FILE SYSTEM & DATA MANAGEMENT

### 📂 **EXACT FILE PATHS & NAMING CONVENTIONS**

#### **Primary Data File**
```python
# From line 22 in legacy
data = pd.read_excel("./Data/data.xlsx")
```

#### **Customer Quotation Files**
```python
# From afterCalculate() - line 1342
filename = "./Data/{}_QuatationData.xlsx".format(custNamVar.get())
data.to_excel(filename, index=False)
```

#### **Invoice Database**
```python
# From Invoice.saveData()
"./Data/WindowDatabaseQuoAndInvoice.xlsx"
```

#### **PDF Output Paths**
```python
# From PDF.generatePDF()
default_filename = "{}_Quotation.pdf".format(custNamVar.get())

# From PDFInvoice.generatePDF()  
default_filename = "{}_Invoice.pdf".format(custNamVar.get())
```

#### **Product Images**
```python
# From PDF class and legacy code
image_path = "./Images/{product_name}.png"
# Examples:
# "./Images/Sliding Window.png"
# "./Images/Sliding Door.png"
# "./Images/Fix Louver.png"
```

### 💾 **EXCEL DATA STRUCTURE**

#### **Complete Column List (59 columns)**
```python
# From legacy toExcel() function - exact order
columns = [
    "Sr.No", "Width", "Height", "windowTypeVar", "trackVar", "aluMatVar", 
    "glaThicVar", "glaTypVar", "hardLocVar", "hardBeaVar", "rubbTypVar", 
    "rubbThicVar", "woolFileVar", "aluNetVar", "fraColVar", "silColVar",
    "screwVar1", "screwVar2", "screwVar3", "screwVar4", "screwVar5", "screwVar6",
    "lowBladVar", "handleVar", "acrSheVar", "hardwaVar", "compSheVar", 
    "maskTapVar", "acpSheVar", "totSqftEntVar", "costEntVar", "profitEntVar",
    "discountEntVar", "labourEntVar", "gstEntVar", "costTotVar", "profTotVar",
    "discTotVar", "laboTotVar", "gstTotVar", "custNamVar", "custAddVar", 
    "custConVar", "address", "dateAndTime", "Sr.NoNew", "Particulars",
    "WidthNew", "HeightNew", "Total Sq.ft", "Cost (INR)", "QuantityNew",
    "Amount", "discountFlag", "installationFlag", "instEntVar", "instTotVar",
    "TotalQuanSum", "TotalQuanSumWithGST", "quatationIDVar", "invoiceIDVar"
]
```

---

## 🖥️ USER INTERFACE SPECIFICATIONS

### 🎨 **MAIN WINDOW LAYOUT**

#### **Exact Window Geometry**
```python
# From legacy main window setup
root.geometry("1000x700+100+50")
root.title("MGA WINDOW QUOTATION")
root.iconbitmap("./Images/MGA Logo.ico")
```

#### **Frame Structure (3-Frame Layout)**
```
Frame 2: Customer Details (top)
├── Customer Name (Entry)
├── Customer Address (Text widget, 4 lines)
└── Customer Contact (Entry)

Frame 0: Product Selection (middle)  
├── Window Type Combobox (14 options)
├── Open Cart Button
└── Open Quotation Button

Frame 1: Logo Area (bottom)
└── MGA_1.png image
```

#### **Product Configuration Windows**

**3-Frame Structure** (consistent across all 14 product types):
```
Frame 2: Customer Details (top, read-only)
├── Display customer name, address, contact

Frame 0: Dimensions & Cost (middle)
├── Width Entry (with ft label)
├── Height Entry (with ft label)  
├── Total Sq.ft Entry (calculated, disabled)
├── Cost Entry (per sq.ft)
├── Cost Amount Entry (total, disabled)
├── Calculate Button
├── Add to Cart Button
└── Next Button

Frame 1: Specifications (bottom, scrollable)
├── Product Image (600x400px)
├── Specification comboboxes (product-specific)
└── Specification labels
```

### 🎛️ **WIDGET SPECIFICATIONS**

#### **Entry Widget Configuration**
```python
# Standard entry widget setup from legacy
entry = tk.Entry(parent, textvariable=variable, relief="solid", width=16)
```

#### **Combobox Configuration**
```python
# Standard combobox setup with search functionality
combo = ttk.Combobox(parent, textvariable=variable, width=20, state="readonly")
combo.bind('<KeyRelease>', self.handleWait)  # Search functionality
```

#### **Window Positioning**
```python
# Calculator window positioning (legacy CalculatePage.costPage)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - (screen_width / 2.8)) / 2 + 30
y = ((screen_height / 1.5)) / 2
window.geometry("+%d+%d" % (x, y))
```

---

## 🛒 CART & WORKFLOW SYSTEM

### 📋 **COMPLETE USER WORKFLOW**

#### **Standard Product Configuration Flow**
```
1. Main Window: Enter customer details
2. Main Window: Select product type from combobox
3. Product Window: Opens with 3-frame layout
4. Product Window: Enter width/height
5. Product Window: Select all specifications from comboboxes
6. Product Window: Enter cost per sq.ft OR let system auto-calculate
7. Product Window: Click "Calculate" button (validates + calculates total)
8. Product Window: Click "Add to Cart" (adds to cart with all specs)
9. Product Window: Click "Next" (opens cart view)
10. Cart Window: Review items, modify quantities
11. Cart Window: Click "Calculate(Quantity)" for quantity validation
12. Cart Window: Click "Next" (opens calculator)
13. Calculator: Enter discounts/installation/GST
14. Calculator: Click "Calculate" (computes final costs)
15. Calculator: Click "Generate PDF" OR "Invoice Page"
```

#### **Cart Management Operations**
```python
# From Cart class methods
def addToCart():    # Add item with all specifications
def updateCart():   # Modify existing cart items  
def removeItem():   # Remove item by Sr.No
def calculateQuant(): # Validate and update quantities
def nextItem():     # Proceed to calculator (requires validation)
def addNewItem():   # Return to main window for more items
```

### 🧾 **CART DATA STRUCTURE**

#### **Display Columns (visible in cart)**
```python
display_columns = [
    "Sr.No", "Particulars", "Width", "Height", 
    "Total Sq.ft", "Cost (INR)", "Quantity", "Amount"
]
```

#### **Hidden Specification Data**
```python
# All specification variables stored with each cart item
hidden_specs = [
    "trackVar", "aluMatVar", "glaThicVar", "glaTypVar", "hardLocVar", 
    "hardBeaVar", "rubbTypVar", "rubbThicVar", "woolFileVar", "aluNetVar",
    "fraColVar", "silColVar", "screwVar1", "screwVar2", "screwVar3", 
    "screwVar4", "screwVar5", "screwVar6", "lowBladVar", "handleVar",
    "acrSheVar", "hardwaVar", "compSheVar", "maskTapVar", "acpSheVar"
]
```

---

## 📊 SPECIFICATION OPTIONS CATALOG

### 🔧 **COMPLETE SPECIFICATION OPTIONS**

#### **Track Options** (trackVar)
```python
track_options = ["2 Track", "3 Track", "4 Track"]
```

#### **Aluminium Material** (aluMatVar)
```python
aluminium_material = [
    "Regular Section", "Domal Section (JINDAL)", "Euro Section", 
    "Euro Thermal Greak section", "Structural Glazing", "Curtain wall",
    "Toughened fix glazing", "Composite pannel structure"
]
```

#### **Glass Thickness** (glaThicVar)  
```python
glass_thickness = ["3.5mm", "4mm", "5mm", "8mm", "12mm"]
```

#### **Glass Type** (glaTypVar)
```python
glass_type = [
    "Plain", "Frosted", "One-way", "Tinted", "Bajra", "Reflective", 
    "Louver", "Fixed Louver", "UPVC", "Wooden", "6mm Toughened", 
    "8mm Toughened", "10mm Toughened", "12mm Toughened"
]
```

#### **Hardware Lock** (hardLocVar)
```python
hardware_lock = [
    "Ozone Delux", "Ozone Sleek", "ozone premium", "Europa", 
    "Dorma", "Local fittings"
]
```

#### **Hardware Bearing** (hardBeaVar)
```python
hardware_bearing = [
    "Ozone Delux", "Ozone Sleek", "ozone premium", "Europa", 
    "Dorma", "Local fittings"
]
```

#### **Handle** (handleVar) - Only for specific products
```python
handle = ["C Type", "S Type"]
```

#### **Louver Blade** (lowBladVar) - Only for louver products
```python
louver_blade = ["3\"", "4\"", "5\"", "6\"", "8\"", "10\"", "12\""]
```

#### **Rubber Type** (rubbTypVar)
```python
rubber_type = ["EPDM", "PVC", "Neoprene"]
```

#### **Rubber Thickness** (rubbThicVar)
```python
rubber_thickness = ["3mm", "4mm", "5mm", "6mm"]
```

#### **Complete Screw Options** (screwVar1-6)
```python
screw_options = [
    "Self drilling screw", "pop rivet", "chemical anchor", 
    "Mechanical anchor", "Structural glazing tape", "Silicon"
]
```

#### **Frame Colors** (fraColVar)
```python
frame_color = [
    "Mill finish", "Golden", "Bronze", "white", "Wooden", 
    "Dual colour", "powder coating"
]
```

#### **Silicon Colors** (silColVar)
```python
silicon_color = [
    "clear", "Golden", "Bronze", "white", "Black", "Grey"
]
```

---

## 📄 PDF GENERATION SYSTEM

### 🎨 **PDF LAYOUT SPECIFICATIONS**

#### **Quotation PDF Structure**
```python
# From PDF class in legacy
class PDF(FPDF):
    def header():     # Company logo + quotation number
    def infoSection(): # Customer details
    def generatePDF(): # Main content generation
    def footerSection(): # Terms and conditions
```

#### **PDF Content Sections**
```
1. Header Section:
   - MGA Logo (left)
   - "QUOTATION" title (center)
   - Quotation No. & Date (right)

2. Customer Information:
   - Customer Name
   - Customer Address  
   - Customer Contact

3. Item Details (for each cart item):
   - Product Image (600x400 scaled to fit)
   - Specifications Table
   - Cost Breakdown

4. Cost Summary:
   - Subtotal
   - Discount (if applied)
   - GST @18%
   - Installation (if applied)
   - Final Total

5. Footer:
   - Terms and Conditions
   - Page Numbers
```

#### **Invoice PDF Differences**
```python
# Additional elements in PDFInvoice class
- Invoice Number (auto-generated)
- HSN/SAC Codes for each item
- CGST @9% + SGST @9% breakdown
- Legal compliance formatting
- Invoice-specific terms
```

#### **Exact Image Dimensions**
```python
# From RATIO dictionary in legacy PDF class
RATIO = {
    "Sliding Window": [45, 55],
    "Sliding Door": [45, 55], 
    "Fix Louver": [40, 55],
    "Patti Louver": [40, 55],
    "Openable Window": [45, 55],
    "Sliding Folding Door": [45, 55],
    "Casement Window": [45, 55],
    "Aluminium Partition": [50, 55],
    "Toughened Partition": [50, 55],
    "Toughened Door": [40, 55],
    "Composite Panel": [50, 55],
    "Curtain Wall": [50, 55],
    "Fix Window": [50, 55],
    "Exhaust Fan Window": [50, 55]
}
```

---

## 🎯 BUSINESS RULES & LOGIC

### 💰 **PRICING LOGIC**

#### **Cost Calculation Hierarchy**
```
1. Auto-calculation from data.xlsx (if rate exists for product type + area)
2. Manual entry in cost field (if no auto-rate available)
3. Validation required before proceeding to cart
4. Per sq.ft cost * total sq.ft = total cost
5. Quantity multiplication happens at cart level
```

#### **Discount Logic**
```python
# From legacy calculateCost()
# Discount is applied BEFORE GST calculation
discounted_amount = total_cost - discount_amount
gst_amount = discounted_amount * 0.18
final_with_gst = discounted_amount + gst_amount
```

#### **Installation Charges**
```python
# Installation is added AFTER GST calculation
final_amount = gst_amount + installation_charges
```

### 🔄 **STATE MANAGEMENT**

#### **Critical Flags**
```python
# From legacy global variables
calculateFlag = False    # Set to True after successful calculation
pressedCalcFlag = False  # Set to True after Calculate button pressed
calcQuantFlag = False    # Set to True after quantity calculation
discFlag = False         # Tracks discount application
```

#### **Global Variables** (exact names from legacy)
```python
# Dimension variables
Width, Height, totSqftEntVar

# Cost variables  
costEntVar, cstAmtInr, costTotVar

# Customer variables
custNamVar, custAddVar, custConVar, address

# Calculation variables
discountEntVar, instEntVar, gstEntVar
discTotVar, instTotVar, gstTotVar

# All specification variables (trackVar, aluMatVar, etc.)
```

---

## ⚠️ CRITICAL IMPLEMENTATION NOTES

### 🚨 **MUST-PRESERVE BEHAVIORS**

1. **Exact Error Messages**: Use identical text from legacy
2. **Button Sequence**: Calculate → Add to Cart → Next workflow mandatory
3. **Validation Order**: Width → Height → Cost → Specifications
4. **File Naming**: Preserve exact customer name in filenames
5. **Currency Format**: Use babel.numbers format_currency exactly as legacy
6. **Window Positioning**: Match exact geometry calculations
7. **GST Rate**: Always 18% (9% CGST + 9% SGST)
8. **Image Paths**: Relative paths starting with "./"
9. **Excel Structure**: 59 columns in exact order
10. **PDF Layout**: Replicate exact fonts, spacing, and positioning

### 🔧 **TECHNICAL REQUIREMENTS**

#### **Dependencies** (exact versions if possible)
```python
import tkinter as tk
import pandas as pd
from fpdf import FPDF
from PIL import Image, ImageTk
from babel.numbers import format_currency
import datetime
import os
```

#### **Error Handling Patterns**
```python
# Legacy pattern for file operations
try:
    # operation
except FileNotFoundError:
    # create empty dataframe or show error
except Exception as e:
    messagebox.showerror("Error", str(e))
```

---

## 📋 TESTING & VALIDATION CHECKLIST

### ✅ **MANDATORY VALIDATION TESTS**

1. **Cost Calculations**
   - [ ] Basic: width × height × cost_per_sqft = total_cost
   - [ ] With discount: (total - discount) × 1.18 = final_with_gst
   - [ ] With installation: final_with_gst + installation = final_total
   - [ ] Currency formatting matches exactly

2. **Validation Messages** 
   - [ ] All error messages match exact text from legacy
   - [ ] Error message parent windows correct
   - [ ] Validation sequence matches legacy

3. **File Operations**
   - [ ] Excel save format matches 59-column structure
   - [ ] File naming convention: "{CustomerName}_QuatationData.xlsx"
   - [ ] PDF output identical to legacy layout

4. **Workflow Integrity**
   - [ ] Cannot proceed without Calculate button
   - [ ] Cannot add to cart without valid cost
   - [ ] Cannot go to next page without quantity calculation
   - [ ] State flags set correctly at each step

5. **UI Layout**
   - [ ] Window positioning matches legacy geometry
   - [ ] 3-frame structure in all product windows
   - [ ] Combobox options exactly match legacy lists
   - [ ] Image loading and display correct

---

## 🔍 REFERENCE SECTION

### 📚 **Legacy Code References**

- **Main Application**: Lines 4901-5832 in `MGA Window Quotaion.py`
- **Cost Calculations**: Lines 2654-2884 (CalculatePage class)
- **Cart Management**: Lines 3653-4169 (Cart class)  
- **PDF Generation**: Lines 185-1244 (PDF class)
- **Invoice Generation**: Lines 1356-1654 (PDFInvoice class)
- **Product Classes**: Lines 4170-4900 (14 product classes)
- **Global Functions**: Lines 22-184 (helper functions)

### 🎯 **Key Legacy Methods**
- `calculateCost()`: Cost calculation logic
- `toExcel()`: Cart data saving (line 1245)
- `afterCalculate()`: Post-calculation actions (line 1328)
- `addNewRowData()`: Cart item addition (line 134)
- `checkDigits()`: Input validation (line 117)
- `selector()`: Product selection (line 4901)

---

**Document Version**: 1.0  
**Last Updated**: Based on legacy code analysis  
**Verified Against**: `MGA Window Quotaion.py` (complete 5,832-line legacy file)  
**Status**: ✅ GROUND TRUTH - PRODUCTION READY 