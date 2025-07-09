# 🔧 MGA Window Quotation Application - Troubleshooting Guide

## **Overview**

This troubleshooting guide provides solutions to common issues, error messages, and performance problems you may encounter while using the MGA Window Quotation application.

---

## **📋 Table of Contents**

- [Quick Diagnostics](#quick-diagnostics)
- [Application Startup Issues](#application-startup-issues)
- [UI and Interface Problems](#ui-and-interface-problems)
- [Data and Cart Issues](#data-and-cart-issues)
- [PDF Generation Problems](#pdf-generation-problems)
- [Excel File Issues](#excel-file-issues)
- [Performance Problems](#performance-problems)
- [Error Messages Reference](#error-messages-reference)
- [Recovery Procedures](#recovery-procedures)

---

## **🔍 Quick Diagnostics**

### **System Health Check**
```bash
# Check Python installation
python --version
# Expected: Python 3.7+ (3.9+ recommended)

# Check required packages
python -c "import pandas, fpdf, PIL, babel; print('All packages OK')"

# Check application files
python -c "
import os
files = ['__main__.py', 'data_manager.py', 'global_state.py', 'pdf_generator.py']
for f in files:
    print(f'{"✓" if os.path.exists(f) else "✗"} {f}')
"

# Run quick test
python quick_test.py
```

### **Common Quick Fixes**
1. **Restart the Application** - Solves 60% of issues
2. **Clear Temporary Data** - Delete any temp files
3. **Check File Permissions** - Ensure read/write access
4. **Update Dependencies** - `pip install --upgrade -r requirements.txt`
5. **Reboot System** - For persistent system-level issues

---

## **🚀 Application Startup Issues**

### **Application Won't Start**

#### **Problem: "Python is not recognized as internal or external command"**
**Symptoms:**
- Command prompt shows python error
- Application won't launch from command line

**Solutions:**
```bash
# Windows: Add Python to PATH
1. Open System Properties → Environment Variables
2. Add Python installation directory to PATH
3. Restart command prompt

# Alternative: Use full path
C:\Python39\python.exe __main__.py

# macOS/Linux: Update shell profile
echo 'export PATH="/usr/local/bin/python3:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

#### **Problem: "No module named 'tkinter'"**
**Symptoms:**
- Error during application startup
- tkinter import fails

**Solutions:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter

# macOS
brew install python-tk

# Windows
# Reinstall Python with tkinter option checked
```

#### **Problem: Application Crashes on Startup**
**Symptoms:**
- Window appears briefly then disappears
- No error message visible

**Solutions:**
```bash
# Run from command line to see errors
python __main__.py

# Check for missing dependencies
pip install -r requirements.txt

# Run in debug mode
python -c "
import logging
logging.basicConfig(level=logging.DEBUG)
exec(open('__main__.py').read())
"
```

### **Import Errors**

#### **Problem: "ModuleNotFoundError"**
**Symptoms:**
- Cannot import pandas, fpdf, or other modules
- Application fails to start

**Solutions:**
```bash
# Check virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# Check Python path
python -c "import sys; print('\n'.join(sys.path))"
```

---

## **🎨 UI and Interface Problems**

### **Window Display Issues**

#### **Problem: Main Window Doesn't Appear**
**Solutions:**
```python
# Check if window is minimized or off-screen
# Try Alt+Tab (Windows) or Cmd+Tab (Mac)

# Reset window position (add to __main__.py)
root.geometry("1200x800+100+100")  # width x height + x_offset + y_offset
```

#### **Problem: UI Elements Overlapping or Missing**
**Solutions:**
```python
# Check screen resolution
# Minimum supported: 1024x768

# Update display scaling
# Windows: Settings → Display → Scale 100%
# macOS: System Preferences → Displays → Resolution

# Force UI refresh
self.parent.update_idletasks()
```

#### **Problem: Dropdown Lists Not Working**
**Symptoms:**
- Comboboxes don't show options
- Cannot select values

**Solutions:**
```python
# Verify global state is initialized
from global_state import get_global_state
gs = get_global_state()
print(len(gs.track_options))  # Should show available options

# Reset global state if needed
gs.reset_specification_vars()
```

### **Input Validation Issues**

#### **Problem: Cannot Enter Dimensions**
**Symptoms:**
- Width/Height fields reject input
- Error messages about invalid characters

**Solutions:**
```python
# Check digit validation
# Only numbers and decimal points allowed
# Valid: 10, 10.5, 12.75
# Invalid: 10', 10", 10 ft

# Clear and re-enter values
# Use only numeric characters
```

#### **Problem: Customer Details Not Saving**
**Solutions:**
```python
# Check for special characters
# Avoid: < > & " ' in names/addresses

# Verify field lengths
# Name: < 100 characters
# Address: < 500 characters
# Contact: < 20 characters

# Test with simple data first
customer_info = {
    'custNamVar': 'Test Customer',
    'custAddVar': '123 Test Street',
    'custConVar': '1234567890'
}
```

---

## **📊 Data and Cart Issues**

### **Cart Problems**

#### **Problem: Items Not Added to Cart**
**Symptoms:**
- "Add to Cart" button doesn't work
- Cart remains empty after adding items

**Solutions:**
```python
# Ensure cost calculation completed
# Click "Calculate" button before adding to cart

# Check required fields
# All specifications must be selected
# Width and height must be provided

# Verify data manager instance
from data_manager import DataManager
dm = DataManager()
print(f"Cart items: {len(dm.get_cart_data())}")
```

#### **Problem: Cart Shows Incorrect Amounts**
**Symptoms:**
- Total amounts don't match expected values
- Quantity changes don't update amounts

**Solutions:**
```python
# Force cart recalculation
dm = DataManager()
dm.recalculate_cart_totals()

# Check for floating point precision issues
# Ensure costs are rounded to 2 decimal places

# Verify rate lookup
# Check Data/data.xlsx for correct pricing
```

#### **Problem: Cannot Remove Items from Cart**
**Symptoms:**
- Remove button doesn't work
- Items persist after removal attempts

**Solutions:**
```python
# Select item row before clicking remove
# Ensure only one item is selected

# Clear entire cart if needed
dm = DataManager()
dm.cart_df = dm.cart_df.iloc[0:0]  # Clear DataFrame
```

### **Customer Data Issues**

#### **Problem: Customer Details Disappear**
**Solutions:**
```python
# Check global state persistence
gs = get_global_state()
print(f"Customer: {gs.custNamVar.get()}")

# Re-enter customer details if lost
# Ensure proper binding to UI elements

# Save frequently used customer data
dm.set_customer_details({
    'custNamVar': 'Regular Customer',
    'custAddVar': 'Saved Address',
    'custConVar': 'Saved Contact'
})
```

---

## **📄 PDF Generation Problems**

### **PDF Creation Failures**

#### **Problem: "No such file or directory" Error**
**Symptoms:**
- PDF generation fails with file path error
- Cannot save to selected location

**Solutions:**
```bash
# Check save location permissions
ls -la /path/to/save/location  # Linux/Mac
dir "C:\path\to\save\location"  # Windows

# Create directory if it doesn't exist
mkdir -p ~/Documents/MGA_Quotations

# Use absolute paths
/home/user/Documents/quotation.pdf  # Linux
C:\Users\Username\Documents\quotation.pdf  # Windows
```

#### **Problem: Images Missing in PDF**
**Symptoms:**
- PDF generates but product images don't appear
- Blank spaces where images should be

**Solutions:**
```bash
# Check Images directory
ls Images/*.png  # Should list all product images

# Verify image files aren't corrupted
python -c "
from PIL import Image
try:
    img = Image.open('Images/Sliding Window.png')
    print('Image OK')
except Exception as e:
    print(f'Image error: {e}')
"

# Re-download missing images if needed
```

#### **Problem: PDF Formatting Issues**
**Symptoms:**
- Text overlapping or cut off
- Poor layout or alignment

**Solutions:**
```python
# Check FPDF version
pip install fpdf==2.5.7  # Use tested version

# Verify customer details length
# Long addresses may cause formatting issues
# Break long text into multiple lines

# Test with minimal data first
```

### **PDF Content Problems**

#### **Problem: Incorrect Specifications in PDF**
**Solutions:**
```python
# Verify all specifications are selected
# Check dropdown values before generating PDF

# Review specification mapping
from pdf_generator import VAR_NAME
print(VAR_NAME)  # Shows variable to display name mapping

# Regenerate with corrected specifications
```

---

## **📊 Excel File Issues**

### **File Access Problems**

#### **Problem: "Permission denied" When Saving**
**Solutions:**
```bash
# Close Excel if file is open
# Check file permissions
chmod 644 Data/*.xlsx  # Linux/Mac

# Save to different location
# Use Documents folder instead of application directory

# Run as administrator if needed (Windows)
```

#### **Problem: "File is corrupted" Error**
**Solutions:**
```bash
# Backup current file
cp Data/data.xlsx Data/data_backup.xlsx

# Try opening in Excel to verify
# If corrupted, restore from backup

# Recreate file if necessary
python -c "
import pandas as pd
df = pd.DataFrame({'Product': ['Test'], 'Rate': [100]})
df.to_excel('Data/data_new.xlsx', index=False)
"
```

### **Data Loading Issues**

#### **Problem: Quotation Won't Load**
**Symptoms:**
- Error when opening saved quotations
- Data doesn't populate correctly

**Solutions:**
```python
# Check Excel file format
# Must be .xlsx format

# Verify file structure
import pandas as pd
try:
    df = pd.read_excel('quotation_file.xlsx')
    print(df.columns.tolist())
    print(df.head())
except Exception as e:
    print(f"File error: {e}")

# Try loading manually:
from data_manager import DataManager
dm = DataManager()
success = dm.load_quotation_from_excel('file.xlsx')
print(f"Load success: {success}")
```

---

## **⚡ Performance Problems**

### **Slow Performance**

#### **Problem: Application Running Slowly**
**Symptoms:**
- Long delays when clicking buttons
- UI freezing or not responding

**Solutions:**
```bash
# Check system resources
# Task Manager (Windows) or Activity Monitor (Mac)

# Close unnecessary applications
# Ensure 4GB+ RAM available

# Restart application periodically
# Clear temporary data

# Check hard disk space
# Ensure 1GB+ free space
```

#### **Problem: PDF Generation Takes Too Long**
**Solutions:**
```python
# Limit cart size for large quotations
# Process in smaller batches if needed

# Check image file sizes
# Large images slow down PDF generation

# Use SSD instead of HDD if possible
```

### **Memory Issues**

#### **Problem: Out of Memory Errors**
**Solutions:**
```bash
# Increase virtual memory (Windows)
# System Properties → Advanced → Performance → Settings

# Close other applications
# Restart application to free memory

# Split large quotations into smaller ones
```

---

## **⚠️ Error Messages Reference**

### **Common Error Messages**

#### **"ValueError: could not convert string to float"**
**Cause:** Invalid numeric input in dimensions or cost fields
**Solution:** Enter only numbers (10, 10.5) without units or symbols

#### **"FileNotFoundError: [Errno 2] No such file or directory"**
**Cause:** Missing file or incorrect path
**Solution:** Verify file exists and path is correct

#### **"PermissionError: [Errno 13] Permission denied"**
**Cause:** Insufficient file permissions
**Solution:** Run as administrator or change file permissions

#### **"AttributeError: 'NoneType' object has no attribute"**
**Cause:** Uninitialized object or missing data
**Solution:** Ensure proper initialization and data validation

#### **"ImportError: No module named 'module_name'"**
**Cause:** Missing dependency
**Solution:** Install required package with pip

### **Critical Errors**

#### **"Segmentation fault" or System Crash**
**Immediate Actions:**
1. Save any unsaved work immediately
2. Restart the application
3. Check system logs for hardware issues
4. Run memory diagnostics

#### **Data Corruption Warning**
**If you see data inconsistencies:**
1. Stop using the application immediately
2. Backup current data files
3. Restore from known good backup
4. Check file integrity

---

## **🔄 Recovery Procedures**

### **Data Recovery**

#### **Lost Quotation Data**
```bash
# Check for autosave files
ls Data/*_autosave.xlsx

# Search for recent Excel files
find . -name "*.xlsx" -mtime -7  # Files modified in last 7 days

# Recover from PDF if data lost
# Use PDF as reference to recreate quotation
```

#### **Corrupted Application Files**
```bash
# Restore from backup
git checkout HEAD -- .  # If using git

# Reinstall application
rm -rf venv/
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **System Recovery**

#### **Reset Application State**
```python
# Clear all global state
from global_state import get_global_state
gs = get_global_state()
gs.reset_specification_vars()

# Clear cart data
from data_manager import DataManager
dm = DataManager()
dm.cart_df = dm.cart_df.iloc[0:0]

# Reset customer details
gs.custNamVar.set("")
gs.custAddVar.set("")
gs.custConVar.set("")
```

#### **Complete Application Reset**
```bash
# Backup important data
cp -r Data/ Data_backup/

# Remove application data
rm -rf __pycache__/
rm -rf venv/

# Reinstall fresh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Restore data
cp -r Data_backup/* Data/
```

---

## **🔧 Advanced Troubleshooting**

### **Debug Mode**

#### **Enable Detailed Logging**
```python
# Add to __main__.py
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

# Run application and check debug.log for details
```

#### **Interactive Debugging**
```python
# Add breakpoints for investigation
import pdb; pdb.set_trace()

# Or use IDE debugger
# Set breakpoints in problem areas
# Step through code execution
```

### **System Diagnostics**

#### **Check System Compatibility**
```python
# Platform information
import platform
print(f"OS: {platform.system()} {platform.release()}")
print(f"Python: {platform.python_version()}")
print(f"Architecture: {platform.architecture()}")

# Package versions
import pkg_resources
packages = ['pandas', 'fpdf', 'Pillow', 'babel']
for pkg in packages:
    try:
        version = pkg_resources.get_distribution(pkg).version
        print(f"{pkg}: {version}")
    except pkg_resources.DistributionNotFound:
        print(f"{pkg}: NOT INSTALLED")
```

---

## **📞 Getting Additional Help**

### **Self-Help Resources**
1. **User Guide** - `docs/USER_GUIDE.md`
2. **Developer Guide** - `docs/DEVELOPER_GUIDE.md`
3. **API Reference** - `docs/API_REFERENCE.md`
4. **Installation Guide** - `docs/INSTALLATION_GUIDE.md`

### **Diagnostic Information to Collect**
When seeking help, provide:
1. **Operating System** and version
2. **Python version** (`python --version`)
3. **Error message** (exact text)
4. **Steps to reproduce** the issue
5. **Log files** if available
6. **Screenshots** of error dialogs

### **Emergency Contacts**
- **Technical Support**: For critical production issues
- **User Community**: For general questions and tips
- **Documentation**: For feature clarification

---

## **✅ Prevention Tips**

### **Regular Maintenance**
1. **Backup Data Weekly** - Save Data/ folder regularly
2. **Update Dependencies Monthly** - Check for package updates
3. **Clear Temporary Files** - Remove old quotation files
4. **Monitor Disk Space** - Maintain 1GB+ free space
5. **Restart Application Daily** - Fresh start prevents memory issues

### **Best Practices**
1. **Save Work Frequently** - Don't lose progress
2. **Use Descriptive Filenames** - Easy to find quotations
3. **Test Changes** - Verify everything works after modifications
4. **Keep Backups Current** - Multiple backup copies
5. **Document Issues** - Note problems and solutions for future reference

---

This troubleshooting guide covers the most common issues encountered with the MGA Window Quotation application. For issues not covered here, refer to the other documentation files or contact technical support with detailed diagnostic information. 