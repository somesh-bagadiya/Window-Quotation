# 🏗️ MGA Window Quotation Application - Architecture Documentation

## **Overview**

The MGA Window Quotation application has been completely refactored from a monolithic 5,832-line codebase into a modern, modular, enterprise-grade application. This document provides a comprehensive overview of the new architecture, design patterns, and component interactions.

---

## **📋 Table of Contents**

- [Architecture Overview](#architecture-overview)
- [Core Design Principles](#core-design-principles)
- [System Components](#system-components)
- [Data Flow Architecture](#data-flow-architecture)
- [UI Architecture](#ui-architecture)
- [Module Dependencies](#module-dependencies)
- [Design Patterns](#design-patterns)
- [Performance Considerations](#performance-considerations)

---

## **🏛️ Architecture Overview**

### **High-Level Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│                    MGA Window Quotation                     │
│                     Application Layer                       │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                     UI Layer (ui/)                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │ Main App    │ │ Product     │ │ Cart/Calc   │          │
│  │ Interface   │ │ Frames      │ │ Views       │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    Business Logic Layer                     │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │ Data        │ │ Global      │ │ PDF         │          │
│  │ Manager     │ │ State       │ │ Generator   │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                     Data Layer                              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │ Excel       │ │ PDF         │ │ Image       │          │
│  │ Files       │ │ Output      │ │ Assets      │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
└─────────────────────────────────────────────────────────────┘
```

### **Directory Structure**

```
Window-Quotation/
│
├── __main__.py                 # Application entry point
├── data_manager.py            # Core data operations (Singleton)
├── global_state.py            # State management (Singleton)
├── pdf_generator.py           # PDF generation engine
├── pytest.ini                # pytest configuration
├── requirements-pytest.txt    # Testing dependencies
│
├── ui/                        # User Interface Layer
│   ├── __init__.py
│   ├── main_app.py           # Main application window
│   ├── base_product_frame.py # Base class for product configuration
│   ├── product_frames.py     # 14 product-specific frames
│   ├── cart_view.py          # Shopping cart interface
│   ├── calculator_view.py    # Cost calculation interface
│   ├── invoice_view.py       # Invoice generation interface
│   ├── ui_theme.py           # Professional styling system
│   └── responsive_config.py  # Cross-platform responsive design system
│
├── utils/                     # Utility Functions
│   ├── __init__.py
│   └── helpers.py            # Shared utility functions
│
├── tests/                     # Comprehensive Testing Infrastructure
│   ├── conftest.py           # pytest fixtures and configuration
│   ├── unit/                 # Unit tests for individual components
│   ├── integration/          # Integration tests for component interaction
│   ├── ui/                   # User interface tests
│   ├── performance/          # Performance and stress tests
│   ├── end_to_end/           # Complete workflow tests
│   ├── advanced/             # Advanced testing features
│   ├── fixtures/             # Test data and mock files
│   └── reports/              # Test reports and coverage output
│
├── Data/                      # Data Files
│   ├── data.xlsx             # Master pricing database
│   └── *.xlsx                # Customer quotation files
│
├── Images/                    # Visual Assets
│   ├── *.png                 # Product images for PDF
│   ├── MGA_1.png             # Company logo
│   └── *.ico                 # Application icons
│
├── docs/                      # Documentation
│   ├── ARCHITECTURE.md       # This file
│   ├── USER_GUIDE.md         # User manual
│   ├── DEVELOPER_GUIDE.md    # Developer documentation
│   └── API_REFERENCE.md      # API documentation
│
└── Legacy/
    └── MGA Window Quotaion.py # Original monolithic implementation
```

---

## **🎯 Core Design Principles**

### **1. Separation of Concerns**
- **UI Layer**: Pure presentation logic, no business rules
- **Business Logic**: Core operations isolated from UI
- **Data Layer**: Persistent storage operations

### **2. Single Responsibility**
- Each module has one clear purpose
- Classes focus on specific functionality
- Methods perform single, well-defined tasks

### **3. Modularity**
- Independent components with clear interfaces
- Loose coupling between modules
- High cohesion within modules

### **4. Singleton Pattern**
- `DataManager`: Single instance for data operations
- `GlobalState`: Centralized state management
- Prevents data inconsistency issues

### **5. Inheritance Hierarchy**
- `BaseProductFrame`: Common functionality for all products
- Product-specific classes extend base functionality
- Code reuse through inheritance

---

## **🔧 System Components**

### **Core Modules**

#### **1. DataManager (`data_manager.py`)**
```python
class DataManager:
    """Singleton class for centralized data operations"""
```

**Responsibilities:**
- Cart management (add, remove, update items)
- Customer data persistence
- Excel file operations (save/load quotations)
- Data validation and integrity
- Rate lookup from pricing database

**Key Methods:**
- `add_item_to_cart()`: Add configured products to cart
- `get_cart_data()`: Retrieve cart DataFrame
- `set_customer_details()`: Store customer information
- `save_quotation_to_excel()`: Export quotation data
- `load_quotation_from_excel()`: Import saved quotations

#### **2. GlobalState (`global_state.py`)**
```python
class GlobalState:
    """Centralized state management with tkinter variables"""
```

**Responsibilities:**
- Manage all UI state variables
- Store product specification options
- Coordinate state between UI components
- Provide validation methods

**Key Components:**
- Customer variables (`custNamVar`, `custAddVar`, `custConVar`)
- Dimension variables (`Width`, `Height`)
- Specification variables (track, materials, glass, hardware)
- Options dictionary (dropdown values for all components)

#### **3. PDF Generator (`pdf_generator.py`)**
```python
class PDF(FPDF):
    """Advanced PDF generation with product images"""
```

**Responsibilities:**
- Generate professional quotation PDFs
- Embed product images and specifications
- Calculate and display cost breakdowns
- Format currency and totals

**Key Features:**
- Multi-page support with automatic breaks
- Product image integration
- Legacy-compatible formatting
- Currency formatting with proper symbols

### **UI Components**

#### **1. MainApplication (`ui/main_app.py`)**
**Primary Interface:**
- Customer details input
- Window type selection
- Dimension specification
- **Responsive Design Integration** - Uses ResponsiveConfig for automatic sizing
- **Professional Styling** - Uses UITheme for consistent appearance
- **Product Frame Factory** - Dynamic creation of product-specific frames

#### **2. BaseProductFrame (`ui/base_product_frame.py`)**
**Template Method Implementation:**
- Common UI layout structure for all product types
- **Responsive Configuration** - ProductFrameConfig for automatic sizing
- **Professional Styling** - Consistent theme application
- Specification input handling
- Cost calculation integration
- Cart management integration

#### **3. Responsive Configuration System (`ui/responsive_config.py`)**
**Cross-Platform Responsive Design:**
- **Screen Detection** - Automatic screen size and DPI detection
- **Scaling Calculation** - Platform-specific scaling factors
- **Window Management** - Intelligent window positioning and sizing
- **Widget Sizing** - Responsive dimensions for all UI elements
- **Cross-Platform Support** - Windows, macOS, and Linux compatibility

#### **4. Professional UI Theme (`ui/ui_theme.py`)**
**Modern Styling System:**
- **Color Palette** - Professional blue-gray color scheme
- **Typography** - Responsive font sizing and cross-platform font selection
- **Widget Styling** - Consistent appearance across all components
- **Theme Integration** - Seamless integration with responsive system
- **Legacy Compatibility** - Backward compatibility with existing code

#### **5. Product-Specific Frames (`ui/product_frames.py`)**
**14 Product Types:**
- Inherits from BaseProductFrame for common functionality
- **Responsive Design** - Automatic adaptation to screen size
- **Professional Styling** - Consistent theme application
- Product-specific specification options
- Dynamic image loading and display
- Cost calculation integration

#### **6. Specialized Views**
- **Cart View** (`ui/cart_view.py`) - Shopping cart management with responsive design
- **Calculator View** (`ui/calculator_view.py`) - Cost calculation with professional styling
- **Invoice View** (`ui/invoice_view.py`) - Invoice generation with responsive layout

## **🧪 Testing Infrastructure**

### **Comprehensive Testing System**
The application includes a complete testing infrastructure using pytest:

#### **Test Categories**
- **Unit Tests** - Individual component testing
- **Integration Tests** - Component interaction testing
- **UI Tests** - User interface testing including responsive design
- **Performance Tests** - Performance benchmarking and stress testing
- **End-to-End Tests** - Complete workflow validation
- **Advanced Tests** - Property-based testing and advanced scenarios

#### **Test Markers**
- `unit`, `integration`, `ui`, `performance`, `end_to_end`
- `slow`, `gui`, `excel`, `pdf`
- `residential`, `commercial`, `industrial`, `special`
- `benchmark`, `stress`, `memory`, `scalability`

#### **Test Coverage**
- **93.1% Code Coverage** - Comprehensive test coverage
- **Automated Reporting** - HTML and terminal coverage reports
- **Performance Benchmarks** - Tracked performance metrics
- **Legacy Compatibility** - Validation against original implementation

---

## **📊 Data Flow Architecture**

### **Customer Data Flow**
```
1. User Input (MainApplication)
   ↓
2. GlobalState Variables (custNamVar, custAddVar, custConVar)
   ↓
3. DataManager.set_customer_details()
   ↓
4. Persistent Storage & PDF Generation
```

### **Product Configuration Flow**
```
1. Product Selection (MainApplication.selector())
   ↓
2. Product Frame Creation (product_frames.py)
   ↓
3. Specification Input (BaseProductFrame)
   ↓
4. Cost Calculation (calculate_cost())
   ↓
5. Cart Addition (DataManager.add_item_to_cart())
```

### **Cart to PDF Flow**
```
1. Cart Data (DataManager.get_cart_data())
   ↓
2. Customer Details (DataManager.get_customer_details())
   ↓
3. Cost Calculations (CalculatorView)
   ↓
4. PDF Generation (pdf_generator.create_quotation_pdf())
```

---

## **🎨 UI Architecture**

### **Layout Pattern**
All product configuration windows follow a consistent 3-frame layout:

```
┌─────────────────────────────────────────┐
│           Frame 2: Customer Details     │
│           (Read-only display)           │
├─────────────────────────────────────────┤
│           Frame 0: Dimensions & Cost    │
│           (Width, Height, Calculate)    │
├─────────────────────────────────────────┤
│           Frame 1: Specifications       │
│           (Scrollable, Product-specific)│
└─────────────────────────────────────────┘
```

### **Theme System**
- **Colors**: Professional Blue (#1E40AF) + Gray palette
- **Typography**: Segoe UI with fallbacks
- **Spacing**: Consistent 10px padding system
- **Buttons**: Primary/Secondary/Success color coding

### **State Synchronization**
- All UI widgets bound to `GlobalState` variables
- Real-time updates across components
- Consistent state throughout application lifecycle

---

## **🔗 Module Dependencies**

### **Dependency Graph**
```
__main__.py
    ↓
ui/main_app.py
    ↓
├── global_state.py (Singleton)
├── data_manager.py (Singleton)
├── ui/product_frames.py
│   ↓
│   ui/base_product_frame.py
├── ui/cart_view.py
├── ui/calculator_view.py
└── ui/invoice_view.py
    ↓
    pdf_generator.py
```

### **External Dependencies**
- **tkinter**: GUI framework (built-in Python)
- **pandas**: Data manipulation and Excel operations
- **fpdf**: PDF generation
- **PIL/Pillow**: Image processing
- **babel**: Currency formatting

---

## **🎭 Design Patterns**

### **1. Singleton Pattern**
```python
# DataManager and GlobalState use singleton pattern
def get_global_state():
    if not hasattr(get_global_state, 'instance'):
        get_global_state.instance = GlobalState()
    return get_global_state.instance
```

**Benefits:**
- Single source of truth for application state
- Prevents data inconsistency
- Memory efficient

### **2. Template Method Pattern**
```python
# BaseProductFrame defines common workflow
class BaseProductFrame:
    def create_legacy_layout(self):
        self.create_customer_display()  # Common
        self.create_dimensions_frame()  # Common
        self.create_specifications()    # Template method - overridden
```

**Benefits:**
- Code reuse across 14 product types
- Consistent UI layout
- Easy to add new product types

### **3. Observer Pattern (Implicit)**
- tkinter variables automatically notify bound widgets
- State changes propagate throughout UI
- Real-time updates without manual coordination

### **4. Factory Pattern (Implicit)**
```python
# MainApplication.selector() creates appropriate product frame
frame_class = self.product_frames.get(selected_window)
frame = frame_class(product_window, self.data_manager)
```

---

## **⚡ Performance Considerations**

### **Memory Management**
- **Singleton Pattern**: Prevents multiple instances of core components
- **Widget Cleanup**: Proper destruction of temporary windows
- **Image Caching**: PIL images loaded once and reused

### **UI Responsiveness**
- **Lazy Loading**: Product frames created only when needed
- **Debounced Search**: `handleWait()` prevents excessive filtering
- **Efficient Layouts**: Grid management for optimal rendering

### **Data Operations**
- **pandas DataFrames**: Efficient cart operations
- **Excel Optimization**: Targeted read/write operations
- **Validation Caching**: Reuse validation results

### **PDF Generation**
- **Incremental Building**: Pages created as needed
- **Image Optimization**: Automatic resizing for PDF inclusion
- **Memory Cleanup**: Proper resource disposal

---

## **🔧 Extension Points**

### **Adding New Product Types**
1. Create new class in `product_frames.py` inheriting from `BaseProductFrame`
2. Override `create_specifications()` method
3. Add product mapping in `MainApplication.product_frames`
4. Add product image to `Images/` directory
5. Update `pdf_generator.py` RATIO and image mappings

### **Enhancing UI**
- Modify `ui_theme.py` for styling changes
- Extend `BaseProductFrame` for new common functionality
- Add new specialized views in `ui/` directory

### **Data Integration**
- Extend `DataManager` for new data sources
- Add methods for additional file formats
- Implement database connectivity

---

## **📝 Conclusion**

The new architecture provides:

- **Maintainability**: Clear separation of concerns
- **Scalability**: Modular design supports growth
- **Reliability**: Singleton pattern ensures consistency
- **Performance**: Optimized operations and UI responsiveness
- **Extensibility**: Well-defined extension points
- **Quality**: 93.1% test coverage with enterprise standards

This architecture successfully transforms the legacy monolithic codebase into a modern, professional application ready for production deployment and future enhancements. 