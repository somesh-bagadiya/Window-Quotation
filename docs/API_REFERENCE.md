# 📚 MGA Window Quotation Application - API Reference

## **Overview**

This API reference provides detailed documentation for all modules, classes, and public methods in the MGA Window Quotation application.

---

## **📋 Table of Contents**

- [Core Modules](#core-modules)
- [UI Package](#ui-package)
- [Utility Functions](#utility-functions)
- [Constants and Configuration](#constants-and-configuration)

---

## **🔧 Core Modules**

### **data_manager.py**

#### **Class: DataManager**
```python
class DataManager:
    """Singleton class for centralized data operations"""
```

**Methods:**

##### **__new__()**
```python
def __new__(cls) -> DataManager
```
Singleton constructor ensuring single instance.

##### **add_item_to_cart(item_details, quantity=1)**
```python
def add_item_to_cart(self, item_details: dict, quantity: int = 1) -> bool
```
**Parameters:**
- `item_details` (dict): Product configuration with specifications
- `quantity` (int): Number of units (default: 1)

**Returns:**
- `bool`: Success status

**Example:**
```python
dm = DataManager()
item = {
    'product_type': 'Sliding Window',
    'width': 10, 'height': 8,
    'specifications': {...}
}
success = dm.add_item_to_cart(item, quantity=2)
```

##### **remove_item_from_cart(serial_number)**
```python
def remove_item_from_cart(self, serial_number: str) -> bool
```
Remove item by serial number from cart.

##### **get_cart_data()**
```python
def get_cart_data(self) -> pd.DataFrame
```
**Returns:**
- `DataFrame`: Cart items with columns [Sr.No, Particulars, Width, Height, Total Sq.ft, Cost (INR), Quantity, Amount]

##### **set_customer_details(customer_info)**
```python
def set_customer_details(self, customer_info: dict) -> None
```
**Parameters:**
- `customer_info` (dict): Customer details with keys ['custNamVar', 'custAddVar', 'custConVar']

##### **save_quotation_to_excel(filename)**
```python
def save_quotation_to_excel(self, filename: str) -> bool
```
Export quotation to Excel file.

##### **load_quotation_from_excel(filename)**
```python
def load_quotation_from_excel(self, filename: str) -> bool
```
Import quotation from Excel file.

---

### **global_state.py**

#### **Class: GlobalState**
```python
class GlobalState:
    """Centralized state management with tkinter variables"""
```

**Attributes:**

##### **Customer Variables**
- `custNamVar: tk.StringVar` - Customer name
- `custAddVar: tk.StringVar` - Customer address  
- `custConVar: tk.StringVar` - Customer contact

##### **Dimension Variables**
- `Width: tk.StringVar` - Product width
- `Height: tk.StringVar` - Product height
- `totSqftEntVar: tk.StringVar` - Total square footage

##### **Specification Variables**
- `trackVar: tk.StringVar` - Track type selection
- `aluMatVar: tk.StringVar` - Aluminium material
- `glaThicVar: tk.StringVar` - Glass thickness
- `glaTypVar: tk.StringVar` - Glass type
- `fraColVar: tk.StringVar` - Frame color
- `silColVar: tk.StringVar` - Silicon color

**Methods:**

##### **get_all_specification_vars()**
```python
def get_all_specification_vars(self) -> dict
```
Returns dictionary of all specification variables.

##### **reset_specification_vars()**
```python
def reset_specification_vars(self) -> None
```
Clear all specification variables.

##### **Module Function: get_global_state()**
```python
def get_global_state() -> GlobalState
```
Get singleton instance of GlobalState.

---

### **pdf_generator.py**

#### **Function: create_quotation_pdf()**
```python
def create_quotation_pdf(filename: str, customer_details: dict, 
                        cart_items: pd.DataFrame, final_costs: dict) -> bool
```
**Parameters:**
- `filename` (str): Output PDF path
- `customer_details` (dict): Customer information
- `cart_items` (DataFrame): Cart data from DataManager
- `final_costs` (dict): Cost breakdown

**Returns:**
- `bool`: Success status

#### **Function: create_invoice_pdf()**
```python
def create_invoice_pdf(filename: str, customer_details: dict, 
                      invoice_details: dict, cart_items_with_hsn: pd.DataFrame, 
                      final_costs: dict) -> bool
```
Generate GST-compliant invoice PDF.

#### **Class: PDF(FPDF)**
```python
class PDF(FPDF):
    """Custom PDF class for quotations"""
```

**Methods:**

##### **header()**
```python
def header(self) -> None
```
Create page header with logo and title.

##### **footer()**
```python
def footer(self) -> None
```
Create page footer with page numbers.

##### **add_customer_section(customer_details)**
```python
def add_customer_section(self, customer_details: dict) -> None
```
Add customer information section.

---

## **🎨 UI Package**

### **ui/main_app.py**

#### **Class: MainApplication**
```python
class MainApplication:
    """Main application window and controller"""
```

**Methods:**

##### **__init__(parent, data_manager)**
```python
def __init__(self, parent: tk.Tk, data_manager: DataManager)
```
Initialize main application window.

##### **create_widgets()**
```python
def create_widgets(self) -> None
```
Create main UI layout with customer details and product selection.

##### **selector(event=None)**
```python
def selector(self, event=None) -> None
```
Handle product type selection and open configuration window.

##### **open_cart_view()**
```python
def open_cart_view(self) -> None
```
Open shopping cart window.

---

### **ui/base_product_frame.py**

#### **Class: BaseProductFrame**
```python
class BaseProductFrame:
    """Base class for all product configuration frames"""
```

**Methods:**

##### **__init__(parent, data_manager)**
```python
def __init__(self, parent: tk.Toplevel, data_manager: DataManager)
```
Initialize base product frame.

##### **create_legacy_layout()**
```python
def create_legacy_layout(self) -> None
```
Create standard 3-frame layout (customer, dimensions, specifications).

##### **create_specifications()**
```python
def create_specifications(self) -> None
```
**Abstract method** - Override in subclasses for product-specific UI.

##### **calculate_cost()**
```python
def calculate_cost(self) -> None
```
Calculate product cost based on dimensions and specifications.

##### **add_to_cart()**
```python
def add_to_cart(self) -> None
```
Add configured product to cart.

---

### **ui/product_frames.py**

#### **Product Frame Classes**
All inherit from `BaseProductFrame`:

- `SlidingWindow` - Sliding window configuration
- `SlidingDoor` - Sliding door configuration  
- `FixLouver` - Fixed louver configuration
- `PattiLouver` - Adjustable louver configuration
- `OpenableWindow` - Openable window configuration
- `SlidingFoldingDoor` - Folding door configuration
- `CasementWindow` - Casement window configuration
- `AluminiumPartition` - Aluminium partition configuration
- `ToughenedPartition` - Toughened partition configuration
- `ToughenedDoor` - Toughened door configuration
- `CompositePanel` - Composite panel configuration
- `CurtainWall` - Curtain wall configuration
- `FixWindow` - Fixed window configuration
- `ExhaustFanWindow` - Exhaust fan window configuration

**Each class implements:**
```python
def create_specifications(self) -> None
    """Create product-specific specification widgets"""
```

---

### **ui/cart_view.py**

#### **Class: CartView**
```python
class CartView:
    """Shopping cart interface for managing cart items"""
```

**Methods:**

##### **__init__(parent, data_manager)**
```python
def __init__(self, parent: tk.Toplevel, data_manager: DataManager)
```

##### **refresh_cart()**
```python
def refresh_cart(self) -> None
```
Reload and display current cart contents.

##### **remove_selected_item()**
```python
def remove_selected_item(self) -> None
```
Remove selected item from cart.

##### **update_quantity(row, new_quantity)**
```python
def update_quantity(self, row: int, new_quantity: int) -> None
```
Update quantity for cart item.

---

### **ui/calculator_view.py**

#### **Class: CalculatorView**
```python
class CalculatorView:
    """Cost calculation interface with discounts and taxes"""
```

**Methods:**

##### **calculate_totals()**
```python
def calculate_totals(self) -> dict
```
**Returns:**
- `dict`: Final cost breakdown with keys ['subtotal', 'discount', 'tax', 'total']

##### **apply_discount()**
```python
def apply_discount(self) -> None
```
Apply percentage or fixed discount to subtotal.

##### **calculate_tax()**
```python
def calculate_tax(self) -> None
```
Calculate GST and other taxes.

---

### **ui/invoice_view.py**

#### **Class: InvoiceView**
```python
class InvoiceView:
    """Invoice generation interface"""
```

**Methods:**

##### **generate_invoice()**
```python
def generate_invoice(self) -> bool
```
Generate invoice PDF with GST details.

---

## **🛠️ Utility Functions**

### **utils/helpers.py**

#### **Function: validate_digits(value)**
```python
def validate_digits(value: str) -> bool
```
Validate if string contains only digits and decimal point.

#### **Function: format_currency(amount)**
```python
def format_currency(amount: float) -> str
```
Format number as currency with INR symbol.

#### **Function: calculate_area(width, height)**
```python
def calculate_area(width: float, height: float) -> float
```
Calculate area in square feet.

---

## **⚙️ Constants and Configuration**

### **PDF Generator Constants**

#### **RATIO Dictionary**
```python
RATIO = {
    "Sliding Window": [45, 55],
    "Sliding Door": [45, 55],
    "Fix Louver": [40, 55],
    # ... all product types with [width, height] for PDF images
}
```

#### **VAR_NAME Dictionary**
```python
VAR_NAME = {
    "trackVar": "Type",
    "aluMatVar": "Aluminium Material",
    "glaThicVar": "Glass Thickness",
    # ... mapping of variable names to display names
}
```

### **Global State Options**

#### **Product Options**
```python
options = {
    "track_options": ["2 Track", "3 Track", "4 Track"],
    "aluminium_material": ["Regular Section", "Domal Section (JINDAL)", ...],
    "glass_thickness": ["3.5mm", "4mm", "5mm", "8mm", "12mm"],
    "glass_type": ["Plain", "Frosted", "One-way", "Tinted", "Bajra"],
    # ... all specification options
}
```

---

## **📝 Usage Examples**

### **Complete Workflow Example**
```python
# Initialize components
from data_manager import DataManager
from global_state import get_global_state
from pdf_generator import create_quotation_pdf

# Get singleton instances
data_manager = DataManager()
global_state = get_global_state()

# Set customer details
customer_info = {
    'custNamVar': 'John Smith',
    'custAddVar': '123 Main Street\nNew York, NY',
    'custConVar': '123-456-7890'
}
data_manager.set_customer_details(customer_info)

# Configure product
item_details = {
    'product_type': 'Sliding Window',
    'width': 10,
    'height': 8,
    'specifications': {
        'trackVar': '2 Track',
        'aluMatVar': 'Regular Section',
        'glaThicVar': '5mm',
        'glaTypVar': 'Plain'
    }
}

# Add to cart
success = data_manager.add_item_to_cart(item_details, quantity=2)

# Get cart data
cart_df = data_manager.get_cart_data()

# Generate PDF
final_costs = {'subtotal': 25000, 'tax': 4500, 'total': 29500}
pdf_success = create_quotation_pdf(
    'customer_quote.pdf',
    customer_info,
    cart_df,
    final_costs
)
```

### **Adding Custom Product Type**
```python
# 1. Create new frame class
class CustomProductFrame(BaseProductFrame):
    def create_specifications(self):
        # Add custom specifications
        self.create_dropdown("Custom Spec", 
                           self.global_state.customVar,
                           ["Option 1", "Option 2"])

# 2. Register in main application
def register_custom_product():
    from ui.main_app import MainApplication
    MainApplication.product_frames["Custom Product"] = CustomProductFrame
```

---

## **🔗 Integration Points**

### **Data Flow**
1. **UI Input** → `GlobalState` variables
2. **GlobalState** → `DataManager` operations
3. **DataManager** → Excel/PDF output
4. **PDF Generator** ← Cart data + Customer details

### **State Synchronization**
- UI widgets bound to `GlobalState` variables
- `DataManager` reads from `GlobalState` when adding items
- Cart operations update both `DataManager` and UI displays

### **File Operations**
- **Excel**: Read pricing data, save/load quotations
- **PDF**: Generate quotations and invoices
- **Images**: Embed product images in PDFs

---

## **⚠️ Important Notes**

### **Singleton Pattern**
Both `DataManager` and `GlobalState` use singleton pattern. Always use factory functions:
```python
# Correct
data_manager = DataManager()
global_state = get_global_state()

# Incorrect - may create multiple instances
data_manager = DataManager.__new__(DataManager)
```

### **Thread Safety**
The application is designed for single-threaded use with tkinter. Avoid threading with UI operations.

### **Memory Management**
- Product frames are created on-demand and destroyed when closed
- Cart data persists throughout application lifecycle
- Images are loaded fresh for each PDF generation

### **Error Handling**
Most methods return boolean success status. Check return values for error handling:
```python
success = data_manager.add_item_to_cart(item)
if not success:
    # Handle error
    print("Failed to add item to cart")
```

---

This API reference provides the essential information for integrating with and extending the MGA Window Quotation application. For implementation details, refer to the Developer Guide. 