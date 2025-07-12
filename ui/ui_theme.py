"""
UI Theme and Styling Module - Responsive Professional Appearance
Defines responsive fonts, colors, and styling for the MGA Window Quotation Application
"""

import tkinter as tk
from tkinter import ttk

class UITheme:
    """Professional UI theme with responsive styling"""
    
    # ============= PROFESSIONAL COLOR PALETTE =============
    
    # Primary Colors (Professional Blue Theme)
    PRIMARY_BLUE = "#3B82F6"        # Primary action color (lighter, more appealing)
    PRIMARY_BLUE_LIGHT = "#60A5FA"  # Hover states (even lighter)
    PRIMARY_BLUE_DARK = "#2563EB"   # Active states (medium blue)
    
    # Neutral Colors (Professional Grays)
    BACKGROUND_WHITE = "#FFFFFF"     # Main backgrounds
    BACKGROUND_LIGHT = "#F8FAFC"     # Secondary backgrounds  
    BACKGROUND_GRAY = "#F1F5F9"      # Input backgrounds
    BORDER_GRAY = "#E2E8F0"          # Borders and dividers
    TEXT_DARK = "#1E293B"            # Primary text
    TEXT_MEDIUM = "#475569"          # Secondary text
    TEXT_LIGHT = "#64748B"           # Disabled text
    
    # Status Colors
    SUCCESS_GREEN = "#10B981"        # Success states
    WARNING_ORANGE = "#F59E0B"       # Warning states
    ERROR_RED = "#EF4444"            # Error states
    
    # Accent Colors
    ACCENT_BLUE = "#0EA5E9"          # Links and highlights
    ACCENT_PURPLE = "#8B5CF6"        # Special elements
    
    # ============= RESPONSIVE INTEGRATION =============
    
    @classmethod
    def get_responsive_config(cls):
        """Get responsive configuration instance"""
        try:
            from ui.responsive_config import get_responsive_config
            return get_responsive_config()
        except ImportError:
            return None
    
    # ============= RESPONSIVE TYPOGRAPHY =============
    
    @classmethod
    def get_header_font(cls):
        """Get responsive font for headers and section titles"""
        responsive = cls.get_responsive_config()
        if responsive:
            return responsive.get_font_tuple("large", "bold")
        else:
            return ("Segoe UI", 12, "bold")
    
    @classmethod
    def get_body_font(cls):
        """Get responsive font for regular body text"""
        responsive = cls.get_responsive_config()
        if responsive:
            return responsive.get_font_tuple("medium", "normal")
        else:
            return ("Segoe UI", 10, "normal")
    
    @classmethod
    def get_small_font(cls):
        """Get responsive font for small text and captions"""
        responsive = cls.get_responsive_config()
        if responsive:
            return responsive.get_font_tuple("small", "normal")
        else:
            return ("Segoe UI", 9, "normal")
    
    # ============= RESPONSIVE SPACING =============
    
    @classmethod
    def get_padding_small(cls):
        """Get responsive small padding"""
        responsive = cls.get_responsive_config()
        if responsive:
            return responsive.get_padding("small")
        else:
            return 5
    
    @classmethod
    def get_padding_medium(cls):
        """Get responsive medium padding"""
        responsive = cls.get_responsive_config()
        if responsive:
            return responsive.get_padding("medium")
        else:
            return 10
    
    @classmethod
    def get_padding_large(cls):
        """Get responsive large padding"""
        responsive = cls.get_responsive_config()
        if responsive:
            return responsive.get_padding("large")
        else:
            return 15
    
    # ============= RESPONSIVE WIDGET DIMENSIONS =============
    
    @classmethod
    def get_button_width_standard(cls):
        """Get responsive standard button width"""
        responsive = cls.get_responsive_config()
        if responsive:
            return responsive.get_button_width("standard")
        else:
            return 20
    
    @classmethod
    def get_button_width_large(cls):
        """Get responsive large button width"""
        responsive = cls.get_responsive_config()
        if responsive:
            return responsive.get_button_width("large")
        else:
            return 25
    
    @classmethod
    def get_entry_width_standard(cls):
        """Get responsive standard entry width"""
        responsive = cls.get_responsive_config()
        if responsive:
            return responsive.get_entry_width("standard")
        else:
            return 25
    
    @classmethod
    def get_entry_width_large(cls):
        """Get responsive large entry width"""
        responsive = cls.get_responsive_config()
        if responsive:
            return responsive.get_entry_width("large")
        else:
            return 35
    
    # ============= LEGACY COMPATIBILITY =============
    # Keep these for backward compatibility with existing code
    
    PADDING_SMALL = property(lambda cls: cls.get_padding_small())
    PADDING_MEDIUM = property(lambda cls: cls.get_padding_medium())
    PADDING_LARGE = property(lambda cls: cls.get_padding_large())
    PADDING_XLARGE = property(lambda cls: cls.get_padding_large())  # Map to large
    
    BUTTON_WIDTH_STANDARD = property(lambda cls: cls.get_button_width_standard())
    BUTTON_WIDTH_LARGE = property(lambda cls: cls.get_button_width_large())
    ENTRY_WIDTH_STANDARD = property(lambda cls: cls.get_entry_width_standard())
    ENTRY_WIDTH_LARGE = property(lambda cls: cls.get_entry_width_large())
    
    # ============= WIDGET STYLES =============
    
    @classmethod
    def configure_ttk_styles(cls, root):
        """Configure ttk styles with responsive fonts"""
        style = ttk.Style(root)
        
        # Configure styles with responsive fonts
        header_font = cls.get_header_font()
        body_font = cls.get_body_font()
        
        # Header styles
        style.configure("Header.TLabel", 
                       font=header_font,
                       foreground=cls.TEXT_DARK,
                       background=cls.BACKGROUND_WHITE)
        
        # Professional styles
        style.configure("Professional.TLabel",
                       font=body_font,
                       foreground=cls.TEXT_DARK,
                       background=cls.BACKGROUND_WHITE)
        
        style.configure("Professional.TCombobox",
                       font=body_font,
                       fieldbackground=cls.BACKGROUND_WHITE,
                       borderwidth=1,
                       relief="solid")
    
    @classmethod
    def apply_theme_to_widget(cls, widget, widget_type, **kwargs):
        """Apply responsive theme to a widget"""
        responsive = cls.get_responsive_config()
        
        if widget_type == "entry":
            widget.configure(
                bg=cls.BACKGROUND_WHITE,
                fg=cls.TEXT_DARK,
                font=cls.get_body_font(),
                relief="solid",
                borderwidth=1,
                insertbackground=cls.TEXT_DARK
            )
        elif widget_type == "button":
            button_type = kwargs.get("button_type", "default")
            
            if button_type == "primary":
                bg_color = cls.PRIMARY_BLUE
                fg_color = cls.BACKGROUND_WHITE
            elif button_type == "success":
                bg_color = cls.SUCCESS_GREEN
                fg_color = cls.BACKGROUND_WHITE
            else:
                bg_color = cls.BACKGROUND_GRAY
                fg_color = cls.TEXT_DARK
            
            widget.configure(
                bg=bg_color,
                fg=fg_color,
                font=cls.get_body_font(),
                relief="flat",
                borderwidth=0,
                activebackground=cls.PRIMARY_BLUE_LIGHT if button_type == "primary" else cls.BACKGROUND_LIGHT,
                activeforeground=fg_color
            )
        elif widget_type == "labelframe":
            widget.configure(
                bg=cls.BACKGROUND_WHITE,
                fg=cls.TEXT_DARK,
                font=cls.get_header_font(),
                relief="groove",
                borderwidth=1
            ) 