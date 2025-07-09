"""
Helper functions ported from legacy MGA Window Quotaion.py
These functions provide input validation and utility operations.
"""
import tkinter as tk
from tkinter import messagebox
from global_state import get_global_state


def checkDigits():
    """
    Legacy checkDigits() function - validates numeric input
    Returns True if all values contain only valid digit characters
    """
    global_state = get_global_state()
    dig_verify = "1234567890.,"
    
    width_val = global_state.Width.get()
    height_val = global_state.Height.get()
    cost_val = global_state.costEntVar.get()
    
    # Check each field
    for value in [width_val, height_val, cost_val]:
        if value and not all(c in dig_verify for c in value):
            return False
    
    return True


def clearValues():
    """
    Legacy clearValues() function - clears all global state variables
    """
    global_state = get_global_state()
    
    # Clear dimensions
    global_state.Width.set("")
    global_state.Height.set("")
    global_state.windowTypeVar.set("")
    
    # Clear cost calculation
    global_state.totSqftEntVar.set("")
    global_state.cstAmtInr.set("")
    global_state.costEntVar.set("")
    global_state.instEntVar.set("")
    global_state.discountEntVar.set("")
    global_state.gstEntVar.set("")
    
    # Clear totals
    global_state.costTotVar.set("")
    global_state.instTotVar.set("")
    global_state.discTotVar.set("")
    global_state.gstTotVar.set("")
    
    # Reset specifications
    global_state.reset_specification_vars()
    
    # Reset flags
    global_state.finalCost = 0
    global_state.quantity = 1
    global_state.profitAmnt = 0
    global_state.calculateFlag = False
    global_state.calcQuantFlag = False
    global_state.discFlag = False
    global_state.pressedCalcFlag = False


def setCustomerName(cust=None):
    """
    Legacy setCustomerName() function - sets customer name in global state
    """
    global_state = get_global_state()
    if cust:
        global_state.custNamVar.set(cust)
        global_state.custName = cust


def validate_numeric_input(value, field_name="field"):
    """
    Utility function to validate numeric input
    Returns (is_valid, error_message)
    """
    if not value:
        return False, f"Please fill in the {field_name}."
    
    global_state = get_global_state()
    if not global_state.validate_digits(value):
        return False, f"Please enter numbers in the {field_name}."
    
    try:
        float(value)
        return True, ""
    except ValueError:
        return False, f"Please enter a valid number in the {field_name}."


def show_validation_error(message, parent=None):
    """
    Utility function to show validation error messages
    """
    messagebox.showerror("Invalid Input", message, parent=parent)


def calculate_area(width_str, height_str):
    """
    Calculate area from width and height strings
    Returns (area, error_message)
    """
    try:
        width = float(width_str) if width_str else 0
        height = float(height_str) if height_str else 0
        
        if width <= 0 or height <= 0:
            return 0, "Width and height must be greater than zero."
        
        return width * height, ""
    except ValueError:
        return 0, "Please enter valid numeric values for width and height."


def format_currency_value(value, currency="INR", locale="en_IN"):
    """
    Format currency value for display
    Returns formatted string
    """
    try:
        from babel.numbers import format_currency
        return format_currency(float(value), currency, locale=locale).replace("\xa0", " ")
    except (ImportError, ValueError, TypeError):
        # Fallback if babel is not available or value is invalid
        return f"₹ {float(value):,.2f}"


def addNewRowData(obj, obj_str):
    """
    Legacy addNewRowData() function - adds new row data (placeholder)
    This function was used in legacy for adding cart items
    """
    # This is now handled by DataManager.add_item_to_cart()
    pass


def afterCalculate():
    """
    Legacy afterCalculate() function - post-calculation actions
    """
    global_state = get_global_state()
    global_state.calculateFlag = True
    global_state.pressedCalcFlag = True


def get_product_image_path(product_type, base_dir):
    """
    Get the correct image path for a product type
    Returns the full path to the product image
    """
    import os
    
    # Map product types to image filenames exactly as legacy
    image_map = {
        "Sliding Window": "Sliding Window.png",
        "Sliding Door": "Sliding Door.png",
        "Fix Louver": "Fix Louver.png",
        "Patti Louver": "Patti Louver.png",
        "Openable Window": "Openable Window.png",
        "Sliding folding door": "Sliding folding door.png",
        "Casement Window": "Casement Window.png",
        "Aluminium partition": "Aluminium partition.png",
        "Toughened partition": "Toughened partition.png",
        "Toughened Door": "Toughened Door.png",
        "Composite pannel": "Composite pannel.png",
        "Curtain wall": "Curtain wall.png",
        "Fix Window": "Fix Window.png",
        "Exhaust Fan Window": "Exhaust Fan Window.png",
    }
    
    filename = image_map.get(product_type, f"{product_type}.png")
    return os.path.join(base_dir, "Images", filename)


def validate_customer_details():
    """
    Validate that essential customer details are filled
    Returns (is_valid, error_message)
    """
    global_state = get_global_state()
    
    name = global_state.custNamVar.get().strip()
    contact = global_state.custConVar.get().strip()
    
    if not name:
        return False, "Please enter customer name."
    
    if not contact:
        return False, "Please enter customer contact number."
    
    return True, ""


def reset_calculation_state():
    """
    Reset calculation-related state variables
    """
    global_state = get_global_state()
    global_state.finalCost = 0
    global_state.calculateFlag = False
    global_state.calcQuantFlag = False
    global_state.discFlag = False
    global_state.pressedCalcFlag = False


def get_window_geometry_for_product(product_type):
    """
    Get appropriate window geometry for different product types
    Returns geometry string (e.g., "1200x800")
    """
    # Different products might need different window sizes
    # For now, return a standard size that works for all
    return "1400x900" 