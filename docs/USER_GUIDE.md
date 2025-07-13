# 📘 MGA Window Quotation Application - User Guide

## **Welcome to MGA Window Quotation**

This comprehensive user guide will help you effectively use the MGA Window Quotation application to create professional quotations for your window and door projects.

---

## **📋 Table of Contents**

- [Getting Started](#getting-started)
- [Application Overview](#application-overview)
- [Creating a New Quotation](#creating-a-new-quotation)
- [Product Configuration](#product-configuration)
- [Managing Your Cart](#managing-your-cart)
- [Cost Calculation](#cost-calculation)
- [Generating PDFs](#generating-pdfs)
- [Saving and Loading Quotations](#saving-and-loading-quotations)
- [Tips and Best Practices](#tips-and-best-practices)
- [Troubleshooting](#troubleshooting)

---

## **🚀 Getting Started**

### **System Requirements**
- Windows 10/11, macOS 10.15+, or Linux
- Python 3.7 or higher
- 1 GB RAM (2 GB recommended)
- 100 MB free disk space
- **Display**: Any screen resolution (responsive design automatically adapts)

### **Launching the Application**
1. Double-click the application icon or run `python __main__.py`
2. The main window will open with the MGA logo and interface
3. **Responsive Design**: The application automatically adapts to your screen size and resolution
4. You're ready to create your first quotation!

### **First Look at the Interface**
The main window contains three sections with **professional styling**:
- **Customer Details** (left top): Enter customer information
- **Window Details** (left bottom): Select product type and dimensions  
- **Company Logo** (right): MGA branding and navigation

### **Responsive Design Features**
- **Automatic Scaling**: Interface automatically adjusts to your screen size and DPI
- **Cross-Platform**: Native appearance on Windows, macOS, and Linux
- **Professional Styling**: Modern blue-gray color scheme with consistent fonts
- **Optimal Sizing**: All elements sized appropriately for your display

---

## **🏠 Application Overview**

### **Supported Product Types**
The application supports 14 different window and door types:

1. **Sliding Window** - Traditional sliding windows
2. **Sliding Door** - Sliding door systems
3. **Fix Louver** - Fixed louver windows
4. **Patti Louver** - Adjustable louver windows
5. **Openable Window** - Casement-style openable windows
6. **Sliding Folding Door** - Multi-panel folding doors
7. **Casement Window** - Hinged windows
8. **Aluminium Partition** - Interior partitions
9. **Toughened Partition** - Safety glass partitions
10. **Toughened Door** - Safety glass doors
11. **Composite Panel** - Composite panel systems
12. **Curtain Wall** - Structural glazing systems
13. **Fix Window** - Fixed glass windows
14. **Exhaust Fan Window** - Ventilation windows

### **Key Features**
- ✅ **Professional quotation generation** - High-quality PDFs with product images
- ✅ **Responsive design system** - Automatically adapts to different screen sizes
- ✅ **Professional styling** - Modern blue-gray theme with consistent appearance
- ✅ **Cross-platform compatibility** - Native look and feel on Windows, macOS, and Linux
- ✅ **Detailed product configuration** - Comprehensive specifications for all products
- ✅ **Automatic cost calculations** - Intelligent pricing with real-time updates
- ✅ **Shopping cart functionality** - Multi-item quotations with quantity management
- ✅ **PDF generation with product images** - Professional quotations with visual product representations
- ✅ **Save and load quotations** - Customer data persistence and quotation management
- ✅ **Customer database management** - Integrated customer information storage

---

## **📝 Creating a New Quotation**

### **Step 1: Enter Customer Details**

1. **Customer Name**
   - Click in the "Enter Customer Name" field
   - Type the customer's full name
   - Example: "John Smith"

2. **Customer Address**
   - Click in the "Enter Customer Address" text area
   - Enter the complete address (multiple lines supported)
   - Example:
     ```
     123 Main Street
     Apartment 4B
     New York, NY 10001
     ```

3. **Customer Contact**
   - Enter the phone number in "Enter Customer Contact No."
   - Use any format: "123-456-7890" or "1234567890"

### **Step 2: Select Product and Dimensions**

1. **Choose Window Type**
   - Click the dropdown under "Select Window Type"
   - Choose from 14 available product types
   - Example: "Sliding Window"

2. **Enter Dimensions**
   - **Width**: Enter width in feet (e.g., "10")
   - **Height**: Enter height in feet (e.g., "8")
   - The application will automatically calculate square footage

3. **Proceed to Configuration**
   - Click the green **"Next"** button
   - A new window will open for detailed product configuration

---

## **🔧 Product Configuration**

### **Configuration Window Layout**

Each product configuration window has three sections:

#### **Top Section: Customer Information**
- Displays your entered customer details (read-only)
- Confirms you're working on the correct quotation

#### **Middle Section: Dimensions and Cost**
- Shows entered width and height
- Displays calculated square footage
- **"Calculate"** button for cost computation
- Cost per square foot and total cost display

#### **Bottom Section: Product Specifications**
- Scrollable area with product-specific options
- Dropdown menus for each specification
- Product image display

### **Common Specifications**

Most products include these specifications:

1. **Track Type**
   - Options: 2 Track, 3 Track, 4 Track
   - Determines number of sliding panels

2. **Aluminium Material**
   - Regular Section, Domal Section, Premium options
   - Affects cost and appearance

3. **Glass Thickness**
   - 3.5mm, 4mm, 5mm, 8mm, 12mm
   - Choose based on safety and insulation needs

4. **Glass Type**
   - Plain, Frosted, One-way, Tinted, Bajra
   - Aesthetic and privacy considerations

5. **Hardware**
   - Lock types: Mortise, Hook, Crescent
   - Bearing types: Nylon, Steel Ball, Premium
   - Handle types: C Type, S Type

6. **Colors**
   - Frame colors: White, Brown, Black, etc.
   - Silicon colors: Clear, White, Gray, etc.

### **Product-Specific Specifications**

#### **Louver Products (Fix Louver, Patti Louver)**
- **Louver Blade Count**: 3-12 blades
- **Louver Blade Type**: Fixed or adjustable

#### **Doors (Sliding Door, Toughened Door)**
- **Door Lock**: Standard, Premium, Security
- **Bottom Rail**: Standard, Low profile

#### **Partitions (Aluminium, Toughened)**
- **Mounting Type**: Floor-to-ceiling, Partial height
- **Structural Requirements**: Load-bearing considerations

### **Configuration Steps**

1. **Review Customer Details**
   - Verify information is correct
   - Make changes in main window if needed

2. **Confirm Dimensions**
   - Check width and height values
   - Modify if necessary

3. **Select Specifications**
   - Work through each dropdown menu
   - Choose appropriate options for your project
   - Use product image as reference

4. **Calculate Cost**
   - Click the blue **"Calculate"** button
   - Review cost per square foot
   - Check total cost calculation

5. **Add to Cart**
   - Click **"Add to Cart"** to save this configuration
   - Specify quantity if needed
   - Item will be added to your quotation

---

## **🛒 Managing Your Cart**

### **Opening the Cart**
- Click the **"Cart"** button in the main window
- Cart window displays all added items

### **Cart Display**
The cart shows a table with these columns:
- **Sr.No**: Sequential item number
- **Particulars**: Product type and details
- **Width**: Product width in feet
- **Height**: Product height in feet
- **Total Sq.ft**: Calculated area
- **Cost (INR)**: Cost per unit
- **Quantity**: Number of units
- **Amount**: Total cost for this item

### **Cart Operations**

#### **Modify Quantity**
1. Click on the quantity cell for any item
2. Enter new quantity
3. Amount will automatically recalculate

#### **Remove Items**
1. Select the item row
2. Click **"Remove Selected"** button
3. Item will be deleted from cart

#### **Edit Item Specifications**
1. Double-click on an item
2. Configuration window will reopen
3. Modify specifications as needed
4. Save changes to update cart

#### **View Item Details**
- Hover over items to see full specifications
- Detailed view shows all selected options

---

## **💰 Cost Calculation**

### **Opening the Calculator**
1. From the cart window, click **"Calculate Total"**
2. Cost calculator window will open
3. Shows detailed cost breakdown

### **Cost Components**

#### **Base Costs**
- **Subtotal**: Sum of all cart items
- **Item-wise breakdown**: Individual product costs

#### **Discounts**
- **Percentage Discount**: Enter discount percentage
- **Fixed Amount Discount**: Enter specific discount amount
- **Automatic Calculation**: Discount applied to subtotal

#### **Installation Charges**
- **Labor Cost**: Installation service charges
- **Additional Services**: Any extra charges
- **Custom Amounts**: Flexible pricing options

#### **Taxes**
- **GST/Tax Rate**: Configurable tax percentage
- **CGST**: Central Goods and Services Tax
- **SGST**: State Goods and Services Tax
- **Tax Base**: Applied to post-discount amount

#### **Final Total**
- **Grand Total**: All costs combined
- **Formatted Display**: Professional currency formatting
- **Print-ready**: Formatted for quotation documents

### **Calculator Operations**

1. **Review Base Costs**
   - Verify all cart items are included
   - Check individual item calculations

2. **Apply Discounts**
   - Enter discount percentage or amount
   - See immediate calculation update

3. **Add Installation Charges**
   - Include labor and service costs
   - Account for project-specific requirements

4. **Configure Taxes**
   - Set appropriate tax rates
   - Verify tax calculations

5. **Generate Final Quote**
   - Review grand total
   - Proceed to PDF generation

---

## **📄 Generating PDFs**

### **Creating a Quotation PDF**
1. Complete cost calculation
2. Click **"Generate PDF"** or **"Create Quotation"**
3. Choose save location and filename
4. PDF will be generated automatically

### **PDF Content**

#### **Header Section**
- Company logo and branding
- Quotation number and date
- Document title

#### **Customer Information**
- Customer name and address
- Contact information
- Project details

#### **Product Details**
For each cart item:
- **Product Image**: Visual reference
- **Specifications Table**: All selected options
- **Dimensions**: Width, height, area
- **Cost Breakdown**: Unit cost and total

#### **Cost Summary**
- Itemized costs
- Discounts applied
- Tax calculations
- Grand total

#### **Footer**
- Terms and conditions
- Company contact information
- Professional disclaimers

### **PDF Features**
- **High Quality**: Professional appearance
- **Multi-page**: Automatic page breaks
- **Product Images**: Visual product references
- **Detailed Specifications**: Complete option listings
- **Proper Formatting**: Currency and number formatting

---

## **💾 Saving and Loading Quotations**

### **Saving Your Work**

#### **Automatic Saving**
- Cart data is automatically saved
- Customer details are preserved
- Specifications are stored with each item

#### **Manual Save**
1. Go to **File Menu → Save Quotation**
2. Choose location and filename
3. Excel file will be created with all data

#### **Save File Contents**
- Customer information
- All cart items with full specifications
- Cost calculations
- Date and time stamps

### **Loading Previous Quotations**

#### **Opening Saved Files**
1. Go to **File Menu → Open Quotation**
2. Browse and select Excel quotation file
3. All data will be loaded automatically

#### **What Gets Loaded**
- Customer details restored
- Cart items recreated
- Specifications preserved
- Ready for modifications

#### **File Compatibility**
- Excel format (.xlsx)
- Cross-platform compatibility
- Version-independent loading

---

## **💡 Tips and Best Practices**

### **Efficient Workflow**

1. **Prepare Customer Information**
   - Have complete customer details ready
   - Include accurate contact information
   - Verify spelling and addresses

2. **Measure Accurately**
   - Use precise dimensions
   - Consider installation clearances
   - Account for structural limitations

3. **Understand Product Options**
   - Review specification options
   - Consider customer requirements
   - Balance cost and features

4. **Use Cart Effectively**
   - Group similar items
   - Verify quantities carefully
   - Review specifications before finalizing

5. **Professional Quotations**
   - Include detailed specifications
   - Provide clear cost breakdowns
   - Add professional notes if needed

### **Quality Assurance**

1. **Double-Check Calculations**
   - Verify dimensions and areas
   - Confirm cost calculations
   - Review discount applications

2. **Specification Accuracy**
   - Ensure all options are selected
   - Match customer requirements
   - Consider installation constraints

3. **PDF Review**
   - Check product images
   - Verify specification tables
   - Confirm cost summaries

### **Data Management**

1. **Regular Backups**
   - Save quotations frequently
   - Keep backup copies
   - Use descriptive filenames

2. **Organization**
   - Create customer-specific folders
   - Use consistent naming conventions
   - Archive completed projects

3. **Version Control**
   - Save quotation revisions
   - Track changes and updates
   - Maintain audit trail

---

## **🔧 Troubleshooting**

### **Common Issues and Solutions**

#### **Application Won't Start**
**Problem**: Application fails to launch
**Solutions**:
- Check Python installation (3.7+)
- Verify required packages are installed
- Check file permissions
- Run as administrator if needed

#### **Customer Details Not Saving**
**Problem**: Entered information disappears
**Solutions**:
- Ensure all required fields are filled
- Check for special characters
- Verify system permissions
- Restart application if needed

#### **Product Configuration Issues**
**Problem**: Specifications don't save or calculate
**Solutions**:
- Complete all required specification fields
- Verify dimensions are numeric
- Check dropdown selections are valid
- Ensure "Calculate" button is clicked

#### **Cart Problems**
**Problem**: Items not appearing in cart
**Solutions**:
- Verify "Add to Cart" was clicked
- Check quantity is greater than zero
- Ensure cost calculation completed
- Restart product configuration if needed

#### **PDF Generation Fails**
**Problem**: PDF creation errors
**Solutions**:
- Check save location permissions
- Verify product images are available
- Ensure customer details are complete
- Try different filename or location

#### **File Loading Issues**
**Problem**: Cannot open saved quotations
**Solutions**:
- Verify file format is Excel (.xlsx)
- Check file isn't corrupted
- Ensure file permissions allow reading
- Try opening in Excel first to verify

### **Performance Optimization**

#### **Slow Performance**
**Solutions**:
- Close unused application windows
- Restart application periodically
- Ensure adequate system memory
- Keep data files reasonably sized

#### **Memory Issues**
**Solutions**:
- Limit cart size for very large quotations
- Save and restart for complex projects
- Close unnecessary programs
- Increase system virtual memory

### **Data Recovery**

#### **Lost Quotations**
**Solutions**:
- Check recent files in File menu
- Look for auto-saved backup files
- Search for .xlsx files by customer name
- Recreate from PDF if available

#### **Corrupted Files**
**Solutions**:
- Try opening in Excel directly
- Use Excel repair functionality
- Restore from backup if available
- Recreate quotation from scratch

---

## **📞 Support and Contact**

### **Getting Help**
- **Documentation**: Refer to this user guide
- **Developer Guide**: For technical issues
- **API Reference**: For integration questions

### **Best Practices for Support**
1. **Describe the Issue Clearly**
   - What were you trying to do?
   - What happened instead?
   - Any error messages?

2. **Provide Context**
   - Operating system and version
   - Application version
   - Steps to reproduce the issue

3. **Include Files if Relevant**
   - Sample quotation files
   - Screenshots of errors
   - Log files if available

---

## **🎓 Conclusion**

The MGA Window Quotation application is designed to streamline your quotation process while maintaining professional standards. By following this guide, you'll be able to:

- Create accurate, professional quotations
- Manage complex product configurations
- Generate high-quality PDF documents
- Maintain organized customer records
- Operate efficiently and effectively

Remember to save your work regularly and keep backup copies of important quotations. The application is designed to be intuitive, but don't hesitate to refer back to this guide whenever needed.

**Happy Quoting!** 🎉 