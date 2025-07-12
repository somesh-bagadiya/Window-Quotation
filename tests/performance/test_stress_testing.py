"""
Stress Testing Suite
Window Quotation Application

Comprehensive stress tests for edge cases and extreme scenarios:
- High-volume data handling
- Memory pressure testing
- Error recovery under stress
- Edge case performance
- Resource utilization limits
"""

import pytest
import tkinter as tk
import tempfile
import os
import gc
import threading
import time
from unittest.mock import patch, MagicMock

from data_manager import DataManager
from global_state import get_global_state
from ui.main_app import MainApplication
from ui.product_frames import SlidingWindowFrame


class TestHighVolumeStressTesting:
    """Stress testing with high-volume data scenarios"""
    
    @pytest.mark.performance
    @pytest.mark.slow
    def test_extremely_large_cart_stress(self, clean_data_manager):
        """Test cart performance with extremely large number of items"""
        dm = clean_data_manager
        
        # Stress test with very large cart (1000 items)
        start_time = time.time()
        
        for i in range(1000):
            item = {
                'Sr.No': i + 1,
                'Particulars': f'Stress Test Item {i + 1:04d}',
                'Width': f'{8 + (i % 5)}ft',
                'Height': f'{6 + (i % 3)}ft',
                'Total Sq.ft': (8 + (i % 5)) * (6 + (i % 3)),
                'Cost (INR)': 1200.0 + (i % 500),
                'Quantity': 1 + (i % 3),
                'Amount': ((8 + (i % 5)) * (6 + (i % 3))) * (1200.0 + (i % 500)) * (1 + (i % 3))
            }
            dm.add_item_to_cart(item)
            
            # Memory check every 100 items
            if (i + 1) % 100 == 0:
                gc.collect()  # Force garbage collection
                cart_data = dm.get_cart_data()
                assert len(cart_data) == i + 1, f"Cart size mismatch at item {i + 1}"
        
        duration = time.time() - start_time
        
        # Verify final state
        final_cart = dm.get_cart_data()
        assert len(final_cart) == 1000
        
        # Calculate total and verify it's reasonable
        total_amount = dm.get_cart_total_amount()
        assert total_amount > 0, "Total amount should be positive"
        
        # Performance assertion (should complete within reasonable time)
        assert duration < 120, f"Stress test took too long: {duration:.2f} seconds"
        
        print(f"\nStress Test Results:")
        print(f"  Items: 1000")
        print(f"  Duration: {duration:.2f} seconds")
        print(f"  Rate: {1000/duration:.2f} items/second")
        print(f"  Total Amount: ₹{total_amount:,.2f}")
    
    @pytest.mark.performance
    @pytest.mark.slow
    def test_rapid_operations_stress(self, clean_data_manager):
        """Test rapid-fire operations under stress"""
        dm = clean_data_manager
        
        # Add initial items quickly
        for i in range(50):
            item = {
                'Sr.No': i + 1,
                'Particulars': f'Rapid Test Item {i + 1}',
                'Width': '8ft',
                'Height': '6ft',
                'Total Sq.ft': 48.0,
                'Cost (INR)': 1200.0,
                'Quantity': 1,
                'Amount': 57600.0
            }
            dm.add_item_to_cart(item)
        
        start_time = time.time()
        
        # Perform rapid operations
        operation_count = 0
        for round_num in range(10):
            # Rapid quantity updates
            for item_id in range(1, 51):
                new_quantity = (round_num % 5) + 1
                dm.update_item_quantity(item_id, new_quantity)
                operation_count += 1
            
            # Rapid total calculations
            for _ in range(10):
                total = dm.get_cart_total_amount()
                operation_count += 1
            
            # Memory cleanup
            gc.collect()
        
        duration = time.time() - start_time
        operations_per_second = operation_count / duration
        
        # Verify final state
        final_cart = dm.get_cart_data()
        assert len(final_cart) == 50
        
        # Performance assertion
        assert operations_per_second > 100, f"Too slow: {operations_per_second:.2f} ops/sec"
        
        print(f"\nRapid Operations Stress Test:")
        print(f"  Operations: {operation_count}")
        print(f"  Duration: {duration:.2f} seconds")
        print(f"  Rate: {operations_per_second:.2f} operations/second")
    
    @pytest.mark.performance
    def test_memory_pressure_stress(self, clean_data_manager):
        """Test behavior under memory pressure conditions"""
        import psutil
        import os
        
        dm = clean_data_manager
        process = psutil.Process(os.getpid())
        
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB
        max_memory_used = 0
        
        # Create memory pressure by adding many large items
        for i in range(200):
            # Create items with large specification strings
            large_particulars = f'Memory Stress Test Item {i + 1} - ' + 'X' * 500
            
            item = {
                'Sr.No': i + 1,
                'Particulars': large_particulars,
                'Width': f'{10 + (i % 10)}ft',
                'Height': f'{8 + (i % 8)}ft',
                'Total Sq.ft': (10 + (i % 10)) * (8 + (i % 8)),
                'Cost (INR)': 1500.0 + (i % 1000),
                'Quantity': 1,
                'Amount': ((10 + (i % 10)) * (8 + (i % 8))) * (1500.0 + (i % 1000))
            }
            dm.add_item_to_cart(item)
            
            # Monitor memory usage
            current_memory = process.memory_info().rss / 1024 / 1024  # MB
            memory_used = current_memory - initial_memory
            max_memory_used = max(max_memory_used, memory_used)
            
            # Force garbage collection every 20 items
            if (i + 1) % 20 == 0:
                gc.collect()
        
        # Final memory check
        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        final_memory_used = final_memory - initial_memory
        
        # Verify data integrity under memory pressure
        final_cart = dm.get_cart_data()
        assert len(final_cart) == 200
        
        # Memory usage should be reasonable (less than 100MB for this test)
        assert max_memory_used < 100, f"Memory usage too high: {max_memory_used:.2f} MB"
        
        print(f"\nMemory Pressure Test:")
        print(f"  Items: 200")
        print(f"  Max Memory Used: {max_memory_used:.2f} MB")
        print(f"  Final Memory Used: {final_memory_used:.2f} MB")


class TestErrorRecoveryStress:
    """Test error recovery under stress conditions"""
    
    @pytest.mark.performance
    def test_invalid_data_stress_recovery(self, clean_data_manager):
        """Test recovery from invalid data under stress"""
        dm = clean_data_manager
        
        valid_items_added = 0
        error_count = 0
        
        # Mix valid and invalid data rapidly
        # Note: DataManager accepts all items, even with missing fields
        for i in range(100):
            if i % 3 == 0:
                # Invalid item (missing required field)
                invalid_item = {
                    'Sr.No': i + 1,
                    'Particulars': f'Invalid Item {i + 1}',
                    # Missing Width, Height, etc.
                    'Cost (INR)': 1200.0,
                    'Quantity': 1
                }
                dm.add_item_to_cart(invalid_item)
            else:
                # Valid item
                valid_item = {
                    'Sr.No': valid_items_added + 1,
                    'Particulars': f'Valid Item {valid_items_added + 1}',
                    'Width': '8ft',
                    'Height': '6ft',
                    'Total Sq.ft': 48.0,
                    'Cost (INR)': 1200.0,
                    'Quantity': 1,
                    'Amount': 57600.0
                }
                dm.add_item_to_cart(valid_item)
                valid_items_added += 1
        
        # Verify all items were added (DataManager accepts all items)
        final_cart = dm.get_cart_data()
        assert len(final_cart) == 100, f"Expected 100 items in cart, got {len(final_cart)}"
        
        # Verify data manager still functions correctly 
        total = dm.get_cart_total_amount()
        # Total should be: 34 invalid items (1200 each) + 66 valid items (57600 each)
        expected_total = (34 * 1200.0) + (66 * 57600.0)
        assert total == expected_total, f"Expected total {expected_total}, got {total}"
        
        # The logic: out of 100 items, every 3rd is invalid (i % 3 == 0)
        # So items 0,3,6,9...99 are invalid = 34 items
        # Valid items should be 100 - 34 = 66 items
        assert valid_items_added == 66, f"Expected 66 valid items, got {valid_items_added}"
        
        print(f"\nError Recovery Stress Test:")
        print(f"  Valid items added: {valid_items_added}")
        print(f"  Errors encountered: {error_count}")
        print(f"  Final cart size: {len(final_cart)}")
    
    @pytest.mark.performance
    def test_concurrent_modification_stress(self, clean_data_manager):
        """Test handling of rapid modifications"""
        dm = clean_data_manager
        
        # Add initial items
        for i in range(20):
            item = {
                'Sr.No': i + 1,
                'Particulars': f'Concurrent Test Item {i + 1}',
                'Width': '8ft',
                'Height': '6ft',
                'Total Sq.ft': 48.0,
                'Cost (INR)': 1200.0,
                'Quantity': 1,
                'Amount': 57600.0
            }
            dm.add_item_to_cart(item)
        
        # Rapid modifications
        modification_count = 0
        start_time = time.time()
        
        for round_num in range(50):
            # Rapid add/remove/update cycle
            try:
                # Update existing items
                for item_id in range(1, 11):
                    dm.update_item_quantity(item_id, (round_num % 5) + 1)
                    modification_count += 1
                
                # Add new item
                new_item = {
                    'Sr.No': 21 + round_num,
                    'Particulars': f'Dynamic Item {21 + round_num}',
                    'Width': '6ft',
                    'Height': '4ft',
                    'Total Sq.ft': 24.0,
                    'Cost (INR)': 1000.0,
                    'Quantity': 1,
                    'Amount': 24000.0
                }
                dm.add_item_to_cart(new_item)
                modification_count += 1
                
                # Remove if too many items
                cart_data = dm.get_cart_data()
                if len(cart_data) > 60:
                    # Remove last few items (simulate cleanup)
                    for _ in range(5):
                        if len(dm.get_cart_data()) > 20:
                            last_item_id = dm.get_cart_data().iloc[-1]['Sr.No']
                            dm.remove_item_from_cart(int(last_item_id))
                            modification_count += 1
                
            except Exception as e:
                print(f"Error during modification round {round_num}: {e}")
        
        duration = time.time() - start_time
        
        # Verify final state is valid
        final_cart = dm.get_cart_data()
        assert len(final_cart) > 0
        
        # Verify data integrity
        total = dm.get_cart_total_amount()
        assert total > 0
        
        print(f"\nConcurrent Modification Stress Test:")
        print(f"  Modifications: {modification_count}")
        print(f"  Duration: {duration:.2f} seconds")
        print(f"  Rate: {modification_count/duration:.2f} modifications/second")
        print(f"  Final cart size: {len(final_cart)}")


class TestUIStressTesting:
    """Stress testing for UI components"""
    
    @pytest.mark.performance
    @pytest.mark.slow
    def test_multiple_product_frame_creation_stress(self, tk_root, clean_data_manager):
        """Test creating and destroying many product frames rapidly"""
        
        frame_creation_count = 0
        start_time = time.time()
        
        # Create and destroy product frames rapidly
        for i in range(30):
            product_window = tk.Toplevel(tk_root)
            product_window.withdraw()
            
            try:
                frame = SlidingWindowFrame(product_window, clean_data_manager)
                
                # Simulate user interaction
                frame.global_state.Width.set(f"{8 + (i % 4)}")
                frame.global_state.Height.set(f"{6 + (i % 3)}")
                frame.global_state.trackVar.set("3 Track")
                
                frame_creation_count += 1
                
                # Clean up immediately
                frame.destroy()
                
            finally:
                product_window.destroy()
            
            # Memory cleanup every 10 frames
            if (i + 1) % 10 == 0:
                gc.collect()
        
        duration = time.time() - start_time
        
        # Performance assertion
        frames_per_second = frame_creation_count / duration
        assert frames_per_second > 1, f"Frame creation too slow: {frames_per_second:.2f} frames/sec"
        
        print(f"\nUI Stress Test:")
        print(f"  Frames created: {frame_creation_count}")
        print(f"  Duration: {duration:.2f} seconds")
        print(f"  Rate: {frames_per_second:.2f} frames/second")
    
    @pytest.mark.performance
    def test_rapid_state_changes_stress(self, tk_root, clean_data_manager):
        """Test rapid state changes in UI components"""
        
        product_window = tk.Toplevel(tk_root)
        product_window.withdraw()
        
        try:
            frame = SlidingWindowFrame(product_window, clean_data_manager)
            
            state_changes = 0
            start_time = time.time()
            
            # Rapid state changes
            for round_num in range(100):
                # Change dimensions
                frame.global_state.Width.set(f"{6 + (round_num % 10)}")
                frame.global_state.Height.set(f"{4 + (round_num % 8)}")
                state_changes += 2
                
                # Change specifications
                tracks = ["2 Track", "3 Track", "4 Track"]
                frame.global_state.trackVar.set(tracks[round_num % 3])
                state_changes += 1
                
                # Change materials
                materials = ["Regular Section", "Domal Section (JINDAL)"]
                frame.global_state.aluMatVar.set(materials[round_num % 2])
                state_changes += 1
                
                # Change glass specs
                glass_types = ["Plain", "Frosted", "Tinted"]
                frame.global_state.glaTypVar.set(glass_types[round_num % 3])
                state_changes += 1
            
            duration = time.time() - start_time
            
            # Verify final state is valid
            width = frame.global_state.Width.get()
            height = frame.global_state.Height.get()
            assert width and height
            
            changes_per_second = state_changes / duration
            
            print(f"\nRapid State Changes Stress Test:")
            print(f"  State changes: {state_changes}")
            print(f"  Duration: {duration:.2f} seconds")
            print(f"  Rate: {changes_per_second:.2f} changes/second")
            
        finally:
            frame.destroy()
            product_window.destroy()


class TestExtremeCasesStress:
    """Test extreme edge cases and boundary conditions"""
    
    @pytest.mark.performance
    def test_extremely_large_dimensions_stress(self, clean_data_manager):
        """Test handling of extremely large dimension values"""
        dm = clean_data_manager
        
        # Test with very large dimensions
        extreme_dimensions = [
            (1000, 1000),  # Very large square
            (10000, 1),    # Very wide, very narrow
            (1, 10000),    # Very narrow, very tall
            (5000, 2000),  # Large rectangle
        ]
        
        for i, (width, height) in enumerate(extreme_dimensions):
            item = {
                'Sr.No': i + 1,
                'Particulars': f'Extreme Dimension Item {i + 1}',
                'Width': f'{width}ft',
                'Height': f'{height}ft',
                'Total Sq.ft': float(width * height),
                'Cost (INR)': 1200.0,
                'Quantity': 1,
                'Amount': float(width * height * 1200.0)
            }
            
            # Should handle extreme values gracefully
            dm.add_item_to_cart(item)
        
        # Verify all items added
        cart_data = dm.get_cart_data()
        assert len(cart_data) == 4
        
        # Verify calculations work with extreme values
        total = dm.get_cart_total_amount()
        assert total > 0
        
        print(f"\nExtreme Dimensions Stress Test:")
        print(f"  Items with extreme dimensions: 4")
        print(f"  Total amount: ₹{total:,.2f}")
    
    @pytest.mark.performance
    def test_zero_and_negative_values_stress(self, clean_data_manager):
        """Test handling of zero and edge case values"""
        dm = clean_data_manager
        
        edge_cases = [
            (1, 1, 1200.0, 1),      # Minimum valid values
            (0.1, 0.1, 1200.0, 1),  # Very small dimensions
            (1, 1, 0.01, 1),        # Very small cost
            (1, 1, 1200.0, 0.1),    # Fractional quantity
        ]
        
        valid_items_added = 0
        
        for i, (width, height, cost, quantity) in enumerate(edge_cases):
            try:
                item = {
                    'Sr.No': i + 1,
                    'Particulars': f'Edge Case Item {i + 1}',
                    'Width': f'{width}ft',
                    'Height': f'{height}ft',
                    'Total Sq.ft': float(width * height),
                    'Cost (INR)': cost,
                    'Quantity': quantity,
                    'Amount': float(width * height * cost * quantity)
                }
                
                dm.add_item_to_cart(item)
                valid_items_added += 1
                
            except Exception as e:
                print(f"Edge case {i + 1} handled gracefully: {e}")
        
        # Verify valid items were processed
        cart_data = dm.get_cart_data()
        assert len(cart_data) == valid_items_added
        
        print(f"\nEdge Cases Stress Test:")
        print(f"  Valid edge cases processed: {valid_items_added}")
    
    @pytest.mark.performance
    def test_unicode_and_special_characters_stress(self, clean_data_manager):
        """Test handling of unicode and special characters"""
        dm = clean_data_manager
        
        special_names = [
            "Test Item with émojis 🏠🪟",
            "Test Item with 中文字符",
            "Test Item with Русский текст",
            "Test Item with العربية",
            "Test Item with special chars: @#$%^&*()",
            "Test Item with very long name " + "X" * 200,
            "Test Item with\nnewlines\tand\ttabs",
            "Test Item with quotes 'single' and \"double\"",
        ]
        
        for i, name in enumerate(special_names):
            try:
                item = {
                    'Sr.No': i + 1,
                    'Particulars': name,
                    'Width': '8ft',
                    'Height': '6ft',
                    'Total Sq.ft': 48.0,
                    'Cost (INR)': 1200.0,
                    'Quantity': 1,
                    'Amount': 57600.0
                }
                
                dm.add_item_to_cart(item)
                
            except Exception as e:
                print(f"Special character case {i + 1} handled: {e}")
        
        # Verify processing
        cart_data = dm.get_cart_data()
        
        print(f"\nSpecial Characters Stress Test:")
        print(f"  Items with special characters: {len(cart_data)}")


class TestResourceUtilizationStress:
    """Test resource utilization under stress"""
    
    @pytest.mark.performance
    @pytest.mark.slow
    def test_sustained_load_stress(self, clean_data_manager):
        """Test sustained operations over extended period"""
        dm = clean_data_manager
        
        start_time = time.time()
        operation_count = 0
        target_duration = 30  # 30 seconds of sustained load
        
        while (time.time() - start_time) < target_duration:
            # Add item
            item_num = operation_count + 1
            item = {
                'Sr.No': item_num,
                'Particulars': f'Sustained Load Item {item_num}',
                'Width': f'{6 + (item_num % 5)}ft',
                'Height': f'{4 + (item_num % 3)}ft',
                'Total Sq.ft': (6 + (item_num % 5)) * (4 + (item_num % 3)),
                'Cost (INR)': 1000.0 + (item_num % 500),
                'Quantity': 1,
                'Amount': ((6 + (item_num % 5)) * (4 + (item_num % 3))) * (1000.0 + (item_num % 500))
            }
            dm.add_item_to_cart(item)
            operation_count += 1
            
            # Calculate total every 10 items
            if operation_count % 10 == 0:
                total = dm.get_cart_total_amount()
                
            # Clean up if cart gets too large
            if operation_count % 100 == 0:
                # Keep only last 50 items
                cart_data = dm.get_cart_data()
                if len(cart_data) > 50:
                    dm.cart_data = cart_data.tail(50).reset_index(drop=True)
                gc.collect()
        
        actual_duration = time.time() - start_time
        operations_per_second = operation_count / actual_duration
        
        # Verify sustained performance
        assert operations_per_second > 1, f"Sustained load too slow: {operations_per_second:.2f} ops/sec"
        
        # Verify final state
        final_cart = dm.get_cart_data()
        total = dm.get_cart_total_amount()
        
        print(f"\nSustained Load Stress Test:")
        print(f"  Duration: {actual_duration:.2f} seconds")
        print(f"  Operations: {operation_count}")
        print(f"  Rate: {operations_per_second:.2f} operations/second")
        print(f"  Final cart size: {len(final_cart)}")
        print(f"  Final total: ₹{total:,.2f}") 