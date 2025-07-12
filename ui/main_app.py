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
        """Create main window layout with responsive styling"""
        # Import responsive config
        from ui.responsive_config import get_responsive_config
        responsive = get_responsive_config(self.parent)
        
        # Configure professional theme for the application
        UITheme.configure_ttk_styles(self.parent)
        
        # Set main window background and center/maximize with unified system
        self.parent.configure(bg=UITheme.BACKGROUND_WHITE)
        responsive.center_main_window(self.parent)
        
        # Configure grid weights to center content in fullscreen window
        self.parent.grid_columnconfigure(0, weight=1)  # Left padding
        self.parent.grid_columnconfigure(1, weight=0)  # Left content column
        self.parent.grid_columnconfigure(2, weight=0)  # Right content column  
        self.parent.grid_columnconfigure(3, weight=1)  # Right padding
        self.parent.grid_rowconfigure(0, weight=1)     # Top padding
        self.parent.grid_rowconfigure(1, weight=0)     # Customer details row
        self.parent.grid_rowconfigure(2, weight=0)     # Window details row
        self.parent.grid_rowconfigure(3, weight=1)     # Bottom padding
        
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
        
        # Get responsive frame dimensions
        frame_width = responsive.get_main_frame_width()
        customer_height = responsive.get_main_frame_height("customer")
        window_height = responsive.get_main_frame_height("window")
        
        # Create frames with responsive styling - centered
        frame0 = tk.LabelFrame(self.parent, labelwidget=custDetails, width=frame_width, height=customer_height)
        UITheme.apply_theme_to_widget(frame0, "labelframe")
        frame0.grid(column=1, row=1, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="NW")
        frame0.grid_propagate(False)  # Maintain fixed dimensions
        
        frame1 = tk.LabelFrame(self.parent, labelwidget=windDetails, width=frame_width, height=window_height)
        UITheme.apply_theme_to_widget(frame1, "labelframe") 
        frame1.grid(column=1, row=2, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="NW")
        frame1.grid_propagate(False)  # Maintain fixed dimensions
        
        # Create a container frame for the logo area and cart button - centered
        self.right_container = tk.Frame(self.parent, bg=UITheme.BACKGROUND_WHITE)
        self.right_container.grid(column=2, row=1, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="NSEW", rowspan=2)
        self.right_container.grid_columnconfigure(0, weight=1)
        self.right_container.grid_rowconfigure(1, weight=1)
        
        # Create a single container for both test and cart buttons
        button_container = tk.Frame(self.right_container, bg=UITheme.BACKGROUND_WHITE)
        button_container.grid(column=0, row=0, sticky="EW", padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"))
        button_container.grid_columnconfigure(0, weight=1)  # Allow expansion
        
        # ============= TEST FUNCTIONALITY - COMMENT OUT WHEN NOT NEEDED =============
        # Create test button with responsive sizing
        test_button = tk.Button(
            button_container,
            text="Fill Test Data",
            command=self.fill_test_data,
            width=responsive.get_button_width("standard"),
            height=2,
            bg="#FF9800",
            fg="white",
            font=responsive.get_font_tuple("medium", "bold"),
            relief="flat"
        )
        test_button.pack(side=tk.LEFT, padx=responsive.get_padding("small"), pady=responsive.get_padding("small"))
        # ============= END TEST FUNCTIONALITY =============
        
        # Create cart button container on the right side
        cart_container = tk.Frame(button_container, bg=UITheme.BACKGROUND_WHITE)
        cart_container.pack(side=tk.RIGHT, padx=responsive.get_padding("small"), pady=responsive.get_padding("small"))
        
        # Create logo container below cart button
        frame2 = tk.LabelFrame(self.right_container, bg=UITheme.BACKGROUND_WHITE)
        UITheme.apply_theme_to_widget(frame2, "labelframe")
        frame2.grid(column=0, row=1, sticky="NSEW", padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"))

        # Store frame references
        self.frame0 = frame0  # Customer details
        self.frame1 = frame1  # Window details  
        self.frame2 = frame2  # Logo area
        self.cart_container = cart_container  # Cart button container
        self.button_container = button_container  # Button container

        # Create logo area with responsive styling
        self.create_logo_area(responsive)
        
        # Create cart button with responsive styling
        self.create_cart_button(responsive)
        
        # Create customer details section with responsive styling
        self.create_customer_details(responsive)
        
        # Create window details section with responsive styling
        self.create_window_details(responsive)

    def create_logo_area(self, responsive):
        """Create logo area with responsive sizing"""
        canvas = tk.Canvas(self.frame2, bg=UITheme.BACKGROUND_WHITE)
        try:
            logo_path = os.path.join(self.image_dir, "MGA_1.png")
            img = Image.open(logo_path)
            
            # Get responsive logo dimensions
            logo_width, logo_height = responsive.get_image_size(360, 250)
            resized_image = img.resize((logo_width, logo_height), Image.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(resized_image)
            
            canvas.create_image(logo_width//2, logo_height//2, image=self.logo_image)
            canvas.configure(width=logo_width, height=logo_height)
            canvas.pack(expand=True, fill=tk.BOTH, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"))
        except FileNotFoundError:
            print(f"Logo image not found at {logo_path}")
            # Add placeholder
            placeholder = ttk.Label(self.frame2, text="MGA Logo", style="Header.TLabel")
            placeholder.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    def create_cart_button(self, responsive):
        """Create cart button with responsive styling"""
        # Create cart button with explicit dimensions and padding
        cartButt = tk.Button(
            self.cart_container,
            text="🛒 Cart",  # Use emoji instead of icon for simplicity
            command=self.open_cart_view,
            width=15,  # Fixed width that should be visible
            height=2,  # Fixed height that should be visible
            font=responsive.get_font_tuple("medium", "bold"),
            bg=UITheme.PRIMARY_BLUE,
            fg="white",
            relief="flat",
            borderwidth=0,
            activebackground=UITheme.PRIMARY_BLUE_LIGHT,
            activeforeground="white"
        )
        cartButt.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Store reference for potential future use
        self.cart_button = cartButt

    def create_customer_details(self, responsive):
        """Create customer details section with responsive styling"""
        # Configure internal grid for consistent alignment
        self.frame0.grid_columnconfigure(0, weight=0, minsize=int(150 * responsive.scale_factor))  # Label column
        self.frame0.grid_columnconfigure(1, weight=1, minsize=int(200 * responsive.scale_factor))  # Entry column
        
        # Customer Name
        custNamLab = ttk.Label(self.frame0, text="Enter Customer Name", style="Professional.TLabel")
        custNamLab.grid(column=0, row=1, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")
        
        custNamEnt = tk.Entry(
            self.frame0, 
            textvariable=self.global_state.custNamVar, 
            width=responsive.get_entry_width("standard"),
            font=responsive.get_font_tuple("medium")
        )
        UITheme.apply_theme_to_widget(custNamEnt, "entry")
        custNamEnt.grid(column=1, row=1, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")

        # Customer Address (Text widget with responsive styling)
        custAddLab = ttk.Label(self.frame0, text="Enter Customer Address", style="Professional.TLabel")
        custAddLab.grid(column=0, row=2, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")
        
        self.custAddEnt = tk.Text(
            self.frame0, 
            height=3, 
            width=responsive.get_entry_width("standard"),
            bg=UITheme.BACKGROUND_WHITE,
            fg=UITheme.TEXT_DARK,
            font=responsive.get_font_tuple("medium"),
            relief="solid",
            borderwidth=1,
            insertbackground=UITheme.TEXT_DARK
        )
        self.custAddEnt.grid(column=1, row=2, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")
        
        # Bind text widget to update global state
        self.custAddEnt.bind('<KeyRelease>', self.update_address)

        # Customer Contact
        custConLab = ttk.Label(self.frame0, text="Enter Customer Contact No.", style="Professional.TLabel")
        custConLab.grid(column=0, row=3, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")
        
        custConEnt = tk.Entry(
            self.frame0, 
            textvariable=self.global_state.custConVar,
            width=responsive.get_entry_width("standard"),
            font=responsive.get_font_tuple("medium")
        )
        UITheme.apply_theme_to_widget(custConEnt, "entry")
        custConEnt.grid(column=1, row=3, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")

    def update_address(self, event=None):
        """Update global state address from text widget"""
        address_text = self.custAddEnt.get("1.0", tk.END).strip()
        self.global_state.custAddVar.set(address_text)
        self.global_state.address = address_text

    def create_window_details(self, responsive):
        """Create window details section with responsive styling"""
        # Configure internal grid for consistent alignment
        self.frame1.grid_columnconfigure(0, weight=0, minsize=int(150 * responsive.scale_factor))  # Label column
        self.frame1.grid_columnconfigure(1, weight=1, minsize=int(200 * responsive.scale_factor))  # Entry column
        
        # Window Type Selection
        selectWinLabel = ttk.Label(self.frame1, text="Select Window Type", style="Professional.TLabel")
        selectWinLabel.grid(column=0, row=5, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")
        
        selectWinDrop = ttk.Combobox(
            self.frame1, 
            state="readonly", 
            textvariable=self.global_state.windowTypeVar, 
            width=responsive.get_entry_width("standard"),
            style="Professional.TCombobox",
            font=responsive.get_font_tuple("medium")
        )
        selectWinDrop["values"] = self.global_state.window_options
        selectWinDrop.grid(column=1, row=5, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")
        selectWinDrop.bind("<<ComboboxSelected>>", lambda e: selectWinLabel.focus())

        # Width Entry
        widthLabel = ttk.Label(self.frame1, text="Enter Width (ft)", style="Professional.TLabel")
        widthLabel.grid(column=0, row=6, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")
        
        enterWidth = tk.Entry(
            self.frame1, 
            textvariable=self.global_state.Width,
            width=responsive.get_entry_width("standard"),
            font=responsive.get_font_tuple("medium")
        )
        UITheme.apply_theme_to_widget(enterWidth, "entry")
        enterWidth.grid(column=1, row=6, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")

        # Height Entry
        heightLabel = ttk.Label(self.frame1, text="Enter Height (ft)", style="Professional.TLabel")
        heightLabel.grid(column=0, row=7, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")
        
        enterHeight = tk.Entry(
            self.frame1, 
            textvariable=self.global_state.Height,
            width=responsive.get_entry_width("standard"),
            font=responsive.get_font_tuple("medium")
        )
        UITheme.apply_theme_to_widget(enterHeight, "entry")
        enterHeight.grid(column=1, row=7, padx=responsive.get_padding("medium"), pady=responsive.get_padding("medium"), sticky="W")

        # Next Button with responsive styling
        nextButt = tk.Button(
            self.frame1, 
            text="Next", 
            width=responsive.get_button_width("standard"), 
            command=self.selector,
            font=responsive.get_font_tuple("medium", "bold")
        )
        UITheme.apply_theme_to_widget(nextButt, "button", button_type="success")
        nextButt.grid(column=1, row=8, padx=responsive.get_padding("medium"), pady=responsive.get_padding("large"), sticky="W")
        
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
        
        # Center product window with unified responsive centering
        from ui.responsive_config import get_responsive_config
        responsive = get_responsive_config(self.parent)
        responsive.center_product_window(product_window)
        
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

    # Note: open_calculator_view method removed since calculation is now integrated into cart view

    # ============= TEST FUNCTIONALITY - COMMENT OUT WHEN NOT NEEDED =============
    def fill_test_data(self):
        """Fill form with test data for quick testing"""
        # Customer Details Test Data
        self.global_state.custNamVar.set("John Doe")
        self.global_state.custConVar.set("9876543210")
        
        # Fill address in text widget
        test_address = "123 Test Street,\nTest City, Test State\nPIN: 123456"
        self.custAddEnt.delete("1.0", tk.END)
        self.custAddEnt.insert("1.0", test_address)
        self.global_state.custAddVar.set(test_address)
        self.global_state.address = test_address
        
        # Window Details Test Data
        self.global_state.windowTypeVar.set("Sliding Window")
        self.global_state.Width.set("10")
        self.global_state.Height.set("8")
        
        print("✓ Test data filled successfully!")
    # ============= END TEST FUNCTIONALITY =============
