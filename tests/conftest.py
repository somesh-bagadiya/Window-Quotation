"""
Pytest Configuration and Shared Fixtures
Window Quotation Application Testing
"""

import pytest
import tkinter as tk
import tempfile
import shutil
import os
import sys
from unittest.mock import Mock, patch, MagicMock
import pandas as pd
from datetime import datetime

# Add project root to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import application modules
from data_manager import DataManager
from global_state import get_global_state, GlobalState
from ui.main_app import MainApplication


# ================================
# Session-wide Fixtures
# ================================

@pytest.fixture
def tk_root():
    """
    Create a fresh tkinter root for each test.
    Ensures proper cleanup to prevent tkinter conflicts.
    """
    import tkinter as tk
    
    # Destroy any existing root to ensure clean state
    try:
        if hasattr(tk, '_default_root') and tk._default_root:
            tk._default_root.destroy()
            tk._default_root = None
    except:
        pass
    
    # Create new root
    root = tk.Tk()
    root.withdraw()  # Hide the window during testing
    
    # Set as default root
    tk._default_root = root
    
    yield root
    
    # Cleanup
    try:
        if root.winfo_exists():
            # Destroy all child widgets first
            for child in root.winfo_children():
                try:
                    child.destroy()
                except:
                    pass
            # Then destroy the root
            root.destroy()
    except Exception as e:
        # If normal cleanup fails, force cleanup
        try:
            root.quit()
        except:
            pass
    finally:
        # Clear the default root
        try:
            tk._default_root = None
        except:
            pass


# ================================
# Component Fixtures
# ================================

@pytest.fixture
def clean_data_manager(tk_root):
    """
    Fresh DataManager instance for each test.
    Resets singleton state to ensure test isolation.
    """
    # Reset singleton to ensure clean state
    DataManager._instance = None
    GlobalState._instance = None
    dm = DataManager()
    
    # Ensure completely clean cart state
    dm.cart_data = pd.DataFrame(columns=[
        'Sr.No', 'Particulars', 'Width', 'Height', 'Total Sq.ft', 'Cost (INR)', 'Quantity', 'Amount'
    ])
    dm._serial_counter = 1
    dm.customer_details = {}
    
    # Reset global state customer variables to empty strings
    dm.global_state.custNamVar.set("")
    dm.global_state.custAddVar.set("")
    dm.global_state.custConVar.set("")
    dm.global_state.address = ""
    
    yield dm
    
    # Thorough cleanup after test
    dm.cart_data = pd.DataFrame(columns=[
        'Sr.No', 'Particulars', 'Width', 'Height', 'Total Sq.ft', 'Cost (INR)', 'Quantity', 'Amount'
    ])
    dm._serial_counter = 1
    dm.customer_details = {}
    
    # Reset global state customer variables after test
    dm.global_state.custNamVar.set("")
    dm.global_state.custAddVar.set("")
    dm.global_state.custConVar.set("")
    dm.global_state.address = ""


@pytest.fixture
def clean_global_state(tk_root):
    """
    Fresh GlobalState instance for each test.
    Resets all variables to default values.
    """
    # Reset singleton
    GlobalState._instance = None
    gs = get_global_state()
    
    # Reset all variables to defaults
    gs.Width.set("")
    gs.Height.set("")
    gs.custNamVar.set("")
    gs.custAddVar.set("")
    gs.custConVar.set("")
    gs.windowTypeVar.set("")
    
    yield gs


@pytest.fixture
def main_application(tk_root, clean_data_manager, clean_global_state):
    """
    MainApplication instance with clean dependencies.
    Automatically hidden during testing.
    """
    app = MainApplication(tk_root)
    app.withdraw()  # Hide application window
    yield app
    try:
        app.destroy()
    except tk.TclError:
        pass


# ================================
# Sample Data Fixtures
# ================================

@pytest.fixture
def sample_customer_data():
    """Sample customer data for testing"""
    return {
        'custNamVar': 'John Smith',
        'custAddVar': '123 Main Street\nAnytown, ST 12345',
        'custConVar': '555-123-4567'
    }


@pytest.fixture
def sample_cart_item():
    """Basic sample cart item for testing"""
    # Application uses: Amount = Cost (per sq.ft) × Area × Quantity
    # Cost (INR) = 1500.0 per sq.ft
    # Area = 10ft × 8ft = 80 sq.ft  
    # Amount = 1500.0 × 80 × 1 = 120,000
    return {
        'Sr.No': 1,
        'Particulars': 'Sliding Window',
        'Width': '10ft',
        'Height': '8ft',
        'Total Sq.ft': 80.0,
        'Cost (INR)': 1500.0,  # Cost per sq.ft
        'Quantity': 1,
        'Amount': 120000.0,    # 1500 × 80 × 1
        # Hidden specification columns (would be populated in real usage)
        'trackVar': '2 Track',
        'aluMatVar': 'Regular Section',
        'glaThicVar': '5mm',
        'glaTypVar': 'Plain'
    }


@pytest.fixture
def sample_cart_items_multiple():
    """Multiple cart items for testing complex scenarios"""
    return [
        {
            'Sr.No': 1,
            'Particulars': 'Sliding Window',
            'Width': '10ft',
            'Height': '8ft',
            'Total Sq.ft': 80.0,
            'Cost (INR)': 1500.0,   # per sq.ft
            'Quantity': 1,
            'Amount': 120000.0      # 1500 × 80 × 1
        },
        {
            'Sr.No': 2,
            'Particulars': 'Sliding Door',
            'Width': '8ft',
            'Height': '10ft',
            'Total Sq.ft': 80.0,
            'Cost (INR)': 2000.0,   # per sq.ft
            'Quantity': 2,
            'Amount': 320000.0      # 2000 × 80 × 2
        },
        {
            'Sr.No': 3,
            'Particulars': 'Fix Window',
            'Width': '6ft',
            'Height': '4ft',
            'Total Sq.ft': 24.0,
            'Cost (INR)': 800.0,    # per sq.ft
            'Quantity': 3,
            'Amount': 57600.0       # 800 × 24 × 3
        }
    ]


@pytest.fixture
def sample_product_specifications():
    """Sample product specifications for testing"""
    return {
        'trackVar': '2 Track',
        'aluMatVar': 'Regular Section',
        'glaThicVar': '5mm',
        'glaTypVar': 'Plain',
        'hardLocVar': 'Mortise Lock',
        'hardBeaVar': 'Nylon Bearing',
        'rubbTypVar': 'EPDM',
        'rubbThicVar': '3mm',
        'fraColVar': 'White',
        'silColVar': 'Clear',
        'handleVar': 'C Type'
    }


# ================================
# File System Fixtures
# ================================

@pytest.fixture
def temp_test_directory():
    """Temporary directory for test files"""
    temp_dir = tempfile.mkdtemp(prefix='pytest_window_quotation_')
    yield temp_dir
    shutil.rmtree(temp_dir, ignore_errors=True)


@pytest.fixture
def sample_excel_file(temp_test_directory):
    """Creates a sample Excel file for testing"""
    import pandas as pd
    
    # Sample data structure matching the application format
    sample_data = pd.DataFrame([
        {'Sr.No': 1, 'Particulars': 'Test Window', 'Cost (INR)': 1000.0, 'Quantity': 1, 'Amount': 1000.0}
    ])
    
    excel_path = os.path.join(temp_test_directory, 'test_quotation.xlsx')
    sample_data.to_excel(excel_path, index=False)
    
    return excel_path


# ================================
# Mock Fixtures
# ================================

@pytest.fixture
def mock_messagebox():
    """Mock tkinter messagebox to prevent UI dialogs during testing"""
    with patch('tkinter.messagebox.showerror') as mock_error, \
         patch('tkinter.messagebox.showwarning') as mock_warning, \
         patch('tkinter.messagebox.showinfo') as mock_info, \
         patch('tkinter.messagebox.askyesno') as mock_yesno:
        
        mock_yesno.return_value = True  # Default to 'Yes' for confirmations
        
        yield {
            'error': mock_error,
            'warning': mock_warning,
            'info': mock_info,
            'yesno': mock_yesno
        }


@pytest.fixture
def mock_file_dialogs():
    """Mock file dialogs for testing file operations"""
    with patch('tkinter.filedialog.asksaveasfilename') as mock_save, \
         patch('tkinter.filedialog.askopenfilename') as mock_open:
        
        mock_save.return_value = "test_file.xlsx"
        mock_open.return_value = "test_file.xlsx"
        
        yield {
            'save': mock_save,
            'open': mock_open
        }


@pytest.fixture
def mock_pdf_generation():
    """Mock PDF generation to avoid file system operations during tests"""
    with patch('pdf_generator.create_quotation_pdf') as mock_create_pdf, \
         patch('pdf_generator.create_invoice_pdf') as mock_create_invoice:
        
        mock_create_pdf.return_value = True
        mock_create_invoice.return_value = True
        
        yield {
            'quotation': mock_create_pdf,
            'invoice': mock_create_invoice
        }


# ================================
# Parametrized Fixtures
# ================================

@pytest.fixture(params=[
    "Sliding Window", "Sliding Door", "Fix Louver", "Patti Louver",
    "Openable Window", "Sliding Folding Door", "Casement Window",
    "Aluminium Partition", "Toughened Partition", "Toughened Door",
    "Composite Panel", "Curtain Wall", "Fix Window", "Exhaust Fan Window"
])
def product_type(request):
    """Parametrized fixture for all product types"""
    return request.param


@pytest.fixture(params=[
    (10, 8, 80.0),    # Standard window
    (6, 4, 24.0),     # Small window
    (15, 10, 150.0),  # Large window
    (3.5, 6.5, 22.75), # Odd dimensions
])
def dimensions_test_data(request):
    """Parametrized fixture for different dimension combinations"""
    width, height, expected_area = request.param
    return {
        'width': width,
        'height': height,
        'expected_area': expected_area
    }


# ================================
# Performance Testing Fixtures
# ================================

@pytest.fixture
def performance_data_manager():
    """DataManager optimized for performance testing with clean state"""
    # Force completely clean singleton for accurate performance measurements
    DataManager._instance = None
    GlobalState._instance = None
    dm = DataManager()
    
    # Ensure completely clean state - NO pre-loaded data
    dm.cart_data = pd.DataFrame(columns=[
        'Sr.No', 'Particulars', 'Width', 'Height', 'Total Sq.ft', 'Cost (INR)', 'Quantity', 'Amount'
    ])
    dm._serial_counter = 1
    dm.customer_details = {}
    
    return dm


# ================================
# Setup and Teardown Hooks
# ================================

def pytest_configure(config):
    """Configure pytest with additional settings"""
    # Ensure reports directory exists
    reports_dir = os.path.join(os.getcwd(), 'tests', 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    
    # Add custom markers if not already defined
    markers = [
        "unit: Unit tests for individual components",
        "integration: Integration tests for component interaction", 
        "ui: User interface tests",
        "performance: Performance and load tests",
        "slow: Tests that take more than 5 seconds",
        "gui: Tests that require GUI interaction",
        "excel: Tests that work with Excel files",
        "pdf: Tests that generate or validate PDFs"
    ]
    
    for marker in markers:
        config.addinivalue_line("markers", marker)


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location"""
    for item in items:
        # Add markers based on file path
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "ui" in str(item.fspath):
            item.add_marker(pytest.mark.ui)
        elif "performance" in str(item.fspath):
            item.add_marker(pytest.mark.performance)
        elif "end_to_end" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        
        # Add slow marker for tests with "slow" in name
        if "slow" in item.name.lower():
            item.add_marker(pytest.mark.slow)


# ================================
# Helper Functions for Tests
# ================================

def create_test_item(sr_no=1, particulars="Test Item", cost=1000.0, quantity=1):
    """Helper function to create standardized test cart items"""
    area = 80.0  # 10ft × 8ft
    return {
        'Sr.No': sr_no,
        'Particulars': particulars,
        'Width': '10ft',
        'Height': '8ft',
        'Total Sq.ft': area,
        'Cost (INR)': cost,  # Cost per sq.ft
        'Quantity': quantity,
        'Amount': cost * area * quantity  # Correct: cost × area × quantity
    }


def assert_cart_item_equals(actual_item, expected_item, check_specifications=False):
    """Helper function to assert cart item equality"""
    core_fields = ['Sr.No', 'Particulars', 'Cost (INR)', 'Quantity', 'Amount']
    
    for field in core_fields:
        if field in expected_item:
            assert actual_item[field] == expected_item[field], f"Field {field} mismatch"
    
    if check_specifications:
        spec_fields = ['trackVar', 'aluMatVar', 'glaThicVar', 'glaTypVar']
        for field in spec_fields:
            if field in expected_item:
                assert actual_item[field] == expected_item[field], f"Specification {field} mismatch" 