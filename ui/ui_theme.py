"""
UI Theme and Styling Module - Professional Appearance
Defines consistent fonts, colors, and styling for the MGA Window Quotation Application
"""

import tkinter as tk
from tkinter import ttk

class UITheme:
    """Professional UI theme with consistent styling"""
    
    # ============= PROFESSIONAL COLOR PALETTE =============
    
    # Primary Colors (Professional Blue Theme)
    PRIMARY_BLUE = "#1E40AF"        # Primary action color
    PRIMARY_BLUE_LIGHT = "#3B82F6"  # Hover states
    PRIMARY_BLUE_DARK = "#1E3A8A"   # Active states
    
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
    
    # ============= TYPOGRAPHY =============
    
    # Font Families (fallback chain for cross-platform compatibility)
    FONT_PRIMARY = ("Segoe UI", "Helvetica Neue", "Arial", "sans-serif")
    FONT_SECONDARY = ("Consolas", "Monaco", "Courier New", "monospace")
    
    # Font Sizes
    FONT_SIZE_LARGE = 12      # Headers and important elements
    FONT_SIZE_MEDIUM = 10     # Standard UI text
    FONT_SIZE_SMALL = 9       # Secondary text and captions
    
    # Font Weights
    FONT_NORMAL = "normal"
    FONT_BOLD = "bold"
    
    # ============= SPACING AND SIZING =============
    
    # Padding and Margins
    PADDING_SMALL = 5
    PADDING_MEDIUM = 10
    PADDING_LARGE = 15
    PADDING_XLARGE = 20
    
    # Widget Dimensions
    BUTTON_WIDTH_STANDARD = 20
    BUTTON_WIDTH_LARGE = 25
    ENTRY_WIDTH_STANDARD = 25
    ENTRY_WIDTH_LARGE = 35
    
    # ============= WIDGET STYLES =============
    
    @classmethod
    def get_header_font(cls):
        """Get font for headers and section titles"""
        return (cls.FONT_PRIMARY[0], cls.FONT_SIZE_LARGE, cls.FONT_BOLD)
    
    @classmethod
    def get_body_font(cls):
        """Get font for regular body text"""
        return (cls.FONT_PRIMARY[0], cls.FONT_SIZE_MEDIUM, cls.FONT_NORMAL)
    
    @classmethod
    def get_small_font(cls):
        """Get font for small text and captions"""
        return (cls.FONT_PRIMARY[0], cls.FONT_SIZE_SMALL, cls.FONT_NORMAL)
    
    @classmethod
    def get_button_style(cls, button_type="primary"):
        """Get button styling configuration"""
        if button_type == "primary":
            return {
                "bg": cls.PRIMARY_BLUE,
                "fg": cls.BACKGROUND_WHITE,
                "font": cls.get_body_font(),
                "relief": "flat",
                "borderwidth": 0,
                "padx": cls.PADDING_MEDIUM,
                "pady": cls.PADDING_SMALL,
                "cursor": "hand2",
                "activebackground": cls.PRIMARY_BLUE_LIGHT,
                "activeforeground": cls.BACKGROUND_WHITE
            }
        elif button_type == "secondary":
            return {
                "bg": cls.BACKGROUND_GRAY,
                "fg": cls.TEXT_DARK,
                "font": cls.get_body_font(),
                "relief": "flat",
                "borderwidth": 1,
                "highlightcolor": cls.BORDER_GRAY,
                "padx": cls.PADDING_MEDIUM,
                "pady": cls.PADDING_SMALL,
                "cursor": "hand2",
                "activebackground": cls.BACKGROUND_LIGHT,
                "activeforeground": cls.TEXT_DARK
            }
        elif button_type == "success":
            return {
                "bg": cls.SUCCESS_GREEN,
                "fg": cls.BACKGROUND_WHITE,
                "font": cls.get_body_font(),
                "relief": "flat",
                "borderwidth": 0,
                "padx": cls.PADDING_MEDIUM,
                "pady": cls.PADDING_SMALL,
                "cursor": "hand2",
                "activebackground": "#059669",
                "activeforeground": cls.BACKGROUND_WHITE
            }
    
    @classmethod
    def get_entry_style(cls, state="normal"):
        """Get entry widget styling configuration"""
        if state == "disabled":
            return {
                "bg": cls.BACKGROUND_LIGHT,
                "fg": cls.TEXT_LIGHT,
                "font": cls.get_body_font(),
                "relief": "solid",
                "borderwidth": 1,
                "highlightcolor": cls.BORDER_GRAY,
                "insertbackground": cls.TEXT_DARK
            }
        else:
            return {
                "bg": cls.BACKGROUND_WHITE,
                "fg": cls.TEXT_DARK,
                "font": cls.get_body_font(),
                "relief": "solid", 
                "borderwidth": 1,
                "highlightcolor": cls.PRIMARY_BLUE,
                "insertbackground": cls.TEXT_DARK
            }
    
    @classmethod
    def get_label_style(cls, label_type="body"):
        """Get label styling configuration"""
        if label_type == "header":
            return {
                "font": cls.get_header_font(),
                "fg": cls.TEXT_DARK,
                "bg": cls.BACKGROUND_WHITE
            }
        elif label_type == "section":
            return {
                "font": (cls.FONT_PRIMARY[0], cls.FONT_SIZE_MEDIUM, cls.FONT_BOLD),
                "fg": cls.TEXT_DARK,
                "bg": cls.BACKGROUND_WHITE
            }
        else:  # body
            return {
                "font": cls.get_body_font(),
                "fg": cls.TEXT_MEDIUM,
                "bg": cls.BACKGROUND_WHITE
            }
    
    @classmethod
    def get_frame_style(cls):
        """Get frame styling configuration"""
        return {
            "bg": cls.BACKGROUND_WHITE,
            "relief": "solid",
            "borderwidth": 1,
            "highlightcolor": cls.BORDER_GRAY
        }
    
    @classmethod
    def get_labelframe_style(cls):
        """Get label frame styling configuration"""
        return {
            "bg": cls.BACKGROUND_WHITE,
            "relief": "groove",
            "borderwidth": 2,
            "font": cls.get_header_font(),
            "fg": cls.TEXT_DARK
        }

    @classmethod
    def apply_theme_to_widget(cls, widget, widget_type, **kwargs):
        """Apply theme styling to any widget"""
        if widget_type == "button":
            button_type = kwargs.get("button_type", "primary")
            style = cls.get_button_style(button_type)
            widget.configure(**style)
        elif widget_type == "entry":
            state = kwargs.get("state", "normal")
            style = cls.get_entry_style(state)
            widget.configure(**style)
        elif widget_type == "label":
            label_type = kwargs.get("label_type", "body")
            style = cls.get_label_style(label_type)
            widget.configure(**style)
        elif widget_type == "frame":
            style = cls.get_frame_style()
            widget.configure(**style)
        elif widget_type == "labelframe":
            style = cls.get_labelframe_style()
            widget.configure(**style)

    @classmethod
    def configure_ttk_styles(cls, root):
        """Configure ttk styles for professional appearance"""
        style = ttk.Style(root)
        
        # Configure ttk label style
        style.configure(
            "Professional.TLabel",
            font=cls.get_body_font(),
            foreground=cls.TEXT_MEDIUM,
            background=cls.BACKGROUND_WHITE
        )
        
        # Configure ttk header label style
        style.configure(
            "Header.TLabel", 
            font=cls.get_header_font(),
            foreground=cls.TEXT_DARK,
            background=cls.BACKGROUND_WHITE
        )
        
        # Configure ttk combobox style
        style.configure(
            "Professional.TCombobox",
            font=cls.get_body_font(),
            foreground=cls.TEXT_DARK,
            fieldbackground=cls.BACKGROUND_WHITE,
            borderwidth=1,
            relief="solid"
        )
        
        # Return the style object for further customization
        return style 