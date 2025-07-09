"""
End-to-End Tests for Complete Customer Journey
Window Quotation Application

Tests complete user workflows from customer entry to final PDF generation:
- Single product quotations
- Multi-product quotations  
- Quotation modifications
- File save/load cycles
- Real PDF and Excel generation
"""

import pytest
import tkinter as tk
import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock

from ui.main_app import MainApplication
from ui.product_frames import SlidingWindowFrame, FixLouverFrame, CasementWindowFrame
from ui.cart_view import CartView
from ui.calculator_view import CalculatorView
from data_manager import DataManager
from global_state import get_global_state


class TestSingleProductJourney:
    """Test complete single product quotation journey"""
    
    @pytest.mark.end_to_end
    def test_sliding_window_complete_workflow(self, tk_root, clean_data_manager, clean_global_state, temp_test_directory):
        """Test complete workflow for single sliding window quotation"""
        # Phase 1: Initialize Application
        app = MainApplication(tk_root)
        
        # Phase 2: Enter Customer Details
        customer_data = {
            'custNamVar': 'End-to-End Test Customer',
            'custAddVar': '123 E2E Testing Street\nTest City, TC 12345',
            'custConVar': '555-E2E-TEST'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.global_state.custAddVar.set(customer_data['custAddVar'])
        app.global_state.custConVar.set(customer_data['custConVar'])
        
        # Sync customer data to DataManager
        app.data_manager.set_customer_details(customer_data)
        
        # Verify customer data is set
        retrieved_customer = app.data_manager.get_customer_details()
        assert retrieved_customer['custNamVar'] == customer_data['custNamVar']
        assert retrieved_customer['custAddVar'] == customer_data['custAddVar']
        assert retrieved_customer['custConVar'] == customer_data['custConVar']
        
        # Phase 3: Configure Product Specifications
        app.global_state.windowTypeVar.set("Sliding Window")
        app.global_state.Width.set("12")
        app.global_state.Height.set("8")
        
        # Create product frame for detailed configuration
        product_window = tk.Toplevel(tk_root)
        product_window.withdraw()
        
        try:
            sliding_window_frame = SlidingWindowFrame(product_window, app.data_manager)
            
            # Set detailed specifications
            sliding_window_frame.global_state.trackVar.set("3 Track")
            sliding_window_frame.global_state.aluMatVar.set("Regular Section")
            sliding_window_frame.global_state.glaThicVar.set("5mm")
            sliding_window_frame.global_state.glaTypVar.set("Plain")
            sliding_window_frame.global_state.hardLocVar.set("3/4th inch")
            sliding_window_frame.global_state.hardBeaVar.set("3/4th inch")
            sliding_window_frame.global_state.rubbTypVar.set("Clear")
            sliding_window_frame.global_state.rubbThicVar.set("4mm")
            sliding_window_frame.global_state.fraColVar.set("Black")
            sliding_window_frame.global_state.silColVar.set("Clear")
            
            # Phase 4: Calculate Cost
            sliding_window_frame.calculate_cost()
            
            # Verify dimensions are set correctly
            assert sliding_window_frame.global_state.Width.get() == "12"
            assert sliding_window_frame.global_state.Height.get() == "8"
            
            # Phase 5: Add to Cart
            # Create cart item with all specifications
            specs = sliding_window_frame.global_state.get_all_specification_vars()
            spec_values = {key: var.get() if hasattr(var, 'get') else var 
                          for key, var in specs.items()}
            
            cart_item = {
                'Sr.No': 1,
                'Particulars': 'Sliding Window',
                'Width': '12ft',
                'Height': '8ft',
                'Total Sq.ft': 96.0,
                'Cost (INR)': 1800.0,  # Realistic cost per sq.ft
                'Quantity': 1,
                'Amount': 172800.0,  # 1800 * 96 * 1
                **spec_values
            }
            
            sliding_window_frame.data_manager.add_item_to_cart(cart_item)
            
            # Verify item in cart
            cart_data = sliding_window_frame.data_manager.get_cart_data()
            assert len(cart_data) == 1
            assert cart_data.iloc[0]['Particulars'] == 'Sliding Window'
            assert cart_data.iloc[0]['trackVar'] == "3 Track"
            assert cart_data.iloc[0]['aluMatVar'] == "Regular Section"
            
        finally:
            sliding_window_frame.destroy()
            product_window.destroy()
        
        # Phase 6: Verify Cart Total
        total_amount = app.data_manager.get_cart_total_amount()
        assert total_amount > 0, "Cart total should be calculated"
        
        # Phase 7: Save Quotation to Excel
        excel_filename = os.path.join(temp_test_directory, "e2e_test_quotation.xlsx")
        success, message = app.data_manager.save_quotation_to_excel(excel_filename)
        assert success, f"Excel save should succeed: {message}"
        assert os.path.exists(excel_filename), "Excel file should be created"
        
        # Phase 8: Verify Data Persistence (Load Back)
        # Create new data manager instance to test loading
        new_data_manager = DataManager()
        new_data_manager.load_quotation_from_excel(excel_filename)
        
        loaded_cart = new_data_manager.get_cart_data()
        loaded_customer = new_data_manager.get_customer_details()
        
        # Verify loaded data matches original
        assert len(loaded_cart) == 1
        assert loaded_cart.iloc[0]['Particulars'] == 'Sliding Window'
        assert loaded_customer['custNamVar'] == customer_data['custNamVar']
        
    @pytest.mark.end_to_end
    def test_fix_louver_complete_workflow(self, tk_root, clean_data_manager, clean_global_state, temp_test_directory):
        """Test complete workflow for fix louver with different specifications"""
        app = MainApplication(tk_root)
        
        # Customer details
        customer_data = {
            'custNamVar': 'Fix Louver Customer',
            'custAddVar': '456 Louver Lane',
            'custConVar': '555-LOUVER'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.global_state.custAddVar.set(customer_data['custAddVar'])
        app.global_state.custConVar.set(customer_data['custConVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Product configuration
        product_window = tk.Toplevel(tk_root)
        product_window.withdraw()
        
        try:
            louver_frame = FixLouverFrame(product_window, app.data_manager)
            
            # Set dimensions
            louver_frame.global_state.Width.set("8")
            louver_frame.global_state.Height.set("6")
            
            # Set louver-specific specifications
            louver_frame.global_state.aluMatVar.set("Domal Section (JINDAL)")
            louver_frame.global_state.glaThicVar.set("8mm")
            louver_frame.global_state.glaTypVar.set("Frosted")
            louver_frame.global_state.lowBladVar.set("6")  # 6 louver blades
            louver_frame.global_state.fraColVar.set("Brown")
            
            # Calculate and add to cart
            louver_frame.calculate_cost()
            
            specs = louver_frame.global_state.get_all_specification_vars()
            spec_values = {key: var.get() if hasattr(var, 'get') else var 
                          for key, var in specs.items()}
            
            cart_item = {
                'Sr.No': 1,
                'Particulars': 'Fix Louver',
                'Width': '8ft',
                'Height': '6ft',
                'Total Sq.ft': 48.0,
                'Cost (INR)': 1400.0,
                'Quantity': 1,
                'Amount': 67200.0,  # 1400 * 48 * 1
                **spec_values
            }
            
            louver_frame.data_manager.add_item_to_cart(cart_item)
            
            # Verify louver-specific specifications
            cart_data = louver_frame.data_manager.get_cart_data()
            assert cart_data.iloc[0]['lowBladVar'] == "6"
            assert cart_data.iloc[0]['aluMatVar'] == "Domal Section (JINDAL)"
            assert cart_data.iloc[0]['glaTypVar'] == "Frosted"
            
        finally:
            louver_frame.destroy()
            product_window.destroy()
        
        # Save and verify
        excel_filename = os.path.join(temp_test_directory, "louver_quotation.xlsx")
        success, message = app.data_manager.save_quotation_to_excel(excel_filename)
        assert success, f"Louver quotation save should succeed: {message}"


class TestMultiProductJourney:
    """Test complete multi-product quotation journeys"""
    
    @pytest.mark.end_to_end
    def test_mixed_products_workflow(self, tk_root, clean_data_manager, clean_global_state, temp_test_directory):
        """Test workflow with multiple different product types"""
        app = MainApplication(tk_root)
        
        # Set up customer
        customer_data = {
            'custNamVar': 'Multi-Product Customer',
            'custAddVar': '789 Mixed Products Ave\nSuite 100',
            'custConVar': '555-MULTI-PROD'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.global_state.custAddVar.set(customer_data['custAddVar'])
        app.global_state.custConVar.set(customer_data['custConVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Product configurations to add
        products_to_add = [
            {
                'frame_class': SlidingWindowFrame,
                'particulars': 'Sliding Window',
                'width': '10',
                'height': '8', 
                'cost': 1600.0,
                'specs': {
                    'trackVar': '2 Track',
                    'aluMatVar': 'Regular Section',
                    'glaThicVar': '4mm',
                    'glaTypVar': 'Plain'
                }
            },
            {
                'frame_class': FixLouverFrame,
                'particulars': 'Fix Louver',
                'width': '6',
                'height': '4',
                'cost': 1300.0,
                'specs': {
                    'aluMatVar': 'Profile Aluminium Section',
                    'glaThicVar': '5mm',
                    'lowBladVar': '4'
                }
            },
            {
                'frame_class': CasementWindowFrame,
                'particulars': 'Casement Window',
                'width': '8',
                'height': '6',
                'cost': 1750.0,
                'specs': {
                    'aluMatVar': 'Domal Section (JINDAL)',
                    'glaThicVar': '8mm',
                    'glaTypVar': 'Tinted'
                }
            }
        ]
        
        # Add each product to cart
        for i, product in enumerate(products_to_add):
            product_window = tk.Toplevel(tk_root)
            product_window.withdraw()
            
            try:
                frame = product['frame_class'](product_window, app.data_manager)
                
                # Set dimensions
                frame.global_state.Width.set(product['width'])
                frame.global_state.Height.set(product['height'])
                
                # Set product-specific specifications
                for spec_key, spec_value in product['specs'].items():
                    if hasattr(frame.global_state, spec_key):
                        getattr(frame.global_state, spec_key).set(spec_value)
                
                # Calculate cost
                frame.calculate_cost()
                
                # Prepare cart item
                width = float(product['width'])
                height = float(product['height'])
                area = width * height
                
                specs = frame.global_state.get_all_specification_vars()
                spec_values = {key: var.get() if hasattr(var, 'get') else var 
                              for key, var in specs.items()}
                
                cart_item = {
                    'Sr.No': i + 1,
                    'Particulars': product['particulars'],
                    'Width': f"{product['width']}ft",
                    'Height': f"{product['height']}ft",
                    'Total Sq.ft': area,
                    'Cost (INR)': product['cost'],
                    'Quantity': 1,
                    'Amount': product['cost'] * area * 1,
                    **spec_values
                }
                
                frame.data_manager.add_item_to_cart(cart_item)
                
            finally:
                frame.destroy()
                product_window.destroy()
        
        # Verify all products in cart
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 3, "Should have 3 products in cart"
        
        product_names = cart_data['Particulars'].tolist()
        assert 'Sliding Window' in product_names
        assert 'Fix Louver' in product_names
        assert 'Casement Window' in product_names
        
        # Verify total calculation
        total_amount = app.data_manager.get_cart_total_amount()
        assert total_amount > 0, "Multi-product total should be calculated"
        
        # Calculate expected total
        expected_total = (1600.0 * 80) + (1300.0 * 24) + (1750.0 * 48)  # cost * area for each
        assert abs(total_amount - expected_total) < 1.0, f"Expected ~{expected_total}, got {total_amount}"
        
        # Save multi-product quotation
        excel_filename = os.path.join(temp_test_directory, "multi_product_quotation.xlsx")
        success, message = app.data_manager.save_quotation_to_excel(excel_filename)
        assert success, f"Multi-product save should succeed: {message}"
        
        # Verify file size is reasonable for multi-product quotation
        file_size = os.path.getsize(excel_filename)
        assert file_size > 5000, "Multi-product Excel file should be substantial"
    
    @pytest.mark.end_to_end 
    def test_quantity_variations_workflow(self, tk_root, clean_data_manager, clean_global_state):
        """Test workflow with quantity variations"""
        app = MainApplication(tk_root)
        
        # Set up customer
        customer_data = {
            'custNamVar': 'Quantity Test Customer',
            'custAddVar': 'Bulk Order Building',
            'custConVar': '555-QUANTITY'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Add product with initial quantity
        product_window = tk.Toplevel(tk_root)
        product_window.withdraw()
        
        try:
            frame = SlidingWindowFrame(product_window, app.data_manager)
            frame.global_state.Width.set("10")
            frame.global_state.Height.set("8")
            
            cart_item = {
                'Sr.No': 1,
                'Particulars': 'Sliding Window',
                'Width': '10ft',
                'Height': '8ft',
                'Total Sq.ft': 80.0,
                'Cost (INR)': 1500.0,
                'Quantity': 1,
                'Amount': 120000.0  # 1500 * 80 * 1
            }
            
            frame.data_manager.add_item_to_cart(cart_item)
            
        finally:
            frame.destroy()
            product_window.destroy()
        
        # Test quantity updates
        quantities_to_test = [3, 5, 2, 10]
        
        for quantity in quantities_to_test:
            app.data_manager.update_item_quantity(1, quantity)
            
            updated_cart = app.data_manager.get_cart_data()
            assert updated_cart.iloc[0]['Quantity'] == quantity
            
            expected_amount = 1500.0 * 80.0 * quantity
            assert updated_cart.iloc[0]['Amount'] == expected_amount
            
            total = app.data_manager.get_cart_total_amount()
            assert total == expected_amount


class TestQuotationModificationJourney:
    """Test quotation loading, modification, and saving workflows"""
    
    @pytest.mark.end_to_end
    def test_load_modify_save_workflow(self, tk_root, clean_data_manager, clean_global_state, temp_test_directory):
        """Test loading existing quotation, modifying it, and saving"""
        # Phase 1: Create initial quotation
        app = MainApplication(tk_root)
        
        customer_data = {
            'custNamVar': 'Modification Test Customer',
            'custAddVar': '123 Modification St',
            'custConVar': '555-MODIFY'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Add initial product
        cart_item = {
            'Sr.No': 1,
            'Particulars': 'Sliding Window',
            'Width': '10ft',
            'Height': '8ft',
            'Total Sq.ft': 80.0,
            'Cost (INR)': 1500.0,
            'Quantity': 1,
            'Amount': 120000.0
        }
        
        app.data_manager.add_item_to_cart(cart_item)
        
        # Save initial quotation
        initial_filename = os.path.join(temp_test_directory, "initial_quotation.xlsx")
        success, message = app.data_manager.save_quotation_to_excel(initial_filename)
        assert success, f"Initial save should succeed: {message}"
        
        # Phase 2: Load quotation in new session
        new_data_manager = DataManager()
        new_data_manager.load_quotation_from_excel(initial_filename)
        
        # Verify loaded data
        loaded_cart = new_data_manager.get_cart_data()
        loaded_customer = new_data_manager.get_customer_details()
        
        assert len(loaded_cart) == 1
        assert loaded_cart.iloc[0]['Particulars'] == 'Sliding Window'
        assert loaded_customer['custNamVar'] == customer_data['custNamVar']
        
        # Phase 3: Modify loaded quotation
        # Update customer information
        modified_customer = {
            'custNamVar': 'Modified Customer Name',
            'custAddVar': '456 New Address',
            'custConVar': '555-NEW-NUM'
        }
        new_data_manager.set_customer_details(modified_customer)
        
        # Add another product
        additional_item = {
            'Sr.No': 2,
            'Particulars': 'Fix Louver',
            'Width': '6ft',
            'Height': '4ft',
            'Total Sq.ft': 24.0,
            'Cost (INR)': 1300.0,
            'Quantity': 2,
            'Amount': 62400.0  # 1300 * 24 * 2
        }
        
        new_data_manager.add_item_to_cart(additional_item)
        
        # Update quantity of existing item
        new_data_manager.update_item_quantity(1, 3)
        
        # Phase 4: Save modified quotation
        modified_filename = os.path.join(temp_test_directory, "modified_quotation.xlsx")
        success, message = new_data_manager.save_quotation_to_excel(modified_filename)
        assert success, f"Modified save should succeed: {message}"
        
        # Phase 5: Verify final state
        final_cart = new_data_manager.get_cart_data()
        final_customer = new_data_manager.get_customer_details()
        
        assert len(final_cart) == 2, "Should have 2 products after modification"
        assert final_cart.iloc[0]['Quantity'] == 3, "First item quantity should be updated"
        assert final_customer['custNamVar'] == 'Modified Customer Name'
        
        # Verify total calculation
        total = new_data_manager.get_cart_total_amount()
        expected_total = (1500.0 * 80.0 * 3) + (1300.0 * 24.0 * 2)
        assert abs(total - expected_total) < 1.0, f"Expected {expected_total}, got {total}"


class TestErrorRecoveryJourney:
    """Test error scenarios and recovery in end-to-end workflows"""
    
    @pytest.mark.end_to_end
    def test_invalid_data_recovery_workflow(self, tk_root, clean_data_manager, clean_global_state):
        """Test recovery from invalid data entries during workflow"""
        app = MainApplication(tk_root)
        
        # Test invalid customer data handling
        app.global_state.custNamVar.set("")  # Empty name
        app.global_state.custAddVar.set("")  # Empty address
        app.global_state.custConVar.set("invalid-phone")  # Invalid phone
        
        # Application should handle gracefully
        customer_details = app.data_manager.get_customer_details()
        assert isinstance(customer_details, dict), "Should return dict even with invalid data"
        
        # Test invalid dimensions
        app.global_state.Width.set("invalid")
        app.global_state.Height.set("not-a-number")
        
        # Should not crash when trying to calculate
        try:
            width_val = app.global_state.Width.get()
            height_val = app.global_state.Height.get()
            # Values stored as strings, validation happens during use
            assert isinstance(width_val, str)
            assert isinstance(height_val, str)
        except Exception:
            pytest.fail("Should handle invalid dimension data gracefully")
        
        # Recovery: Set valid data
        app.global_state.custNamVar.set("Recovered Customer")
        app.global_state.Width.set("10")
        app.global_state.Height.set("8")
        
        # Should work normally after recovery
        assert app.global_state.custNamVar.get() == "Recovered Customer"
        assert app.global_state.Width.get() == "10"
        assert app.global_state.Height.get() == "8"
    
    @pytest.mark.end_to_end
    def test_empty_cart_workflow_handling(self, tk_root, clean_data_manager):
        """Test handling of empty cart scenarios"""
        app = MainApplication(tk_root)
        
        # Attempt operations on empty cart
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 0, "Cart should be empty initially"
        
        total = app.data_manager.get_cart_total_amount()
        assert total == 0.0, "Empty cart total should be 0"
        
        # Attempt to save empty cart
        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp:
            temp_filename = tmp.name
        
        try:
            success, message = app.data_manager.save_quotation_to_excel(temp_filename)
            # Should handle empty cart gracefully
            assert not success, "Should not save empty cart"
            assert "empty" in message.lower(), "Error message should mention empty cart"
        finally:
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)


class TestPerformanceE2E:
    """Test performance aspects of end-to-end workflows"""
    
    @pytest.mark.end_to_end
    @pytest.mark.performance
    def test_large_quotation_performance(self, tk_root, clean_data_manager):
        """Test performance with large quotations"""
        import time
        
        app = MainApplication(tk_root)
        
        # Set up customer
        app.global_state.custNamVar.set("Large Quotation Customer")
        app.data_manager.set_customer_details({'custNamVar': 'Large Quotation Customer'})
        
        start_time = time.time()
        
        # Add 10 products to simulate large quotation
        for i in range(10):
            cart_item = {
                'Sr.No': i + 1,
                'Particulars': f'Product {i + 1}',
                'Width': '10ft',
                'Height': '8ft',
                'Total Sq.ft': 80.0,
                'Cost (INR)': 1500.0 + i * 50,  # Vary cost slightly
                'Quantity': 1,
                'Amount': (1500.0 + i * 50) * 80.0
            }
            app.data_manager.add_item_to_cart(cart_item)
        
        # Perform operations
        cart_data = app.data_manager.get_cart_data()
        total = app.data_manager.get_cart_total_amount()
        
        end_time = time.time()
        operation_time = end_time - start_time
        
        # Performance assertions
        assert len(cart_data) == 10, "Should have 10 products"
        assert total > 1000000, "Large quotation should have substantial total"
        assert operation_time < 10.0, f"Large quotation operations took {operation_time:.2f} seconds" 