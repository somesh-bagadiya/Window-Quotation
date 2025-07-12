"""
Invoice View - Window Quotation Application
==========================================

This module provides the invoice generation interface, refactored from the legacy
Invoice class in MGA Window Quotaion.py to match the original layout and functionality.

Key Features:
- Customer details section (read-only from global state)
- Invoice details input (invoice number, quotation number, payment terms, etc.)
- Cart items display with editable HSN/SAC codes
- PDF generation with proper tax calculations
- Default HSN codes based on product types
- Auto-generated invoice numbers
- Legacy-style UI layout and styling

Matches legacy Invoice.invWindow() method functionality exactly.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename
from datetime import datetime
from pdf_generator import create_invoice_pdf
from global_state import get_global_state


class InvoiceView(tk.Toplevel):
    def __init__(self, parent, data_manager, final_costs):
        super().__init__(parent)
        self.parent = parent
        self.data_manager = data_manager
        self.final_costs = final_costs
        self.global_state = get_global_state()

        # Configure window exactly as legacy
        self.title("Invoice Window")
        self.configure(bg="#f0f0f0")
        self.resizable(True, True)
        
        # Center the window on screen
        self.center_window()
        
        # Set window icon if available
        try:
            if hasattr(parent, 'iconbitmap'):
                self.iconbitmap(parent.iconbitmap())
        except:
            pass

        # --- Invoice Specific Variables (matching legacy exactly) ---
        self.invNumbVar = tk.StringVar()
        self.quotNumbVar = tk.StringVar()
        self.modeTermVar = tk.StringVar()
        self.termOfDelVar = tk.StringVar()
        self.destinVar = tk.StringVar()
        self.custGstVar = tk.StringVar()
        self.custPanVar = tk.StringVar()
        
        # Date selection variables
        self.invoice_day_var = tk.StringVar()
        self.invoice_month_var = tk.StringVar()
        self.invoice_year_var = tk.StringVar()
        self.use_custom_date_var = tk.BooleanVar(value=False)  # Default to current date
        
        self.hsn_vars = [
            tk.StringVar() for _ in range(len(self.data_manager.get_cart_data()))
        ]

        # Create UI matching legacy layout
        self.create_legacy_invoice_window()
        
        # Set default values matching legacy behavior
        self.set_default_values()
        
        # Make window modal and focused
        self.transient(parent)
        self.grab_set()
        self.focus_set()

    def center_window(self):
        """Center the window on screen with unified responsive centering"""
        # Get responsive configuration
        from ui.responsive_config import get_responsive_config
        responsive = get_responsive_config()
        
        # Use unified centering system for consistent positioning
        responsive.center_invoice_window(self)

    def create_legacy_invoice_window(self):
        """Create invoice window layout matching legacy implementation"""
        # Main container frame - matching legacy layout structure
        main_frame = tk.Frame(self, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Title label matching legacy
        title_label = tk.Label(
            main_frame,
            text="Invoice Generation",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=(0, 15))

        # Create three main sections exactly as legacy
        self.create_customer_section(main_frame)
        self.create_invoice_details_section(main_frame)
        self.create_cart_items_section(main_frame)
        self.create_action_buttons(main_frame)

    def create_customer_section(self, parent):
        """Create customer details section matching legacy layout"""
        # Customer Details Frame
        frame2 = tk.LabelFrame(
            parent,
            text="Customer Details",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            relief="groove",
            borderwidth=2
        )
        frame2.pack(fill="x", pady=(0, 10))

        # Customer details layout - 3 columns as in legacy
        # Row 1: Name, Address, Contact
        tk.Label(frame2, text="Customer Name", bg="#f0f0f0").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        custNameEnt = tk.Entry(
            frame2,
            textvariable=self.global_state.custNamVar,
            width=25,
            state="readonly",
            relief="solid"
        )
        custNameEnt.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        tk.Label(frame2, text="Customer Address", bg="#f0f0f0").grid(
            row=0, column=1, padx=10, pady=10, sticky="w"
        )
        custAddEnt = tk.Text(
            frame2,
            height=3,
            width=30,
            relief="solid",
            bg="#f8f8f8"
        )
        custAddEnt.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        # Insert address from global state
        address_text = self.global_state.custAddVar.get()
        if address_text.strip():
            custAddEnt.insert("1.0", address_text)
        custAddEnt.config(state="disabled")

        tk.Label(frame2, text="Customer Contact No.", bg="#f0f0f0").grid(
            row=0, column=2, padx=10, pady=10, sticky="w"
        )
        custConEnt = tk.Entry(
            frame2,
            textvariable=self.global_state.custConVar,
            width=25,
            state="readonly",
            relief="solid"
        )
        custConEnt.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Row 2: GST and PAN
        tk.Label(frame2, text="Customer GST No.", bg="#f0f0f0").grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        custGstEnt = tk.Entry(
            frame2,
            textvariable=self.custGstVar,
            width=25,
            relief="solid"
        )
        custGstEnt.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        tk.Label(frame2, text="Customer PAN No.", bg="#f0f0f0").grid(
            row=2, column=1, padx=10, pady=10, sticky="w"
        )
        custPanEnt = tk.Entry(
            frame2,
            textvariable=self.custPanVar,
            width=25,
            relief="solid"
        )
        custPanEnt.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    def create_invoice_details_section(self, parent):
        """Create invoice details section matching legacy layout"""
        # Invoice Details Frame
        inv_frame = tk.LabelFrame(
            parent,
            text="Invoice Details",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            relief="groove",
            borderwidth=2
        )
        inv_frame.pack(fill="x", pady=(0, 10))

        # Invoice details layout - 3 columns as in legacy
        # Row 1: Invoice Number, Quotation Number, Mode/Terms
        tk.Label(inv_frame, text="Invoice Number", bg="#f0f0f0").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        invNumbEnt = tk.Entry(
            inv_frame,
            textvariable=self.invNumbVar,
            width=25,
            relief="solid"
        )
        invNumbEnt.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        tk.Label(inv_frame, text="Quotation Number", bg="#f0f0f0").grid(
            row=0, column=1, padx=10, pady=10, sticky="w"
        )
        quotNumbEnt = tk.Entry(
            inv_frame,
            textvariable=self.quotNumbVar,
            width=25,
            relief="solid"
        )
        quotNumbEnt.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        tk.Label(inv_frame, text="Mode/Terms of Payment", bg="#f0f0f0").grid(
            row=0, column=2, padx=10, pady=10, sticky="w"
        )
        modeTermEnt = tk.Entry(
            inv_frame,
            textvariable=self.modeTermVar,
            width=25,
            relief="solid"
        )
        modeTermEnt.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Row 2: Terms of Delivery, Destination
        tk.Label(inv_frame, text="Terms of Delivery", bg="#f0f0f0").grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        termOfDelEnt = tk.Entry(
            inv_frame,
            textvariable=self.termOfDelVar,
            width=25,
            relief="solid"
        )
        termOfDelEnt.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        tk.Label(inv_frame, text="Destination", bg="#f0f0f0").grid(
            row=2, column=1, padx=10, pady=10, sticky="w"
        )
        destinEnt = tk.Entry(
            inv_frame,
            textvariable=self.destinVar,
            width=25,
            relief="solid"
        )
        destinEnt.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Row 3: Invoice Date Selection
        tk.Label(inv_frame, text="Invoice Date", bg="#f0f0f0").grid(
            row=2, column=2, padx=10, pady=10, sticky="w"
        )
        
        # Date selection frame
        date_frame = tk.Frame(inv_frame, bg="#f0f0f0")
        date_frame.grid(row=3, column=2, padx=10, pady=5, sticky="w")
        
        # Checkbox for custom date
        use_custom_check = tk.Checkbutton(
            date_frame,
            text="Custom Date:",
            variable=self.use_custom_date_var,
            command=self.toggle_date_selection,
            bg="#f0f0f0"
        )
        use_custom_check.grid(row=0, column=0, sticky="w")
        
        # Date selection dropdowns
        self.date_selection_frame = tk.Frame(date_frame, bg="#f0f0f0")
        self.date_selection_frame.grid(row=1, column=0, sticky="w", pady=(5, 0))
        
        # Day dropdown
        tk.Label(self.date_selection_frame, text="Day:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
        self.day_combo = ttk.Combobox(
            self.date_selection_frame,
            textvariable=self.invoice_day_var,
            values=[str(i) for i in range(1, 32)],
            width=5,
            state="disabled"
        )
        self.day_combo.grid(row=0, column=1, padx=(2, 5))
        
        # Month dropdown
        tk.Label(self.date_selection_frame, text="Month:", bg="#f0f0f0").grid(row=0, column=2, sticky="w")
        self.month_combo = ttk.Combobox(
            self.date_selection_frame,
            textvariable=self.invoice_month_var,
            values=[str(i) for i in range(1, 13)],
            width=5,
            state="disabled"
        )
        self.month_combo.grid(row=0, column=3, padx=(2, 5))
        
        # Year dropdown
        tk.Label(self.date_selection_frame, text="Year:", bg="#f0f0f0").grid(row=0, column=4, sticky="w")
        current_year = datetime.now().year
        self.year_combo = ttk.Combobox(
            self.date_selection_frame,
            textvariable=self.invoice_year_var,
            values=[str(i) for i in range(current_year - 5, current_year + 5)],
            width=8,
            state="disabled"
        )
        self.year_combo.grid(row=0, column=5, padx=(2, 0))

    def create_cart_items_section(self, parent):
        """Create cart items section with HSN/SAC codes matching legacy"""
        # Cart Items Frame
        cart_frame = tk.LabelFrame(
            parent,
            text="Cart Items & HSN/SAC Codes",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            relief="groove",
            borderwidth=2
        )
        cart_frame.pack(fill="both", expand=True, pady=(0, 10))

        # Create scrollable frame for cart items
        canvas = tk.Canvas(cart_frame, bg="white")
        scrollbar = tk.Scrollbar(cart_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Table headers matching legacy format
        headers = ["Sr.No", "Description of Goods", "HSN/SAC", "Rate", "Quantity", "Amount"]
        for col, header in enumerate(headers):
            header_label = tk.Label(
                scrollable_frame,
                text=header,
                font=("Arial", 10, "bold"),
                relief="groove",
                bg="#e0e0e0",
                borderwidth=1
            )
            header_label.grid(row=0, column=col, padx=2, pady=2, sticky="ew", ipadx=10, ipady=5)

        # Cart data rows
        cart_data = self.data_manager.get_cart_data()
        for i, (_, cart_row) in enumerate(cart_data.iterrows()):
            # Sr.No
            tk.Label(
                scrollable_frame,
                text=str(cart_row["Sr.No"]),
                relief="solid",
                borderwidth=1,
                bg="white"
            ).grid(row=i + 1, column=0, padx=2, pady=2, sticky="ew", ipadx=10, ipady=5)

            # Description
            desc = f"{cart_row['Particulars']} ({cart_row['Width']} x {cart_row['Height']})"
            tk.Label(
                scrollable_frame,
                text=desc,
                relief="solid",
                borderwidth=1,
                bg="white",
                wraplength=200
            ).grid(row=i + 1, column=1, padx=2, pady=2, sticky="ew", ipadx=10, ipady=5)

            # HSN/SAC Entry with default value based on product type
            # Set default HSN code based on product type (matching legacy)
            product_type = cart_row['Particulars']
            default_hsn = self.get_default_hsn_code(product_type)
            if not self.hsn_vars[i].get():  # Only set if empty
                self.hsn_vars[i].set(default_hsn)
                
            hsn_entry = tk.Entry(
                scrollable_frame,
                textvariable=self.hsn_vars[i],
                width=15,
                relief="solid",
                justify="center"
            )
            hsn_entry.grid(row=i + 1, column=2, padx=2, pady=2, sticky="ew", ipadx=5, ipady=5)

            # Rate
            tk.Label(
                scrollable_frame,
                text=str(cart_row["Cost (INR)"]),
                relief="solid",
                borderwidth=1,
                bg="white"
            ).grid(row=i + 1, column=3, padx=2, pady=2, sticky="ew", ipadx=10, ipady=5)

            # Quantity
            tk.Label(
                scrollable_frame,
                text=str(cart_row["Quantity"]),
                relief="solid",
                borderwidth=1,
                bg="white"
            ).grid(row=i + 1, column=4, padx=2, pady=2, sticky="ew", ipadx=10, ipady=5)

            # Amount
            tk.Label(
                scrollable_frame,
                text=str(cart_row["Amount"]),
                relief="solid",
                borderwidth=1,
                bg="white"
            ).grid(row=i + 1, column=5, padx=2, pady=2, sticky="ew", ipadx=10, ipady=5)

        # Configure column weights for proper expansion
        for col in range(6):
            scrollable_frame.columnconfigure(col, weight=1)

    def create_action_buttons(self, parent):
        """Create action buttons matching legacy layout"""
        button_frame = tk.Frame(parent, bg="#f0f0f0")
        button_frame.pack(fill="x", pady=10)

        # Generate Invoice button matching legacy style
        generate_btn = tk.Button(
            button_frame,
            text="Generate Invoice PDF",
            command=self.generate_invoice_pdf,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="raised",
            borderwidth=2,
            padx=20,
            pady=10
        )
        generate_btn.pack(side="right", padx=10)

        # Cancel button
        cancel_btn = tk.Button(
            button_frame,
            text="Cancel",
            command=self.destroy,
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            relief="raised",
            borderwidth=2,
            padx=20,
            pady=10
        )
        cancel_btn.pack(side="right", padx=10)

    def toggle_date_selection(self):
        """Toggle date selection widgets based on checkbox state"""
        if self.use_custom_date_var.get():
            # Enable date selection
            self.day_combo.config(state="readonly")
            self.month_combo.config(state="readonly")
            self.year_combo.config(state="readonly")
            
            # Set current date as default
            current_date = datetime.now()
            self.invoice_day_var.set(str(current_date.day))
            self.invoice_month_var.set(str(current_date.month))
            self.invoice_year_var.set(str(current_date.year))
        else:
            # Disable date selection
            self.day_combo.config(state="disabled")
            self.month_combo.config(state="disabled")
            self.year_combo.config(state="disabled")
            
            # Clear date values
            self.invoice_day_var.set("")
            self.invoice_month_var.set("")
            self.invoice_year_var.set("")

    def get_invoice_date(self):
        """Get the invoice date - either custom or current date"""
        if self.use_custom_date_var.get():
            try:
                day = int(self.invoice_day_var.get())
                month = int(self.invoice_month_var.get())
                year = int(self.invoice_year_var.get())
                return datetime(year, month, day)
            except (ValueError, TypeError):
                # If invalid date, fall back to current date
                return datetime.now()
        else:
            return datetime.now()

    def set_default_values(self):
        """Set default values matching legacy behavior"""
        # Generate default invoice number based on current date/time
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        self.invNumbVar.set(f"INV_{timestamp}")
        
        # Set default quotation number if available
        if hasattr(self.data_manager, 'current_quotation_number'):
            self.quotNumbVar.set(self.data_manager.current_quotation_number)
        
        # Set default payment terms
        self.modeTermVar.set("Cash/Cheque/NEFT")
        self.termOfDelVar.set("Ex-Works")
        
        # Default destination based on customer address if available
        customer_address = self.global_state.custAddVar.get()
        if customer_address.strip():
            # Extract city from address for destination
            address_lines = customer_address.split('\n')
            if len(address_lines) > 1:
                self.destinVar.set(address_lines[1].strip())
        
        # Set focus to invoice number for easy editing
        self.focus_set()

    def get_default_hsn_code(self, product_type):
        """Get default HSN/SAC code based on product type (matching legacy)"""
        # Standard HSN codes for different window/door types
        hsn_codes = {
            "Sliding Window": "7610",
            "Sliding Door": "7610", 
            "Fix Louver": "7610",
            "Patti Louver": "7610",
            "Openable Window": "7610",
            "Sliding folding door": "7610",
            "Casement Window": "7610",
            "Aluminium partition": "7610",
            "Toughened partition": "7006",
            "Toughened Door": "7006",
            "Composite pannel": "3921",
            "Curtain wall": "7610",
            "Fix Window": "7610",
            "Exhaust Fan Window": "7610"
        }
        
        # Return HSN code for product type, default to 7610 for aluminium products
        return hsn_codes.get(product_type, "7610")

    def generate_invoice_pdf(self):
        """Generate invoice PDF matching legacy functionality"""
        try:
            # Validate required fields
            if not self.invNumbVar.get().strip():
                messagebox.showerror(
                    "Validation Error", 
                    "Please enter Invoice Number", 
                    parent=self
                )
                return

            # 1. Collect all invoice data from StringVars
            invoice_details = {
                "invNumbVar": self.invNumbVar.get(),
                "quotNumbVar": self.quotNumbVar.get(),
                "modeTermVar": self.modeTermVar.get(),
                "termOfDelVar": self.termOfDelVar.get(),
                "destinVar": self.destinVar.get(),
                "custGstVar": self.custGstVar.get(),
                "custPanVar": self.custPanVar.get(),
                    "invoice_date": self.get_invoice_date(),  # Add custom/current date
            }

            # 2. Get cart data from data_manager and add HSN codes
            cart_data_with_hsn = self.data_manager.get_cart_data().copy()
            hsn_codes = [var.get() for var in self.hsn_vars]
            cart_data_with_hsn["hsn_sac"] = hsn_codes

            # 3. Get customer data from global state (matching legacy)
            customer_details = {
                "custNamVar": self.global_state.custNamVar.get(),
                "custAddVar": self.global_state.custAddVar.get(),
                "custConVar": self.global_state.custConVar.get(),
            }

            # 4. Prompt for filename (matching legacy behavior)
            filename = asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Documents", "*.pdf"), ("All Files", "*.*")],
                title="Save Invoice PDF As...",
                parent=self,
                initialfile=f"Invoice_{self.invNumbVar.get()}"
            )
            
            if not filename:
                return  # User cancelled

            # 5. Call create_invoice_pdf function (matching legacy PDF generation)
            success, message = create_invoice_pdf(
                filename,
                customer_details,
                invoice_details,
                cart_data_with_hsn,
                self.final_costs,
            )

            if success:
                messagebox.showinfo(
                    "Success", 
                    f"Invoice PDF generated successfully!\n\nSaved to: {filename}", 
                    parent=self
                )
                # Auto-close window after successful generation (matching legacy)
                self.destroy()
            else:
                messagebox.showerror(
                    "PDF Generation Error", 
                    f"Failed to generate invoice PDF:\n\n{message}", 
                    parent=self
                )

        except Exception as e:
            messagebox.showerror(
                "Unexpected Error", 
                f"An unexpected error occurred while generating the invoice:\n\n{str(e)}", 
                parent=self
            )
