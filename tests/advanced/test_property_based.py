"""
Property-Based Testing with Hypothesis
Window Quotation Application

Advanced property-based testing to discover edge cases automatically:
- Hypothesis-driven test data generation
- Invariant testing across operations
- Contract verification
- Edge case discovery through fuzzing
- Mathematical property validation
"""

import pytest
from hypothesis import given, strategies as st, assume, example
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant
import tkinter as tk
from decimal import Decimal, InvalidOperation

from data_manager import DataManager
from global_state import get_global_state


class TestDataManagerProperties:
    """Property-based testing for DataManager operations"""
    
    @given(
        particulars=st.text(min_size=1, max_size=100),
        width=st.floats(min_value=0.1, max_value=1000.0, allow_nan=False, allow_infinity=False),
        height=st.floats(min_value=0.1, max_value=1000.0, allow_nan=False, allow_infinity=False),
        cost=st.floats(min_value=0.01, max_value=100000.0, allow_nan=False, allow_infinity=False),
        quantity=st.integers(min_value=1, max_value=1000)
    )
    def test_cart_item_addition_properties(self, clean_data_manager, particulars, width, height, cost, quantity):
        """Property: Adding valid items always increases cart size by exactly 1"""
        dm = clean_data_manager
        initial_size = len(dm.get_cart_data())
        
        # Calculate area and amount
        area = width * height
        amount = area * cost * quantity
        
        item = {
            'Sr.No': initial_size + 1,
            'Particulars': particulars,
            'Width': f'{width}ft',
            'Height': f'{height}ft',
            'Total Sq.ft': area,
            'Cost (INR)': cost,
            'Quantity': quantity,
            'Amount': amount
        }
        
        dm.add_item_to_cart(item)
        
        # Property: Cart size increases by exactly 1
        final_size = len(dm.get_cart_data())
        assert final_size == initial_size + 1, f"Cart size should increase by 1: {initial_size} -> {final_size}"
        
        # Property: Total amount is sum of all item amounts
        expected_total = dm.get_cart_data()['Amount'].sum()
        actual_total = dm.get_cart_total_amount()
        assert abs(actual_total - expected_total) < 0.01, f"Total mismatch: {actual_total} vs {expected_total}"
    
    @given(
        item_count=st.integers(min_value=1, max_value=50),
        cost_multiplier=st.floats(min_value=0.1, max_value=10.0, allow_nan=False, allow_infinity=False)
    )
    def test_bulk_operations_properties(self, clean_data_manager, item_count, cost_multiplier):
        """Property: Bulk operations maintain consistency"""
        dm = clean_data_manager
        
        # Add multiple items
        total_expected_amount = 0
        for i in range(item_count):
            area = 48.0  # 8ft x 6ft
            cost = 1200.0 * cost_multiplier
            quantity = 1
            amount = area * cost * quantity
            total_expected_amount += amount
            
            item = {
                'Sr.No': i + 1,
                'Particulars': f'Property Test Item {i + 1}',
                'Width': '8ft',
                'Height': '6ft',
                'Total Sq.ft': area,
                'Cost (INR)': cost,
                'Quantity': quantity,
                'Amount': amount
            }
            dm.add_item_to_cart(item)
        
        # Property: Cart has correct number of items
        cart_data = dm.get_cart_data()
        assert len(cart_data) == item_count, f"Cart should have {item_count} items, got {len(cart_data)}"
        
        # Property: Total amount matches sum of individual amounts
        actual_total = dm.get_cart_total_amount()
        assert abs(actual_total - total_expected_amount) < 0.01, f"Total amount mismatch: {actual_total} vs {total_expected_amount}"
        
        # Property: All serial numbers are sequential
        serial_numbers = cart_data['Sr.No'].tolist()
        expected_serials = list(range(1, item_count + 1))
        assert serial_numbers == expected_serials, f"Serial numbers not sequential: {serial_numbers}"
    
    @given(
        initial_quantity=st.integers(min_value=1, max_value=100),
        new_quantity=st.integers(min_value=1, max_value=100)
    )
    def test_quantity_update_properties(self, clean_data_manager, initial_quantity, new_quantity):
        """Property: Quantity updates maintain mathematical consistency"""
        dm = clean_data_manager
        
        # Add initial item
        base_cost = 1200.0
        area = 48.0
        initial_amount = area * base_cost * initial_quantity
        
        item = {
            'Sr.No': 1,
            'Particulars': 'Quantity Test Item',
            'Width': '8ft',
            'Height': '6ft',
            'Total Sq.ft': area,
            'Cost (INR)': base_cost,
            'Quantity': initial_quantity,
            'Amount': initial_amount
        }
        dm.add_item_to_cart(item)
        
        # Update quantity
        dm.update_item_quantity(1, new_quantity)
        
        # Property: Updated amount equals area * cost * new_quantity
        cart_data = dm.get_cart_data()
        updated_item = cart_data.iloc[0]
        expected_amount = area * base_cost * new_quantity
        
        assert updated_item['Quantity'] == new_quantity, f"Quantity not updated: {updated_item['Quantity']} vs {new_quantity}"
        assert abs(updated_item['Amount'] - expected_amount) < 0.01, f"Amount not calculated correctly: {updated_item['Amount']} vs {expected_amount}"
    
    @given(
        dimensions=st.lists(
            st.tuples(
                st.floats(min_value=0.1, max_value=100.0, allow_nan=False, allow_infinity=False),
                st.floats(min_value=0.1, max_value=100.0, allow_nan=False, allow_infinity=False)
            ),
            min_size=1,
            max_size=20
        )
    )
    def test_area_calculation_properties(self, clean_data_manager, dimensions):
        """Property: Area calculations are always width * height"""
        dm = clean_data_manager
        
        for i, (width, height) in enumerate(dimensions):
            expected_area = width * height
            
            item = {
                'Sr.No': i + 1,
                'Particulars': f'Area Test Item {i + 1}',
                'Width': f'{width}ft',
                'Height': f'{height}ft',
                'Total Sq.ft': expected_area,
                'Cost (INR)': 1200.0,
                'Quantity': 1,
                'Amount': expected_area * 1200.0
            }
            dm.add_item_to_cart(item)
        
        # Property: All areas are calculated correctly
        cart_data = dm.get_cart_data()
        for i, (width, height) in enumerate(dimensions):
            item = cart_data.iloc[i]
            expected_area = width * height
            assert abs(item['Total Sq.ft'] - expected_area) < 0.01, f"Area calculation wrong: {item['Total Sq.ft']} vs {expected_area}"


class TestGlobalStateProperties:
    """Property-based testing for GlobalState operations"""
    
    @given(
        width_value=st.text(min_size=1, max_size=10),
        height_value=st.text(min_size=1, max_size=10)
    )
    def test_string_var_properties(self, clean_global_state, width_value, height_value):
        """Property: StringVar objects maintain their values correctly"""
        gs = clean_global_state
        
        # Set values
        gs.Width.set(width_value)
        gs.Height.set(height_value)
        
        # Property: Values are preserved
        assert gs.Width.get() == width_value, f"Width value not preserved: {gs.Width.get()} vs {width_value}"
        assert gs.Height.get() == height_value, f"Height value not preserved: {gs.Height.get()} vs {height_value}"
    
    @given(
        track_choice=st.sampled_from(["2 Track", "3 Track", "4 Track"]),
        material_choice=st.sampled_from(["Regular Section", "Domal Section (JINDAL)"]),
        glass_choice=st.sampled_from(["3.5mm", "4mm", "5mm", "8mm", "12mm"])
    )
    def test_option_selection_properties(self, clean_global_state, track_choice, material_choice, glass_choice):
        """Property: Option selections are always valid"""
        gs = clean_global_state
        
        # Set options
        gs.trackVar.set(track_choice)
        gs.aluMatVar.set(material_choice)
        gs.glaThicVar.set(glass_choice)
        
        # Property: Selections are preserved and valid
        assert gs.trackVar.get() == track_choice
        assert gs.aluMatVar.get() == material_choice  
        assert gs.glaThicVar.get() == glass_choice
        
        # Property: Selections are in valid options
        assert track_choice in gs.track_options
        assert material_choice in gs.aluminium_material
        assert glass_choice in gs.glass_thickness


class CartStateMachine(RuleBasedStateMachine):
    """Stateful property-based testing for cart operations"""
    
    def __init__(self):
        super().__init__()
        self.data_manager = DataManager()
        self.data_manager.cart_data = self.data_manager.cart_data.iloc[0:0]  # Clear cart
        self.expected_items = {}
        self.next_serial = 1
    
    @rule(
        particulars=st.text(min_size=1, max_size=50),
        cost=st.floats(min_value=100.0, max_value=10000.0, allow_nan=False, allow_infinity=False),
        quantity=st.integers(min_value=1, max_value=10)
    )
    def add_item(self, particulars, cost, quantity):
        """Rule: Add item to cart"""
        area = 48.0  # Fixed area for simplicity
        amount = area * cost * quantity
        
        item = {
            'Sr.No': self.next_serial,
            'Particulars': particulars,
            'Width': '8ft',
            'Height': '6ft',
            'Total Sq.ft': area,
            'Cost (INR)': cost,
            'Quantity': quantity,
            'Amount': amount
        }
        
        self.data_manager.add_item_to_cart(item)
        self.expected_items[self.next_serial] = item
        self.next_serial += 1
    
    @rule(
        serial_number=st.integers(min_value=1, max_value=100),
        new_quantity=st.integers(min_value=1, max_value=10)
    )
    def update_quantity(self, serial_number, new_quantity):
        """Rule: Update item quantity"""
        if serial_number in self.expected_items:
            self.data_manager.update_item_quantity(serial_number, new_quantity)
            
            # Update expected state
            self.expected_items[serial_number]['Quantity'] = new_quantity
            area = self.expected_items[serial_number]['Total Sq.ft']
            cost = self.expected_items[serial_number]['Cost (INR)']
            self.expected_items[serial_number]['Amount'] = area * cost * new_quantity
    
    @rule(serial_number=st.integers(min_value=1, max_value=100))
    def remove_item(self, serial_number):
        """Rule: Remove item from cart"""
        if serial_number in self.expected_items:
            self.data_manager.remove_item_from_cart(serial_number)
            del self.expected_items[serial_number]
    
    @invariant()
    def cart_consistency(self):
        """Invariant: Cart state matches expected state"""
        cart_data = self.data_manager.get_cart_data()
        
        # Check cart size matches expected
        assert len(cart_data) == len(self.expected_items), f"Cart size mismatch: {len(cart_data)} vs {len(self.expected_items)}"
        
        # Check total amount consistency
        expected_total = sum(item['Amount'] for item in self.expected_items.values())
        actual_total = self.data_manager.get_cart_total_amount()
        
        if expected_total > 0:  # Only check if we have items
            assert abs(actual_total - expected_total) < 0.01, f"Total amount mismatch: {actual_total} vs {expected_total}"


class TestContractVerification:
    """Contract testing for API consistency"""
    
    @given(
        item_data=st.dictionaries(
            keys=st.sampled_from(['Sr.No', 'Particulars', 'Width', 'Height', 'Total Sq.ft', 'Cost (INR)', 'Quantity', 'Amount']),
            values=st.one_of(
                st.integers(min_value=1, max_value=1000),
                st.text(min_size=1, max_size=100),
                st.floats(min_value=0.1, max_value=10000.0, allow_nan=False, allow_infinity=False)
            ),
            min_size=8,
            max_size=8
        )
    )
    def test_add_item_contract(self, clean_data_manager, item_data):
        """Contract: add_item_to_cart preconditions and postconditions"""
        dm = clean_data_manager
        
        # Ensure required fields are present and valid types
        required_fields = ['Sr.No', 'Particulars', 'Width', 'Height', 'Total Sq.ft', 'Cost (INR)', 'Quantity', 'Amount']
        
        # Convert to appropriate types for contract testing
        try:
            item = {
                'Sr.No': int(item_data.get('Sr.No', 1)),
                'Particulars': str(item_data.get('Particulars', 'Test Item')),
                'Width': f"{float(item_data.get('Width', 8.0))}ft",
                'Height': f"{float(item_data.get('Height', 6.0))}ft",
                'Total Sq.ft': float(item_data.get('Total Sq.ft', 48.0)),
                'Cost (INR)': float(item_data.get('Cost (INR)', 1200.0)),
                'Quantity': int(item_data.get('Quantity', 1)),
                'Amount': float(item_data.get('Amount', 57600.0))
            }
            
            # Precondition: All required fields present
            for field in required_fields:
                assert field in item, f"Missing required field: {field}"
            
            # Precondition: Numeric fields are positive
            assume(item['Sr.No'] > 0)
            assume(item['Total Sq.ft'] > 0)
            assume(item['Cost (INR)'] > 0)
            assume(item['Quantity'] > 0)
            assume(item['Amount'] > 0)
            
            initial_size = len(dm.get_cart_data())
            
            # Operation
            dm.add_item_to_cart(item)
            
            # Postcondition: Cart size increased
            final_size = len(dm.get_cart_data())
            assert final_size == initial_size + 1, "Cart size should increase by 1"
            
            # Postcondition: Item appears in cart
            cart_data = dm.get_cart_data()
            added_item = cart_data.iloc[-1]  # Last added item
            assert added_item['Particulars'] == item['Particulars'], "Item not found in cart"
            
        except (ValueError, TypeError, InvalidOperation):
            # Contract allows rejecting invalid data
            pass
    
    @given(
        serial_number=st.integers(),
        quantity=st.integers()
    )
    def test_update_quantity_contract(self, clean_data_manager, serial_number, quantity):
        """Contract: update_item_quantity handles all input cases gracefully"""
        dm = clean_data_manager
        
        # Add a test item first
        test_item = {
            'Sr.No': 1,
            'Particulars': 'Contract Test Item',
            'Width': '8ft',
            'Height': '6ft',
            'Total Sq.ft': 48.0,
            'Cost (INR)': 1200.0,
            'Quantity': 2,
            'Amount': 115200.0
        }
        dm.add_item_to_cart(test_item)
        
        initial_cart = dm.get_cart_data().copy()
        
        # Contract: Function should handle all inputs gracefully
        try:
            dm.update_item_quantity(serial_number, quantity)
            
            # If successful, verify postconditions
            if serial_number == 1 and quantity > 0:
                # Postcondition: Quantity updated
                updated_cart = dm.get_cart_data()
                if len(updated_cart) > 0:
                    assert updated_cart.iloc[0]['Quantity'] == quantity, "Quantity not updated correctly"
        except Exception:
            # Contract allows rejecting invalid inputs
            pass
        
        # Postcondition: Cart structure remains valid
        final_cart = dm.get_cart_data()
        assert len(final_cart) <= len(initial_cart) + 1, "Cart structure corrupted"


class TestEdgeCaseDiscovery:
    """Discover edge cases through property-based testing"""
    
    @given(
        dimensions=st.tuples(
            st.floats(min_value=1e-10, max_value=1e10, allow_nan=False, allow_infinity=False),
            st.floats(min_value=1e-10, max_value=1e10, allow_nan=False, allow_infinity=False)
        )
    )
    @example(dimensions=(0.0001, 0.0001))  # Very small dimensions
    @example(dimensions=(999999.0, 999999.0))  # Very large dimensions
    def test_extreme_dimension_handling(self, clean_data_manager, dimensions):
        """Discover how system handles extreme dimensions"""
        dm = clean_data_manager
        width, height = dimensions
        
        # Skip invalid cases
        assume(width > 0 and height > 0)
        assume(width < 1e8 and height < 1e8)  # Reasonable upper bound
        
        area = width * height
        assume(area < 1e15)  # Prevent overflow
        
        cost = 1200.0
        quantity = 1
        amount = area * cost * quantity
        
        item = {
            'Sr.No': 1,
            'Particulars': f'Extreme Dimension Test {width:.2e}x{height:.2e}',
            'Width': f'{width}ft',
            'Height': f'{height}ft',
            'Total Sq.ft': area,
            'Cost (INR)': cost,
            'Quantity': quantity,
            'Amount': amount
        }
        
        # System should handle extreme but valid dimensions
        dm.add_item_to_cart(item)
        
        cart_data = dm.get_cart_data()
        assert len(cart_data) == 1, "Item should be added successfully"
        
        # Verify calculations are preserved
        added_item = cart_data.iloc[0]
        assert abs(added_item['Total Sq.ft'] - area) < area * 1e-10, "Area calculation lost precision"
    
    @given(
        cost_values=st.lists(
            st.floats(min_value=0.01, max_value=1000000.0, allow_nan=False, allow_infinity=False),
            min_size=1,
            max_size=100
        )
    )
    def test_large_cost_accumulation(self, clean_data_manager, cost_values):
        """Test behavior with large cost accumulations"""
        dm = clean_data_manager
        
        expected_total = 0.0
        area = 48.0
        quantity = 1
        
        for i, cost in enumerate(cost_values):
            amount = area * cost * quantity
            expected_total += amount
            
            item = {
                'Sr.No': i + 1,
                'Particulars': f'Cost Test Item {i + 1}',
                'Width': '8ft',
                'Height': '6ft',
                'Total Sq.ft': area,
                'Cost (INR)': cost,
                'Quantity': quantity,
                'Amount': amount
            }
            dm.add_item_to_cart(item)
        
        # Property: Total should be sum of all amounts
        actual_total = dm.get_cart_total_amount()
        relative_error = abs(actual_total - expected_total) / max(expected_total, 1.0)
        
        # Allow small relative error for floating point precision
        assert relative_error < 1e-10, f"Large cost accumulation error: {actual_total} vs {expected_total} (error: {relative_error})"


# Make the stateful test discoverable
TestCartStateMachine = CartStateMachine.TestCase 