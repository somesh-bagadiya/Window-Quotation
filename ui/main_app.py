import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image, ImageTk
from data_manager import DataManager
from global_state import get_global_state
from ui.ui_theme import UITheme
from ui.product_frames import (
    SlidingWindowFrame,
    SlidingDoorFrame,
    FixLouverFrame,
    PattiLouverFrame,
    OpenableWindowFrame,
    SlidingFoldingDoorFrame,
    CasementWindowFrame,
    AluminiumPartitionFrame,
    ToughenedPartitionFrame,
    ToughenedDoorFrame,
    CompositePanelFrame,
    CurtainWallFrame,
    FixWindowFrame,
    ExhaustFanWindowFrame,
)
from ui.cart_view import CartView
from ui.calculator_view import CalculatorView


class MainApplication:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.data_manager = DataManager()
        self.global_state = get_global_state()
        
        # Correctly determine the base directory
        # __file__ is in Window-Quotation/ui/main_app.py
        # We want to get to Window-Quotation/
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.image_dir = os.path.join(self.base_dir, "Images")

        # --- Product Frame Class Mapping ---
        self.product_frames = {
            "Sliding Window": SlidingWindowFrame,
            "Sliding Door": SlidingDoorFrame,
            "Fix Louver": FixLouverFrame,
            "Patti Louver": PattiLouverFrame,
            "Openable Window": OpenableWindowFrame,
            "Sliding folding door": SlidingFoldingDoorFrame,
            "Casement Window": CasementWindowFrame,
            "Aluminium partition": AluminiumPartitionFrame,
            "Toughened partition": ToughenedPartitionFrame,
            "Toughened Door": ToughenedDoorFrame,
            "Composite pannel": CompositePanelFrame,
            "Curtain wall": CurtainWallFrame,
            "Fix Window": FixWindowFrame,
            "Exhaust Fan Window": ExhaustFanWindowFrame,
        }

        # Images
        self.logo_image = None
        self.cart_icon = None

        self.create_widgets()
        self.create_menu()

    def create_menu(self):
        """Create menu exactly as legacy"""
        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="Open from file", command=self.open_quotation)
        menubar.add_cascade(label="Menu", menu=file_menu)

    def create_widgets(self):
        """Create main window layout with professional styling"""
        # Configure professional theme for the application
        UITheme.configure_ttk_styles(self.parent)
        
        # Set main window background
        self.parent.configure(bg=UITheme.BACKGROUND_WHITE)
        
        # Create frame labels with professional styling
        custDetails = ttk.Label(
            self.parent, 
            text="Enter Customer Details", 
            style="Header.TLabel"
        )
        windDetails = ttk.Label(
            self.parent, 
            text="Enter Window Details", 
            style="Header.TLabel"
        )
        
        # Create frames with professional styling
        frame0 = tk.LabelFrame(self.parent, labelwidget=custDetails)
        UITheme.apply_theme_to_widget(frame0, "labelframe")
        frame0.grid(column=0, row=0, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")
        
        frame1 = tk.LabelFrame(self.parent, labelwidget=windDetails)
        UITheme.apply_theme_to_widget(frame1, "labelframe") 
        frame1.grid(column=0, row=1, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")
        
        frame2 = tk.LabelFrame(self.parent)
        UITheme.apply_theme_to_widget(frame2, "labelframe")
        frame2.grid(column=1, row=0, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W", rowspan=2)

        # Store frame references
        self.frame0 = frame0  # Customer details
        self.frame1 = frame1  # Window details  
        self.frame2 = frame2  # Logo area

        # Create logo area with professional styling
        self.create_logo_area()
        
        # Create cart button with professional styling
        self.create_cart_button()
        
        # Create customer details section with professional styling
        self.create_customer_details()
        
        # Create window details section with professional styling
        self.create_window_details()

    def create_logo_area(self):
        """Create logo area exactly as legacy"""
        canvas = tk.Canvas(self.frame2)
        try:
            logo_path = os.path.join(self.image_dir, "MGA_1.png")
            img = Image.open(logo_path)
            resized_image = img.resize((360, 250), Image.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(resized_image)
            canvas.create_image(190, 135, image=self.logo_image)
            canvas.grid(column=0, row=0, rowspan=2)
        except FileNotFoundError:
            print(f"Logo image not found at {logo_path}")
            # Add placeholder
            placeholder = ttk.Label(self.frame2, text="MGA Logo")
            placeholder.grid(column=0, row=0, rowspan=2, padx=20, pady=20)

    def create_cart_button(self):
        """Create cart button with professional styling"""
        try:
            cart_icon_path = os.path.join(self.image_dir, "CartIcon.png")
            cart = Image.open(cart_icon_path)
            carImg = cart.resize((20, 17), Image.LANCZOS)
            self.cart_icon = ImageTk.PhotoImage(carImg)
            
            cartButt = tk.Button(
                self.parent,
                text=" Cart ",
                command=self.open_cart_view,
                image=self.cart_icon,
                compound=tk.RIGHT,
                width=UITheme.BUTTON_WIDTH_STANDARD
            )
            UITheme.apply_theme_to_widget(cartButt, "button", button_type="primary")
            cartButt.grid(column=1, row=0, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_LARGE, sticky="NE")
            
        except FileNotFoundError:
            print(f"Cart icon not found at {cart_icon_path}")
            cartButt = tk.Button(
                self.parent,
                text=" Cart ",
                command=self.open_cart_view,
                width=UITheme.BUTTON_WIDTH_STANDARD
            )
            UITheme.apply_theme_to_widget(cartButt, "button", button_type="primary")
            cartButt.grid(column=1, row=0, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_LARGE, sticky="NE")

    def create_customer_details(self):
        """Create customer details section with professional styling"""
        # Customer Name
        custNamLab = ttk.Label(self.frame0, text="Enter Customer Name", style="Professional.TLabel")
        custNamLab.grid(column=0, row=1, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")
        
        custNamEnt = tk.Entry(
            self.frame0, 
            textvariable=self.global_state.custNamVar, 
            width=UITheme.ENTRY_WIDTH_STANDARD
        )
        UITheme.apply_theme_to_widget(custNamEnt, "entry")
        custNamEnt.grid(column=1, row=1, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")

        # Customer Address (Text widget with professional styling)
        custAddLab = ttk.Label(self.frame0, text="Enter Customer Address", style="Professional.TLabel")
        custAddLab.grid(column=0, row=2, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")
        
        self.custAddEnt = tk.Text(
            self.frame0, 
            height=3, 
            width=UITheme.ENTRY_WIDTH_STANDARD,
            bg=UITheme.BACKGROUND_WHITE,
            fg=UITheme.TEXT_DARK,
            font=UITheme.get_body_font(),
            relief="solid",
            borderwidth=1,
            insertbackground=UITheme.TEXT_DARK
        )
        self.custAddEnt.grid(column=1, row=2, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")
        
        # Bind text widget to update global state
        self.custAddEnt.bind('<KeyRelease>', self.update_address)

        # Customer Contact
        custConLab = ttk.Label(self.frame0, text="Enter Customer Contact No.", style="Professional.TLabel")
        custConLab.grid(column=0, row=3, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")
        
        custConEnt = tk.Entry(
            self.frame0, 
            textvariable=self.global_state.custConVar,
            width=UITheme.ENTRY_WIDTH_STANDARD
        )
        UITheme.apply_theme_to_widget(custConEnt, "entry")
        custConEnt.grid(column=1, row=3, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")

    def update_address(self, event=None):
        """Update global state address from text widget"""
        address_text = self.custAddEnt.get("1.0", tk.END).strip()
        self.global_state.custAddVar.set(address_text)
        self.global_state.address = address_text

    def create_window_details(self):
        """Create window details section with professional styling"""
        # Window Type Selection
        selectWinLabel = ttk.Label(self.frame1, text="Select Window Type", style="Professional.TLabel")
        selectWinLabel.grid(column=0, row=5, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")
        
        selectWinDrop = ttk.Combobox(
            self.frame1, 
            state="readonly", 
            textvariable=self.global_state.windowTypeVar, 
            width=UITheme.ENTRY_WIDTH_STANDARD,
            style="Professional.TCombobox"
        )
        selectWinDrop["values"] = self.global_state.window_options
        selectWinDrop.grid(column=1, row=5, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")
        selectWinDrop.bind("<<ComboboxSelected>>", lambda e: selectWinLabel.focus())

        # Width Entry
        widthLabel = ttk.Label(self.frame1, text="Enter Width (ft)", style="Professional.TLabel")
        widthLabel.grid(column=0, row=6, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")
        
        enterWidth = tk.Entry(
            self.frame1, 
            textvariable=self.global_state.Width,
            width=UITheme.ENTRY_WIDTH_STANDARD
        )
        UITheme.apply_theme_to_widget(enterWidth, "entry")
        enterWidth.grid(column=1, row=6, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")

        # Height Entry
        heightLabel = ttk.Label(self.frame1, text="Enter Height (ft)", style="Professional.TLabel")
        heightLabel.grid(column=0, row=7, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")
        
        enterHeight = tk.Entry(
            self.frame1, 
            textvariable=self.global_state.Height,
            width=UITheme.ENTRY_WIDTH_STANDARD
        )
        UITheme.apply_theme_to_widget(enterHeight, "entry")
        enterHeight.grid(column=1, row=7, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_MEDIUM, sticky="W")

        # Next Button with professional styling
        nextButt = tk.Button(
            self.frame1, 
            text="Next", 
            width=UITheme.BUTTON_WIDTH_STANDARD, 
            command=self.selector
        )
        UITheme.apply_theme_to_widget(nextButt, "button", button_type="success")
        nextButt.grid(column=1, row=8, padx=UITheme.PADDING_MEDIUM, pady=UITheme.PADDING_LARGE, sticky="W")
        
    def selector(self, event=None):
        """Open product configuration window exactly as legacy selector() function"""
        selected_window = self.global_state.windowTypeVar.get()
        if not selected_window:
            messagebox.showwarning("Selection Required", "Please select a window type.", parent=self.parent)
            return

        frame_class = self.product_frames.get(selected_window)
        if not frame_class:
            messagebox.showerror("Error", f"No configuration available for {selected_window}", parent=self.parent)
            return

        # Validate dimensions are entered
        try:
            width = float(self.global_state.Width.get()) if self.global_state.Width.get() else 0
            height = float(self.global_state.Height.get()) if self.global_state.Height.get() else 0
            if width <= 0 or height <= 0:
                messagebox.showerror("Invalid Dimensions", "Please enter valid width and height values.", parent=self.parent)
                return
        except ValueError:
            messagebox.showerror("Invalid Dimensions", "Please enter numeric values for width and height.", parent=self.parent)
            return

        # Update customer details in data manager before opening product window
        self.update_customer_details_in_data_manager()

        # Create a new Toplevel window for the product configuration
        product_window = tk.Toplevel(self.parent)
        product_window.title(selected_window)
        
        # Set window size and position - can be adjusted based on product type
        product_window.geometry("1200x800")
        
        # Pass the Toplevel window as the parent to the frame
        frame = frame_class(product_window, self.data_manager)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Configure the product window to expand with the frame
        product_window.grid_rowconfigure(0, weight=1)
        product_window.grid_columnconfigure(0, weight=1)
        
        product_window.transient(self.parent)
        product_window.grab_set()

    def update_customer_details_in_data_manager(self):
        """Update customer details in DataManager"""
        customer_details = {
            "custNamVar": self.global_state.custNamVar.get(),
            "custAddVar": self.global_state.custAddVar.get(),
            "custConVar": self.global_state.custConVar.get()
        }
        self.data_manager.set_customer_details(customer_details)

    def open_quotation(self):
        """Open quotation from file exactly as legacy open_file1()"""
        filename = filedialog.askopenfilename(
            title="Open Quotation",
            filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")],
            defaultextension=".xlsx",
            parent=self.parent
        )
        if not filename:
            return

        success, message = self.data_manager.load_quotation_from_excel(filename)

        if success:
            # Update the UI with the loaded customer details
            loaded_details = self.data_manager.get_customer_details()
            self.global_state.custNamVar.set(loaded_details.get('custNamVar', ''))
            self.global_state.custConVar.set(loaded_details.get('custConVar', ''))
            
            # Update address text widget
            address = loaded_details.get('custAddVar', '')
            self.global_state.custAddVar.set(address)
            self.global_state.address = address
            self.custAddEnt.delete("1.0", tk.END)
            self.custAddEnt.insert("1.0", address)
            
            messagebox.showinfo("Success", message, parent=self.parent)
            self.open_cart_view() # Open cart to show loaded items
        else:
            messagebox.showerror("Error", message, parent=self.parent)

    def open_cart_view(self):
        """Open cart view"""
        # Update customer details in DataManager before opening cart
        self.update_customer_details_in_data_manager()
        
        # Open Cart - pass self.parent (the root window) as parent, and self as main_app
        cart_view = CartView(self.parent, self.data_manager, main_app=self)
        cart_view.grab_set()

    def open_calculator_view(self):
        """Open calculator view"""
        calculator_view = CalculatorView(self.parent, self.data_manager)
        calculator_view.grab_set()
