import tkinter as tk
from tkinter import ttk, messagebox
from babel.numbers import format_currency
from global_state import get_global_state
import pandas as pd


class CartView(tk.Toplevel):
    def __init__(self, parent_window, data_manager, main_app=None):
        super().__init__(parent_window)
        self.parent_window = parent_window  # This is the root tk window
        self.main_app = main_app  # This is the MainApplication instance
        self.data_manager = data_manager
        self.global_state = get_global_state()
        
        self.title("Cart")
        
        # Set window position exactly as legacy
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - (screen_width / 2.5)) / 2 - 30
        y = (screen_height - (screen_height / 2.5)) / 2 - 150
        self.geometry("+%d+%d" % (x, y))
        
        self.attributes("-topmost", True)

        # Store quantity Entry widgets for each row
        self.quantity_entries = []

        self.create_widgets()
        self.populate_cart()

    def create_widgets(self):
        """Create cart layout exactly as legacy"""
        # Customer Details Frame (top) - exactly as legacy
        custDetails = ttk.Label(self, text="Customer Details", font=("", 10, "bold"))
        frame2 = tk.LabelFrame(self, borderwidth=2, width=1000, labelwidget=custDetails)
        frame2.grid(column=0, row=0, columnspan=3, padx=5, pady=5, sticky="W")
        self.frame2 = frame2

        # Customer details layout exactly as legacy
        # Spacer labels for proper alignment
        for i in range(4):
            spacer = ttk.Label(self.frame2, text="", font=("", 10, "bold"))
            spacer.grid(column=i+1, row=0, padx=8, pady=10, sticky="W")

        # Customer details fields
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=10, pady=10, sticky="W")
        custAddLab = ttk.Label(self.frame2, text="Customer Address") 
        custAddLab.grid(column=0, row=2, padx=10, pady=10, sticky="W")
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=0, row=3, padx=10, pady=10, sticky="W")

        # Customer details entries (disabled as in legacy)
        custNamEnt = tk.Entry(
            self.frame2, textvariable=self.global_state.custNamVar,
            font=("", 10, ""), relief="solid", width=43, state="disabled"
        )
        custNamEnt.grid(column=5, row=1, padx=10, pady=10, sticky="W")
        
        custAddEnt = tk.Text(
            self.frame2, font=("", 10, ""), relief="solid", height=3, width=43,
            background="#f0f0f0", foreground="#6d6d6d"
        )
        custAddEnt.grid(column=5, row=2, padx=10, pady=10, sticky="W")
        custAddEnt.insert(1.0, self.global_state.address)
        custAddEnt.config(state=tk.DISABLED)
        
        custConEnt = tk.Entry(
            self.frame2, textvariable=self.global_state.custConVar,
            font=("", 10, ""), relief="solid", width=43, state="disabled"
        )
        custConEnt.grid(column=5, row=3, padx=10, pady=10, sticky="W")

        # Scrollable cart area exactly as legacy
        frame_canvas = tk.Frame(self, borderwidth=2)
        frame_canvas.grid(row=2, column=0, columnspan=3, pady=(5, 0), sticky="nw")
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        frame_canvas.grid_propagate(False)

        canvas = tk.Canvas(frame_canvas)
        canvas.grid(row=0, column=0, sticky="news")

        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=vsb.set)

        self.frame_buttons = tk.LabelFrame(canvas, borderwidth=2, padx=5)
        canvas.create_window((0, 0), window=self.frame_buttons, anchor="nw")
        
        # Configure canvas size
        frame_canvas.config(width=1000, height=400)
        self.canvas = canvas

        # Cart Details title
        cartDetails = ttk.Label(self.frame_buttons, text="Cart Details", font=("", 10, "bold"))
        cartDetails.grid(column=0, row=0, padx=10, pady=10, sticky="W")

        # Create table headers exactly as legacy
        self.create_table_headers()

        # Action buttons at bottom exactly as legacy
        self.create_action_buttons()

    def create_table_headers(self):
        """Create table headers exactly as legacy"""
        headers = [
            ("Sr.No", 0), ("Window Type", 1), ("Width", 2), ("Height", 3),
            ("Cost", 4), ("Quantity", 5), ("Amount", 6)
        ]
        
        for text, col in headers:
            header = tk.Label(
                self.frame_buttons, text=text, font=("", 10, "bold"),
                background="#f0f0f0", relief=tk.GROOVE, padx=10, pady=5
            )
            header.grid(column=col, row=1, padx=10, pady=10, sticky="W")

    def create_action_buttons(self):
        """Create action buttons exactly as legacy placement"""
        buttons_frame = tk.Frame(self)
        buttons_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # Add More Items button (left side)
        add_item_btn = tk.Button(
            buttons_frame, text="Add More Items", font=("", 10, "bold"),
            width=15, command=self.add_more_items
        )
        add_item_btn.pack(side="left", padx=5)

        # Calculate Quantity button (center)
        calc_qty_btn = tk.Button(
            buttons_frame, text="Calculate(Quantity)", font=("", 10, "bold"),
            width=18, command=self.calculate_quantity
        )
        calc_qty_btn.pack(side="left", padx=5)

        # Next button (right side)
        next_btn = tk.Button(
            buttons_frame, text="Next", font=("", 10, "bold"),
            width=15, command=self.next_page
        )
        next_btn.pack(side="right", padx=5)

    def populate_cart(self):
        """Populate cart with items exactly as legacy layout"""
        self.quantity_entries = []
        cart_df = self.data_manager.get_cart_data()

        if cart_df.empty:
            no_items_label = tk.Label(
                self.frame_buttons, text="No items in cart", 
                font=("", 12, "italic"), fg="gray"
            )
            no_items_label.grid(column=0, row=2, columnspan=8, padx=10, pady=20)
            return

        # Populate each row exactly as legacy
        for i, (index, row) in enumerate(cart_df.iterrows()):
            self.create_cart_row(i, row)
            
        # Add total line and amount at bottom
        self.add_total_section(len(cart_df))
        
        # Update canvas scroll region
        self.frame_buttons.update_idletasks()
        bbox = self.canvas.bbox("all")
        self.canvas.config(scrollregion=bbox)

    def create_cart_row(self, row_index, data_row):
        """Create a cart row exactly as legacy"""
        grid_row = row_index + 2  # Start after header
        
        # Sr.No
        sr_label = tk.Label(self.frame_buttons, text=str(row_index + 1), padx=10)
        sr_label.grid(column=0, row=grid_row, padx=10, pady=10, sticky="W")
        
        # Window Type  
        type_label = tk.Label(self.frame_buttons, text=data_row.get("Particulars", ""), padx=10)
        type_label.grid(column=1, row=grid_row, padx=10, pady=10, sticky="W")
        
        # Width & Height
        width_label = tk.Label(self.frame_buttons, text=data_row.get("Width", ""), padx=10)
        width_label.grid(column=2, row=grid_row, padx=10, pady=10, sticky="W")
        height_label = tk.Label(self.frame_buttons, text=data_row.get("Height", ""), padx=10)
        height_label.grid(column=3, row=grid_row, padx=10, pady=10, sticky="W")
        
        # Cost (format as currency)
        cost_value = data_row.get("Cost (INR)", 0)
        try:
            cost_float = float(str(cost_value).replace("₹", "").replace(",", ""))
            cost_formatted = format_currency(cost_float, "INR", locale="en_IN").replace("\xa0", " ")
        except (ValueError, TypeError):
            cost_formatted = str(cost_value)
        cost_label = tk.Label(self.frame_buttons, text=cost_formatted, padx=10)
        cost_label.grid(column=4, row=grid_row, padx=10, pady=10, sticky="W")
        
        # Quantity (editable Entry widget)
        quantity_var = tk.StringVar(value=str(data_row.get("Quantity", 1)))
        quantity_entry = tk.Entry(
            self.frame_buttons, textvariable=quantity_var, relief="solid", width=12
        )
        quantity_entry.grid(column=5, row=grid_row, padx=10, pady=10, sticky="W")
        self.quantity_entries.append((data_row.get("Sr.No", row_index + 1), quantity_var))
        
        # Amount (calculated field)
        amount_value = data_row.get("Amount", 0)
        try:
            amount_float = float(str(amount_value).replace("₹", "").replace(",", ""))
            amount_formatted = format_currency(amount_float, "INR", locale="en_IN").replace("\xa0", " ")
        except (ValueError, TypeError):
            amount_formatted = str(amount_value)
        amount_label = tk.Label(self.frame_buttons, text=amount_formatted, padx=10)
        amount_label.grid(column=6, row=grid_row, padx=10, pady=10, sticky="W")
        
        # Delete button (red X)
        delete_btn = tk.Button(
            self.frame_buttons, text="X", font=("", 10, "bold"), width=2, fg="red",
            command=lambda sr_no=data_row.get("Sr.No", row_index + 1): self.delete_row(sr_no)
        )
        delete_btn.grid(column=7, row=grid_row, padx=10, pady=10, sticky="W")

    def add_total_section(self, num_rows):
        """Add total section at bottom exactly as legacy"""
        grid_row = num_rows + 3
        
        # Separator line
        line = ttk.Label(
            self.frame_buttons,
            text="________________________________________________________________________________________________________________________________________________"
        )
        line.grid(column=0, row=grid_row, columnspan=8, padx=10, pady=10, sticky="N")
        
        # Total amount display
        total_amount = self.data_manager.get_cart_total_amount()
        indCurr = lambda x: format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")
        
        total_label = tk.Label(
            self.frame_buttons, text="Total Amount:", font=("", 12, "bold"), padx=10
        )
        total_label.grid(column=5, row=grid_row + 1, padx=10, pady=10, sticky="W")
        
        total_value_label = tk.Label(
            self.frame_buttons, text=indCurr(total_amount), 
            font=("", 12, "bold"), fg="blue", padx=10
        )
        total_value_label.grid(column=6, row=grid_row + 1, padx=10, pady=10, sticky="W")

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
            
            # Clear and repopulate the cart display
            for widget in self.frame_buttons.winfo_children():
                if int(widget.grid_info().get("row", 0)) > 1:
                    widget.destroy()
            
            self.populate_cart()
            messagebox.showinfo("Success", "Quantities calculated successfully!", parent=self)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating quantities: {str(e)}", parent=self)

    def delete_row(self, sr_no):
        """Delete a cart row exactly as legacy deleteRow() method"""
        if messagebox.askyesno(
            "Confirm Delete", f"Are you sure you want to delete item {sr_no}?", parent=self
        ):
            self.data_manager.remove_item_from_cart(sr_no)
            
            # Refresh the entire cart display
            for widget in self.frame_buttons.winfo_children():
                if int(widget.grid_info().get("row", 0)) > 1:
                    widget.destroy()
            
            self.populate_cart()

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

    def next_page(self):
        """Go to next page exactly as legacy nextItem() method"""
        cart_df = self.data_manager.get_cart_data()
        
        if cart_df.empty:
            messagebox.showerror("Empty Cart", "Cannot proceed with an empty cart.", parent=self)
            return
            
        # Check if quantities have been calculated (legacy calcQuantFlag check)
        calculated_quantities = True
        for sr_no, quantity_var in self.quantity_entries:
            try:
                qty = int(float(quantity_var.get()))
                if qty < 1:
                    calculated_quantities = False
                    break
            except ValueError:
                calculated_quantities = False
                break
        
        if not calculated_quantities:
            messagebox.showerror(
                "Invalid",
                "Please calculate quantity values by clicking on Calculate(Quantity) Button",
                parent=self
            )
            return
            
        # Save data to Excel as legacy does
        customer_name = self.global_state.custNamVar.get()
        if customer_name:
            filename = f"./Data/{customer_name}_QuatationData.xlsx"
            success, message = self.data_manager.save_quotation_to_excel(filename)
            if not success:
                messagebox.showerror("Save Error", f"Could not save data: {message}", parent=self)
                return
        
        # Open calculation page
        self.main_app.open_calculator_view()
        self.destroy()

    def display_cart_items(self):
        """Display cart items in the UI"""
        cart_df = self.data_manager.get_cart_data()
        if cart_df.empty:
            return
        
        # Clear existing items
        for widget in self.items_frame.winfo_children():
            widget.destroy()
            
        # Create headers
        headers = ['Sr.No', 'Window Type', 'Width', 'Height', 'Cost', 'Quantity', 'Amount']
        for col, header in enumerate(headers):
            label = tk.Label(
                self.items_frame,
                text=header,
                font=('', 10, 'bold'),
                background='#f0f0f0',
                relief=tk.GROOVE,
                padx=10,
                pady=5
            )
            label.grid(column=col, row=0, padx=10, pady=10, sticky='W')
            
        # Display items
        self.quantity_entries = []  # Reset quantity entries list
        for idx, row in cart_df.iterrows():
            # Sr.No
            sr_no = int(row['Sr.No']) if 'Sr.No' in row and pd.notna(row['Sr.No']) else idx + 1
            tk.Label(self.items_frame, text=sr_no, padx=10).grid(
                column=0, row=idx+1, padx=10, pady=10, sticky='W'
            )
            
            # Window Type
            window_type = row['windowTypeVar'] if 'windowTypeVar' in row else ''
            tk.Label(self.items_frame, text=window_type, padx=10).grid(
                column=1, row=idx+1, padx=10, pady=10, sticky='W'
            )
            
            # Width
            width = row['Width'] if 'Width' in row else ''
            tk.Label(self.items_frame, text=width, padx=10).grid(
                column=2, row=idx+1, padx=10, pady=10, sticky='W'
            )
            
            # Height
            height = row['Height'] if 'Height' in row else ''
            tk.Label(self.items_frame, text=height, padx=10).grid(
                column=3, row=idx+1, padx=10, pady=10, sticky='W'
            )
            
            # Cost
            cost = row['cstAmtInr'] if 'cstAmtInr' in row else ''
            tk.Label(self.items_frame, text=cost, padx=10).grid(
                column=4, row=idx+1, padx=10, pady=10, sticky='W'
            )
            
            # Quantity
            qty_var = tk.StringVar()
            qty = row['quantity'] if 'quantity' in row and pd.notna(row['quantity']) else '1'
            qty_var.set(str(qty))
            qty_entry = tk.Entry(
                self.items_frame,
                textvariable=qty_var,
                relief='solid',
                width=12
            )
            qty_entry.grid(column=5, row=idx+1, padx=10, pady=10, sticky='W')
            self.quantity_entries.append((sr_no, qty_var))
            
            # Amount
            amount = row['quantAmnt'] if 'quantAmnt' in row else ''
            tk.Label(self.items_frame, text=amount, padx=10).grid(
                column=6, row=idx+1, padx=10, pady=10, sticky='W'
            )
            
            # Delete button
            delete_btn = tk.Button(
                self.items_frame,
                text='X',
                font=('', 10, 'bold'),
                width=2,
                fg='red',
                command=lambda num=sr_no: self.delete_item(num)
            )
            delete_btn.grid(column=7, row=idx+1, padx=10, pady=10, sticky='W')
            
        # Update scroll region
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        
        # Update total cost if available
        if 'finalCost' in cart_df.columns and not cart_df.empty:
            final_cost = cart_df.iloc[-1]['finalCost']
            if pd.notna(final_cost):
                self.total_cost_var.set(final_cost)
            
        if 'totQuanSum' in cart_df.columns and not cart_df.empty:
            total_quantity = cart_df.iloc[-1]['totQuanSum']
            if pd.notna(total_quantity):
                self.total_quantity_var.set(total_quantity)