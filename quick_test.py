#!/usr/bin/env python3
"""
Quick Test Script for Window Quotation Application
For rapid validation during development
"""

import sys
import os
import tkinter as tk
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_basic_functionality():
    """Quick test of basic functionality"""
    print("🚀 Running Quick Tests...")
    
    try:
        # Test 1: Import all modules
        print("  1. Testing imports...", end="")
        from data_manager import DataManager
        from global_state import get_global_state
        from ui.main_app import MainApplication
        print(" ✅")
        
        # Test 2: Initialize core components
        print("  2. Testing core initialization...", end="")
        root = tk.Tk()
        root.withdraw()
        
        dm = DataManager()
        gs = get_global_state()
        app = MainApplication(root)
        print(" ✅")
        
        # Test 3: Add item to cart
        print("  3. Testing cart functionality...", end="")
        test_item = {
            'Sr.No': 1,
            'Particulars': 'Quick Test Window',
            'Width': '10ft',
            'Height': '8ft',
            'Cost (INR)': 999.0,
            'Quantity': 1,
            'Amount': 999.0
        }
        dm.add_item_to_cart(test_item)
        
        cart_data = dm.get_cart_data()
        assert not cart_data.empty, "Cart should have items"
        assert len(cart_data) == 1, "Cart should have exactly 1 item"
        print(" ✅")
        
        # Test 4: Calculate total
        print("  4. Testing calculations...", end="")
        total = dm.get_cart_total_amount()
        assert total == 999.0, f"Total should be 999.0, got {total}"
        print(" ✅")
        
        # Test 5: Test global state
        print("  5. Testing global state...", end="")
        gs.custNamVar.set("Test Customer")
        assert gs.custNamVar.get() == "Test Customer", "Global state should store customer name"
        print(" ✅")
        
        root.destroy()
        
        print("\n🎉 All quick tests PASSED!")
        return True
        
    except Exception as e:
        print(f" ❌ FAILED: {e}")
        if 'root' in locals():
            root.destroy()
        return False

def test_product_frame_imports():
    """Test that all product frames can be imported"""
    print("🔧 Testing Product Frame Imports...")
    
    try:
        from ui.product_frames import (
            SlidingWindowFrame,
            SlidingDoorFrame,
            FixLouverFrame,
            PattiLouverFrame,
            OpenableWindowFrame,
            SlidingFoldingDoorFrame,
            CasementWindowFrame,
            AluminiumPartitionFrame,
            ToughenedPartitionFrame,
            ToughenedDoorFrame,
            CompositePanelFrame,
            CurtainWallFrame,
            FixWindowFrame,
            ExhaustFanWindowFrame,
        )
        print("  All 14 product frames imported successfully ✅")
        return True
    except Exception as e:
        print(f"  Product frame import failed ❌: {e}")
        return False

def test_calculator_workflow():
    """Test calculator workflow quickly"""
    print("🧮 Testing Calculator Workflow...")
    
    try:
        root = tk.Tk()
        root.withdraw()
        
        from data_manager import DataManager
        from ui.calculator_view import CalculatorView
        
        # Setup test data
        dm = DataManager()
        test_item = {'Sr.No': 1, 'Cost (INR)': 1000.0, 'Quantity': 1, 'Amount': 1000.0}
        dm.add_item_to_cart(test_item)
        
        # Create calculator
        calc = CalculatorView(root, dm)
        calc.withdraw()
        
        # Test calculation
        calc.gst_var.set("18")
        calc.discount_var.set("100")
        calc.calculate_cost()
        
        # Verify results
        assert calc.calculation_done, "Calculation should be marked as done"
        
        calc.destroy()
        root.destroy()
        
        print("  Calculator workflow test PASSED ✅")
        return True
        
    except Exception as e:
        print(f"  Calculator workflow test FAILED ❌: {e}")
        return False

def main():
    """Run all quick tests"""
    print("=" * 50)
    print("🔧 QUICK TEST SUITE - Window Quotation App")
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    tests = [
        test_basic_functionality,
        test_product_frame_imports,
        test_calculator_workflow
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  Test {test.__name__} crashed: {e}")
            failed += 1
        print()
    
    print("=" * 50)
    print("📊 QUICK TEST SUMMARY")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📈 Success Rate: {passed/(passed+failed)*100:.1f}%")
    
    if failed == 0:
        print("\n🎉 ALL QUICK TESTS PASSED! Ready for development.")
    else:
        print(f"\n⚠️  {failed} test(s) failed. Check issues above.")
    
    print("=" * 50)
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 