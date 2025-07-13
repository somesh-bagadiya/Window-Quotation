# 🔧 MGA Window Quotation Application - Developer Guide

## **Overview**

This developer guide provides comprehensive technical documentation for maintaining, enhancing, and extending the MGA Window Quotation application. This guide is essential for developers working on the codebase, whether for bug fixes, feature enhancements, or major upgrades.

---

## **📋 Table of Contents**

- [Development Environment Setup](#development-environment-setup)
- [Codebase Structure](#codebase-structure)
- [Core Components Deep Dive](#core-components-deep-dive)
- [Development Workflow](#development-workflow)
- [Testing Framework](#testing-framework)
- [Adding New Features](#adding-new-features)
- [Debugging and Troubleshooting](#debugging-and-troubleshooting)
- [Performance Optimization](#performance-optimization)
- [Deployment Guidelines](#deployment-guidelines)
- [Maintenance Procedures](#maintenance-procedures)

---

## **🚀 Development Environment Setup**

### **Prerequisites**
- **Python**: 3.7+ (3.9+ recommended)
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: 500MB free space

### **Required Dependencies**
```bash
# Core dependencies
pip install pandas>=1.3.0
pip install fpdf>=2.5.0
pip install Pillow>=8.0.0
pip install babel>=2.9.0

# Testing dependencies (use requirements-pytest.txt)
pip install -r requirements-pytest.txt

# Development dependencies  
pip install black>=21.0.0
pip install flake8>=3.9.0
pip install mypy>=0.950
```

### **Testing Dependencies (requirements-pytest.txt)**
```bash
# Install comprehensive testing suite
pip install -r requirements-pytest.txt

# Includes:
# - pytest==7.4.3 (Core testing framework)
# - pytest-html==4.1.1 (HTML test reports)
# - pytest-cov==4.1.0 (Coverage reporting)
# - pytest-mock==3.12.0 (Enhanced mocking)
# - pytest-xdist==3.3.1 (Parallel execution)
# - pytest-timeout==2.2.0 (Timeout handling)
# - pytest-benchmark==4.0.0 (Performance benchmarking)
# - pytest-qt==4.2.0 (GUI testing utilities)
# - hypothesis==6.92.1 (Property-based testing)
```

### **Development Tools**
```bash
# Code formatting
pip install black isort

# Linting
pip install flake8 pylint

# Type checking
pip install mypy

# Documentation
pip install sphinx sphinx-rtd-theme
```

### **IDE Configuration**

#### **VS Code Settings**
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "files.associations": {
        "*.py": "python"
    }
}
```

#### **PyCharm Configuration**
- **Interpreter**: Set to project virtual environment
- **Code Style**: Black formatter
- **Inspections**: Enable all Python inspections
- **Testing**: Configure pytest as default test runner

---

## **📁 Codebase Structure**

### **Root Level Files**

#### **Entry Point**
```python
# __main__.py
"""
Application entry point
- Initializes tkinter root window
- Sets up window properties (size, icon, title)
- Creates and starts MainApplication
- Handles graceful shutdown
"""
```

#### **Core Modules**
```python
# data_manager.py
"""
Singleton data management system
- Cart operations (CRUD)
- Customer data persistence
- Excel file operations
- Rate lookup from pricing database
- Data validation and integrity
"""

# global_state.py
"""
Centralized state management
- All tkinter variables (StringVar, IntVar)
- Dropdown options and configurations
- State synchronization methods
- Validation utilities
"""

# pdf_generator.py
"""
PDF generation engine
- Quotation PDF creation
- Invoice PDF generation
- Product image embedding
- Professional formatting
"""
```

### **UI Package Structure**
```
ui/
├── __init__.py              # Package initialization
├── main_app.py             # Main application window
├── base_product_frame.py   # Base class for product frames
├── product_frames.py       # 14 product-specific frames
├── cart_view.py           # Shopping cart interface
├── calculator_view.py     # Cost calculation interface
├── invoice_view.py        # Invoice generation interface
├── ui_theme.py           # Professional styling system
└── responsive_config.py   # Cross-platform responsive design system
```

### **Testing Infrastructure Structure**
```
tests/
├── conftest.py           # pytest fixtures and configuration
├── unit/                 # Unit tests for individual components
│   ├── test_data_manager.py
│   ├── test_global_state.py
│   └── test_*.py
├── integration/          # Integration tests for component interaction
│   ├── test_data_flow.py
│   └── test_*.py
├── ui/                   # User interface tests
│   ├── test_main_app.py
│   ├── test_product_frames.py
│   └── test_*.py
├── performance/          # Performance and stress tests
│   ├── test_performance_benchmarks.py
│   ├── test_stress_testing.py
│   └── test_*.py
├── end_to_end/           # Complete workflow tests
│   ├── test_business_scenarios.py
│   ├── test_customer_journey.py
│   └── test_*.py
├── advanced/             # Advanced testing features
│   ├── test_property_based.py
│   ├── test_reporting.py
│   └── test_*.py
├── fixtures/             # Test data and mock files
│   ├── test_excel_files/
│   ├── mock_images/
│   └── __init__.py
└── reports/              # Test reports and coverage output
    ├── coverage/
    └── report.html
```

### **Module Dependencies**
```
__main__.py
    └── ui/main_app.py
        ├── ui/ui_theme.py (styling system)
        ├── ui/responsive_config.py (responsive design)
        ├── global_state.py (singleton)
        ├── data_manager.py (singleton)
        ├── ui/product_frames.py
        │   └── ui/base_product_frame.py
        ├── ui/cart_view.py
        ├── ui/calculator_view.py
        └── ui/invoice_view.py
            └── pdf_generator.py
```

---

## **🔍 Core Components Deep Dive**

### **DataManager Class**

#### **Singleton Implementation**
```python
class DataManager:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if DataManager._initialized:
            return
        DataManager._initialized = True
        # Initialize data structures
```

#### **Cart Management**
```python
def add_item_to_cart(self, item_details, quantity=1):
    """
    Add configured item to cart
    
    Args:
        item_details (dict): Product configuration
        quantity (int): Number of units
        
    Returns:
        bool: Success status
        
    Process:
        1. Validate item_details structure
        2. Generate unique serial number
        3. Calculate costs using rate lookup
        4. Create cart entry with specifications
        5. Update cart DataFrame
        6. Sync with global state
    """
```

#### **Excel Operations**
```python
def save_quotation_to_excel(self, filename):
    """
    Export quotation to Excel file
    
    File Structure:
        - Sheet 1: Customer Details
        - Sheet 2: Cart Items with specifications
        - Sheet 3: Cost breakdown
        - Sheet 4: Metadata (timestamps, version)
    """

def load_quotation_from_excel(self, filename):
    """
    Import quotation from Excel file
    
    Process:
        1. Validate file format and structure
        2. Load customer details → global_state
        3. Recreate cart items with specifications
        4. Restore cost calculations
        5. Update UI state
    """
```

### **GlobalState Class**

#### **Variable Management**
```python
class GlobalState:
    def __init__(self):
        # Customer variables
        self.custNamVar = tk.StringVar()
        self.custAddVar = tk.StringVar()
        self.custConVar = tk.StringVar()
        
        # Dimension variables
        self.Width = tk.StringVar()
        self.Height = tk.StringVar()
        
        # Product specifications (50+ variables)
        self.trackVar = tk.StringVar()
        self.aluMatVar = tk.StringVar()
        # ... all specification variables
        
        # Options dictionary
        self.options = {
            "track_options": ["2 Track", "3 Track", "4 Track"],
            "aluminium_material": [...],
            # ... all dropdown options
        }
```

#### **State Synchronization**
```python
def get_all_specification_vars(self):
    """
    Returns dictionary of all specification variables
    Used by DataManager when adding items to cart
    """
    
def reset_specification_vars(self):
    """
    Clears all specification variables
    Called when starting new product configuration
    """
```

### **BaseProductFrame Class**

#### **Template Method Pattern**
```python
class BaseProductFrame:
    def __init__(self, parent, data_manager):
        self.parent = parent
        self.data_manager = data_manager
        self.global_state = get_global_state()
        
    def create_legacy_layout(self):
        """Template method defining common layout"""
        self.create_customer_display()    # Common
        self.create_dimensions_frame()    # Common
        self.create_specifications()      # Override in subclasses
        
    def create_specifications(self):
        """Override this method in product-specific classes"""
        raise NotImplementedError
```

#### **Cost Calculation Engine**
```python
def calculate_cost(self):
    """
    Calculate product cost using rate lookup
    
    Process:
        1. Validate dimensions (width, height)
        2. Calculate area (sq ft)
        3. Lookup base rate from data.xlsx
        4. Apply specification modifiers
        5. Calculate final cost
        6. Update cost display
        7. Enable "Add to Cart" button
    """
```

### **PDF Generation System**

#### **PDF Class Structure**
```python
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        """Page header with logo and title"""
        
    def footer(self):
        """Page footer with page numbers"""
        
    def add_customer_section(self, customer_details):
        """Customer information section"""
        
    def add_product_section(self, item):
        """Product details with image and specs"""
        
    def add_cost_summary(self, final_costs):
        """Cost breakdown and totals"""
```

#### **Image Integration**
```python
# Image mapping for products
RATIO = {
    "Sliding Window": [45, 55],
    "Sliding Door": [45, 55],
    # ... all product types with dimensions
}

def embed_product_image(self, product_type):
    """
    Embed product image in PDF
    
    Process:
        1. Lookup image path from product type
        2. Verify image exists
        3. Calculate optimal dimensions
        4. Add image to current position
        5. Adjust layout for text
    """
```

---

## **⚙️ Development Workflow**

### **Git Workflow**
```bash
# Feature development
git checkout -b feature/new-product-type
# ... make changes
git add .
git commit -m "feat: Add new product type support"
git push origin feature/new-product-type
# Create pull request

# Bug fixes
git checkout -b fix/cart-calculation-bug
# ... fix issue
git commit -m "fix: Correct cart amount calculation"
```

### **Code Style Guidelines**

#### **Python Conventions**
```python
# Use descriptive variable names
customer_details = {}  # Good
cd = {}               # Bad

# Function documentation
def calculate_cost(self, width: float, height: float) -> float:
    """
    Calculate product cost based on dimensions.
    
    Args:
        width (float): Product width in feet
        height (float): Product height in feet
        
    Returns:
        float: Total cost in INR
        
    Raises:
        ValueError: If dimensions are invalid
    """

# Class documentation
class ProductFrame(BaseProductFrame):
    """
    Product configuration frame for specific window type.
    
    Attributes:
        product_type (str): Type of window/door
        specifications (dict): Current configuration
        
    Methods:
        create_specifications(): Build product-specific UI
        calculate_cost(): Compute pricing
    """
```

#### **UI Code Conventions**
```python
# Widget creation pattern
def create_specification_widget(self, parent, label, variable, options):
    """Create standardized specification dropdown"""
    frame = tk.Frame(parent)
    label_widget = tk.Label(frame, text=label)
    combo_widget = ttk.Combobox(
        frame, 
        textvariable=variable,
        values=options,
        state="readonly"
    )
    # Layout and return
```

### **Testing During Development**

#### **Unit Testing**
```python
# test_data_manager.py
import unittest
from data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.dm = DataManager()
        
    def test_add_item_to_cart(self):
        """Test cart item addition"""
        item = {
            'product_type': 'Sliding Window',
            'width': 10,
            'height': 8,
            # ... specifications
        }
        result = self.dm.add_item_to_cart(item, quantity=2)
        self.assertTrue(result)
        
    def test_cost_calculation(self):
        """Test cost calculation accuracy"""
        # ... test implementation
```

#### **Integration Testing**
```python
# test_end_to_end.py
def test_complete_quotation_workflow():
    """Test full workflow from UI to PDF"""
    # 1. Set customer details
    # 2. Configure product
    # 3. Add to cart
    # 4. Calculate costs
    # 5. Generate PDF
    # 6. Verify output
```

---

## **🧪 Testing Framework**

### **Comprehensive Testing Infrastructure**

The application includes a complete testing infrastructure using pytest with extensive coverage and multiple test categories.

#### **pytest Configuration**
```bash
# Install testing dependencies
pip install -r requirements-pytest.txt

# Run all tests
pytest

# Run with coverage reporting
pytest --cov=. --cov-report=html

# Run specific test categories
pytest -m unit              # Unit tests only
pytest -m integration       # Integration tests only
pytest -m ui                # UI tests only
pytest -m performance       # Performance tests only
pytest -m end_to_end        # Complete workflow tests
pytest -m "not slow"        # Exclude slow tests

# Run tests in parallel
pytest -n auto              # Use all CPU cores
pytest -n 4                 # Use 4 cores

# Generate HTML reports
pytest --html=tests/reports/report.html --self-contained-html
```

#### **Test Categories and Markers**

**Core Test Types:**
- `unit` - Individual component testing
- `integration` - Component interaction testing  
- `ui` - User interface testing
- `performance` - Performance and load testing
- `end_to_end` - Complete workflow validation

**Specialized Tests:**
- `slow` - Tests taking more than 5 seconds
- `gui` - Tests requiring GUI interaction
- `excel` - Excel file handling tests
- `pdf` - PDF generation and validation tests

**Business Scenarios:**
- `residential` - Residential customer scenarios
- `commercial` - Commercial business scenarios
- `industrial` - Industrial facility scenarios
- `special` - Special business cases and edge scenarios

**Performance Tests:**
- `benchmark` - Performance benchmarking
- `stress` - Stress testing with extreme scenarios
- `memory` - Memory usage testing
- `scalability` - Scalability testing

#### **Test Structure and Organization**

```
tests/
├── conftest.py                      # pytest fixtures and configuration
├── unit/                           # Unit tests
│   ├── test_data_manager.py        # DataManager functionality
│   ├── test_global_state.py        # GlobalState management
│   ├── test_pdf_generator.py       # PDF generation
│   └── test_responsive_config.py   # Responsive system
├── integration/                    # Integration tests
│   ├── test_data_flow.py          # End-to-end data processing
│   └── test_ui_integration.py     # UI component integration
├── ui/                            # UI tests
│   ├── test_main_app.py           # Main application UI
│   ├── test_product_frames.py     # Product frame UI
│   └── test_responsive_ui.py      # Responsive design testing
├── performance/                   # Performance tests
│   ├── test_performance_benchmarks.py
│   └── test_stress_testing.py
├── end_to_end/                    # Complete workflow tests
│   ├── test_business_scenarios.py
│   └── test_customer_journey.py
├── advanced/                      # Advanced testing
│   ├── test_property_based.py
│   └── test_reporting.py
├── fixtures/                      # Test data and mocks
│   ├── test_excel_files/
│   ├── mock_images/
│   └── __init__.py
└── reports/                       # Test reports and coverage
    ├── coverage/
    └── report.html
```

#### **Test Coverage Goals**
- **Overall Coverage**: 93.1% (current achievement)
- **Critical Components**: 95%+ coverage for core modules
- **UI Components**: 85%+ coverage for user interface
- **Performance**: Tracked benchmarks for critical operations

#### **Test Data Management**
```python
# conftest.py
import pytest
import pandas as pd
from unittest.mock import Mock, patch

@pytest.fixture
def sample_customer_data():
    return {
        'custNamVar': 'Test Customer',
        'custAddVar': '123 Test Street',
        'custConVar': '1234567890'
    }

@pytest.fixture
def sample_cart_item():
    return {
        'product_type': 'Sliding Window',
        'width': 10,
        'height': 8,
        'specifications': {
            'trackVar': '2 Track',
            'aluMatVar': 'Regular Section'
        }
    }

@pytest.fixture
def mock_responsive_config():
    """Mock responsive configuration for testing"""
    with patch('ui.responsive_config.get_responsive_config') as mock:
        mock_config = Mock()
        mock_config.get_window_width.return_value = 1000
        mock_config.get_window_height.return_value = 800
        mock_config.get_font_size.return_value = 10
        mock.return_value = mock_config
        yield mock_config
```

#### **Running Tests During Development**
```bash
# Quick validation during development
pytest -m "unit and not slow" -v

# Test specific component
pytest tests/unit/test_data_manager.py -v

# Test with coverage
pytest --cov=data_manager tests/unit/test_data_manager.py

# Test responsive UI
pytest tests/ui/test_responsive_ui.py -v

# Performance testing
pytest -m performance --benchmark-only

# Generate comprehensive report
pytest --cov=. --cov-report=html --html=tests/reports/report.html
```

---

## **🆕 Adding New Features**

### **Adding a New Product Type**

#### **Step 1: Create Product Frame Class**
```python
# In ui/product_frames.py
class NewProductFrame(BaseProductFrame):
    def create_specifications(self):
        """Create product-specific specifications"""
        # Add specification widgets
        self.create_dropdown("Track Type", self.global_state.trackVar, 
                           self.global_state.track_options)
        # ... other specifications
        
        # Add product image
        self.add_product_image("New Product.png")
```

#### **Step 2: Update Main Application**
```python
# In ui/main_app.py
def __init__(self):
    # Add to product_frames mapping
    self.product_frames = {
        # ... existing products
        "New Product": NewProductFrame,
    }
    
    # Update window type options
    self.window_types = [
        # ... existing types
        "New Product"
    ]
```

#### **Step 3: Add Product Image**
```bash
# Add product image to Images/ directory
cp new_product_image.png Images/New\ Product.png
```

#### **Step 4: Update PDF Generator**
```python
# In pdf_generator.py
RATIO = {
    # ... existing ratios
    "New Product": [40, 50],  # Width, Height for PDF
}

# Add image mapping if different from product name
IMAGE_MAP = {
    # ... existing mappings
    "New Product": "New Product.png"
}
```

#### **Step 5: Update Global State**
```python
# In global_state.py
def __init__(self):
    # Add product-specific variables if needed
    self.newProductSpecVar = tk.StringVar()
    
    # Add to options
    self.options.update({
        "new_product_specs": ["Option 1", "Option 2", "Option 3"]
    })
```

### **Adding New Specifications**

#### **Step 1: Add Variable to Global State**
```python
# In global_state.py
def __init__(self):
    # Add new specification variable
    self.newSpecVar = tk.StringVar()
    
    # Add options
    self.options["new_spec_options"] = ["Value 1", "Value 2", "Value 3"]
```

#### **Step 2: Update Product Frames**
```python
# In relevant product frame classes
def create_specifications(self):
    # ... existing specifications
    self.create_dropdown("New Specification", 
                        self.global_state.newSpecVar,
                        self.global_state.options["new_spec_options"])
```

#### **Step 3: Update PDF Generation**
```python
# In pdf_generator.py
VAR_NAME = {
    # ... existing mappings
    "newSpecVar": "New Specification",
}
```

### **Adding New UI Views**

#### **Step 1: Create View Class**
```python
# ui/new_view.py
import tkinter as tk
from tkinter import ttk
from global_state import get_global_state

class NewView:
    def __init__(self, parent, data_manager):
        self.parent = parent
        self.data_manager = data_manager
        self.global_state = get_global_state()
        self.create_interface()
        
    def create_interface(self):
        """Create the view interface"""
        # Implementation
```

#### **Step 2: Add Navigation**
```python
# In calling component
def open_new_view(self):
    new_window = tk.Toplevel(self.parent)
    new_view = NewView(new_window, self.data_manager)
```

---

## **🐛 Debugging and Troubleshooting**

### **Common Issues and Solutions**

#### **Import Errors**
```python
# Problem: ModuleNotFoundError
# Solution: Check PYTHONPATH and module structure
import sys
print(sys.path)  # Verify path includes project directory

# Ensure __init__.py files exist in packages
touch ui/__init__.py
touch utils/__init__.py
```

#### **tkinter Variable Issues**
```python
# Problem: tkinter variables not updating
# Solution: Ensure proper variable binding
entry = tk.Entry(parent, textvariable=global_state.Width)  # Correct
entry = tk.Entry(parent)  # Incorrect - no binding

# Problem: Variable values not persisting
# Solution: Store reference to global_state instance
self.global_state = get_global_state()  # Correct
global_state = get_global_state()       # May be garbage collected
```

#### **PDF Generation Issues**
```python
# Problem: Images not appearing in PDF
# Check image path resolution
image_path = os.path.join("Images", f"{product_type}.png")
if not os.path.exists(image_path):
    print(f"Image not found: {image_path}")

# Problem: PDF formatting issues
# Verify FPDF version compatibility
pip install fpdf==2.5.7  # Use tested version
```

### **Debugging Tools**

#### **Logging Setup**
```python
# debug_config.py
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )

# Usage in modules
import logging
logger = logging.getLogger(__name__)

def add_item_to_cart(self, item):
    logger.debug(f"Adding item to cart: {item}")
    # ... implementation
    logger.info("Item successfully added to cart")
```

#### **State Inspection**
```python
# debug_tools.py
def print_global_state():
    """Print all global state variables"""
    gs = get_global_state()
    for attr in dir(gs):
        if isinstance(getattr(gs, attr), tk.StringVar):
            print(f"{attr}: {getattr(gs, attr).get()}")

def print_cart_contents():
    """Print current cart contents"""
    dm = DataManager()
    cart_df = dm.get_cart_data()
    print(cart_df.to_string())
```

#### **Performance Profiling**
```python
# performance_debug.py
import cProfile
import pstats

def profile_function(func):
    """Decorator for profiling functions"""
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        
        stats = pstats.Stats(pr)
        stats.sort_stats('cumulative')
        stats.print_stats()
        
        return result
    return wrapper

# Usage
@profile_function
def calculate_cost(self):
    # ... implementation
```

---

## **⚡ Performance Optimization**

### **Memory Management**

#### **Widget Cleanup**
```python
class ProductFrame:
    def __init__(self, parent):
        self.widgets = []  # Track created widgets
        
    def create_widget(self, widget_class, parent, **kwargs):
        widget = widget_class(parent, **kwargs)
        self.widgets.append(widget)
        return widget
        
    def cleanup(self):
        """Clean up widgets before window destruction"""
        for widget in self.widgets:
            widget.destroy()
        self.widgets.clear()
```

#### **Data Structure Optimization**
```python
# Use pandas for large datasets
import pandas as pd

# Efficient cart operations
class DataManager:
    def __init__(self):
        self.cart_df = pd.DataFrame()  # Efficient for tabular data
        
    def add_item_to_cart(self, item):
        # Use concat instead of append for better performance
        new_row = pd.DataFrame([item])
        self.cart_df = pd.concat([self.cart_df, new_row], ignore_index=True)
```

### **UI Responsiveness**

#### **Lazy Loading**
```python
class MainApplication:
    def __init__(self):
        self.product_frames = {}  # Don't create all frames at startup
        
    def selector(self, event=None):
        window_type = self.windowTypeVar.get()
        
        # Create frame only when needed
        if window_type not in self.product_frames:
            frame_class = self.get_frame_class(window_type)
            self.product_frames[window_type] = frame_class
```

#### **Debounced Operations**
```python
def handleWait(self, event=None):
    """Debounced search for comboboxes"""
    if hasattr(self, 'search_timer'):
        self.parent.after_cancel(self.search_timer)
    
    self.search_timer = self.parent.after(300, self.perform_search)
```

### **File I/O Optimization**

#### **Efficient Excel Operations**
```python
def save_quotation_to_excel(self, filename):
    """Optimized Excel export"""
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        # Write multiple sheets efficiently
        self.customer_df.to_excel(writer, sheet_name='Customer', index=False)
        self.cart_df.to_excel(writer, sheet_name='Cart', index=False)
        # ... other sheets
```

#### **Image Caching**
```python
class PDFGenerator:
    def __init__(self):
        self.image_cache = {}  # Cache loaded images
        
    def load_product_image(self, product_type):
        if product_type not in self.image_cache:
            image_path = f"Images/{product_type}.png"
            self.image_cache[product_type] = Image.open(image_path)
        return self.image_cache[product_type]
```

---

## **🚀 Deployment Guidelines**

### **Environment Preparation**

#### **Production Environment**
```bash
# Create production virtual environment
python -m venv prod_env
source prod_env/bin/activate  # Linux/Mac
# or
prod_env\Scripts\activate     # Windows

# Install production dependencies
pip install -r requirements.txt

# Verify installation
python -c "import tkinter; print('tkinter OK')"
python -c "import pandas; print('pandas OK')"
python -c "import fpdf; print('fpdf OK')"
```

#### **Requirements File**
```txt
# requirements.txt
pandas>=1.3.0,<2.0.0
fpdf>=2.5.0,<3.0.0
Pillow>=8.0.0,<10.0.0
babel>=2.9.0,<3.0.0
openpyxl>=3.0.0,<4.0.0
```

### **Building Executable**

#### **Using PyInstaller**
```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed --icon=Images/MGA_Logo.ico __main__.py

# Advanced options
pyinstaller \
    --onefile \
    --windowed \
    --icon=Images/MGA_Logo.ico \
    --add-data "Images;Images" \
    --add-data "Data;Data" \
    --name "MGA_Window_Quotation" \
    __main__.py
```

#### **Spec File Configuration**
```python
# MGA_Window_Quotation.spec
a = Analysis(['__main__.py'],
             pathex=['.'],
             binaries=[],
             datas=[('Images', 'Images'), ('Data', 'Data')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
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
          icon='Images/MGA_Logo.ico')
```

### **Installation Package**

#### **Windows Installer (NSIS)**
```nsis
; installer.nsi
!define APPNAME "MGA Window Quotation"
!define COMPANYNAME "MGA Windows"
!define DESCRIPTION "Professional Window Quotation System"

Name "${APPNAME}"
OutFile "MGA_Window_Quotation_Installer.exe"
InstallDir "$PROGRAMFILES\${COMPANYNAME}\${APPNAME}"

Section "Install"
    SetOutPath $INSTDIR
    File "dist\MGA_Window_Quotation.exe"
    File /r "Images"
    File /r "Data"
    
    CreateDirectory "$SMPROGRAMS\${COMPANYNAME}"
    CreateShortCut "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk" "$INSTDIR\MGA_Window_Quotation.exe"
    CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\MGA_Window_Quotation.exe"
SectionEnd
```

---

## **🔧 Maintenance Procedures**

### **Regular Maintenance Tasks**

#### **Weekly Tasks**
- Check application logs for errors
- Monitor performance metrics
- Review user feedback
- Update test data if needed

#### **Monthly Tasks**
- Update dependencies to latest stable versions
- Run full test suite
- Review and update documentation
- Backup configuration files

#### **Quarterly Tasks**
- Comprehensive security review
- Performance benchmarking
- User training updates
- Infrastructure assessment

### **Version Management**

#### **Versioning Strategy**
```
MAJOR.MINOR.PATCH
- MAJOR: Breaking changes or major features
- MINOR: New features, backward compatible
- PATCH: Bug fixes, no new features

Examples:
- 1.0.0: Initial release
- 1.1.0: New product type added
- 1.1.1: Bug fix for cost calculation
- 2.0.0: Major UI overhaul
```

#### **Release Process**
```bash
# 1. Update version
echo "1.2.0" > VERSION

# 2. Update changelog
git log --oneline v1.1.0..HEAD > CHANGELOG.md

# 3. Create release branch
git checkout -b release/1.2.0

# 4. Final testing
python -m pytest tests/

# 5. Merge to main
git checkout main
git merge release/1.2.0

# 6. Tag release
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin v1.2.0

# 7. Build and distribute
pyinstaller MGA_Window_Quotation.spec
```

### **Database Maintenance**

#### **Excel File Management**
```python
# data_maintenance.py
def cleanup_old_quotations():
    """Archive quotations older than 1 year"""
    import os
    import shutil
    from datetime import datetime, timedelta
    
    archive_date = datetime.now() - timedelta(days=365)
    
    for file in os.listdir("Data"):
        if file.endswith("_QuotationData.xlsx"):
            file_path = os.path.join("Data", file)
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if mod_time < archive_date:
                archive_path = os.path.join("Archive", file)
                shutil.move(file_path, archive_path)
```

#### **Pricing Data Updates**
```python
def update_pricing_data():
    """Update product rates from master database"""
    # 1. Backup current data.xlsx
    # 2. Download/import new pricing data
    # 3. Validate data format
    # 4. Update application database
    # 5. Test with sample calculations
```

### **Monitoring and Logging**

#### **Application Monitoring**
```python
# monitoring.py
import logging
import psutil
import time

def monitor_application():
    """Monitor application performance"""
    while True:
        # CPU usage
        cpu_percent = psutil.cpu_percent()
        
        # Memory usage
        memory = psutil.virtual_memory()
        
        # Log metrics
        logging.info(f"CPU: {cpu_percent}%, Memory: {memory.percent}%")
        
        time.sleep(60)  # Check every minute
```

---

## **📝 Best Practices Summary**

### **Code Quality**
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Write comprehensive docstrings
- Implement proper error handling
- Maintain test coverage above 85%

### **Architecture**
- Maintain separation of concerns
- Use design patterns appropriately
- Keep components loosely coupled
- Implement proper abstraction layers
- Follow SOLID principles

### **Testing**
- Write tests before fixing bugs
- Test edge cases and error conditions
- Use meaningful test data
- Maintain test environment separate from production
- Automate testing where possible

### **Documentation**
- Keep documentation up to date
- Document all public APIs
- Provide usage examples
- Maintain architectural decision records
- Document known limitations and workarounds

### **Performance**
- Profile before optimizing
- Optimize bottlenecks first
- Use appropriate data structures
- Implement caching where beneficial
- Monitor production performance

---

## **🎯 Conclusion**

This developer guide provides the foundation for effective development, maintenance, and enhancement of the MGA Window Quotation application. By following these guidelines and procedures, developers can:

- Understand the codebase architecture thoroughly
- Implement new features efficiently
- Maintain code quality and performance
- Deploy updates safely
- Troubleshoot issues effectively

The modular architecture and comprehensive testing framework ensure that the application can evolve and scale while maintaining reliability and professional standards.

For specific questions or clarifications, refer to the API Reference documentation or consult the project's issue tracking system. 