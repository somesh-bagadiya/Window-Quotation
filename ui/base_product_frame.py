import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from babel.numbers import format_currency
from global_state import get_global_state


class BaseProductFrame(tk.Frame):
    def __init__(self, parent, data_manager):
        super().__init__(parent)
        self.parent = parent  # Parent is the Toplevel window
        self.data_manager = data_manager
        self.global_state = get_global_state()
        self.data = data_manager.get_data()

        # Get base directory for images
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.image_dir = os.path.join(self.base_dir, "Images")
        
        # After ID for search debouncing
        self._after_id = None
        
        # Legacy frame references
        self.frame0 = None  # Dimensions and cost (middle)
        self.frame1 = None  # Scrollable specifications (bottom)  
        self.frame2 = None  # Customer details (top)
        
        # Cost calculation widgets
        self.totSqftEnt = None
        self.costEnt = None
        self.costTot = None
        
        # Canvas and scrolling
        self.canvas = None
        self.frame_canvas = None
        self.frame_buttons = None
        
        # Product image
        self.product_image = None
        
        # Create the legacy layout
        self.create_legacy_layout()
        self.create_customer_details()
        self.create_dimensions_section()
        self.create_scrollable_specifications()
        
        # This will be populated by child classes
        self.create_specifications()

    def create_legacy_layout(self):
        """Create the exact 3-frame layout structure from legacy"""
        # Frame 2: Customer Details (top) - row 0
        self.frame2 = tk.LabelFrame(self.parent, borderwidth=2)
        self.frame2.grid(column=0, row=0, padx=5, pady=5, sticky="ew")
        
        # Frame 0: Dimensions & Cost (middle) - row 1  
        self.frame0 = tk.LabelFrame(self.parent, borderwidth=2)
        self.frame0.grid(column=0, row=1, padx=5, pady=5, columnspan=4, sticky="W")
        
        # Frame Canvas: Container for scrollable specifications (bottom) - row 2
        self.frame_canvas = tk.Frame(self.parent, borderwidth=2)
        self.frame_canvas.grid(row=2, column=0, columnspan=3, pady=(5, 0), sticky="nw")
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        self.frame_canvas.grid_propagate(False)

    def create_customer_details(self):
        """Create customer details section exactly as legacy"""
        custDetails = ttk.Label(
            self.frame2, text="Customer Details", font=("", 10, "bold")
        )
        custDetails.grid(column=0, row=0, padx=10, pady=10, sticky="W")

        # Customer name
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky="W")
        custNamEnt = tk.Entry(
            self.frame2,
            textvariable=self.global_state.custNamVar,
            font=("", 10, ""),
            relief="solid",
            width=24,
            state="disabled",
        )
        custNamEnt.grid(column=1, row=1, padx=10, pady=10, sticky="W")

        # Customer address
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=10, pady=10, sticky="W")
        custAddEnt = tk.Text(
            self.frame2,
            font=("", 10, ""),
            relief="solid",
            height=3,
            width=24,
            background="#f0f0f0",
            foreground="#6d6d6d",
        )
        custAddEnt.grid(column=3, row=1, padx=10, pady=10, sticky="W")
        custAddEnt.insert(1.0, self.global_state.address)
        custAddEnt.config(state=tk.DISABLED)

        # Customer contact
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=10, pady=10, sticky="W")
        custConEnt = tk.Entry(
            self.frame2,
            textvariable=self.global_state.custConVar,
            font=("", 10, ""),
            relief="solid",
            width=24,
            state="disabled",
        )
        custConEnt.grid(column=5, row=1, padx=10, pady=10, sticky="W")

    def create_dimensions_section(self):
        """Create dimensions and cost calculation section exactly as legacy"""
        # Product type label
        selectWinLabel = ttk.Label(
            self.frame0, text=self.parent.title(), font=("", 10, "bold")
        )
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky="W")

        # Width input
        widthLabel = ttk.Label(self.frame0, text="Enter Width (ft)")
        widthLabel.grid(column=0, row=1, padx=10, pady=10, sticky="W")
        enterWidth = tk.Entry(
            self.frame0, textvariable=self.global_state.Width, relief="solid", width=33, state="disabled"
        )
        enterWidth.grid(column=1, row=1, padx=10, pady=10, sticky="W")

        # Height input
        heightLabel = ttk.Label(self.frame0, text="Enter Height (ft)")
        heightLabel.grid(column=0, row=2, padx=10, pady=10, sticky="W")
        enterHeight = tk.Entry(
            self.frame0, textvariable=self.global_state.Height, relief="solid", width=33, state="disabled"
        )
        enterHeight.grid(column=1, row=2, padx=10, pady=10, sticky="W")

        # Total area display
        totSqft = ttk.Label(self.frame0, text="Total Area(In Sq.Ft)")
        totSqft.grid(column=2, row=1, padx=10, pady=10, sticky="W")
        self.totSqftEnt = tk.Entry(
            self.frame0,
            textvariable=self.global_state.totSqftEntVar,
            relief="solid",
            width=28,
            state="disabled",
        )
        self.totSqftEnt.grid(column=3, row=1, padx=10, pady=10, sticky="W")

        # Cost per sq ft input
        cost = ttk.Label(self.frame0, text="Enter Cost (Cost per Sq.Ft)")
        cost.grid(column=2, row=2, padx=10, pady=10, sticky="W")
        self.costEnt = tk.Entry(
            self.frame0, textvariable=self.global_state.costEntVar, relief="solid", width=28
        )
        self.costEnt.grid(column=3, row=2, padx=10, pady=10, sticky="W")

        # Total cost display
        cost = ttk.Label(self.frame0, text="Total Cost")
        cost.grid(column=4, row=1, padx=10, pady=10, sticky="W")
        self.costTot = tk.Entry(
            self.frame0,
            textvariable=self.global_state.cstAmtInr,
            relief="solid",
            width=28,
            state="disabled",
        )
        self.costTot.grid(column=5, row=1, padx=10, pady=10, sticky="W")

        # Calculate button
        calculate = tk.Button(
            self.frame0, text="Calculate", width=34, command=self.calculate_cost
        )
        calculate.grid(column=4, row=2, padx=10, pady=15, sticky="w", columnspan=2)

    def create_scrollable_specifications(self):
        """Create scrollable canvas area for specifications exactly as legacy"""
        # Create canvas with scrollbar
        self.canvas = tk.Canvas(self.frame_canvas)
        self.canvas.grid(row=0, column=0, sticky="news")

        vsb = tk.Scrollbar(self.frame_canvas, orient=tk.VERTICAL, command=self.canvas.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=vsb.set)

        # Create frame inside canvas for specifications
        self.frame_buttons = tk.LabelFrame(self.canvas, borderwidth=2, padx=5)
        self.frame_buttons.grid(column=0, row=2, padx=5, pady=5)
        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor="nw")
        
        # Set frame1 to the scrollable frame for specifications
        self.frame1 = self.frame_buttons
        
        # Configure canvas size exactly as legacy
        self.frame_buttons.update_idletasks()
        self.frame_canvas.config(width=1000, height=500)
        self.canvas.config(scrollregion=(0, 0, 700, 685))

    def create_specifications(self):
        """Override this in child classes to add product-specific specifications"""
        # Add specifications title
        selectWinLabel = ttk.Label(
            self.frame1, text="Specifications", font=("", 10, "bold")
        )
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        
        # This will be implemented by child classes
        pass

    def add_product_image(self, image_filename):
        """Add large product image to specifications area"""
        try:
            image_path = os.path.join(self.image_dir, image_filename)
            image = Image.open(image_path)
            resize_image = image.resize((600, 400))  # Exact legacy size
            self.product_image = ImageTk.PhotoImage(resize_image)
            
            imgLab = tk.Label(self.frame1, image=self.product_image)
            imgLab.image = self.product_image  # Keep a reference
            imgLab.grid(column=2, row=1, rowspan=15, padx=10, pady=10)
            
            # Product title below image
            selectWinLabel = ttk.Label(
                self.frame1, text=self.parent.title(), font=("", 20, "bold")
            )
            selectWinLabel.grid(column=2, row=16, padx=10, pady=5)
            
            # Disclaimer text
            selectWinLabel = ttk.Label(
                self.frame1,
                text="(This is an Illustration, not actual product)",
                font=("", 10, ""),
            )
            selectWinLabel.grid(column=2, row=17, padx=10, pady=5)
            
        except FileNotFoundError:
            print(f"Product image not found: {image_path}")
            # Add placeholder
            placeholder = ttk.Label(self.frame1, text=f"Image: {image_filename}")
            placeholder.grid(column=2, row=1, rowspan=15, padx=10, pady=10)

    def search(self, widget, selOpt):
        """Implement live search exactly as legacy"""
        value = widget.get()
        value = value.strip().lower()
        
        if value == "":
            data = self.global_state.options[selOpt]
        else:
            data = []
            for item in self.global_state.options[selOpt]:
                if value in item.lower():
                    data.append(item)
        widget["values"] = data

        if value != "" and data:
            widget.event_generate("<Down>")

    def handleWait(self, event, widget, selOpt):
        """Handle debounced search exactly as legacy"""
        if self._after_id is not None:
            widget.after_cancel(self._after_id)
        self._after_id = widget.after(1000, lambda: self.search(widget, selOpt))

    def calculate_cost(self):
        """Enhanced cost calculation with automatic rate lookup support"""
        try:
            width = float(self.global_state.Width.get()) if self.global_state.Width.get() else 0
            height = float(self.global_state.Height.get()) if self.global_state.Height.get() else 0
            total_sqft = width * height
            
            if width <= 0 or height <= 0:
                messagebox.showerror("Invalid Dimensions", "Please enter valid width and height values.", parent=self.parent)
                return False
                
            # Update total square feet
            self.global_state.totSqftEntVar.set(f"{total_sqft:.2f}")
            
            # Check if this product type supports automatic rate lookup
            product_type = self.parent.title()
            cost_per_sqft = self.get_automatic_rate(product_type, total_sqft)
            
            if cost_per_sqft is not None:
                # Automatic rate found - update cost field and calculate
                self.global_state.costEntVar.set(str(cost_per_sqft))
                total_cost = total_sqft * cost_per_sqft

                # Format currency exactly as legacy
                indCurr = lambda x: format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")
                self.global_state.cstAmtInr.set(indCurr(total_cost))
                
                return True
            else:
                # Manual cost entry required
                cost_per_sqft_str = self.global_state.costEntVar.get()
                
                if not cost_per_sqft_str:
                    messagebox.showerror(
                        "Invalid", "Please fill in the cost field.", parent=self.parent
                    )
                    return False
                    
                if not self.global_state.validate_digits(cost_per_sqft_str):
                    messagebox.showerror(
                        "Invalid", "Please enter numbers in the cost field.", parent=self.parent
                    )
                    return False
                    
                cost_per_sqft = float(cost_per_sqft_str)
                total_cost = total_sqft * cost_per_sqft

                # Format currency exactly as legacy
                indCurr = lambda x: format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")
                self.global_state.cstAmtInr.set(indCurr(total_cost))
                
                return True
            
        except (ValueError, TypeError) as e:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for dimensions and cost.", parent=self.parent)
            return False

    def get_automatic_rate(self, product_type, total_sqft):
        """
        Get automatic rate for products that have predefined rates in the pricing data file
        Returns rate or None if manual entry is required
        """
        try:
            # Try to load pricing data
            import pandas as pd
            import os
            
            pricing_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data", "pricing_data.xlsx")
            
            if os.path.exists(pricing_file):
                pricing_df = pd.read_excel(pricing_file)
                
                # Find matching product type
                matching_row = pricing_df[pricing_df['Product_Type'] == product_type]
                
                if not matching_row.empty:
                    rate = matching_row.iloc[0]['Rate_Per_SqFt']
                    min_area = matching_row.iloc[0]['Min_Area']
                    max_area = matching_row.iloc[0]['Max_Area']
                    
                    # Check if area is within valid range
                    if min_area <= total_sqft <= max_area:
                        print(f"Auto-rate found for {product_type}: ₹{rate}/sq.ft for {total_sqft} sq.ft")
                        return rate
                    else:
                        print(f"Area {total_sqft} outside valid range ({min_area}-{max_area}) for {product_type}")
                        return None
                else:
                    print(f"No rate found for product type: {product_type}")
                    return None
            else:
                print(f"Pricing file not found: {pricing_file}")
                return None
                
        except Exception as e:
            print(f"Error loading pricing data: {e}")
            return None

    def add_to_cart(self):
        """Add item to cart using legacy data structure"""
        if not self.calculate_cost():
            return

        # Gather all item details exactly as legacy
        item_data = {
            "windowTypeVar": self.parent.title(),
            "Width": self.global_state.Width.get(),
            "Height": self.global_state.Height.get(),
            "totSqftEntVar": self.global_state.totSqftEntVar.get(),
            "cstAmtInr": self.global_state.cstAmtInr.get(),
            "costEntVar": self.global_state.costEntVar.get(),
        }

        # Add all specification variables from global state
        spec_vars = self.global_state.get_all_specification_vars()
        for name, var in spec_vars.items():
            item_data[name] = var.get()

        self.data_manager.add_item_to_cart(item_data)
        messagebox.showinfo("Success", f"{item_data['windowTypeVar']} added to cart.", parent=self.parent)
        self.parent.destroy()  # Close the Toplevel window

    def add_next_button(self):
        """Add Next button exactly as legacy"""
        nextButt = tk.Button(
            self.frame1, 
            text="Next", 
            font=("", 10, "bold"), 
            width=24, 
            command=self.add_to_cart
        )
        nextButt.grid(column=1, row=18, padx=10, pady=15, sticky="W") 