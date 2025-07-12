"""
RESPONSIVE PRODUCT FRAME SYSTEM
===============================

This file contains the ProductFrameConfig class which automatically adapts
all dimensions and sizing to different screen resolutions and DPI settings.

RESPONSIVE FEATURES:
- Automatic screen size detection and scaling
- DPI-aware font and widget sizing  
- Cross-platform compatibility (Windows, macOS, Linux)
- Minimum/maximum size constraints for usability
- Percentage-based layouts that adapt to screen size

The system automatically calculates appropriate sizes based on:
- Screen resolution (1920x1080 baseline)
- System DPI settings (96 DPI baseline)
- Physical screen size
- Platform-specific adjustments

All changes take effect when you restart the application.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from babel.numbers import format_currency
from global_state import get_global_state
from ui.responsive_config import get_responsive_config


class ProductFrameConfig:
    """
    Responsive configuration for all product frame dimensions and sizing
    
    RESPONSIVE SYSTEM:
    ==================
    
    This class now uses the ResponsiveConfig system to automatically
    calculate appropriate dimensions based on:
    
    1. SCREEN DETECTION: Automatically detects screen size and DPI
    2. SCALING CALCULATION: Calculates optimal scaling factors
    3. CONSTRAINT APPLICATION: Applies min/max limits for usability
    4. CROSS-PLATFORM: Works on Windows, macOS, and Linux
    
    The system ensures that:
    - UI elements are appropriately sized for the display
    - Text remains readable at all resolutions
    - Windows fit properly on screen
    - Layouts remain functional across different screen sizes
    """
    
    # Initialize responsive configuration
    _responsive = None
    _config_cache = None
    
    @classmethod
    def _get_responsive_config(cls):
        """Get or create responsive configuration instance"""
        if cls._responsive is None:
            cls._responsive = get_responsive_config()
        return cls._responsive
    
    @classmethod
    def _get_config(cls):
        """Get cached responsive configuration"""
        if cls._config_cache is None:
            responsive = cls._get_responsive_config()
            cls._config_cache = responsive.get_product_frame_config()
        return cls._config_cache
    
    @classmethod
    def _get_value(cls, key):
        """Get a responsive configuration value"""
        config = cls._get_config()
        return config.get(key, 0)
    
    # ============= RESPONSIVE VALUE GETTERS =============
    
    @classmethod
    def get_window_width(cls):
        return cls._get_value("WINDOW_WIDTH")
    
    @classmethod
    def get_window_height(cls):
        return cls._get_value("WINDOW_HEIGHT")
    
    @classmethod
    def get_frame_padding_x(cls):
        return cls._get_value("FRAME_PADDING_X")
    
    @classmethod
    def get_frame_padding_y(cls):
        return cls._get_value("FRAME_PADDING_Y")
    
    @classmethod
    def get_frame_border_width(cls):
        return cls._get_value("FRAME_BORDER_WIDTH")
    
    @classmethod
    def get_customer_section_width(cls):
        return cls._get_value("CUSTOMER_SECTION_WIDTH")
    
    @classmethod
    def get_customer_section_height(cls):
        return cls._get_value("CUSTOMER_SECTION_HEIGHT")
    
    @classmethod
    def get_customer_field_width(cls):
        return cls._get_value("CUSTOMER_FIELD_WIDTH")
    
    @classmethod
    def get_customer_address_height(cls):
        return cls._get_value("CUSTOMER_ADDRESS_HEIGHT")
    
    @classmethod
    def get_dimensions_section_width(cls):
        return cls._get_value("DIMENSIONS_SECTION_WIDTH")
    
    @classmethod
    def get_dimensions_section_height(cls):
        return cls._get_value("DIMENSIONS_SECTION_HEIGHT")
    
    @classmethod
    def get_dimensions_field_width(cls):
        return cls._get_value("DIMENSIONS_FIELD_WIDTH")
    
    @classmethod
    def get_cost_field_width(cls):
        return cls._get_value("COST_FIELD_WIDTH")
    
    @classmethod
    def get_calculate_button_width(cls):
        return cls._get_value("CALCULATE_BUTTON_WIDTH")
    
    @classmethod
    def get_specs_canvas_width(cls):
        return cls._get_value("SPECS_CANVAS_WIDTH")
    
    @classmethod
    def get_specs_canvas_height(cls):
        return cls._get_value("SPECS_CANVAS_HEIGHT")
    
    @classmethod
    def get_specs_scroll_width(cls):
        return cls._get_value("SPECS_SCROLL_WIDTH")
    
    @classmethod
    def get_specs_scroll_height(cls):
        return cls._get_value("SPECS_SCROLL_HEIGHT")
    
    @classmethod
    def get_specs_label_column_width(cls):
        return cls._get_value("SPECS_LABEL_COLUMN_WIDTH")
    
    @classmethod
    def get_specs_entry_column_width(cls):
        return cls._get_value("SPECS_ENTRY_COLUMN_WIDTH")
    
    @classmethod
    def get_specs_image_column_width(cls):
        return cls._get_value("SPECS_IMAGE_COLUMN_WIDTH")
    
    @classmethod
    def get_product_image_width(cls):
        return cls._get_value("PRODUCT_IMAGE_WIDTH")
    
    @classmethod
    def get_product_image_height(cls):
        return cls._get_value("PRODUCT_IMAGE_HEIGHT")
    
    @classmethod
    def get_dropdown_width(cls):
        return cls._get_value("DROPDOWN_WIDTH")
    
    @classmethod
    def get_entry_field_width(cls):
        return cls._get_value("ENTRY_FIELD_WIDTH")
    
    @classmethod
    def get_button_width(cls):
        return cls._get_value("BUTTON_WIDTH")
    
    @classmethod
    def get_button_height(cls):
        return cls._get_value("BUTTON_HEIGHT")
    
    @classmethod
    def get_next_button_width(cls):
        return cls._get_value("NEXT_BUTTON_WIDTH")
    
    @classmethod
    def get_next_button_height(cls):
        return cls._get_value("NEXT_BUTTON_HEIGHT")
    
    @classmethod
    def get_next_button_padding(cls):
        return cls._get_value("NEXT_BUTTON_PADDING")
    
    # ============= LEGACY COMPATIBILITY =============
    # Keep these for backward compatibility with existing code
    
    @classmethod
    @property
    def WINDOW_WIDTH(cls):
        return cls.get_window_width()
    
    @classmethod
    @property  
    def WINDOW_HEIGHT(cls):
        return cls.get_window_height()
    
    @classmethod
    @property
    def FRAME_PADDING_X(cls):
        return cls.get_frame_padding_x()
    
    @classmethod
    @property
    def FRAME_PADDING_Y(cls):
        return cls.get_frame_padding_y()
    
    @classmethod
    @property
    def FRAME_BORDER_WIDTH(cls):
        return cls.get_frame_border_width()
    
    @classmethod
    @property
    def CUSTOMER_SECTION_WIDTH(cls):
        return cls.get_customer_section_width()
    
    @classmethod
    @property
    def CUSTOMER_SECTION_HEIGHT(cls):
        return cls.get_customer_section_height()
    
    @classmethod
    @property
    def CUSTOMER_FIELD_WIDTH(cls):
        return cls.get_customer_field_width()
    
    @classmethod
    @property
    def CUSTOMER_ADDRESS_HEIGHT(cls):
        return cls.get_customer_address_height()
    
    @classmethod
    @property
    def DIMENSIONS_SECTION_WIDTH(cls):
        return cls.get_dimensions_section_width()
    
    @classmethod
    @property
    def DIMENSIONS_SECTION_HEIGHT(cls):
        return cls.get_dimensions_section_height()
    
    @classmethod
    @property
    def DIMENSIONS_FIELD_WIDTH(cls):
        return cls.get_dimensions_field_width()
    
    @classmethod
    @property
    def COST_FIELD_WIDTH(cls):
        return cls.get_cost_field_width()
    
    @classmethod
    @property
    def CALCULATE_BUTTON_WIDTH(cls):
        return cls.get_calculate_button_width()
    
    @classmethod
    @property
    def SPECS_CANVAS_WIDTH(cls):
        return cls.get_specs_canvas_width()
    
    @classmethod
    @property
    def SPECS_CANVAS_HEIGHT(cls):
        return cls.get_specs_canvas_height()
    
    @classmethod
    @property
    def SPECS_SCROLL_WIDTH(cls):
        return cls.get_specs_scroll_width()
    
    @classmethod
    @property
    def SPECS_SCROLL_HEIGHT(cls):
        return cls.get_specs_scroll_height()
    
    @classmethod
    @property
    def SPECS_LABEL_COLUMN_WIDTH(cls):
        return cls.get_specs_label_column_width()
    
    @classmethod
    @property
    def SPECS_ENTRY_COLUMN_WIDTH(cls):
        return cls.get_specs_entry_column_width()
    
    @classmethod
    @property
    def SPECS_IMAGE_COLUMN_WIDTH(cls):
        return cls.get_specs_image_column_width()
    
    @classmethod
    @property
    def PRODUCT_IMAGE_WIDTH(cls):
        return cls.get_product_image_width()
    
    @classmethod
    @property
    def PRODUCT_IMAGE_HEIGHT(cls):
        return cls.get_product_image_height()
    
    @classmethod
    @property
    def DROPDOWN_WIDTH(cls):
        return cls.get_dropdown_width()
    
    @classmethod
    @property
    def ENTRY_FIELD_WIDTH(cls):
        return cls.get_entry_field_width()
    
    @classmethod
    @property
    def BUTTON_WIDTH(cls):
        return cls.get_button_width()
    
    @classmethod
    @property
    def BUTTON_HEIGHT(cls):
        return cls.get_button_height()
    
    @classmethod
    @property
    def NEXT_BUTTON_WIDTH(cls):
        return cls.get_next_button_width()
    
    @classmethod
    @property
    def NEXT_BUTTON_HEIGHT(cls):
        return cls.get_next_button_height()
    
    @classmethod
    @property
    def NEXT_BUTTON_PADDING(cls):
        return cls.get_next_button_padding()
    
    @classmethod
    def get_scroll_region(cls):
        """Get scroll region tuple"""
        responsive = cls._get_responsive_config()
        scroll_width = responsive.get_window_width(1000)
        scroll_height = int(800 * responsive.scale_factor)
        return (0, 0, scroll_width, scroll_height)
    
    @classmethod
    def get_responsive_font(cls, size="medium", weight="normal"):
        """Get responsive font tuple"""
        responsive = cls._get_responsive_config()
        return responsive.get_font_tuple(size, weight)
    
    @classmethod
    def print_debug_info(cls):
        """Print responsive configuration debug information"""
        responsive = cls._get_responsive_config()
        responsive.print_screen_info()
        
        print("\n=== Product Frame Responsive Values ===")
        config = cls._get_config()
        for key, value in config.items():
            print(f"{key}: {value}")
        print("========================================")


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
        
        # Center the window on screen
        self.center_window()
        
        # Legacy frame references
        self.frame0 = None  # Dimensions and cost (middle)
        self.frame1 = None  # Scrollable specifications (bottom)  
        self.frame2 = None  # Customer details (top)
        self.frame_next = None  # Next button frame (fixed position)
        
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
        
        # Next button will be added by child classes calling add_next_button()

    def center_window(self):
        """Center the window on screen with unified responsive centering"""
        # Get responsive configuration
        responsive = ProductFrameConfig._get_responsive_config()
        
        # Use unified centering system for consistent positioning
        responsive.center_product_window(self.parent)

    def create_legacy_layout(self):
        """Create the exact 3-frame layout structure from legacy with responsive dimensions"""
        # Get responsive configuration
        responsive = ProductFrameConfig._get_responsive_config()
        
        # Frame 2: Customer Details (top) - row 0
        self.frame2 = tk.LabelFrame(
            self.parent, 
            borderwidth=responsive.get_border_width(),
            width=responsive.get_window_width(1000),
            height=int(120 * responsive.scale_factor)
        )
        self.frame2.grid(column=0, row=0, padx=responsive.get_padding("small"), pady=responsive.get_padding("small"), sticky="ew")
        self.frame2.grid_propagate(False)  # Maintain fixed dimensions
        
        # Frame 0: Dimensions & Cost (middle) - row 1  
        self.frame0 = tk.LabelFrame(
            self.parent, 
            borderwidth=responsive.get_border_width(),
            width=responsive.get_window_width(1000),
            height=int(150 * responsive.scale_factor)
        )
        self.frame0.grid(column=0, row=1, padx=responsive.get_padding("small"), pady=responsive.get_padding("small"), columnspan=4, sticky="W")
        self.frame0.grid_propagate(False)  # Maintain fixed dimensions
        
        # Frame Canvas: Container for scrollable specifications (bottom) - row 2
        self.frame_canvas = tk.Frame(self.parent, borderwidth=responsive.get_border_width())
        self.frame_canvas.grid(row=2, column=0, columnspan=3, pady=(responsive.get_padding("small"), 0), sticky="ew")
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        self.frame_canvas.grid_propagate(False)
        
        # Frame for Next button (bottom) - row 3 - Fixed position below specifications
        self.frame_next = tk.Frame(self.parent)
        self.frame_next.grid(row=3, column=0, columnspan=3, pady=responsive.get_padding("medium"), sticky="ew")

    def create_customer_details(self):
        """Create customer details section exactly as legacy with responsive sizing"""
        # Get responsive configuration
        responsive = ProductFrameConfig._get_responsive_config()
        
        custDetails = ttk.Label(
            self.frame2, text="Customer Details", font=responsive.get_font_tuple("medium", "bold")
        )
        custDetails.grid(column=0, row=0, padx=5, pady=10, sticky="W")

        # Customer name
        custNamLab = ttk.Label(self.frame2, text="Customer Name")
        custNamLab.grid(column=0, row=1, padx=5, pady=10, sticky="W")
        custNamEnt = tk.Entry(
            self.frame2,
            textvariable=self.global_state.custNamVar,
            font=responsive.get_font_tuple("medium"),
            relief="solid",
            width=responsive.get_entry_width("standard"),
            state="disabled",
        )
        custNamEnt.grid(column=1, row=1, padx=5, pady=10, sticky="W")

        # Customer address
        custAddLab = ttk.Label(self.frame2, text="Customer Address")
        custAddLab.grid(column=2, row=1, padx=5, pady=10, sticky="W")
        custAddEnt = tk.Text(
            self.frame2,
            font=responsive.get_font_tuple("medium"),
            relief="solid",
            height=2,  # Keep as lines
            width=responsive.get_entry_width("standard"),
            background="#f0f0f0",
            foreground="#6d6d6d",
        )
        custAddEnt.grid(column=3, row=1, padx=5, pady=10, sticky="W")
        custAddEnt.insert(1.0, self.global_state.address)
        custAddEnt.config(state=tk.DISABLED)

        # Customer contact
        custConLab = ttk.Label(self.frame2, text="Customer Contact No.")
        custConLab.grid(column=4, row=1, padx=5, pady=10, sticky="W")
        custConEnt = tk.Entry(
            self.frame2,
            textvariable=self.global_state.custConVar,
            font=responsive.get_font_tuple("medium"),
            relief="solid",
            width=responsive.get_entry_width("standard"),
            state="disabled",
        )
        custConEnt.grid(column=5, row=1, padx=5, pady=10, sticky="W")

    def create_dimensions_section(self):
        """Create dimensions and cost calculation section exactly as legacy with responsive sizing"""
        # Get responsive configuration
        responsive = ProductFrameConfig._get_responsive_config()
        
        # Product type label
        selectWinLabel = ttk.Label(
            self.frame0, text=self.parent.title(), font=responsive.get_font_tuple("medium", "bold")
        )
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky="W")

        # Width input
        widthLabel = ttk.Label(self.frame0, text="Enter Width (ft)")
        widthLabel.grid(column=0, row=1, padx=10, pady=10, sticky="W")
        enterWidth = tk.Entry(
            self.frame0, textvariable=self.global_state.Width, relief="solid", width=responsive.get_entry_width("large"), state="disabled"
        )
        enterWidth.grid(column=1, row=1, padx=10, pady=10, sticky="W")

        # Height input
        heightLabel = ttk.Label(self.frame0, text="Enter Height (ft)")
        heightLabel.grid(column=0, row=2, padx=10, pady=10, sticky="W")
        enterHeight = tk.Entry(
            self.frame0, textvariable=self.global_state.Height, relief="solid", width=responsive.get_entry_width("large"), state="disabled"
        )
        enterHeight.grid(column=1, row=2, padx=10, pady=10, sticky="W")

        # Total area display
        totSqft = ttk.Label(self.frame0, text="Total Area(In Sq.Ft)")
        totSqft.grid(column=2, row=1, padx=10, pady=10, sticky="W")
        self.totSqftEnt = tk.Entry(
            self.frame0,
            textvariable=self.global_state.totSqftEntVar,
            relief="solid",
            width=responsive.get_entry_width("standard"),
            state="disabled",
        )
        self.totSqftEnt.grid(column=3, row=1, padx=10, pady=10, sticky="W")

        # Cost per sq ft input
        cost = ttk.Label(self.frame0, text="Enter Cost (Cost per Sq.Ft)")
        cost.grid(column=2, row=2, padx=10, pady=10, sticky="W")
        self.costEnt = tk.Entry(
            self.frame0, textvariable=self.global_state.costEntVar, relief="solid", width=responsive.get_entry_width("standard")
        )
        self.costEnt.grid(column=3, row=2, padx=10, pady=10, sticky="W")

        # Total cost display
        cost = ttk.Label(self.frame0, text="Total Cost")
        cost.grid(column=4, row=1, padx=10, pady=10, sticky="W")
        self.costTot = tk.Entry(
            self.frame0,
            textvariable=self.global_state.cstAmtInr,
            relief="solid",
            width=responsive.get_entry_width("standard"),
            state="disabled",
        )
        self.costTot.grid(column=5, row=1, padx=10, pady=10, sticky="W")

        # Calculate button
        calculate = tk.Button(
            self.frame0, text="Calculate", width=responsive.get_button_width("large"), command=self.calculate_cost
        )
        calculate.grid(column=4, row=2, padx=10, pady=15, sticky="w", columnspan=2)

    def create_scrollable_specifications(self):
        """Create scrollable canvas area for specifications exactly as legacy with responsive sizing"""
        # Get responsive configuration
        responsive = ProductFrameConfig._get_responsive_config()
        
        # Create canvas with scrollbar
        self.canvas = tk.Canvas(self.frame_canvas)
        self.canvas.grid(row=0, column=0, sticky="news")

        vsb = tk.Scrollbar(self.frame_canvas, orient=tk.VERTICAL, command=self.canvas.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=vsb.set)

        # Create frame inside canvas for specifications with proper grid configuration
        self.frame_buttons = tk.LabelFrame(self.canvas, borderwidth=responsive.get_border_width(), padx=5)
        self.frame_buttons.grid(column=0, row=2, padx=5, pady=5)
        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor="nw")
        
        # Configure grid columns for proper alignment with responsive widths
        self.frame_buttons.grid_columnconfigure(0, weight=0, minsize=int(100 * responsive.scale_factor))  # Label column
        self.frame_buttons.grid_columnconfigure(1, weight=0, minsize=int(150 * responsive.scale_factor))  # Entry column
        self.frame_buttons.grid_columnconfigure(2, weight=1, minsize=int(800 * responsive.scale_factor))  # Image column
        
        # Set frame1 to the scrollable frame for specifications
        self.frame1 = self.frame_buttons
        
        # Bind mouse wheel events for scrolling
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>", self._on_mousewheel)
        self.canvas.bind("<Button-5>", self._on_mousewheel)
        
        # Bind mouse wheel to frame_canvas to catch events when mouse is over the scroll area
        self.frame_canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.frame_canvas.bind("<Button-4>", self._on_mousewheel)
        self.frame_canvas.bind("<Button-5>", self._on_mousewheel)
        
        # Make sure the canvas can receive focus for mouse events
        self.canvas.focus_set()
        
        # Bind mouse wheel to parent window so scrolling works anywhere in the window
        self.parent.bind("<MouseWheel>", self._on_mousewheel)
        self.parent.bind("<Button-4>", self._on_mousewheel)
        self.parent.bind("<Button-5>", self._on_mousewheel)
        
        # Configure canvas size using responsive configuration
        canvas_width = responsive.get_window_width(1000)
        canvas_height = int(500 * responsive.scale_factor)
        scroll_width = responsive.get_window_width(1000)
        scroll_height = int(800 * responsive.scale_factor)
        
        self.frame_buttons.update_idletasks()
        self.frame_canvas.config(width=canvas_width, height=canvas_height)
        self.canvas.config(scrollregion=(0, 0, scroll_width, scroll_height))
        
        # Update scroll region when content changes
        self.frame_buttons.bind("<Configure>", self._on_frame_configure)

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
        """Add large product image to specifications area with responsive sizing"""
        # Get responsive configuration
        responsive = ProductFrameConfig._get_responsive_config()
        
        try:
            image_path = os.path.join(self.image_dir, image_filename)
            image = Image.open(image_path)
            
            # Get responsive image dimensions
            img_width, img_height = responsive.get_image_size(600, 400)
            resize_image = image.resize((img_width, img_height))
            self.product_image = ImageTk.PhotoImage(resize_image)
            
            imgLab = tk.Label(self.frame1, image=self.product_image)
            imgLab.image = self.product_image  # Keep a reference
            imgLab.grid(column=2, row=1, rowspan=15, sticky="w")
            
            # Product title below image with responsive font
            selectWinLabel = ttk.Label(
                self.frame1, text=self.parent.title(), font=responsive.get_font_tuple("header", "bold")
            )
            selectWinLabel.grid(column=2, row=16, sticky="wn")
            
            # Disclaimer text with responsive font
            selectWinLabel = ttk.Label(
                self.frame1,
                text="(This is an Illustration, not actual product)",
                font=responsive.get_font_tuple("small"),
            )
            selectWinLabel.grid(column=2, row=17, sticky="wn")
            
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

        # Enhanced cost data to ensure proper cart synchronization
        try:
            # Get the calculated values from global state
            width = float(self.global_state.Width.get()) if self.global_state.Width.get() else 0
            height = float(self.global_state.Height.get()) if self.global_state.Height.get() else 0
            total_sqft = width * height
            cost_per_sqft = float(self.global_state.costEntVar.get()) if self.global_state.costEntVar.get() else 0
            
            # Calculate the total cost to ensure consistency
            total_cost = total_sqft * cost_per_sqft
            
            # Override the cost data with calculated values for proper cart display
            item_data.update({
                "Total Sq.ft": total_sqft,
                "Cost (INR)": cost_per_sqft,  # Cost per sq.ft
                "Amount": total_cost,  # Total cost for this item
                "Quantity": 1,  # Default quantity
            })
            
            print(f"Adding to cart - Cost per sq.ft: ₹{cost_per_sqft}, Total cost: ₹{total_cost}")
            
        except (ValueError, TypeError) as e:
            print(f"Error processing cost data: {e}")
            # Fall back to original data if calculation fails

        self.data_manager.add_item_to_cart(item_data)
        messagebox.showinfo("Success", f"{item_data['windowTypeVar']} added to cart.", parent=self.parent)
        self.parent.destroy()  # Close the Toplevel window

    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling for specifications section"""
        # Cross-platform mouse wheel handling
        if event.delta:
            # Windows and MacOS
            delta = -1 if event.delta > 0 else 1
        else:
            # Linux
            delta = -1 if event.num == 4 else 1
        
        self.canvas.yview_scroll(delta, "units")
        
    def _on_frame_configure(self, event):
        """Update scroll region when frame content changes"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def add_next_button(self):
        """Add Next button in fixed position below specifications section with responsive sizing"""
        # Get responsive configuration
        responsive = ProductFrameConfig._get_responsive_config()
        
        nextButt = tk.Button(
            self.frame_next, 
            text="Add to Cart", 
            font=responsive.get_font_tuple("large", "bold"), 
            width=responsive.get_button_width("standard"), 
            command=self.add_to_cart,
            bg="#4CAF50",
            fg="white",
            relief="flat",
            pady=2  # Keep as lines
        )
        nextButt.pack(pady=responsive.get_padding("medium")) 