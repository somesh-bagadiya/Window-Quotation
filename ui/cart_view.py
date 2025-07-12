import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename
from babel.numbers import format_currency
from datetime import datetime
from random import randint
from pdf_generator import create_quotation_pdf
from global_state import get_global_state
import pandas as pd


class CartView(tk.Toplevel):
    def __init__(self, parent_window, data_manager, main_app=None):
        super().__init__(parent_window)
        self.parent_window = parent_window  # This is the root tk window
        self.main_app = main_app  # This is the MainApplication instance
        self.data_manager = data_manager
        self.global_state = get_global_state()
        
        self.title("Cart & Calculation")
        
        # Center the window on screen
        self.center_window()
        
        self.attributes("-topmost", True)

        # Store quantity Entry widgets for each row
        self.quantity_entries = []

        # Calculator variables exactly as legacy
        self.discount_var = tk.StringVar()
        self.installation_var = tk.StringVar()
        self.gst_var = tk.StringVar(value="18")
        
        self.cost_total_var = tk.StringVar()
        self.discount_total_var = tk.StringVar()
        self.installation_total_var = tk.StringVar()
        self.gst_total_var = tk.StringVar()
        
        # Date selection variables for quotations
        self.quotation_day_var = tk.StringVar()
        self.quotation_month_var = tk.StringVar()
        self.quotation_year_var = tk.StringVar()
        self.use_custom_quotation_date_var = tk.BooleanVar(value=False)
        
        # Flags exactly as legacy
        self.calculation_done = False

        self.create_widgets()
        self.populate_cart()
        self.load_initial_data()

    def toggle_quotation_date_selection(self):
        """Toggle quotation date selection widgets based on checkbox state"""
        if self.use_custom_quotation_date_var.get():
            # Enable date selection
            self.quotation_day_combo.config(state="readonly")
            self.quotation_month_combo.config(state="readonly")
            self.quotation_year_combo.config(state="readonly")
            
            # Set current date as default
            current_date = datetime.now()
            self.quotation_day_var.set(str(current_date.day))
            self.quotation_month_var.set(str(current_date.month))
            self.quotation_year_var.set(str(current_date.year))
        else:
            # Disable date selection
            self.quotation_day_combo.config(state="disabled")
            self.quotation_month_combo.config(state="disabled")
            self.quotation_year_combo.config(state="disabled")
            
            # Clear date values
            self.quotation_day_var.set("")
            self.quotation_month_var.set("")
            self.quotation_year_var.set("")

    def get_quotation_date(self):
        """Get the quotation date - either custom or current date"""
        if self.use_custom_quotation_date_var.get():
            try:
                day = int(self.quotation_day_var.get())
                month = int(self.quotation_month_var.get())
                year = int(self.quotation_year_var.get())
                return datetime(year, month, day)
            except (ValueError, TypeError):
                # If invalid date, fall back to current date
                return datetime.now()
        else:
            return datetime.now()

    def center_window(self):
        """Center the window on screen with unified responsive centering"""
        # Get responsive configuration
        from ui.responsive_config import get_responsive_config
        responsive = get_responsive_config()
        
        # Use unified centering system for consistent positioning
        responsive.center_cart_window(self)

    def create_widgets(self):
        """Create redesigned cart layout with clear sections"""
        # Configure main window grid
        self.grid_rowconfigure(1, weight=1)  # Cart section gets most space
        self.grid_columnconfigure(0, weight=1)
        
        # ============= SECTION 1: CUSTOMER DETAILS =============
        self.create_customer_section()
        
        # ============= SECTION 2: CART MANAGEMENT =============
        self.create_cart_section()
        
        # ============= SECTION 3: COST CALCULATION =============
        self.create_calculation_section()
        
        # ============= SECTION 4: FINAL ACTIONS =============
        self.create_final_actions_section()

    def create_customer_section(self):
        """Create customer details section (read-only display)"""
        customer_frame = tk.LabelFrame(
            self, text="Customer Details", font=("Arial", 12, "bold"),
            relief=tk.GROOVE, borderwidth=2, bg="#f8f9fa"
        )
        customer_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        customer_frame.grid_columnconfigure(1, weight=1)
        customer_frame.grid_columnconfigure(3, weight=1)
        
        # Customer Name
        tk.Label(customer_frame, text="Name:", font=("Arial", 10, "bold"), bg="#f8f9fa").grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        tk.Label(customer_frame, textvariable=self.global_state.custNamVar, 
                font=("Arial", 10), bg="#f8f9fa").grid(
            row=0, column=1, padx=10, pady=5, sticky="w"
        )
        
        # Customer Contact
        tk.Label(customer_frame, text="Contact:", font=("Arial", 10, "bold"), bg="#f8f9fa").grid(
            row=0, column=2, padx=10, pady=5, sticky="w"
        )
        tk.Label(customer_frame, textvariable=self.global_state.custConVar,
                font=("Arial", 10), bg="#f8f9fa").grid(
            row=0, column=3, padx=10, pady=5, sticky="w"
        )
        
        # Customer Address
        tk.Label(customer_frame, text="Address:", font=("Arial", 10, "bold"), bg="#f8f9fa").grid(
            row=1, column=0, padx=10, pady=5, sticky="nw"
        )
        address_label = tk.Label(customer_frame, text=self.global_state.address,
                                font=("Arial", 10), bg="#f8f9fa", wraplength=400, justify="left")
        address_label.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky="w")

    def create_cart_section(self):
        """Create cart management section with items table and actions"""
        cart_frame = tk.LabelFrame(
            self, text="Cart Management", font=("Arial", 12, "bold"),
            relief=tk.GROOVE, borderwidth=2
        )
        cart_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        cart_frame.grid_rowconfigure(0, weight=1)  # Table gets most space
        cart_frame.grid_columnconfigure(0, weight=1)
        
        # Scrollable cart table
        self.create_cart_table(cart_frame)
        
        # Cart action buttons
        cart_actions_frame = tk.Frame(cart_frame, bg="#e9ecef")
        cart_actions_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        
        # Cart management buttons
        tk.Button(
            cart_actions_frame, text="Add More Items", 
            command=self.add_more_items, width=15,
            bg="#17a2b8", fg="white", font=("Arial", 10, "bold")
        ).pack(side="left", padx=5, pady=5)
        
        tk.Button(
            cart_actions_frame, text="Update Quantities", 
            command=self.calculate_quantity, width=18,
            bg="#28a745", fg="white", font=("Arial", 10, "bold")
        ).pack(side="left", padx=5, pady=5)
        
        # Total display on the right
        total_frame = tk.Frame(cart_actions_frame, bg="#e9ecef")
        total_frame.pack(side="right", padx=5, pady=5)
        
        tk.Label(total_frame, text="Cart Total:", font=("Arial", 12, "bold"), bg="#e9ecef").pack(side="left")
        self.cart_total_label = tk.Label(total_frame, text="₹0.00", 
                                        font=("Arial", 12, "bold"), fg="#007bff", bg="#e9ecef")
        self.cart_total_label.pack(side="left", padx=(5, 0))

    def create_cart_table(self, parent):
        """Create scrollable cart items table"""
        # Table container with scrollbar
        table_container = tk.Frame(parent)
        table_container.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        table_container.grid_rowconfigure(0, weight=1)
        table_container.grid_columnconfigure(0, weight=1)
        
        # Canvas and scrollbar for cart items
        canvas = tk.Canvas(table_container, bg="white")
        scrollbar = tk.Scrollbar(table_container, orient="vertical", command=canvas.yview)
        
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Scrollable frame inside canvas
        self.cart_items_frame = tk.Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=self.cart_items_frame, anchor="nw")
        
        self.canvas = canvas

        # Create table headers
        headers = ["Sr.No", "Product Type", "Width (ft)", "Height (ft)", "Area (sq.ft)", "Rate (₹)", "Cost/Item (₹)", "Qty", "Total Cost (₹)", "Action"]
        header_widths = [6, 18, 10, 10, 10, 12, 15, 6, 15, 8]
        
        for i, (header, width) in enumerate(zip(headers, header_widths)):
            tk.Label(
                self.cart_items_frame, text=header, font=("Arial", 10, "bold"),
                bg="#6c757d", fg="white", relief=tk.RAISED, width=width
            ).grid(row=0, column=i, padx=1, pady=1, sticky="ew")

    def create_calculation_section(self):
        """Create cost calculation section"""
        calc_frame = tk.LabelFrame(
            self, text="Cost Calculation", font=("Arial", 12, "bold"),
            relief=tk.GROOVE, borderwidth=2, bg="#fff3cd"
        )
        calc_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
        calc_frame.grid_columnconfigure(1, weight=1)
        calc_frame.grid_columnconfigure(3, weight=1)
        
        # Row 0: Headers
        tk.Label(calc_frame, text="Enter Values", font=("Arial", 11, "bold"), bg="#fff3cd").grid(
            row=0, column=1, padx=10, pady=5
        )
        tk.Label(calc_frame, text="Calculated Totals", font=("Arial", 11, "bold"), bg="#fff3cd").grid(
            row=0, column=3, padx=10, pady=5
        )
        
        # Row 1: Cart Total (read-only)
        tk.Label(calc_frame, text="Cart Total:", font=("Arial", 10), bg="#fff3cd").grid(
            row=1, column=0, padx=10, pady=5, sticky="e"
        )
        tk.Entry(calc_frame, textvariable=self.cost_total_var, state="readonly", width=20,
                font=("Arial", 10), justify="right").grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        # Row 2: Discount
        tk.Label(calc_frame, text="Discount Amount:", font=("Arial", 10), bg="#fff3cd").grid(
            row=2, column=0, padx=10, pady=5, sticky="e"
        )
        tk.Entry(calc_frame, textvariable=self.discount_var, width=20,
                font=("Arial", 10), justify="right").grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        tk.Label(calc_frame, text="After Discount:", font=("Arial", 10), bg="#fff3cd").grid(
            row=2, column=2, padx=10, pady=5, sticky="e"
        )
        tk.Entry(calc_frame, textvariable=self.discount_total_var, state="readonly", width=20,
                font=("Arial", 10), justify="right").grid(row=2, column=3, padx=10, pady=5, sticky="w")
        
        # Row 3: GST
        tk.Label(calc_frame, text="GST (%):", font=("Arial", 10), bg="#fff3cd").grid(
            row=3, column=0, padx=10, pady=5, sticky="e"
        )
        tk.Entry(calc_frame, textvariable=self.gst_var, width=20,
                font=("Arial", 10), justify="right").grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        tk.Label(calc_frame, text="With GST:", font=("Arial", 10), bg="#fff3cd").grid(
            row=3, column=2, padx=10, pady=5, sticky="e"
        )
        tk.Entry(calc_frame, textvariable=self.gst_total_var, state="readonly", width=20,
                font=("Arial", 10), justify="right").grid(row=3, column=3, padx=10, pady=5, sticky="w")
        
        # Row 4: Installation
        tk.Label(calc_frame, text="Installation Charges:", font=("Arial", 10), bg="#fff3cd").grid(
            row=4, column=0, padx=10, pady=5, sticky="e"
        )
        tk.Entry(calc_frame, textvariable=self.installation_var, width=20,
                font=("Arial", 10), justify="right").grid(row=4, column=1, padx=10, pady=5, sticky="w")
        
        tk.Label(calc_frame, text="Final Total:", font=("Arial", 10, "bold"), bg="#fff3cd").grid(
            row=4, column=2, padx=10, pady=5, sticky="e"
        )
        tk.Entry(calc_frame, textvariable=self.installation_total_var, state="readonly", width=20,
                font=("Arial", 10, "bold"), justify="right").grid(row=4, column=3, padx=10, pady=5, sticky="w")
        
        # Calculate button
        tk.Button(
            calc_frame, text="CALCULATE FINAL COSTS", 
            command=self.calculate_cost, width=25,
            bg="#ffc107", fg="black", font=("Arial", 11, "bold")
        ).grid(row=5, column=0, columnspan=4, pady=15)

    def create_final_actions_section(self):
        """Create final actions section for PDF and Invoice generation"""
        actions_frame = tk.LabelFrame(
            self, text="Generate Documents", font=("Arial", 12, "bold"),
            relief=tk.GROOVE, borderwidth=2, bg="#d1ecf1"
        )
        actions_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
        
        # Date selection for quotations
        date_container = tk.Frame(actions_frame, bg="#d1ecf1")
        date_container.pack(expand=True, pady=(10, 5))
        
        # Checkbox for custom quotation date
        use_custom_check = tk.Checkbutton(
            date_container,
            text="Custom Quotation Date:",
            variable=self.use_custom_quotation_date_var,
            command=self.toggle_quotation_date_selection,
            bg="#d1ecf1",
            font=("Arial", 10, "bold")
        )
        use_custom_check.pack(side="left", padx=5)
        
        # Date selection frame
        self.quotation_date_frame = tk.Frame(date_container, bg="#d1ecf1")
        self.quotation_date_frame.pack(side="left", padx=10)
        
        # Day dropdown
        tk.Label(self.quotation_date_frame, text="Day:", bg="#d1ecf1").grid(row=0, column=0, sticky="w")
        self.quotation_day_combo = ttk.Combobox(
            self.quotation_date_frame,
            textvariable=self.quotation_day_var,
            values=[str(i) for i in range(1, 32)],
            width=5,
            state="disabled"
        )
        self.quotation_day_combo.grid(row=0, column=1, padx=(2, 5))
        
        # Month dropdown
        tk.Label(self.quotation_date_frame, text="Month:", bg="#d1ecf1").grid(row=0, column=2, sticky="w")
        self.quotation_month_combo = ttk.Combobox(
            self.quotation_date_frame,
            textvariable=self.quotation_month_var,
            values=[str(i) for i in range(1, 13)],
            width=5,
            state="disabled"
        )
        self.quotation_month_combo.grid(row=0, column=3, padx=(2, 5))
        
        # Year dropdown
        tk.Label(self.quotation_date_frame, text="Year:", bg="#d1ecf1").grid(row=0, column=4, sticky="w")
        current_year = datetime.now().year
        self.quotation_year_combo = ttk.Combobox(
            self.quotation_date_frame,
            textvariable=self.quotation_year_var,
            values=[str(i) for i in range(current_year - 5, current_year + 5)],
            width=8,
            state="disabled"
        )
        self.quotation_year_combo.grid(row=0, column=5, padx=(2, 0))
        
        # Center the buttons
        button_container = tk.Frame(actions_frame, bg="#d1ecf1")
        button_container.pack(expand=True, pady=15)
        
        tk.Button(
            button_container, text="Generate PDF Quote", 
            command=self.generate_pdf, width=20,
            bg="#007bff", fg="white", font=("Arial", 11, "bold")
        ).pack(side="left", padx=10)
        
        tk.Button(
            button_container, text="Create Invoice", 
            command=self.open_invoice, width=20,
            bg="#28a745", fg="white", font=("Arial", 11, "bold")
        ).pack(side="left", padx=10)
        
        tk.Button(
            button_container, text="Save Cart", 
            command=self.save_cart_to_excel, width=15,
            bg="#6c757d", fg="white", font=("Arial", 11, "bold")
        ).pack(side="left", padx=10)

    def populate_cart(self):
        """Populate cart with items in the new table format"""
        # Clear existing items (except header)
        for widget in self.cart_items_frame.winfo_children():
            row = widget.grid_info().get("row", 0)
            if row > 0:  # Keep header row (row 0)
                widget.destroy()
        
        self.quantity_entries = []
        cart_df = self.data_manager.get_cart_data()

        if cart_df.empty:
            tk.Label(
                self.cart_items_frame, text="No items in cart", 
                font=("Arial", 12, "italic"), fg="gray", bg="white"
            ).grid(row=1, column=0, columnspan=10, pady=20)
            return

        # Populate each row
        for i, (index, row) in enumerate(cart_df.iterrows()):
            self.create_cart_table_row(i + 1, row)  # +1 to skip header
        
        # Update canvas scroll region
        self.cart_items_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        # Update cart total display
        self.update_cart_total_display()

    def create_cart_table_row(self, row_num, data_row):
        """Create a single row in the cart table"""
        bg_color = "#f8f9fa" if row_num % 2 == 0 else "white"
        
        # Sr.No
        tk.Label(self.cart_items_frame, text=str(row_num), bg=bg_color, width=6).grid(
            row=row_num, column=0, padx=1, pady=1, sticky="ew"
        )
        
        # Product Type
        tk.Label(self.cart_items_frame, text=data_row.get("Particulars", ""), 
                bg=bg_color, width=18).grid(row=row_num, column=1, padx=1, pady=1, sticky="ew")
        
        # Width & Height
        width_val = data_row.get("Width", 0)
        height_val = data_row.get("Height", 0)
        tk.Label(self.cart_items_frame, text=str(width_val), 
                bg=bg_color, width=10).grid(row=row_num, column=2, padx=1, pady=1, sticky="ew")
        tk.Label(self.cart_items_frame, text=str(height_val), 
                bg=bg_color, width=10).grid(row=row_num, column=3, padx=1, pady=1, sticky="ew")
        
        # Calculate Area (Width × Height) - use stored Total Sq.ft if available
        try:
            # First try to use the stored Total Sq.ft (more accurate)
            stored_area = data_row.get("Total Sq.ft", None)
            if stored_area is not None and stored_area != "":
                area = float(stored_area)
                area_formatted = f"{area:.2f}"
            else:
                # Fall back to calculating from width and height
                width_float = float(str(width_val).replace("'", "").replace('"', ''))
                height_float = float(str(height_val).replace("'", "").replace('"', ''))
                area = width_float * height_float
                area_formatted = f"{area:.2f}"
        except (ValueError, TypeError):
            area = 0
            area_formatted = "0.00"
        tk.Label(self.cart_items_frame, text=area_formatted, bg=bg_color, width=10).grid(
            row=row_num, column=4, padx=1, pady=1, sticky="ew"
        )
        
        # Rate per sq.ft - use stored Cost (INR) as rate per sq.ft directly
        try:
            # Cost (INR) should now be stored as rate per sq.ft from the product page
            cost_per_sqft = data_row.get("Cost (INR)", 0)
            if isinstance(cost_per_sqft, str):
                cost_per_sqft = float(str(cost_per_sqft).replace("₹", "").replace(",", ""))
            else:
                cost_per_sqft = float(cost_per_sqft)
            rate_formatted = f"₹{cost_per_sqft:,.2f}"
        except (ValueError, TypeError):
            cost_per_sqft = 0
            rate_formatted = "₹0.00"
        tk.Label(self.cart_items_frame, text=rate_formatted, bg=bg_color, width=12).grid(
            row=row_num, column=5, padx=1, pady=1, sticky="ew"
        )
        
        # Cost per Item (Area × Rate)
        try:
            cost_per_item = area * cost_per_sqft
            cost_per_item_formatted = f"₹{cost_per_item:,.2f}"
        except (ValueError, TypeError):
            cost_per_item = 0
            cost_per_item_formatted = "₹0.00"
        tk.Label(self.cart_items_frame, text=cost_per_item_formatted, bg=bg_color, width=15).grid(
            row=row_num, column=6, padx=1, pady=1, sticky="ew"
        )
        
        # Quantity (editable)
        quantity_var = tk.StringVar(value=str(data_row.get("Quantity", 1)))
        quantity_entry = tk.Entry(
            self.cart_items_frame, textvariable=quantity_var, 
            width=6, justify="center", font=("Arial", 10)
        )
        quantity_entry.grid(row=row_num, column=7, padx=1, pady=1)
        self.quantity_entries.append((data_row.get("Sr.No", row_num), quantity_var))
        
        # Total Cost (Area × Rate × Quantity)
        try:
            quantity = float(data_row.get("Quantity", 1))
            total_cost = cost_per_item * quantity
            total_cost_formatted = f"₹{total_cost:,.2f}"
        except (ValueError, TypeError):
            total_cost_formatted = "₹0.00"
        tk.Label(self.cart_items_frame, text=total_cost_formatted, bg=bg_color, width=15).grid(
            row=row_num, column=8, padx=1, pady=1, sticky="ew"
        )
        
        # Delete button
        delete_btn = tk.Button(
            self.cart_items_frame, text="✕", font=("Arial", 8, "bold"), 
            width=8, fg="red", bg=bg_color,
            command=lambda sr_no=data_row.get("Sr.No", row_num): self.delete_row(sr_no)
        )
        delete_btn.grid(row=row_num, column=9, padx=1, pady=1)

    def update_cart_total_display(self):
        """Update the cart total display"""
        total_amount = self.data_manager.get_cart_total_amount()
        formatted_total = format_currency(total_amount, "INR", locale="en_IN").replace("\xa0", " ")
        self.cart_total_label.config(text=formatted_total)

    def load_initial_data(self):
        """Load initial data exactly as legacy"""
        # Get total cost from cart
        total_cost = self.data_manager.get_cart_total_amount()
        indCurr = lambda x: format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")
        self.cost_total_var.set(indCurr(total_cost))

    def calculate_cost(self):
        """Calculate costs exactly as legacy calculateCost() method"""
        self.calculation_done = True

        if self.gst_var.get() == "":
            messagebox.showerror(
                "Invalid", "Please fill GST percentage", parent=self
            )
            return False

        indCurr = lambda x: format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")
        
        # Get total cost and convert to float
        total_cost_str = self.cost_total_var.get()
        totalcost = float(total_cost_str[1:].replace(",", ""))

        discountedCost = 0.0
        installationCost = 0.0
        gstCost = 0.0
        finalTotal = 0.0
        
        # Get GST percentage from input
        gst_percent = float(self.gst_var.get())

        # Parse discount and installation, treat empty as zero
        discount_val = float(self.discount_var.get()) if self.discount_var.get() else 0.0
        installation_val = float(self.installation_var.get()) if self.installation_var.get() else 0.0

        # Calculate discounted cost
        discountedCost = totalcost - discount_val
        # Calculate GST
        gstCost = discountedCost + (discountedCost * gst_percent / 100)
        # Calculate final total
        finalTotal = gstCost + installation_val

        # Set all calculated fields
        self.discount_total_var.set(indCurr(discountedCost))
        self.gst_total_var.set(indCurr(gstCost))
        self.installation_total_var.set(indCurr(finalTotal))

        print(totalcost, discountedCost, installation_val, gstCost, finalTotal)

    def calculate_quantity(self):
        """Calculate quantities exactly as legacy calcQuant() method"""
        try:
            # Update quantities from Entry widgets
            for sr_no, quantity_var in self.quantity_entries:
                try:
                    new_quantity = int(float(quantity_var.get()))
                    if new_quantity < 1:
                        raise ValueError("Quantity must be positive")
                    self.data_manager.update_item_quantity(sr_no, new_quantity)
                except ValueError:
                    messagebox.showerror(
                        "Invalid Quantity", 
                        f"Please enter a valid positive number for item {sr_no}.",
                        parent=self
                    )
                    return

            # Recalculate all totals
            self.data_manager.recalculate_cart_totals()
            
            # Refresh the display
            self.populate_cart()
            self.load_initial_data()
            
            messagebox.showinfo("Success", "Quantities updated successfully!", parent=self)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating quantities: {str(e)}", parent=self)

    def delete_row(self, sr_no):
        """Delete a cart row exactly as legacy deleteRow() method"""
        if messagebox.askyesno(
            "Confirm Delete", f"Are you sure you want to delete item {sr_no}?", parent=self
        ):
            self.data_manager.remove_item_from_cart(sr_no)
            self.populate_cart()
            self.load_initial_data()

    def add_more_items(self):
        """Add more items exactly as legacy addNewItem() method"""
        # Save current cart data to Excel first (as legacy does)
        customer_name = self.global_state.custNamVar.get()
        if customer_name:
            filename = f"./Data/{customer_name}_QuatationData.xlsx"
            success, message = self.data_manager.save_quotation_to_excel(filename)
            if success:
                print(f"Cart saved to {filename}")
        
        # Close cart and return to main window
        self.destroy()

    def generate_pdf(self):
        """Generate PDF exactly as legacy generatePDF() method"""
        if not self.calculation_done:
            messagebox.showerror(
                "Invalid", "Please calculate final costs first by clicking 'CALCULATE FINAL COSTS'", parent=self
            )
            return False

        self.attributes("-topmost", False)

        # Generate quotation number exactly as legacy
        today = datetime.now()
        quotation_number = (
            "QUO"
            + "/"
            + str(today.day)
            + str(today.month)
            + "-"
            + str(today.year)
            + "/"
            + str(randint(100, 999))
        )

        prog = tk.Toplevel()
        screen_width = self.parent_window.winfo_screenwidth()
        screen_height = self.parent_window.winfo_screenheight()
        x = (screen_width - (screen_width / 2.8)) / 2
        y = ((screen_height / 1.5)) / 2 + 100
        prog.geometry("+%d+%d" % (x, y))
        prog.title("Generating PDF...")

        tk.Label(
            prog,
            text="PDF is generating, please wait...",
            font=("Arial", 12, "bold"), padx=20, pady=20
        ).pack()
        
        files = [("PDF Files", "*.pdf"), ("All Files", "*.*")]
        file = asksaveasfilename(filetypes=files, defaultextension=".pdf", parent=self)
        
        if not file:
            prog.destroy()
            self.attributes("-topmost", True)
            return
        
        try:
            customer_details = self.data_manager.get_customer_details()
            cart_items = self.data_manager.get_cart_data()

            # Prepare final costs
            final_costs = {
                "discount": float(self.discount_var.get()) if self.discount_var.get() else 0,
                "installation": float(self.installation_var.get()) if self.installation_var.get() else 0,
                "gst_percent": float(self.gst_var.get()),
                "quotation_number": quotation_number,
                "quotation_date": self.get_quotation_date()  # Add custom/current date
            }

            prog.attributes("-topmost", True)
            
            # Generate PDF using the pdf_generator
            create_quotation_pdf(file, customer_details, cart_items, final_costs)
            
            prog.destroy()
            self.attributes("-topmost", True)
            
            messagebox.showinfo("Success", "PDF generated successfully!", parent=self)

        except Exception as e:
            prog.destroy()
            self.attributes("-topmost", True)
            messagebox.showerror("Error", f"Error generating PDF: {str(e)}", parent=self)

    def open_invoice(self):
        """Open invoice exactly as legacy callInvoice() method"""
        if not self.calculation_done:
            messagebox.showerror(
                "Invalid", "Please calculate final costs first by clicking 'CALCULATE FINAL COSTS'", parent=self
            )
            return False

        # Import InvoiceView here to avoid circular import
        try:
            from ui.invoice_view import InvoiceView
            
            # Prepare final costs data for invoice
            final_costs = {
                "discount": float(self.discount_var.get()) if self.discount_var.get() else 0,
                "installation": float(self.installation_var.get()) if self.installation_var.get() else 0,
                "gst_percent": float(self.gst_var.get()),
                "discount_total": self.discount_total_var.get(),
                "installation_total": self.installation_total_var.get(), 
                "gst_total": self.gst_total_var.get(),
                "total_cost": self.cost_total_var.get()
            }
            
            self.destroy()
            invoice_view = InvoiceView(self.parent_window, self.data_manager, final_costs)
        except ImportError:
            messagebox.showinfo("Coming Soon", "Invoice functionality will be available soon.", parent=self)

    def save_cart_to_excel(self):
        """Save current cart data to Excel file in Data folder"""
        try:
            # Get customer name for filename
            customer_name = self.global_state.custNamVar.get()
            if not customer_name.strip():
                customer_name = "UnknownCustomer"
            
            # Clean customer name for filename (remove invalid characters)
            import re
            clean_name = re.sub(r'[<>:"/\\|?*]', '_', customer_name)
            
            # Generate filename with timestamp
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{clean_name}_Cart_{timestamp}.xlsx"
            
            # Create full path in Data folder
            import os
            data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data")
            if not os.path.exists(data_folder):
                os.makedirs(data_folder)
            
            full_path = os.path.join(data_folder, filename)
            
            # Save cart data using data_manager
            success, message = self.data_manager.save_quotation_to_excel(full_path)
            
            if success:
                messagebox.showinfo(
                    "Cart Saved", 
                    f"Cart saved successfully!\n\nFile: {filename}\nLocation: Data folder", 
                    parent=self
                )
                print(f"Cart saved to: {full_path}")
            else:
                messagebox.showerror(
                    "Save Failed", 
                    f"Failed to save cart:\n\n{message}", 
                    parent=self
                )
                
        except Exception as e:
            messagebox.showerror(
                "Save Error", 
                f"An error occurred while saving cart:\n\n{str(e)}", 
                parent=self
            )