"""
Responsive Configuration System - Window Quotation Application
============================================================

This module provides a comprehensive responsive design system that automatically
scales UI elements based on screen resolution and DPI settings.

Key Features:
- Screen resolution detection and scaling factors
- DPI-aware font and widget sizing
- Responsive window dimensions with min/max constraints
- Percentage-based layouts that adapt to different screen sizes
- Cross-platform compatibility (Windows, Linux, macOS)

Usage:
    from ui.responsive_config import ResponsiveConfig
    
    # Get responsive instance
    responsive = ResponsiveConfig()
    
    # Use responsive dimensions
    window_width = responsive.get_window_width()
    font_size = responsive.get_font_size("medium")
    padding = responsive.get_padding("medium")
"""

import tkinter as tk
import platform
import math


class ResponsiveConfig:
    """
    Responsive configuration system that adapts UI elements to screen size and DPI
    """
    
    def __init__(self, root_window=None):
        """
        Initialize responsive configuration
        
        Args:
            root_window: tkinter root window for screen detection (optional)
        """
        # Create temporary window for screen detection if none provided
        if root_window is None:
            temp_root = tk.Tk()
            temp_root.withdraw()  # Hide the window
            self.root = temp_root
            self._temp_root = True
        else:
            self.root = root_window
            self._temp_root = False
        
        # Detect screen properties
        self._detect_screen_properties()
        
        # Calculate scaling factors
        self._calculate_scaling_factors()
        
        # Clean up temporary window
        if self._temp_root:
            self.root.destroy()
            self.root = None
    
    def _detect_screen_properties(self):
        """Detect screen dimensions and DPI"""
        try:
            # Get screen dimensions
            self.screen_width = self.root.winfo_screenwidth()
            self.screen_height = self.root.winfo_screenheight()
            
            # Get DPI (dots per inch)
            self.dpi = self.root.winfo_fpixels('1i')
            
            # Calculate screen diagonal in inches
            diagonal_pixels = math.sqrt(self.screen_width**2 + self.screen_height**2)
            self.screen_diagonal_inches = diagonal_pixels / self.dpi
            
            # Determine screen category
            self._categorize_screen()
            
        except Exception as e:
            print(f"Error detecting screen properties: {e}")
            # Fallback to standard values
            self.screen_width = 1920
            self.screen_height = 1080
            self.dpi = 96
            self.screen_diagonal_inches = 24
            self.screen_category = "medium"
    
    def _categorize_screen(self):
        """Categorize screen size for responsive behavior"""
        # Screen categories based on resolution and physical size
        if self.screen_width <= 1366 or self.screen_diagonal_inches < 15:
            self.screen_category = "small"
        elif self.screen_width <= 1920 or self.screen_diagonal_inches < 24:
            self.screen_category = "medium"
        elif self.screen_width <= 2560 or self.screen_diagonal_inches < 32:
            self.screen_category = "large"
        else:
            self.screen_category = "xlarge"
    
    def _calculate_scaling_factors(self):
        """Calculate scaling factors based on screen properties"""
        # Base scaling factor from DPI (96 DPI = 1.0 scale)
        self.dpi_scale = self.dpi / 96.0
        
        # Resolution-based scaling factor (1920x1080 = 1.0 scale)
        base_width = 1920
        base_height = 1080
        
        width_scale = self.screen_width / base_width
        height_scale = self.screen_height / base_height
        self.resolution_scale = min(width_scale, height_scale)  # Use smaller to prevent overflow
        
        # Combined scaling factor with constraints
        raw_scale = (self.dpi_scale + self.resolution_scale) / 2
        
        # Apply constraints to prevent extreme scaling
        self.scale_factor = max(0.7, min(raw_scale, 2.0))
        
        # Platform-specific adjustments
        if platform.system() == "Darwin":  # macOS
            self.scale_factor *= 0.9  # macOS tends to have larger default fonts
        elif platform.system() == "Linux":
            self.scale_factor *= 1.05  # Linux may need slight boost
    
    # ============= WINDOW DIMENSIONS =============
    
    def get_window_width(self, base_width=1000):
        """Get responsive window width"""
        responsive_width = int(base_width * self.scale_factor)
        
        # Constraints based on screen size
        min_width = int(self.screen_width * 0.4)  # Minimum 40% of screen
        max_width = int(self.screen_width * 0.9)  # Maximum 90% of screen
        
        return max(min_width, min(responsive_width, max_width))
    
    def get_window_height(self, base_height=900):
        """Get responsive window height"""
        responsive_height = int(base_height * self.scale_factor)
        
        # Constraints based on screen size
        min_height = int(self.screen_height * 0.5)  # Minimum 50% of screen
        max_height = int(self.screen_height * 0.9)  # Maximum 90% of screen
        
        return max(min_height, min(responsive_height, max_height))
    
    def get_main_frame_width(self):
        """Get responsive width for main application frames"""
        base_width = 420
        responsive_width = int(base_width * self.scale_factor)
        
        # Ensure reasonable constraints
        min_width = 350
        max_width = 600
        
        return max(min_width, min(responsive_width, max_width))
    
    def get_main_frame_height(self, frame_type="customer"):
        """Get responsive height for main application frames"""
        base_heights = {
            "customer": 190,
            "window": 210,
            "logo": 300
        }
        
        base_height = base_heights.get(frame_type, 200)
        responsive_height = int(base_height * self.scale_factor)
        
        # Constraints
        min_height = int(base_height * 0.8)
        max_height = int(base_height * 1.5)
        
        return max(min_height, min(responsive_height, max_height))
    
    # ============= WIDGET DIMENSIONS =============
    
    def get_entry_width(self, size="standard"):
        """Get responsive entry widget width"""
        base_widths = {
            "small": 15,
            "standard": 25,
            "large": 35,
            "xlarge": 45
        }
        
        base_width = base_widths.get(size, 25)
        responsive_width = int(base_width * self.scale_factor)
        
        # Constraints
        min_width = max(10, int(base_width * 0.7))
        max_width = int(base_width * 1.8)
        
        return max(min_width, min(responsive_width, max_width))
    
    def get_button_width(self, size="standard"):
        """Get responsive button width"""
        base_widths = {
            "small": 15,
            "standard": 20,
            "large": 25,
            "xlarge": 30
        }
        
        base_width = base_widths.get(size, 20)
        responsive_width = int(base_width * self.scale_factor)
        
        # Constraints
        min_width = max(10, int(base_width * 0.8))
        max_width = int(base_width * 1.5)
        
        return max(min_width, min(responsive_width, max_width))
    
    def get_button_height(self, size="standard"):
        """Get responsive button height"""
        base_heights = {
            "small": 2,
            "standard": 3,
            "large": 4,
            "xlarge": 5
        }
        
        base_height = base_heights.get(size, 3)
        responsive_height = int(base_height * self.scale_factor)
        
        # Constraints to ensure buttons are always usable
        min_height = 2
        max_height = max(6, int(base_height * 1.5))
        
        return max(min_height, min(responsive_height, max_height))

    def get_image_size(self, base_width, base_height):
        """Get responsive image dimensions"""
        responsive_width = int(base_width * self.scale_factor)
        responsive_height = int(base_height * self.scale_factor)
        
        # Constraints to prevent images from becoming too large or small
        min_width = int(base_width * 0.6)
        max_width = int(base_width * 1.8)
        min_height = int(base_height * 0.6)
        max_height = int(base_height * 1.8)
        
        final_width = max(min_width, min(responsive_width, max_width))
        final_height = max(min_height, min(responsive_height, max_height))
        
        return final_width, final_height
    
    # ============= SPACING AND PADDING =============
    
    def get_padding(self, size="medium"):
        """Get responsive padding values"""
        base_paddings = {
            "small": 5,
            "medium": 10,
            "large": 15,
            "xlarge": 20
        }
        
        base_padding = base_paddings.get(size, 10)
        responsive_padding = int(base_padding * self.scale_factor)
        
        # Constraints
        min_padding = max(2, int(base_padding * 0.5))
        max_padding = int(base_padding * 2.0)
        
        return max(min_padding, min(responsive_padding, max_padding))
    
    def get_border_width(self):
        """Get responsive border width"""
        base_border = 2
        responsive_border = max(1, int(base_border * self.scale_factor))
        return min(responsive_border, 4)  # Cap at 4 pixels
    
    # ============= FONT SIZING =============
    
    def get_font_size(self, size="medium"):
        """Get responsive font size"""
        base_sizes = {
            "small": 9,
            "medium": 10,
            "large": 12,
            "xlarge": 14,
            "header": 16
        }
        
        base_size = base_sizes.get(size, 10)
        responsive_size = int(base_size * self.scale_factor)
        
        # Font size constraints
        min_size = max(8, int(base_size * 0.8))
        max_size = int(base_size * 1.6)
        
        return max(min_size, min(responsive_size, max_size))
    
    def get_font_tuple(self, size="medium", weight="normal"):
        """Get complete font tuple (family, size, weight)"""
        font_size = self.get_font_size(size)
        
        # Cross-platform font family
        if platform.system() == "Windows":
            font_family = "Segoe UI"
        elif platform.system() == "Darwin":
            font_family = "SF Pro Display"
        else:
            font_family = "Ubuntu"
        
        return (font_family, font_size, weight)
    
    # ============= SPECIALIZED CALCULATIONS =============
    
    def get_product_frame_config(self):
        """Get complete responsive configuration for product frames"""
        return {
            # Main window
            "WINDOW_WIDTH": self.get_window_width(1000),
            "WINDOW_HEIGHT": self.get_window_height(900),
            
            # Frame dimensions
            "CUSTOMER_SECTION_WIDTH": self.get_window_width(1000),
            "CUSTOMER_SECTION_HEIGHT": int(120 * self.scale_factor),
            "DIMENSIONS_SECTION_WIDTH": self.get_window_width(1000),
            "DIMENSIONS_SECTION_HEIGHT": int(150 * self.scale_factor),
            
            # Canvas and scrolling
            "SPECS_CANVAS_WIDTH": self.get_window_width(1000),
            "SPECS_CANVAS_HEIGHT": int(500 * self.scale_factor),
            "SPECS_SCROLL_WIDTH": self.get_window_width(1000),
            "SPECS_SCROLL_HEIGHT": int(800 * self.scale_factor),
            
            # Column widths
            "SPECS_LABEL_COLUMN_WIDTH": int(100 * self.scale_factor),
            "SPECS_ENTRY_COLUMN_WIDTH": int(150 * self.scale_factor),
            "SPECS_IMAGE_COLUMN_WIDTH": int(800 * self.scale_factor),
            
            # Product image
            "PRODUCT_IMAGE_WIDTH": int(600 * self.scale_factor),
            "PRODUCT_IMAGE_HEIGHT": int(400 * self.scale_factor),
            
            # Widget dimensions
            "CUSTOMER_FIELD_WIDTH": self.get_entry_width("standard"),
            "DIMENSIONS_FIELD_WIDTH": self.get_entry_width("large"),
            "COST_FIELD_WIDTH": self.get_entry_width("standard"),
            "CALCULATE_BUTTON_WIDTH": self.get_button_width("large"),
            "DROPDOWN_WIDTH": self.get_entry_width("standard"),
            "ENTRY_FIELD_WIDTH": self.get_entry_width("standard"),
            "BUTTON_WIDTH": self.get_button_width("standard"),
            "NEXT_BUTTON_WIDTH": self.get_button_width("standard"),
            
            # Spacing
            "FRAME_PADDING_X": self.get_padding("small"),
            "FRAME_PADDING_Y": self.get_padding("small"),
            "FRAME_BORDER_WIDTH": self.get_border_width(),
            "NEXT_BUTTON_PADDING": self.get_padding("medium"),
            
            # Heights
            "CUSTOMER_ADDRESS_HEIGHT": 2,  # Text widget height in lines
            "BUTTON_HEIGHT": 2,  # Button height in lines
            "NEXT_BUTTON_HEIGHT": 2,  # Next button height in lines
        }
    
    def get_cart_window_size(self):
        """Get responsive size for cart window"""
        # Cart window uses percentage of screen size
        width = int(self.screen_width * 0.40)
        height = int(self.screen_height * 0.70)
        
        # Ensure minimum usable size
        # min_width = 800
        # min_height = 600
        
        # return max(width, min_width), max(height, min_height)
    
        return width, height

    def get_invoice_window_size(self):
        """Get responsive size for invoice window"""
        base_width = 400
        base_height = 800
        
        width = self.get_window_width(base_width)
        height = self.get_window_height(base_height)
        
        return width, height
    
    # ============= UTILITY METHODS =============
    
    def center_window(self, window, window_name=None, width=None, height=None, base_width=None, base_height=None):
        """
        Center any window on screen with unified positioning
        
        This method provides consistent centering for all windows in the application
        to give a unified look and feel.
        
        Args:
            window: tkinter window object (Toplevel, Tk, etc.)
            width: specific width to use (optional)
            height: specific height to use (optional)  
            base_width: base width for responsive calculation (optional)
            base_height: base height for responsive calculation (optional)
        
        Usage:
            # Center with specific dimensions
            responsive.center_window(window, width=800, height=600)
            
            # Center with responsive dimensions
            responsive.center_window(window, base_width=1000, base_height=900)
            
            # Center with current window size
            responsive.center_window(window)
        """
        # Wait for window to be properly initialized
        window.update_idletasks()
        
        # Determine window dimensions
        if width is not None and height is not None:
            # Use provided dimensions
            window_width = width
            window_height = height
        elif base_width is not None and base_height is not None:
            # Calculate responsive dimensions
            window_width = self.get_window_width(base_width)
            window_height = self.get_window_height(base_height)
        else:
            # Use current window dimensions
            window_width = window.winfo_reqwidth()
            window_height = window.winfo_reqheight()
            
            # If dimensions are too small, use defaults
            if window_width < 100:
                window_width = self.get_window_width(800)
            if window_height < 100:
                window_height = self.get_window_height(600)
        
        # Get screen dimensions
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        # DEBUG: Compare screen dimensions for cart windows
        if window_name == 'cart':
            print(f"=== CART WINDOW DEBUG ===")
            print(f"ResponsiveConfig.screen_width: {self.screen_width}")
            print(f"window.winfo_screenwidth(): {screen_width}")
            print(f"ResponsiveConfig.screen_height: {self.screen_height}")
            print(f"window.winfo_screenheight(): {screen_height}")
            print(f"Window dimensions: {window_width}x{window_height}")
            print(f"Cart size calculation used: {self.screen_width} * 0.40 = {int(self.screen_width * 0.40)}")
            print(f"Cart size calculation used: {self.screen_height} * 0.70 = {int(self.screen_height * 0.70)}")
        
        # Calculate center position
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # DEBUG: Show centering calculation for cart
        if window_name == 'cart':
            print(f"Centering calculation:")
            print(f"x = ({screen_width} - {window_width}) // 2 = {x}")
            print(f"y = ({screen_height} - {window_height}) // 2 = {y}")
        
        # Move all windows 100 pixels higher (towards the top) for better positioning
        y = y - 150
        
        if window_name == 'cart':
            # TEST: print parent root location for debugging
            try:
                root_x = window.master.winfo_rootx()
                root_y = window.master.winfo_rooty()
                print(f"Root window origin: ({root_x}, {root_y})")
            except Exception as e:
                print(f"Could not get root coordinates: {e}")
            # Revert to normal x centering calculation (no forcing)
            # Remove any manual shift
            # x = screen_width - window_width - 50  # previous test
            print(f"After adjustments: x = {x}, y = {y}")
            print(f"Expected window center: {x + window_width//2}")
            print(f"Screen center: {screen_width//2}")
            print(f"Distance from screen center: {(x + window_width//2) - screen_width//2}")
            print(f"========================")
        else:
            # Ensure window doesn't go off-screen
            x = max(0, min(x, screen_width - window_width))
            y = max(0, min(y, screen_height - window_height))
        
        # Set window geometry and position
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        print(f"Window geometry: {window_width}x{window_height}+{x}+{y}")
        return window_width, window_height, x, y
    
    def center_main_window(self, window):
        """Center the main application window (maximized)"""
        # For main window, we typically want to maximize
        window.state('zoomed')  # Windows
        # Note: For other platforms, might need different approaches
        return self.screen_width, self.screen_height, 0, 0
    
    def center_product_window(self, window):
        """Center product configuration windows with consistent sizing"""
        return self.center_window(window, base_width=1000, base_height=900)
    
    def _center_over_parent(self, window, parent_window, width, height, y_offset=-150):
        """Center a child window over its parent window"""
        # Ensure parent dimensions are updated
        parent_window.update_idletasks()
        pw = parent_window.winfo_width()
        ph = parent_window.winfo_height()
        px = parent_window.winfo_rootx()
        py = parent_window.winfo_rooty()

        print(pw,ph,px,py)
        # Fallback if parent not yet sized
        if pw == 1 or ph == 1:
            pw = parent_window.winfo_screenwidth()
            ph = parent_window.winfo_screenheight()
            px = 0
            py = 0

        # Calculate coordinates
        x = px + (pw - width) // 2
        y = py + (ph - height) // 2 + y_offset

        # Ensure on-screen
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = max(0, min(x, screen_width - width))
        y = max(0, min(y, screen_height - height))


        window.geometry(f"{width}x{height}+{x}+{y}")
        return width, height, x, y

    def center_cart_window(self, window):
        """Center cart window relative to parent (main) window"""
        width, height = self.get_cart_window_size()
        parent_window = window.master if window.master is not None else window
        # Prefer centering over parent instead of full screen for better visual alignment
        return self._center_over_parent(window, parent_window, width, height)
    
    def center_invoice_window(self, window):
        """Center invoice window with consistent sizing"""
        width, height = self.get_invoice_window_size()
        return self.center_window(window, width=width, height=height)
    
    def center_calculator_window(self, window):
        """Center calculator window with appropriate sizing"""
        return self.center_window(window, base_width=600, base_height=400)

    def get_screen_info(self):
        """Get detailed screen information for debugging"""
        return {
            "screen_width": self.screen_width,
            "screen_height": self.screen_height,
            "dpi": self.dpi,
            "screen_diagonal_inches": round(self.screen_diagonal_inches, 1),
            "screen_category": self.screen_category,
            "dpi_scale": round(self.dpi_scale, 2),
            "resolution_scale": round(self.resolution_scale, 2),
            "final_scale_factor": round(self.scale_factor, 2),
            "platform": platform.system()
        }
    
    def print_screen_info(self):
        """Print screen information for debugging"""
        info = self.get_screen_info()
        print("=== Responsive Configuration Debug Info ===")
        for key, value in info.items():
            print(f"{key}: {value}")
        print("==========================================")


# Global instance for easy access
_responsive_instance = None

def get_responsive_config(root_window=None):
    """
    Get global responsive configuration instance
    
    Args:
        root_window: tkinter root window (only needed on first call)
    
    Returns:
        ResponsiveConfig: Global responsive configuration instance
    """
    global _responsive_instance
    
    if _responsive_instance is None:
        _responsive_instance = ResponsiveConfig(root_window)
    
    return _responsive_instance

def reset_responsive_config():
    """Reset the global responsive configuration (for testing)"""
    global _responsive_instance
    _responsive_instance = None 