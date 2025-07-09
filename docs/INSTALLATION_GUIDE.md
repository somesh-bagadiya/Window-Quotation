# 📦 MGA Window Quotation Application - Installation & Deployment Guide

## **Overview**

This guide provides step-by-step instructions for installing and deploying the MGA Window Quotation application across different environments and operating systems.

---

## **📋 Table of Contents**

- [System Requirements](#system-requirements)
- [Quick Start Installation](#quick-start-installation)
- [Development Environment Setup](#development-environment-setup)
- [Production Deployment](#production-deployment)
- [Creating Executable](#creating-executable)
- [Platform-Specific Instructions](#platform-specific-instructions)
- [Troubleshooting Installation](#troubleshooting-installation)

---

## **⚙️ System Requirements**

### **Minimum Requirements**
- **Operating System**: Windows 10/11, macOS 10.15+, Ubuntu 18.04+
- **Python**: 3.7 or higher (3.9+ recommended)
- **Memory**: 2GB RAM (4GB recommended)
- **Storage**: 500MB free space (1GB recommended)
- **Display**: 1024x768 resolution minimum

### **Recommended Requirements**
- **Python**: 3.9 or 3.10
- **Memory**: 8GB RAM
- **Storage**: 2GB free space
- **Display**: 1920x1080 resolution

### **Dependencies**
```txt
pandas>=1.3.0,<2.0.0
fpdf>=2.5.0,<3.0.0
Pillow>=8.0.0,<10.0.0
babel>=2.9.0,<3.0.0
openpyxl>=3.0.0,<4.0.0
```

---

## **🚀 Quick Start Installation**

### **Option 1: Pre-built Executable (Recommended for End Users)**

1. **Download the Application**
   ```
   Download: MGA_Window_Quotation_Installer.exe
   Size: ~50MB
   ```

2. **Run the Installer**
   - Double-click the installer file
   - Follow the installation wizard
   - Choose installation directory (default: `C:\Program Files\MGA Windows\`)
   - Create desktop shortcut (recommended)

3. **Launch the Application**
   - Double-click desktop shortcut, or
   - Start Menu → MGA Windows → MGA Window Quotation

### **Option 2: Python Source (For Developers)**

1. **Download Source Code**
   ```bash
   git clone https://github.com/mga-windows/window-quotation.git
   cd window-quotation
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application**
   ```bash
   python __main__.py
   ```

---

## **🛠️ Development Environment Setup**

### **Step 1: Python Installation**

#### **Windows**
```bash
# Download from python.org or use chocolatey
choco install python --version=3.9.13

# Verify installation
python --version
pip --version
```

#### **macOS**
```bash
# Using Homebrew
brew install python@3.9

# Or download from python.org
# Verify installation
python3 --version
pip3 --version
```

#### **Linux (Ubuntu/Debian)**
```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3.9 python3.9-venv python3-pip

# Verify installation
python3 --version
pip3 --version
```

### **Step 2: Create Virtual Environment**

```bash
# Create virtual environment
python -m venv mga_env

# Activate virtual environment
# Windows:
mga_env\Scripts\activate

# macOS/Linux:
source mga_env/bin/activate

# Verify activation (should show virtual env in prompt)
which python  # Should point to virtual environment
```

### **Step 3: Clone Repository**

```bash
# Clone the repository
git clone https://github.com/mga-windows/window-quotation.git
cd window-quotation

# Or download and extract ZIP file
```

### **Step 4: Install Dependencies**

```bash
# Install required packages
pip install -r requirements.txt

# Install development dependencies (optional)
pip install -r requirements-dev.txt

# Verify installation
pip list
```

### **Step 5: Verify Installation**

```bash
# Test import of core modules
python -c "import tkinter; print('tkinter: OK')"
python -c "import pandas; print('pandas: OK')"
python -c "import fpdf; print('fpdf: OK')"
python -c "from PIL import Image; print('Pillow: OK')"

# Run quick test
python quick_test.py
```

### **Step 6: Run Application**

```bash
# Launch the application
python __main__.py

# Should open the MGA Window Quotation main window
```

---

## **🏭 Production Deployment**

### **Server Environment Setup**

#### **System Preparation**
```bash
# Create application user (Linux)
sudo useradd -m -s /bin/bash mga-app
sudo usermod -aG sudo mga-app

# Create application directory
sudo mkdir -p /opt/mga-window-quotation
sudo chown mga-app:mga-app /opt/mga-window-quotation
```

#### **Python Environment**
```bash
# Switch to application user
sudo su - mga-app

# Navigate to application directory
cd /opt/mga-window-quotation

# Create production virtual environment
python3 -m venv production_env
source production_env/bin/activate

# Upgrade pip
pip install --upgrade pip
```

### **Application Deployment**

#### **Method 1: Git Deployment**
```bash
# Clone application
git clone https://github.com/mga-windows/window-quotation.git .

# Install dependencies
pip install -r requirements.txt

# Set file permissions
chmod +x __main__.py
chmod -R 755 ui/
chmod -R 755 utils/
chmod -R 644 Data/
chmod -R 644 Images/
```

#### **Method 2: Archive Deployment**
```bash
# Upload application archive
scp mga-window-quotation.tar.gz mga-app@server:/opt/mga-window-quotation/

# Extract archive
tar -xzf mga-window-quotation.tar.gz
rm mga-window-quotation.tar.gz

# Install dependencies
pip install -r requirements.txt
```

### **Configuration**

#### **Environment Variables**
```bash
# Create environment file
cat > .env << EOF
MGA_DATA_PATH=/opt/mga-window-quotation/Data/
MGA_IMAGES_PATH=/opt/mga-window-quotation/Images/
MGA_LOG_LEVEL=INFO
MGA_LOG_FILE=/var/log/mga-window-quotation.log
EOF
```

#### **Logging Setup**
```bash
# Create log directory
sudo mkdir -p /var/log/
sudo touch /var/log/mga-window-quotation.log
sudo chown mga-app:mga-app /var/log/mga-window-quotation.log
```

### **Service Configuration (Linux)**

#### **Systemd Service File**
```bash
# Create service file
sudo tee /etc/systemd/system/mga-window-quotation.service << EOF
[Unit]
Description=MGA Window Quotation Application
After=network.target

[Service]
Type=simple
User=mga-app
WorkingDirectory=/opt/mga-window-quotation
Environment=PATH=/opt/mga-window-quotation/production_env/bin
Environment=DISPLAY=:0
ExecStart=/opt/mga-window-quotation/production_env/bin/python __main__.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable mga-window-quotation
sudo systemctl start mga-window-quotation

# Check status
sudo systemctl status mga-window-quotation
```

---

## **📱 Creating Executable**

### **Using PyInstaller**

#### **Step 1: Install PyInstaller**
```bash
# Activate virtual environment
source mga_env/bin/activate  # Linux/Mac
# or
mga_env\Scripts\activate     # Windows

# Install PyInstaller
pip install pyinstaller
```

#### **Step 2: Create Executable**
```bash
# Basic executable creation
pyinstaller --onefile --windowed __main__.py

# Advanced executable with resources
pyinstaller \
    --onefile \
    --windowed \
    --icon=Images/MGA_Logo.ico \
    --add-data "Images;Images" \
    --add-data "Data;Data" \
    --name "MGA_Window_Quotation" \
    __main__.py
```

#### **Step 3: Custom Spec File**
```python
# MGA_Window_Quotation.spec
import os

# Analysis
a = Analysis(
    ['__main__.py'],
    pathex=[os.getcwd()],
    binaries=[],
    datas=[
        ('Images', 'Images'),
        ('Data', 'Data'),
        ('ui', 'ui'),
        ('utils', 'utils'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'pandas',
        'fpdf',
        'PIL',
        'babel.numbers',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        'test',
        'tests',
        'pytest',
        'matplotlib',
        'numpy.distutils',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# Python bytecode
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# Executable
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MGA_Window_Quotation',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='Images/MGA_Logo.ico'
)
```

#### **Step 4: Build Executable**
```bash
# Build using spec file
pyinstaller MGA_Window_Quotation.spec

# Output will be in dist/ directory
ls dist/
# MGA_Window_Quotation.exe (Windows)
# MGA_Window_Quotation (Linux/Mac)
```

### **Creating Installer Package**

#### **Windows Installer (NSIS)**
```nsis
; installer.nsi
!define APPNAME "MGA Window Quotation"
!define COMPANYNAME "MGA Windows"
!define DESCRIPTION "Professional Window Quotation System"
!define VERSIONMAJOR 1
!define VERSIONMINOR 0
!define VERSIONBUILD 0

Name "${APPNAME}"
InstallDir "$PROGRAMFILES64\${COMPANYNAME}\${APPNAME}"
LicenseData "LICENSE.txt"
RequestExecutionLevel admin
OutFile "MGA_Window_Quotation_Installer.exe"

Page license
Page directory
Page instfiles

Section "Install"
    SetOutPath $INSTDIR
    
    ; Main executable
    File "dist\MGA_Window_Quotation.exe"
    
    ; Create uninstaller
    WriteUninstaller "$INSTDIR\uninstall.exe"
    
    ; Start menu shortcuts
    CreateDirectory "$SMPROGRAMS\${COMPANYNAME}"
    CreateShortCut "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk" "$INSTDIR\MGA_Window_Quotation.exe"
    CreateShortCut "$SMPROGRAMS\${COMPANYNAME}\Uninstall.lnk" "$INSTDIR\uninstall.exe"
    
    ; Desktop shortcut
    CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\MGA_Window_Quotation.exe"
    
    ; Registry entries
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayName" "${APPNAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "UninstallString" "$INSTDIR\uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "Publisher" "${COMPANYNAME}"
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\MGA_Window_Quotation.exe"
    Delete "$INSTDIR\uninstall.exe"
    RMDir "$INSTDIR"
    
    Delete "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk"
    Delete "$SMPROGRAMS\${COMPANYNAME}\Uninstall.lnk"
    RMDir "$SMPROGRAMS\${COMPANYNAME}"
    Delete "$DESKTOP\${APPNAME}.lnk"
    
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"
SectionEnd
```

#### **Build Installer**
```bash
# Install NSIS (Windows)
# Download from: https://nsis.sourceforge.io/

# Compile installer
makensis installer.nsi

# Output: MGA_Window_Quotation_Installer.exe
```

---

## **💻 Platform-Specific Instructions**

### **Windows Deployment**

#### **Prerequisites**
```bash
# Install Visual C++ Redistributable (if needed)
# Download from Microsoft

# Install Python from python.org
# Ensure "Add Python to PATH" is checked
```

#### **Installation Steps**
```cmd
# Open Command Prompt as Administrator
# Navigate to application directory
cd C:\MGA-Window-Quotation

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create batch file for easy launching
echo @echo off > launch.bat
echo cd /d "%~dp0" >> launch.bat
echo venv\Scripts\activate >> launch.bat
echo python __main__.py >> launch.bat
echo pause >> launch.bat
```

#### **Windows Service Installation**
```bash
# Install service wrapper
pip install pywin32

# Create service script (mga_service.py)
import win32serviceutil
import win32service
import win32event
import subprocess
import os

class MGAWindowQuotationService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MGAWindowQuotation"
    _svc_display_name_ = "MGA Window Quotation Service"
    
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        
    def SvcDoRun(self):
        os.chdir(r"C:\MGA-Window-Quotation")
        subprocess.call([r"C:\MGA-Window-Quotation\venv\Scripts\python.exe", "__main__.py"])

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(MGAWindowQuotationService)

# Install service
python mga_service.py install
python mga_service.py start
```

### **macOS Deployment**

#### **Prerequisites**
```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.9
brew install python-tk
```

#### **Application Bundle Creation**
```bash
# Install py2app
pip install py2app

# Create setup.py for app bundle
cat > setup.py << EOF
from setuptools import setup

APP = ['__main__.py']
DATA_FILES = [
    ('Images', ['Images']),
    ('Data', ['Data']),
    ('ui', ['ui']),
    ('utils', ['utils'])
]
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'MGA Window Quotation',
        'CFBundleDisplayName': 'MGA Window Quotation',
        'CFBundleGetInfoString': "Professional Window Quotation System",
        'CFBundleIdentifier': 'com.mga.window-quotation',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHumanReadableCopyright': 'Copyright © 2024 MGA Windows. All rights reserved.'
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
EOF

# Build app bundle
python setup.py py2app

# Result: dist/MGA Window Quotation.app
```

### **Linux Deployment**

#### **Ubuntu/Debian**
```bash
# Install system dependencies
sudo apt update
sudo apt install python3.9 python3.9-venv python3-pip
sudo apt install python3-tk
sudo apt install build-essential

# Install application
git clone https://github.com/mga-windows/window-quotation.git
cd window-quotation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create desktop entry
cat > ~/.local/share/applications/mga-window-quotation.desktop << EOF
[Desktop Entry]
Version=1.0
Name=MGA Window Quotation
Comment=Professional Window Quotation System
Exec=/path/to/window-quotation/venv/bin/python /path/to/window-quotation/__main__.py
Icon=/path/to/window-quotation/Images/MGA_Logo.ico
Terminal=false
Type=Application
Categories=Office;Business;
EOF

# Update desktop database
update-desktop-database ~/.local/share/applications/
```

#### **CentOS/RHEL**
```bash
# Install EPEL repository
sudo yum install epel-release

# Install Python and dependencies
sudo yum install python39 python39-pip python39-tkinter
sudo yum groupinstall "Development Tools"

# Follow Ubuntu installation steps
```

---

## **🔧 Troubleshooting Installation**

### **Common Issues**

#### **Python Not Found**
```bash
# Windows
# Add Python to PATH in System Environment Variables
# Or reinstall Python with "Add to PATH" option

# macOS/Linux
# Install Python through package manager
# Update .bashrc or .zshrc with Python path
export PATH="/usr/local/bin/python3:$PATH"
```

#### **Permission Denied**
```bash
# Linux/macOS
sudo chown -R $USER:$USER /path/to/application
chmod +x __main__.py

# Windows
# Run Command Prompt as Administrator
# Or check file permissions in Properties
```

#### **Module Import Errors**
```bash
# Verify virtual environment is activated
which python  # Should point to virtual environment

# Reinstall dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# Check for conflicting packages
pip list --outdated
```

#### **tkinter Issues**
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# CentOS/RHEL
sudo yum install tkinter

# macOS
brew install python-tk

# Windows
# tkinter included with Python - reinstall Python if missing
```

#### **Excel File Errors**
```bash
# Install openpyxl
pip install openpyxl

# Check file permissions
chmod 644 Data/*.xlsx

# Verify Excel files aren't corrupted
python -c "import pandas as pd; print(pd.read_excel('Data/data.xlsx').head())"
```

#### **PDF Generation Issues**
```bash
# Install/update fpdf
pip install --upgrade fpdf2

# Check PIL/Pillow installation
pip install --upgrade Pillow

# Verify image files exist
ls Images/*.png
```

### **Performance Issues**

#### **Slow Startup**
```bash
# Check available memory
free -h  # Linux
vm_stat  # macOS

# Close unnecessary applications
# Increase virtual memory if needed
```

#### **UI Responsiveness**
```bash
# Update graphics drivers
# Reduce screen resolution if needed
# Close other GUI applications
```

### **Logging and Debugging**

#### **Enable Debug Logging**
```python
# Add to __main__.py
import logging
logging.basicConfig(level=logging.DEBUG, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
```

#### **Check System Resources**
```bash
# Monitor during runtime
htop      # Linux
Activity Monitor  # macOS
Task Manager     # Windows
```

---

## **✅ Installation Verification**

### **Basic Functionality Test**
```bash
# Launch application
python __main__.py

# Verify main window opens
# Test customer details entry
# Test product selection
# Test cart functionality
# Test PDF generation
```

### **Automated Testing**
```bash
# Run test suite
python -m pytest tests/

# Quick functionality test
python quick_test.py

# Performance benchmark
python performance_test.py
```

### **File Integrity Check**
```bash
# Verify all required files exist
python -c "
import os
required_files = ['__main__.py', 'data_manager.py', 'global_state.py', 'pdf_generator.py']
for file in required_files:
    if os.path.exists(file):
        print(f'✓ {file}')
    else:
        print(f'✗ {file} MISSING')
"
```

---

## **📞 Support**

### **Installation Support**
- Check troubleshooting section above
- Verify system requirements
- Review platform-specific instructions
- Check application logs for errors

### **Additional Resources**
- User Guide: `docs/USER_GUIDE.md`
- Developer Guide: `docs/DEVELOPER_GUIDE.md`
- API Reference: `docs/API_REFERENCE.md`

---

This installation guide provides comprehensive instructions for deploying the MGA Window Quotation application across different environments. Follow the appropriate section for your target platform and use case. 