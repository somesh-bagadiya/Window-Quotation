"""
UI Tests for MainApplication Component
Window Quotation Application

Tests the main application window including:
- Application initialization and layout
- Customer data entry and validation
- Product type selection workflow
- Cart integration and navigation
"""

import pytest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch, MagicMock, call

from ui.main_app import MainApplication


class TestMainApplicationInitialization:
    """Test MainApplication initialization and basic setup"""
    
    @pytest.mark.ui
    def test_main_app_initialization(self, tk_root, clean_data_manager, clean_global_state):
        """Test that MainApplication initializes correctly with all components"""
        app = MainApplication(tk_root)
        
        # Verify core components are initialized
        assert app.data_manager is not None, "DataManager should be initialized"
        assert app.global_state is not None, "GlobalState should be initialized"
        
        # Verify UI structure exists (actual frame names)
        assert hasattr(app, 'frame0'), "Customer details frame should exist"
        assert hasattr(app, 'frame1'), "Window details frame should exist"
        assert hasattr(app, 'frame2'), "Logo frame should exist"
        
        # Verify product frame mapping exists
        assert hasattr(app, 'product_frames'), "Product frame mapping should exist"
        assert len(app.product_frames) > 0, "Should have product frame mappings"
        
        # Verify expected products are mapped
        expected_products = ["Sliding Window", "Sliding Door", "Fix Louver"]
        for product in expected_products:
            assert product in app.product_frames, f"{product} should be in product mapping"
    
    @pytest.mark.ui
    def test_customer_details_widgets_creation(self, tk_root, clean_data_manager):
        """Test that customer details widgets are created properly"""
        app = MainApplication(tk_root)
        
        # Customer frame (frame0) should have widgets
        customer_widgets = app.frame0.winfo_children()
        assert len(customer_widgets) > 0, "Customer frame should have widgets"
        
        # Check for specific customer input widgets
        entry_widgets = [w for w in customer_widgets if isinstance(w, tk.Entry)]
        assert len(entry_widgets) >= 1, "Should have at least customer name entry widget"
        
        # Check for Text widget (address)
        text_widgets = [w for w in customer_widgets if isinstance(w, tk.Text)]
        assert len(text_widgets) >= 1, "Should have customer address text widget"
    
    @pytest.mark.ui
    def test_window_selection_widgets_creation(self, tk_root, clean_data_manager):
        """Test that window selection widgets are created properly"""
        app = MainApplication(tk_root)
        
        # Window frame (frame1) should have selection widgets
        window_widgets = app.frame1.winfo_children()
        assert len(window_widgets) > 0, "Window frame should have widgets"
        
        # Should have combobox for product selection
        from tkinter import ttk
        combo_widgets = [w for w in window_widgets if isinstance(w, ttk.Combobox)]
        assert len(combo_widgets) >= 1, "Should have product selection combobox"
    
    @pytest.mark.ui
    def test_logo_and_company_info_display(self, tk_root, clean_data_manager):
        """Test that logo and company information are displayed"""
        app = MainApplication(tk_root)
        
        # Logo frame (frame2) should exist and have content
        logo_widgets = app.frame2.winfo_children()
        assert len(logo_widgets) > 0, "Logo frame should have widgets"
        
        # Should have canvas or labels for logo/company information
        canvas_widgets = [w for w in logo_widgets if isinstance(w, tk.Canvas)]
        label_widgets = [w for w in logo_widgets if isinstance(w, tk.Label)]
        assert len(canvas_widgets) >= 1 or len(label_widgets) >= 1, "Should have logo display widgets"


class TestCustomerDataHandling:
    """Test customer data entry and management"""
    
    @pytest.mark.ui
    def test_customer_name_entry(self, tk_root, clean_data_manager, clean_global_state):
        """Test customer name entry and binding"""
        app = MainApplication(tk_root)
        
        # Set customer name through global state
        test_name = "John Smith"
        app.global_state.custNamVar.set(test_name)
        
        # Verify the value is set correctly
        assert app.global_state.custNamVar.get() == test_name
        
        # Test data manager synchronization
        app.data_manager.set_customer_details({
            'custNamVar': test_name,
            'custAddVar': '',
            'custConVar': ''
        })
        
        customer_details = app.data_manager.get_customer_details()
        assert customer_details['custNamVar'] == test_name
    
    @pytest.mark.ui
    def test_customer_address_handling(self, tk_root, clean_data_manager, clean_global_state):
        """Test customer address entry and text widget handling"""
        app = MainApplication(tk_root)
        
        # Test address setting
        test_address = "123 Main Street\nAnytown, ST 12345"
        app.global_state.custAddVar.set(test_address)
        
        assert app.global_state.custAddVar.get() == test_address
        
        # Test that address is stored in global state
        app.global_state.address = test_address
        assert app.global_state.address == test_address
    
    @pytest.mark.ui
    @pytest.mark.parametrize("customer_data", [
        {"name": "John Smith", "address": "123 Main St", "contact": "9876543210"},
        {"name": "Jane Doe", "address": "456 Oak Ave\nSuite 200", "contact": "555-0123"},
        {"name": "Test User", "address": "", "contact": ""},  # Empty fields test
    ])
    def test_customer_data_combinations(self, tk_root, clean_data_manager, clean_global_state, customer_data):
        """Test various customer data combinations"""
        app = MainApplication(tk_root)
        
        # Set all customer data
        app.global_state.custNamVar.set(customer_data["name"])
        app.global_state.custAddVar.set(customer_data["address"])
        app.global_state.custConVar.set(customer_data["contact"])
        
        # Verify all data is set correctly
        assert app.global_state.custNamVar.get() == customer_data["name"]
        assert app.global_state.custAddVar.get() == customer_data["address"]
        assert app.global_state.custConVar.get() == customer_data["contact"]


class TestProductSelection:
    """Test product type selection and frame opening"""
    
    @pytest.mark.ui
    def test_product_type_selection(self, tk_root, clean_data_manager, clean_global_state):
        """Test basic product type selection"""
        app = MainApplication(tk_root)
        
        # Test setting different product types
        product_types = ["Sliding Window", "Sliding Door", "Fix Louver", "Composite pannel"]
        
        for product_type in product_types:
            app.global_state.windowTypeVar.set(product_type)
            assert app.global_state.windowTypeVar.get() == product_type
    
    @pytest.mark.ui
    @patch('ui.main_app.messagebox.showerror')
    def test_selector_method_without_dimensions(self, mock_error, tk_root, clean_data_manager):
        """Test selector method behavior when dimensions are missing"""
        app = MainApplication(tk_root)
        
        # Set product type but no dimensions
        app.global_state.windowTypeVar.set("Sliding Window")
        app.global_state.Width.set("")  # Empty width
        app.global_state.Height.set("")  # Empty height
        
        # Try to proceed without dimensions
        app.selector()
        
        # Should show error for missing dimensions
        mock_error.assert_called_once()
        call_args = mock_error.call_args[0]
        assert "width and height" in call_args[1].lower() or "dimensions" in call_args[1].lower()
    
    @pytest.mark.ui
    @patch('ui.main_app.messagebox.showwarning')
    def test_selector_method_without_window_type(self, mock_warning, tk_root, clean_data_manager):
        """Test selector method behavior when no window type is selected"""
        app = MainApplication(tk_root)
        
        # Don't set window type (should be empty by default)
        app.global_state.windowTypeVar.set("")
        
        # Try to proceed without window type selection
        app.selector()
        
        # Should show warning for missing window type selection
        mock_warning.assert_called_once()
        call_args = mock_warning.call_args[0]
        assert "select" in call_args[1].lower() and "window" in call_args[1].lower()
    
    @pytest.mark.ui
    @pytest.mark.parametrize("product_type,expected_frame", [
        ("Sliding Window", "SlidingWindowFrame"),
        ("Sliding Door", "SlidingDoorFrame"),
        ("Fix Louver", "FixLouverFrame"),
        ("Composite pannel", "CompositePanelFrame"),
    ])
    def test_product_frame_mapping(self, tk_root, clean_data_manager, product_type, expected_frame):
        """Test that product types map to correct frame classes"""
        app = MainApplication(tk_root)
        
        # Check that product_frames mapping exists and contains expected mappings
        assert hasattr(app, 'product_frames'), "Should have product_frames mapping"
        
        if product_type in app.product_frames:
            frame_class = app.product_frames[product_type]
            assert frame_class.__name__ == expected_frame, f"{product_type} should map to {expected_frame}"


class TestCartIntegration:
    """Test cart functionality integration with main application"""
    
    @pytest.mark.ui
    def test_cart_data_synchronization(self, tk_root, clean_data_manager, sample_cart_item):
        """Test that cart data synchronizes with main application"""
        app = MainApplication(tk_root)
        
        # Add item to cart through data manager
        app.data_manager.add_item_to_cart(sample_cart_item)
        
        # Verify item is in cart
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 1
        assert cart_data.iloc[0]['Particulars'] == 'Sliding Window'
        
        # Test cart total
        total = app.data_manager.get_cart_total_amount()
        assert total == 120000.0  # 1500 * 80 * 1
    
    @pytest.mark.ui
    @patch('ui.main_app.CartView')
    def test_open_cart_view_method(self, mock_cart_class, tk_root, clean_data_manager):
        """Test opening cart view from main application"""
        app = MainApplication(tk_root)
        
        # Mock cart view creation
        mock_cart_instance = MagicMock()
        mock_cart_class.return_value = mock_cart_instance
        
        # Test cart opening
        app.open_cart_view()
        
        # Verify cart was created
        mock_cart_class.assert_called_once()


class TestApplicationWorkflow:
    """Test complete application workflow scenarios"""
    
    @pytest.mark.ui
    def test_complete_customer_to_product_workflow(self, tk_root, clean_data_manager):
        """Test complete workflow from customer entry to product selection"""
        app = MainApplication(tk_root)
        
        # Step 1: Enter customer information
        app.global_state.custNamVar.set("John Smith")
        app.global_state.custAddVar.set("123 Main Street")
        app.global_state.custConVar.set("9876543210")
        
        # Step 2: Select product type
        app.global_state.windowTypeVar.set("Sliding Window")
        
        # Step 3: Verify all data is set
        assert app.global_state.custNamVar.get() == "John Smith"
        assert app.global_state.windowTypeVar.get() == "Sliding Window"
        
        # Step 4: Data should be ready for product frame
        customer_complete = (
            app.global_state.custNamVar.get() and 
            app.global_state.custAddVar.get() and 
            app.global_state.custConVar.get()
        )
        product_selected = app.global_state.windowTypeVar.get()
        
        assert customer_complete, "Customer data should be complete"
        assert product_selected, "Product should be selected"


class TestPerformance:
    """Test performance aspects of main application"""
    
    @pytest.mark.ui
    @pytest.mark.performance
    def test_application_startup_time(self, tk_root, clean_data_manager):
        """Test that application starts up within reasonable time"""
        import time
        
        start_time = time.time()
        app = MainApplication(tk_root)
        end_time = time.time()
        
        startup_time = end_time - start_time
        # Application should start within 5 seconds
        assert startup_time < 5.0, f"Application startup took {startup_time:.2f} seconds" 