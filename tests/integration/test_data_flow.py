"""
Integration Tests for Data Flow
Window Quotation Application

Tests data flow between major components:
- GlobalState ↔ UI Components
- DataManager ↔ GlobalState 
- UI Components ↔ DataManager
- Customer data synchronization
- Product specification flow
"""

import pytest
import tkinter as tk
from unittest.mock import patch, MagicMock

from ui.main_app import MainApplication
from ui.product_frames import SlidingWindowFrame, FixLouverFrame
from data_manager import DataManager
from global_state import get_global_state


class TestGlobalStateDataManagerSync:
    """Test synchronization between GlobalState and DataManager"""
    
    @pytest.mark.integration
    def test_customer_data_bidirectional_sync(self, tk_root, clean_data_manager, clean_global_state):
        """Test that customer data syncs bidirectionally between GlobalState and DataManager"""
        app = MainApplication(tk_root)
        
        # Test: GlobalState → DataManager
        test_customer = {
            'custNamVar': 'John Smith',
            'custAddVar': '123 Main Street\nAnytown, ST 12345', 
            'custConVar': '555-123-4567'
        }
        
        # Set in GlobalState
        app.global_state.custNamVar.set(test_customer['custNamVar'])
        app.global_state.custAddVar.set(test_customer['custAddVar'])
        app.global_state.custConVar.set(test_customer['custConVar'])
        
        # Sync to DataManager
        app.data_manager.set_customer_details(test_customer)
        
        # Verify DataManager has the data
        retrieved = app.data_manager.get_customer_details()
        assert retrieved['custNamVar'] == test_customer['custNamVar']
        assert retrieved['custAddVar'] == test_customer['custAddVar']
        assert retrieved['custConVar'] == test_customer['custConVar']
        
        # Test: DataManager → GlobalState (simulating load from file)
        modified_customer = {
            'custNamVar': 'Jane Doe',
            'custAddVar': '456 Oak Avenue',
            'custConVar': '555-987-6543'
        }
        
        # Set in DataManager
        app.data_manager.set_customer_details(modified_customer)
        
        # Update GlobalState (simulating file load)
        loaded_details = app.data_manager.get_customer_details()
        app.global_state.custNamVar.set(loaded_details['custNamVar'])
        app.global_state.custAddVar.set(loaded_details['custAddVar'])
        app.global_state.custConVar.set(loaded_details['custConVar'])
        
        # Verify GlobalState updated
        assert app.global_state.custNamVar.get() == modified_customer['custNamVar']
        assert app.global_state.custAddVar.get() == modified_customer['custAddVar']
        assert app.global_state.custConVar.get() == modified_customer['custConVar']
    
    @pytest.mark.integration
    def test_product_specifications_flow(self, tk_root, clean_data_manager, clean_global_state):
        """Test product specification data flow from UI to DataManager"""
        # Create product frame 
        product_window = tk.Toplevel(tk_root)
        product_window.withdraw()
        frame = SlidingWindowFrame(product_window, clean_data_manager)
        
        try:
            # Set product specifications in GlobalState
            frame.global_state.Width.set("12")
            frame.global_state.Height.set("8") 
            frame.global_state.trackVar.set("3 Track")
            frame.global_state.aluMatVar.set("Regular Section")
            frame.global_state.glaThicVar.set("5mm")
            frame.global_state.glaTypVar.set("Plain")
            
            # Simulate cost calculation (this reads from GlobalState)
            frame.calculate_cost()
            
            # Verify specifications are captured (StringVar objects)
            specs = frame.global_state.get_all_specification_vars()
            assert specs['trackVar'].get() == "3 Track"
            assert specs['aluMatVar'].get() == "Regular Section"
            assert specs['glaThicVar'].get() == "5mm"
            assert specs['glaTypVar'].get() == "Plain"
            
            # Simulate adding to cart (this writes to DataManager)
            # Convert StringVar objects to values for cart storage
            spec_values = {key: var.get() if hasattr(var, 'get') else var 
                          for key, var in specs.items()}
            
            sample_item = {
                'Sr.No': 1,
                'Particulars': 'Sliding Window',
                'Width': '12ft',
                'Height': '8ft', 
                'Total Sq.ft': 96.0,
                'Cost (INR)': 2000.0,
                'Quantity': 1,
                'Amount': 2000.0,
                **spec_values  # Include specification values
            }
            
            frame.data_manager.add_item_to_cart(sample_item)
            
            # Verify item in cart with specifications
            cart_data = frame.data_manager.get_cart_data()
            assert len(cart_data) == 1
            assert cart_data.iloc[0]['Particulars'] == 'Sliding Window'
            assert cart_data.iloc[0]['trackVar'] == "3 Track"
            assert cart_data.iloc[0]['aluMatVar'] == "Regular Section"
            
        finally:
            frame.destroy()
            product_window.destroy()
    
    @pytest.mark.integration 
    def test_dimension_area_calculation_flow(self, tk_root, clean_data_manager, clean_global_state):
        """Test dimension entry and area calculation flow"""
        app = MainApplication(tk_root)
        
        # Test various dimension combinations
        test_cases = [
            {"width": "10", "height": "8", "expected_area": 80.0},
            {"width": "12.5", "height": "6.5", "expected_area": 81.25},
            {"width": "15", "height": "10", "expected_area": 150.0}
        ]
        
        for case in test_cases:
            # Set dimensions in GlobalState
            app.global_state.Width.set(case["width"])
            app.global_state.Height.set(case["height"])
            
            # Calculate area (simulating what product frames do)
            try:
                width = float(app.global_state.Width.get())
                height = float(app.global_state.Height.get())
                calculated_area = width * height
                
                assert calculated_area == case["expected_area"], f"Area calculation failed for {case}"
                
                # Set calculated area back to GlobalState
                app.global_state.totSqftEntVar.set(str(calculated_area))
                
                # Verify area is stored correctly
                assert float(app.global_state.totSqftEntVar.get()) == case["expected_area"]
                
            except ValueError:
                pytest.fail(f"Failed to calculate area for valid inputs: {case}")


class TestUIComponentIntegration:
    """Test integration between different UI components"""
    
    @pytest.mark.integration
    def test_main_app_to_product_frame_flow(self, tk_root, clean_data_manager, clean_global_state):
        """Test complete flow from MainApplication to ProductFrame"""
        app = MainApplication(tk_root)
        
        # Step 1: Set customer data in MainApplication
        app.global_state.custNamVar.set("Integration Test Customer")
        app.global_state.custAddVar.set("123 Integration Street")
        app.global_state.custConVar.set("555-TEST-123")
        
        # Step 2: Set product selection and dimensions
        app.global_state.windowTypeVar.set("Sliding Window")
        app.global_state.Width.set("10")
        app.global_state.Height.set("8")
        
        # Step 3: Verify data is ready for product frame
        assert app.global_state.custNamVar.get() == "Integration Test Customer"
        assert app.global_state.windowTypeVar.get() == "Sliding Window"
        assert app.global_state.Width.get() == "10"
        assert app.global_state.Height.get() == "8"
        
        # Step 4: Customer details should sync to DataManager when selector is called
        app.update_customer_details_in_data_manager()
        
        retrieved_customer = app.data_manager.get_customer_details()
        assert retrieved_customer['custNamVar'] == "Integration Test Customer"
        assert retrieved_customer['custAddVar'] == "123 Integration Street"
        assert retrieved_customer['custConVar'] == "555-TEST-123"
        
        # Step 5: Verify product frame can access this data
        product_window = tk.Toplevel(tk_root)
        product_window.withdraw()
        
        try:
            frame = SlidingWindowFrame(product_window, app.data_manager)
            
            # Product frame should have access to same GlobalState
            assert frame.global_state.custNamVar.get() == "Integration Test Customer"
            assert frame.global_state.Width.get() == "10"
            assert frame.global_state.Height.get() == "8"
            
            # Product frame should have access to same DataManager
            frame_customer = frame.data_manager.get_customer_details()
            assert frame_customer['custNamVar'] == "Integration Test Customer"
            
        finally:
            frame.destroy()
            product_window.destroy()
    
    @pytest.mark.integration
    @patch('ui.main_app.CartView')
    def test_main_app_to_cart_integration(self, mock_cart_class, tk_root, clean_data_manager, sample_cart_item):
        """Test integration from MainApplication to CartView"""
        app = MainApplication(tk_root)
        
        # Add some items to cart first
        app.data_manager.add_item_to_cart(sample_cart_item)
        
        additional_item = sample_cart_item.copy()
        additional_item['Sr.No'] = 2
        additional_item['Particulars'] = 'Fix Louver'
        additional_item['Amount'] = 1200.0
        app.data_manager.add_item_to_cart(additional_item)
        
        # Mock cart view
        mock_cart_instance = MagicMock()
        mock_cart_class.return_value = mock_cart_instance
        
        # Open cart view
        app.open_cart_view()
        
        # Verify cart was created with correct data
        mock_cart_class.assert_called_once()
        call_args = mock_cart_class.call_args
        
        # Should be called with parent, data_manager, and main_app
        assert len(call_args[0]) >= 2  # parent and data_manager
        assert 'main_app' in call_args[1]  # main_app as keyword argument
        
        # Verify data manager has the expected items
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 2
        assert 'Sliding Window' in cart_data['Particulars'].values
        assert 'Fix Louver' in cart_data['Particulars'].values
    
    @pytest.mark.integration
    def test_product_frame_specification_inheritance(self, tk_root, clean_data_manager, clean_global_state):
        """Test that different product frames inherit base functionality correctly"""
        product_types = [
            (SlidingWindowFrame, "Sliding Window"),
            (FixLouverFrame, "Fix Louver")
        ]
        
        for frame_class, product_name in product_types:
            product_window = tk.Toplevel(tk_root)
            product_window.withdraw()
            
            try:
                frame = frame_class(product_window, clean_data_manager)
                
                # All frames should have base functionality
                assert hasattr(frame, 'global_state'), f"{product_name} should have global_state"
                assert hasattr(frame, 'data_manager'), f"{product_name} should have data_manager"
                assert hasattr(frame, 'calculate_cost'), f"{product_name} should have calculate_cost"
                assert hasattr(frame, 'add_to_cart'), f"{product_name} should have add_to_cart"
                
                # All frames should be able to set basic dimensions
                frame.global_state.Width.set("10")
                frame.global_state.Height.set("8")
                
                assert frame.global_state.Width.get() == "10"
                assert frame.global_state.Height.get() == "8"
                
                # All frames should access same global state instance
                assert frame.global_state is clean_global_state
                
            finally:
                frame.destroy()
                product_window.destroy()


class TestCartWorkflowIntegration:
    """Test complete cart workflow integration"""
    
    @pytest.mark.integration
    def test_complete_cart_workflow(self, tk_root, clean_data_manager, clean_global_state):
        """Test complete workflow: Product Configuration → Cart → Calculations"""
        app = MainApplication(tk_root)
        
        # Step 1: Set customer data
        customer_data = {
            'custNamVar': 'Cart Workflow Customer',
            'custAddVar': '456 Cart Street', 
            'custConVar': '555-CART-456'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.global_state.custAddVar.set(customer_data['custAddVar'])
        app.global_state.custConVar.set(customer_data['custConVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Step 2: Configure and add multiple products
        products_to_add = [
            {
                'name': 'Sliding Window',
                'width': '12',
                'height': '8',
                'cost': 1800.0,
                'frame_class': SlidingWindowFrame
            },
            {
                'name': 'Fix Louver', 
                'width': '8',
                'height': '6',
                'cost': 1200.0,
                'frame_class': FixLouverFrame
            }
        ]
        
        for product in products_to_add:
            product_window = tk.Toplevel(tk_root)
            product_window.withdraw()
            
            try:
                frame = product['frame_class'](product_window, app.data_manager)
                
                # Configure product
                frame.global_state.Width.set(product['width'])
                frame.global_state.Height.set(product['height'])
                
                # Calculate area
                width = float(product['width'])
                height = float(product['height'])
                area = width * height
                
                # Simulate adding to cart
                cart_item = {
                    'Sr.No': len(app.data_manager.get_cart_data()) + 1,
                    'Particulars': product['name'],
                    'Width': f"{product['width']}ft",
                    'Height': f"{product['height']}ft",
                    'Total Sq.ft': area,
                    'Cost (INR)': product['cost'],
                    'Quantity': 1,
                    'Amount': product['cost'] * 1
                }
                
                frame.data_manager.add_item_to_cart(cart_item)
                
            finally:
                frame.destroy()
                product_window.destroy()
        
        # Step 3: Verify cart contains all items
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 2, "Cart should contain 2 items"
        
        # Verify specific items
        product_names = cart_data['Particulars'].tolist()
        assert 'Sliding Window' in product_names
        assert 'Fix Louver' in product_names
        
        # Step 4: Test cart calculations
        total_amount = app.data_manager.get_cart_total_amount()
        expected_total = 1800.0 + 1200.0  # Sum of both products
        assert total_amount == expected_total, f"Expected {expected_total}, got {total_amount}"
        
        # Step 5: Test item removal
        initial_count = len(cart_data)
        app.data_manager.remove_item_from_cart(1)  # Remove first item
        
        updated_cart = app.data_manager.get_cart_data()
        assert len(updated_cart) == initial_count - 1, "Item should be removed from cart"
        
        # Verify total recalculated
        new_total = app.data_manager.get_cart_total_amount()
        assert new_total < total_amount, "Total should be reduced after item removal"
    
    @pytest.mark.integration
    def test_cart_quantity_updates(self, tk_root, clean_data_manager, sample_cart_item):
        """Test cart quantity updates and recalculations"""
        app = MainApplication(tk_root)
        
        # Add item to cart
        app.data_manager.add_item_to_cart(sample_cart_item)
        
        # Verify initial state
        initial_cart = app.data_manager.get_cart_data()
        assert len(initial_cart) == 1
        assert initial_cart.iloc[0]['Quantity'] == 1
        assert initial_cart.iloc[0]['Amount'] == 1500.0
        
        # Update quantity
        app.data_manager.update_item_quantity(1, 3)  # Change quantity to 3
        
        # Verify quantity and amount updated
        # Real calculation: Cost (INR) is per sq.ft, so:
        # total_cost = 1500 (per sq.ft) * 80 (sq.ft) = 120,000
        # Amount = 120,000 * 3 (quantity) = 360,000
        updated_cart = app.data_manager.get_cart_data()
        assert updated_cart.iloc[0]['Quantity'] == 3
        assert updated_cart.iloc[0]['Amount'] == 360000.0  # 1500 * 80 * 3
        
        # Verify total amount updated
        total = app.data_manager.get_cart_total_amount()
        assert total == 360000.0
        
        # Test fractional quantity
        app.data_manager.update_item_quantity(1, 2.5)
        
        updated_cart = app.data_manager.get_cart_data()
        assert updated_cart.iloc[0]['Quantity'] == 2.5
        assert updated_cart.iloc[0]['Amount'] == 300000.0  # 1500 * 80 * 2.5


class TestErrorHandlingIntegration:
    """Test error handling across component integrations"""
    
    @pytest.mark.integration
    def test_invalid_data_flow_handling(self, tk_root, clean_data_manager, clean_global_state):
        """Test how system handles invalid data flowing between components"""
        app = MainApplication(tk_root)
        
        # Test invalid dimensions
        app.global_state.Width.set("invalid")
        app.global_state.Height.set("also_invalid")
        
        # System should handle gracefully - no exceptions
        try:
            width_val = app.global_state.Width.get()
            height_val = app.global_state.Height.get()
            
            # Values should be stored as strings
            assert width_val == "invalid"
            assert height_val == "also_invalid"
            
            # Validation should happen when trying to use values
            with pytest.raises(ValueError):
                float(width_val)
            
        except Exception as e:
            pytest.fail(f"System should handle invalid data gracefully: {e}")
    
    @pytest.mark.integration
    def test_missing_customer_data_handling(self, tk_root, clean_data_manager, clean_global_state):
        """Test handling of missing customer data across components"""
        app = MainApplication(tk_root)
        
        # Don't set customer data - test defaults
        customer_details = app.data_manager.get_customer_details()
        
        # Should have default empty values, not crash
        assert 'custNamVar' in customer_details
        assert 'custAddVar' in customer_details  
        assert 'custConVar' in customer_details
        
        # Values might be empty strings or None
        for key, value in customer_details.items():
            assert value is not None or value == "", f"Customer field {key} should have default value"
    
    @pytest.mark.integration
    def test_empty_cart_operations(self, tk_root, clean_data_manager):
        """Test cart operations with empty cart"""
        app = MainApplication(tk_root)
        
        # Test operations on empty cart
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 0, "Cart should be empty initially"
        
        # Test total calculation with empty cart
        total = app.data_manager.get_cart_total_amount()
        assert total == 0.0, "Empty cart total should be 0"
        
        # Test removing from empty cart (should not crash)
        try:
            app.data_manager.remove_item_from_cart(1)  # Non-existent item
            # Should handle gracefully
        except Exception as e:
            # If it raises an exception, it should be a reasonable one
            assert "not found" in str(e).lower() or "invalid" in str(e).lower()


class TestStateConsistency:
    """Test state consistency across all components"""
    
    @pytest.mark.integration
    def test_singleton_consistency(self, tk_root, clean_data_manager, clean_global_state):
        """Test that singletons maintain consistency across components"""
        app = MainApplication(tk_root)
        
        # Create multiple product frames
        frames = []
        windows = []
        
        try:
            for i in range(3):
                product_window = tk.Toplevel(tk_root)
                product_window.withdraw()
                frame = SlidingWindowFrame(product_window, clean_data_manager)
                frames.append(frame)
                windows.append(product_window)
            
            # All frames should share same GlobalState instance
            for frame in frames:
                assert frame.global_state is clean_global_state
                assert frame.global_state is app.global_state
            
            # All frames should share same DataManager instance  
            for frame in frames:
                assert frame.data_manager is clean_data_manager
                assert frame.data_manager is app.data_manager
            
            # Changes in one should reflect in all
            test_value = "Consistency Test"
            frames[0].global_state.custNamVar.set(test_value)
            
            for frame in frames[1:]:
                assert frame.global_state.custNamVar.get() == test_value
            
            assert app.global_state.custNamVar.get() == test_value
            
        finally:
            for frame in frames:
                frame.destroy()
            for window in windows:
                window.destroy()
    
    @pytest.mark.integration
    def test_data_consistency_across_operations(self, tk_root, clean_data_manager, sample_cart_item):
        """Test data consistency across multiple operations"""
        app = MainApplication(tk_root)
        
        # Perform series of operations
        operations = [
            lambda: app.data_manager.add_item_to_cart(sample_cart_item),
            lambda: app.data_manager.update_item_quantity(1, 2),
            lambda: app.global_state.custNamVar.set("Consistency Customer"),
            lambda: app.data_manager.set_customer_details({
                'custNamVar': app.global_state.custNamVar.get(),
                'custAddVar': 'Test Address',
                'custConVar': '555-0123'
            })
        ]
        
        # Execute operations
        for operation in operations:
            operation()
        
        # Verify final state consistency
        cart_data = app.data_manager.get_cart_data()
        customer_data = app.data_manager.get_customer_details()
        global_state_name = app.global_state.custNamVar.get()
        
        # All should be consistent
        assert len(cart_data) == 1, "Cart should have one item"
        assert cart_data.iloc[0]['Quantity'] == 2, "Quantity should be updated"
        assert customer_data['custNamVar'] == "Consistency Customer"
        assert global_state_name == "Consistency Customer"
        assert customer_data['custNamVar'] == global_state_name


class TestPerformanceIntegration:
    """Test performance aspects of component integration"""
    
    @pytest.mark.integration
    @pytest.mark.performance
    def test_multiple_component_creation_performance(self, tk_root, clean_data_manager):
        """Test performance when creating multiple integrated components"""
        import time
        
        start_time = time.time()
        
        # Create main app and multiple product frames
        app = MainApplication(tk_root)
        frames = []
        windows = []
        
        try:
            for i in range(5):  # Create 5 product frames
                product_window = tk.Toplevel(tk_root)
                product_window.withdraw()
                frame = SlidingWindowFrame(product_window, app.data_manager)
                frames.append(frame)
                windows.append(product_window)
        
        finally:
            for frame in frames:
                frame.destroy()
            for window in windows:
                window.destroy()
        
        end_time = time.time()
        creation_time = end_time - start_time
        
        # Should create multiple components quickly
        assert creation_time < 10.0, f"Creating multiple components took {creation_time:.2f} seconds"
    
    @pytest.mark.integration
    @pytest.mark.performance
    def test_large_cart_operations_performance(self, tk_root, clean_data_manager):
        """Test performance with large number of cart operations"""
        import time
        
        app = MainApplication(tk_root)
        
        start_time = time.time()
        
        # Add many items to cart
        for i in range(50):
            item = {
                'Sr.No': i + 1,
                'Particulars': f'Product {i + 1}',
                'Width': '10ft',
                'Height': '8ft',
                'Total Sq.ft': 80.0,
                'Cost (INR)': 1000.0 + i,  # Vary cost slightly
                'Quantity': 1,
                'Amount': 1000.0 + i
            }
            app.data_manager.add_item_to_cart(item)
        
        # Perform various operations
        total = app.data_manager.get_cart_total_amount()
        cart_data = app.data_manager.get_cart_data()
        
        end_time = time.time()
        operation_time = end_time - start_time
        
        # Should handle large cart efficiently (realistic baseline with debug output)
        assert operation_time < 15.0, f"Large cart operations took {operation_time:.2f} seconds"
        assert len(cart_data) == 50, "All items should be in cart"
        assert total > 50000, "Total should be calculated correctly" 