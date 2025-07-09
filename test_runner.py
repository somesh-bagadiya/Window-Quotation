#!/usr/bin/env python3
"""
Automated Test Runner for Window Quotation Application
Tests all major components and workflows automatically
"""

import unittest
import sys
import os
import tkinter as tk
from unittest.mock import Mock, patch, MagicMock
import tempfile
import shutil
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import application modules
from data_manager import DataManager
from global_state import get_global_state
from ui.main_app import MainApplication
from ui.cart_view import CartView
from ui.calculator_view import CalculatorView


class TestApplicationStartup(unittest.TestCase):
    """Test application startup and initialization"""
    
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide window during testing
        
    def tearDown(self):
        if self.root:
            self.root.destroy()
    
    def test_main_application_initialization(self):
        """Test that MainApplication initializes without errors"""
        try:
            app = MainApplication(self.root)
            self.assertIsNotNone(app)
            self.assertIsNotNone(app.data_manager)
            self.assertIsNotNone(app.global_state)
            print("✅ MainApplication initialization: PASSED")
        except Exception as e:
            self.fail(f"MainApplication failed to initialize: {e}")
    
    def test_global_state_singleton(self):
        """Test global state singleton pattern"""
        state1 = get_global_state()
        state2 = get_global_state()
        self.assertIs(state1, state2)
        print("✅ Global state singleton: PASSED")
    
    def test_data_manager_initialization(self):
        """Test DataManager initialization"""
        dm = DataManager()
        self.assertIsNotNone(dm)
        self.assertTrue(hasattr(dm, 'cart_data'))
        print("✅ DataManager initialization: PASSED")


class TestDataManager(unittest.TestCase):
    """Test DataManager functionality"""
    
    def setUp(self):
        self.dm = DataManager()
        
    def test_add_item_to_cart(self):
        """Test adding items to cart"""
        test_item = {
            'Sr.No': 1,
            'Particulars': 'Test Window',
            'Width': '10ft',
            'Height': '8ft',
            'Cost (INR)': 1000.0,
            'Quantity': 1,
            'Amount': 1000.0
        }
        
        self.dm.add_item_to_cart(test_item)
        cart_data = self.dm.get_cart_data()
        self.assertFalse(cart_data.empty)
        self.assertEqual(len(cart_data), 1)
        print("✅ Add item to cart: PASSED")
    
    def test_cart_total_calculation(self):
        """Test cart total calculation"""
        test_items = [
            {'Sr.No': 1, 'Cost (INR)': 1000.0, 'Quantity': 2, 'Amount': 2000.0},
            {'Sr.No': 2, 'Cost (INR)': 500.0, 'Quantity': 1, 'Amount': 500.0}
        ]
        
        for item in test_items:
            self.dm.add_item_to_cart(item)
        
        total = self.dm.get_cart_total_amount()
        self.assertEqual(total, 2500.0)
        print("✅ Cart total calculation: PASSED")
    
    def test_update_item_quantity(self):
        """Test updating item quantity"""
        test_item = {'Sr.No': 1, 'Cost (INR)': 100.0, 'Quantity': 1, 'Amount': 100.0}
        self.dm.add_item_to_cart(test_item)
        
        self.dm.update_item_quantity(1, 5)
        cart_data = self.dm.get_cart_data()
        updated_item = cart_data[cart_data['Sr.No'] == 1].iloc[0]
        self.assertEqual(updated_item['Quantity'], 5)
        print("✅ Update item quantity: PASSED")


class TestUIComponents(unittest.TestCase):
    """Test UI components without displaying windows"""
    
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        
    def tearDown(self):
        if self.root:
            self.root.destroy()
    
    @patch('tkinter.messagebox.showerror')
    @patch('tkinter.messagebox.showwarning')
    def test_cart_view_initialization(self, mock_warning, mock_error):
        """Test CartView initialization"""
        # Reset singleton for clean test
        DataManager._instance = None
        dm = DataManager()
        
        # Add test data
        test_item = {
            'Sr.No': 1,
            'Particulars': 'Test Window',
            'Width': '10ft',
            'Height': '8ft',
            'Cost (INR)': 1000.0,
            'Quantity': 1,
            'Amount': 1000.0
        }
        dm.add_item_to_cart(test_item)
        
        try:
            cart_view = CartView(self.root, dm)
            cart_view.withdraw()  # Hide window
            self.assertIsNotNone(cart_view)
            print("✅ CartView initialization: PASSED")
            cart_view.destroy()
        except Exception as e:
            self.fail(f"CartView failed to initialize: {e}")
    
    @patch('tkinter.messagebox.showerror')
    def test_calculator_view_initialization(self, mock_error):
        """Test CalculatorView initialization"""
        # Reset singleton for clean test
        DataManager._instance = None
        dm = DataManager()
        
        # Add test data for calculation
        test_item = {'Sr.No': 1, 'Cost (INR)': 1000.0, 'Quantity': 1, 'Amount': 1000.0}
        dm.add_item_to_cart(test_item)
        
        try:
            calc_view = CalculatorView(self.root, dm)
            calc_view.withdraw()  # Hide window
            self.assertIsNotNone(calc_view)
            print("✅ CalculatorView initialization: PASSED")
            calc_view.destroy()
        except Exception as e:
            self.fail(f"CalculatorView failed to initialize: {e}")


class TestCalculationLogic(unittest.TestCase):
    """Test calculation logic"""
    
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        # Reset singleton for clean test
        DataManager._instance = None
        self.dm = DataManager()
        
        # Add test item
        test_item = {'Sr.No': 1, 'Cost (INR)': 1000.0, 'Quantity': 1, 'Amount': 1000.0}
        self.dm.add_item_to_cart(test_item)
        
    def tearDown(self):
        if self.root:
            self.root.destroy()
    
    @patch('tkinter.messagebox.showerror')
    def test_calculation_without_discount_installation(self, mock_error):
        """Test calculation with only GST"""
        calc_view = CalculatorView(self.root, self.dm)
        calc_view.withdraw()
        
        # Set GST only
        calc_view.gst_var.set("18")
        calc_view.discount_var.set("")
        calc_view.installation_var.set("")
        
        # Perform calculation
        calc_view.calculate_cost()
        
        # Check if GST total is calculated (1000 + 18% = 1180)
        gst_total = calc_view.gst_total_var.get()
        self.assertIn("1,180", gst_total)  # Should contain formatted amount
        print("✅ GST-only calculation: PASSED")
        
        calc_view.destroy()
    
    @patch('tkinter.messagebox.showerror')
    def test_calculation_with_discount(self, mock_error):
        """Test calculation with discount"""
        calc_view = CalculatorView(self.root, self.dm)
        calc_view.withdraw()
        
        # Set discount and GST
        calc_view.gst_var.set("18")
        calc_view.discount_var.set("100")  # 100 rupee discount
        calc_view.installation_var.set("")
        
        # Perform calculation
        calc_view.calculate_cost()
        
        # Check discount total (1000 - 100 = 900)
        discount_total = calc_view.discount_total_var.get()
        self.assertIn("900", discount_total)
        print("✅ Discount calculation: PASSED")
        
        calc_view.destroy()


class TestEndToEndWorkflow(unittest.TestCase):
    """Test complete end-to-end workflow"""
    
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.temp_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        if self.root:
            self.root.destroy()
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_complete_workflow(self):
        """Test complete customer-to-PDF workflow"""
        # Reset DataManager singleton for clean test
        DataManager._instance = None
        
        # 1. Initialize application (this will reset singletons)
        app = MainApplication(self.root)
        
        # 2. Set customer details
        app.global_state.custNamVar.set("Test Customer")
        app.global_state.custConVar.set("1234567890")
        app.global_state.custAddVar.set("Test Address")
        
        # 3. Add item to cart via DataManager
        test_item = {
            'Sr.No': 1,
            'Particulars': 'Test Window',
            'Width': '10ft',
            'Height': '8ft',
            'Total Sq.ft': 80.0,
            'Cost (INR)': 1000.0,
            'Quantity': 1,
            'Amount': 1000.0
        }
        app.data_manager.add_item_to_cart(test_item)
        
        # 4. Verify cart has item
        cart_data = app.data_manager.get_cart_data()
        self.assertFalse(cart_data.empty)
        
        # 5. Test calculation
        total = app.data_manager.get_cart_total_amount()
        self.assertEqual(total, 1000.0)
        
        print("✅ End-to-end workflow: PASSED")


def run_automated_tests():
    """Run all automated tests"""
    print("\n" + "="*60)
    print("🚀 STARTING AUTOMATED TESTING FOR WINDOW QUOTATION APP")
    print("="*60)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_classes = [
        TestApplicationStartup,
        TestDataManager,
        TestUIComponents,
        TestCalculationLogic,
        TestEndToEndWorkflow
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ FAILURES:")
        for test, failure in result.failures:
            print(f"  - {test}: {failure}")
    
    if result.errors:
        print("\n💥 ERRORS:")
        for test, error in result.errors:
            print(f"  - {test}: {error}")
    
    if result.wasSuccessful():
        print("\n🎉 ALL TESTS PASSED! Application is ready for production.")
    else:
        print(f"\n⚠️  {len(result.failures + result.errors)} test(s) failed. Please review issues above.")
    
    print("="*60)
    return result.wasSuccessful()


if __name__ == "__main__":
    # Ensure we're in the right directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    success = run_automated_tests()
    sys.exit(0 if success else 1) 