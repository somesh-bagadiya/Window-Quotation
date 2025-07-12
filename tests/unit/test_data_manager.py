"""
Unit Tests for DataManager Class
Window Quotation Application

Tests the core data management functionality including:
- Singleton pattern implementation
- Cart operations (add, update, remove)
- Customer data management
- Excel file operations
- Total calculations
"""

import pytest
import pandas as pd
import os
import tempfile
from unittest.mock import patch, mock_open, MagicMock

from data_manager import DataManager


class TestDataManagerCore:
    """Core DataManager functionality tests"""
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_singleton_pattern(self, clean_data_manager):
        """Test that DataManager follows singleton pattern correctly"""
        dm1 = DataManager()
        dm2 = DataManager()
        
        # Both instances should be the same object
        assert dm1 is dm2
        assert id(dm1) == id(dm2)
        
        # Verify singleton behavior with state
        dm1.test_value = "test"
        assert hasattr(dm2, 'test_value')
        assert dm2.test_value == "test"
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_initialization_state(self, clean_data_manager):
        """Test DataManager initializes with correct default state"""
        dm = clean_data_manager
        
        # Verify cart_data is empty DataFrame
        assert isinstance(dm.cart_data, pd.DataFrame)
        assert dm.cart_data.empty
        
        # Verify customer details are empty
        customer_details = dm.get_customer_details()
        assert customer_details['custNamVar'] == ""
        assert customer_details['custAddVar'] == ""
        assert customer_details['custConVar'] == ""
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_cart_data_property(self, clean_data_manager):
        """Test cart_data property returns correct DataFrame"""
        dm = clean_data_manager
        
        cart_data = dm.get_cart_data()
        assert isinstance(cart_data, pd.DataFrame)
        assert len(cart_data) == 0


class TestCartOperations:
    """Test cart operations"""
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_add_single_item_to_cart(self, clean_data_manager, sample_cart_item):
        """Test adding a single item to cart"""
        dm = clean_data_manager

        # Add item to cart
        dm.add_item_to_cart(sample_cart_item)

        # Verify item was added
        cart_data = dm.get_cart_data()
        assert len(cart_data) == 1
        assert cart_data.iloc[0]['Particulars'] == 'Sliding Window'
        # Correct expectation: cost × area × quantity = 1500 × 80 × 1 = 120000
        assert cart_data.iloc[0]['Amount'] == 120000.0
        assert cart_data.iloc[0]['Sr.No'] == 1
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_add_multiple_items_to_cart(self, clean_data_manager, sample_cart_items_multiple):
        """Test adding multiple items to cart"""
        dm = clean_data_manager
        
        # Add all items
        for item in sample_cart_items_multiple:
            dm.add_item_to_cart(item)
        
        # Verify all items were added
        cart_data = dm.get_cart_data()
        assert len(cart_data) == 3
        
        # Verify specific items  
        sliding_window = cart_data[cart_data['Particulars'] == 'Sliding Window'].iloc[0]
        assert sliding_window['Amount'] == 120000.0  # 1500 × 80 × 1

        sliding_door = cart_data[cart_data['Particulars'] == 'Sliding Door'].iloc[0]
        assert sliding_door['Amount'] == 320000.0  # 2000 × 80 × 2  
        assert sliding_door['Quantity'] == 2
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    @pytest.mark.parametrize("quantity,expected_amount", [
        (1, 120000.0),    # 1500 × 80 × 1
        (2, 240000.0),    # 1500 × 80 × 2
        (5, 600000.0),    # 1500 × 80 × 5
        (0.5, 60000.0),   # 1500 × 80 × 0.5
        (10, 1200000.0)   # 1500 × 80 × 10
    ])
    def test_cart_item_quantity_calculations(self, clean_data_manager, sample_cart_item, quantity, expected_amount):
        """Test cart calculations with different quantities"""
        dm = clean_data_manager
        
        # Modify item quantity and amount (correct calculation: cost × area × quantity)
        area = sample_cart_item['Total Sq.ft']
        cost_per_sqft = sample_cart_item['Cost (INR)']
        sample_cart_item['Quantity'] = quantity
        sample_cart_item['Amount'] = cost_per_sqft * area * quantity
        
        dm.add_item_to_cart(sample_cart_item)
        
        # Verify calculation
        total = dm.get_cart_total_amount()
        assert total == expected_amount
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_update_item_quantity(self, clean_data_manager, sample_cart_item):
        """Test updating item quantity in cart"""
        dm = clean_data_manager
        
        # Add item first
        dm.add_item_to_cart(sample_cart_item)
        
        # Update quantity
        dm.update_item_quantity(1, 3)
        
        # Verify update
        cart_data = dm.get_cart_data()
        updated_item = cart_data[cart_data['Sr.No'] == 1].iloc[0]
        assert updated_item['Quantity'] == 3
        
        # Verify amount was recalculated (correct: cost × area × quantity)
        cost_per_sqft = sample_cart_item['Cost (INR)']
        area = sample_cart_item['Total Sq.ft']
        expected_amount = cost_per_sqft * area * 3  # 1500 × 80 × 3 = 360,000
        assert updated_item['Amount'] == expected_amount
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_remove_item_from_cart(self, clean_data_manager, sample_cart_items_multiple):
        """Test removing items from cart"""
        dm = clean_data_manager
        
        # Add multiple items
        for item in sample_cart_items_multiple:
            dm.add_item_to_cart(item)
        
        # Remove middle item (Sr.No = 2)
        dm.remove_item_from_cart(2)
        
        # Verify removal
        cart_data = dm.get_cart_data()
        assert len(cart_data) == 2
        
        # Verify correct item was removed
        remaining_sr_nos = cart_data['Sr.No'].tolist()
        assert 2 not in remaining_sr_nos
        assert 1 in remaining_sr_nos
        assert 3 in remaining_sr_nos
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_cart_total_calculation(self, clean_data_manager, sample_cart_items_multiple):
        """Test cart total amount calculation"""
        dm = clean_data_manager
        
        # Add all items
        for item in sample_cart_items_multiple:
            dm.add_item_to_cart(item)
        
        # Calculate expected total
        expected_total = sum(item['Amount'] for item in sample_cart_items_multiple)
        
        # Verify total calculation
        total = dm.get_cart_total_amount()
        assert total == expected_total
        assert total == 497600.0  # 120000 + 320000 + 57600
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_cart_recalculate_totals(self, clean_data_manager, sample_cart_item):
        """Test recalculating cart totals after changes"""
        dm = clean_data_manager
        
        # Add item
        dm.add_item_to_cart(sample_cart_item)
        initial_total = dm.get_cart_total_amount()
        
        # Change quantity directly in cart_data
        dm.cart_data.loc[0, 'Quantity'] = 2
        
        # Recalculate totals
        dm.recalculate_cart_totals()
        
        # Verify recalculation
        new_total = dm.get_cart_total_amount()
        assert new_total == initial_total * 2
        
        # Verify amount column was updated (correct calculation: cost × area × quantity)
        cart_data = dm.get_cart_data()
        assert cart_data.iloc[0]['Amount'] == 240000.0  # 1500 × 80 × 2


class TestCustomerDataManagement:
    """Test customer data operations"""
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_set_customer_details(self, clean_data_manager, sample_customer_data):
        """Test setting customer details"""
        dm = clean_data_manager
        
        dm.set_customer_details(sample_customer_data)
        
        # Verify customer details were set
        retrieved_data = dm.get_customer_details()
        assert retrieved_data['custNamVar'] == sample_customer_data['custNamVar']
        assert retrieved_data['custAddVar'] == sample_customer_data['custAddVar']
        assert retrieved_data['custConVar'] == sample_customer_data['custConVar']
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_get_customer_details_default(self, clean_data_manager):
        """Test getting customer details with default values"""
        dm = clean_data_manager
        
        customer_details = dm.get_customer_details()
        
        assert customer_details['custNamVar'] == ""
        assert customer_details['custAddVar'] == ""
        assert customer_details['custConVar'] == ""
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_customer_details_persistence(self, clean_data_manager, sample_customer_data):
        """Test that customer details persist across operations"""
        dm = clean_data_manager
        
        # Set customer details
        dm.set_customer_details(sample_customer_data)
        
        # Perform other operations
        sample_item = {'Sr.No': 1, 'Cost (INR)': 1000.0, 'Quantity': 1, 'Amount': 1000.0}
        dm.add_item_to_cart(sample_item)
        
        # Verify customer details are still there
        retrieved_data = dm.get_customer_details()
        assert retrieved_data['custNamVar'] == sample_customer_data['custNamVar']


class TestExcelOperations:
    """Test Excel file operations"""
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    @pytest.mark.excel
    def test_save_quotation_to_excel(self, clean_data_manager, sample_cart_item, sample_customer_data, temp_test_directory):
        """Test saving quotation to Excel file"""
        dm = clean_data_manager
        
        # Set up data
        dm.set_customer_details(sample_customer_data)
        dm.add_item_to_cart(sample_cart_item)
        
        # Create test file path
        excel_path = os.path.join(temp_test_directory, 'test_quotation.xlsx')
        
        # Actually call the method - it should work with the temp directory
        result = dm.save_quotation_to_excel(excel_path)
        
        # Verify the method returned success
        success, message = result
        assert success is True
        assert "Successfully saved" in message
        
        # Verify file was created
        assert os.path.exists(excel_path)
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    @pytest.mark.excel
    def test_load_quotation_from_excel(self, clean_data_manager, sample_excel_file):
        """Test loading quotation from Excel file"""
        dm = clean_data_manager
        
        # Mock pandas read_excel
        mock_data = pd.DataFrame([
            {'Sr.No': 1, 'Particulars': 'Test Window', 'Cost (INR)': 1000.0, 'Quantity': 1, 'Amount': 1000.0}
        ])
        
        with patch('pandas.read_excel', return_value=mock_data) as mock_read_excel:
            dm.load_quotation_from_excel(sample_excel_file)
            
            # Verify read_excel was called
            mock_read_excel.assert_called_once_with(sample_excel_file)
            
            # Verify data was loaded
            cart_data = dm.get_cart_data()
            assert len(cart_data) == 1
            assert cart_data.iloc[0]['Particulars'] == 'Test Window'
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    @pytest.mark.excel
    def test_load_quotation_file_not_found(self, clean_data_manager):
        """Test loading quotation when file doesn't exist"""
        dm = clean_data_manager
        
        # Try to load non-existent file
        with patch('pandas.read_excel', side_effect=FileNotFoundError()):
            dm.load_quotation_from_excel('nonexistent.xlsx')
            
            # Cart should remain empty
            cart_data = dm.get_cart_data()
            assert cart_data.empty


class TestErrorHandling:
    """Test error handling and edge cases"""
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_update_nonexistent_item_quantity(self, clean_data_manager):
        """Test updating quantity for non-existent item"""
        dm = clean_data_manager
        
        # Try to update item that doesn't exist
        dm.update_item_quantity(999, 5)
        
        # Cart should remain empty
        cart_data = dm.get_cart_data()
        assert cart_data.empty
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_remove_nonexistent_item(self, clean_data_manager):
        """Test removing non-existent item from cart"""
        dm = clean_data_manager
        
        # Try to remove item that doesn't exist
        dm.remove_item_from_cart(999)
        
        # Cart should remain empty
        cart_data = dm.get_cart_data()
        assert cart_data.empty
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_cart_total_empty_cart(self, clean_data_manager):
        """Test calculating total for empty cart"""
        dm = clean_data_manager
        
        total = dm.get_cart_total_amount()
        assert total == 0.0
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    @pytest.mark.parametrize("invalid_item", [
        {},  # Empty dict
        {'Sr.No': 1},  # Missing required fields
        {'Cost (INR)': 'invalid'},  # Invalid data type
    ])
    def test_add_invalid_item_to_cart(self, clean_data_manager, invalid_item):
        """Test adding invalid items to cart"""
        dm = clean_data_manager
        
        # This should handle invalid items gracefully
        try:
            dm.add_item_to_cart(invalid_item)
            # If no exception, verify cart state
            cart_data = dm.get_cart_data()
            # Should either be empty or have reasonable defaults
        except (KeyError, ValueError, TypeError):
            # Expected for some invalid items
            pass


class TestDataIntegrity:
    """Test data integrity and consistency"""
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_serial_number_uniqueness(self, clean_data_manager):
        """Test that serial numbers remain unique in cart"""
        dm = clean_data_manager
        
        # Add items with different serial numbers
        items = [
            {'Sr.No': 1, 'Particulars': 'Window 1', 'Cost (INR)': 1000.0, 'Quantity': 1, 'Amount': 1000.0},
            {'Sr.No': 2, 'Particulars': 'Window 2', 'Cost (INR)': 1500.0, 'Quantity': 1, 'Amount': 1500.0},
            {'Sr.No': 3, 'Particulars': 'Window 3', 'Cost (INR)': 2000.0, 'Quantity': 1, 'Amount': 2000.0}
        ]
        
        for item in items:
            dm.add_item_to_cart(item)
        
        # Verify serial numbers are unique
        cart_data = dm.get_cart_data()
        serial_numbers = cart_data['Sr.No'].tolist()
        assert len(set(serial_numbers)) == len(serial_numbers)  # All unique
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_amount_consistency(self, clean_data_manager):
        """Test that Amount = Cost * Area * Quantity consistently"""
        dm = clean_data_manager
        
        items = [
            {'Sr.No': 1, 'Width': '10ft', 'Height': '8ft', 'Total Sq.ft': 80.0, 'Cost (INR)': 1000.0, 'Quantity': 2, 'Amount': 160000.0},
            {'Sr.No': 2, 'Width': '6ft', 'Height': '4ft', 'Total Sq.ft': 24.0, 'Cost (INR)': 1500.0, 'Quantity': 3, 'Amount': 108000.0},
        ]
        
        for item in items:
            dm.add_item_to_cart(item)
        
        # Verify amount consistency (cost × area × quantity)
        cart_data = dm.get_cart_data()
        for _, row in cart_data.iterrows():
            expected_amount = row['Cost (INR)'] * row['Total Sq.ft'] * row['Quantity']
            assert row['Amount'] == expected_amount, f"Row {row['Sr.No']}: Expected {expected_amount}, got {row['Amount']}"
    
    @pytest.mark.unit
    @pytest.mark.datamanager
    def test_cart_state_after_operations(self, clean_data_manager, sample_cart_items_multiple):
        """Test cart state consistency after multiple operations"""
        dm = clean_data_manager
        
        # Add items
        for item in sample_cart_items_multiple:
            dm.add_item_to_cart(item)
        
        initial_count = len(dm.get_cart_data())
        initial_total = dm.get_cart_total_amount()
        
        # Remove one item
        dm.remove_item_from_cart(2)
        
        # Update another item
        dm.update_item_quantity(1, 2)
        
        # Verify final state
        final_data = dm.get_cart_data()
        assert len(final_data) == initial_count - 1
        
        # Verify total is recalculated correctly
        final_total = dm.get_cart_total_amount()
        assert final_total != initial_total
        
        # Manually calculate expected total
        expected_total = 0
        for _, row in final_data.iterrows():
            expected_total += row['Amount']
        assert final_total == expected_total 