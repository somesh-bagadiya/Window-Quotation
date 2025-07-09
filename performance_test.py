#!/usr/bin/env python3
"""
Performance Test Suite for Window Quotation Application
Tests application performance with larger datasets
"""

import sys
import os
import time
import tkinter as tk
from datetime import datetime
import statistics

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_manager import DataManager
from global_state import get_global_state
from ui.main_app import MainApplication

def measure_time(func):
    """Decorator to measure execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper

class PerformanceTests:
    def __init__(self):
        self.results = {}
        
    @measure_time
    def test_large_cart_performance(self, num_items=100):
        """Test performance with large number of cart items"""
        dm = DataManager()
        
        # Add many items to cart
        for i in range(num_items):
            test_item = {
                'Sr.No': i + 1,
                'Particulars': f'Test Window {i+1}',
                'Width': f'{10 + i % 5}ft',
                'Height': f'{8 + i % 3}ft',
                'Cost (INR)': 1000.0 + (i * 100),
                'Quantity': 1 + (i % 3),
                'Amount': (1000.0 + (i * 100)) * (1 + (i % 3))
            }
            dm.add_item_to_cart(test_item)
        
        # Test retrieval performance
        cart_data = dm.get_cart_data()
        total = dm.get_cart_total_amount()
        
        return len(cart_data), total
    
    @measure_time
    def test_calculation_performance(self, num_calculations=50):
        """Test calculation performance with multiple scenarios"""
        root = tk.Tk()
        root.withdraw()
        
        try:
            from ui.calculator_view import CalculatorView
            
            dm = DataManager()
            test_item = {'Sr.No': 1, 'Cost (INR)': 10000.0, 'Quantity': 1, 'Amount': 10000.0}
            dm.add_item_to_cart(test_item)
            
            calc_times = []
            
            for i in range(num_calculations):
                calc = CalculatorView(root, dm)
                calc.withdraw()
                
                # Different calculation scenarios
                calc.gst_var.set("18")
                calc.discount_var.set(str(100 * (i % 10)))
                calc.installation_var.set(str(500 * (i % 5)))
                
                start = time.time()
                calc.calculate_cost()
                calc_time = time.time() - start
                calc_times.append(calc_time)
                
                calc.destroy()
            
            root.destroy()
            return calc_times
            
        except Exception as e:
            if root:
                root.destroy()
            raise e
    
    @measure_time
    def test_application_startup_performance(self, num_startups=10):
        """Test application startup performance"""
        startup_times = []
        
        for i in range(num_startups):
            root = tk.Tk()
            root.withdraw()
            
            start = time.time()
            app = MainApplication(root)
            startup_time = time.time() - start
            startup_times.append(startup_time)
            
            root.destroy()
        
        return startup_times
    
    @measure_time
    def test_data_manager_scalability(self, operations=1000):
        """Test DataManager with many operations"""
        dm = DataManager()
        
        # Test multiple add/update/remove operations
        for i in range(operations // 3):
            # Add item
            test_item = {
                'Sr.No': i + 1,
                'Particulars': f'Scalability Test {i+1}',
                'Cost (INR)': 1000.0,
                'Quantity': 1,
                'Amount': 1000.0
            }
            dm.add_item_to_cart(test_item)
            
            # Update quantity
            if i > 0:
                dm.update_item_quantity(i, 2)
            
            # Remove some items
            if i > 10 and i % 10 == 0:
                dm.remove_item_from_cart(i - 5)
        
        final_count = len(dm.get_cart_data())
        return final_count
    
    def run_all_performance_tests(self):
        """Run all performance tests and generate report"""
        print("🚀 STARTING PERFORMANCE TESTING")
        print("=" * 60)
        
        tests = [
            ("Large Cart (100 items)", self.test_large_cart_performance, [100]),
            ("Large Cart (500 items)", self.test_large_cart_performance, [500]),
            ("Calculation Performance", self.test_calculation_performance, [50]),
            ("Application Startup", self.test_application_startup_performance, [10]),
            ("Data Manager Scalability", self.test_data_manager_scalability, [1000])
        ]
        
        for test_name, test_func, args in tests:
            print(f"\n🧪 Running: {test_name}")
            try:
                result, execution_time = test_func(*args)
                self.results[test_name] = {
                    'execution_time': execution_time,
                    'result': result,
                    'status': 'PASSED'
                }
                print(f"  ⏱️  Execution Time: {execution_time:.4f} seconds")
                print(f"  📊 Result: {result}")
                print(f"  ✅ Status: PASSED")
                
            except Exception as e:
                self.results[test_name] = {
                    'execution_time': None,
                    'result': None,
                    'status': 'FAILED',
                    'error': str(e)
                }
                print(f"  ❌ Status: FAILED - {e}")
        
        self.generate_performance_report()
    
    def generate_performance_report(self):
        """Generate detailed performance report"""
        print("\n" + "=" * 60)
        print("📈 PERFORMANCE REPORT")
        print("=" * 60)
        
        total_tests = len(self.results)
        passed_tests = sum(1 for r in self.results.values() if r['status'] == 'PASSED')
        failed_tests = total_tests - passed_tests
        
        print(f"📊 Test Summary:")
        print(f"  Total Tests: {total_tests}")
        print(f"  Passed: {passed_tests}")
        print(f"  Failed: {failed_tests}")
        print(f"  Success Rate: {passed_tests/total_tests*100:.1f}%")
        
        print(f"\n⏱️  Performance Metrics:")
        execution_times = [r['execution_time'] for r in self.results.values() 
                          if r['execution_time'] is not None]
        
        if execution_times:
            print(f"  Average Execution Time: {statistics.mean(execution_times):.4f}s")
            print(f"  Fastest Test: {min(execution_times):.4f}s")
            print(f"  Slowest Test: {max(execution_times):.4f}s")
        
        print(f"\n📋 Detailed Results:")
        for test_name, result in self.results.items():
            status_emoji = "✅" if result['status'] == 'PASSED' else "❌"
            print(f"  {status_emoji} {test_name}")
            if result['execution_time']:
                print(f"    Time: {result['execution_time']:.4f}s")
            if result['status'] == 'FAILED':
                print(f"    Error: {result.get('error', 'Unknown error')}")
        
        # Performance benchmarks
        print(f"\n🎯 Performance Benchmarks:")
        if 'Large Cart (100 items)' in self.results:
            cart_time = self.results['Large Cart (100 items)']['execution_time']
            if cart_time and cart_time < 1.0:
                print(f"  ✅ Cart Performance: Excellent ({cart_time:.4f}s < 1.0s)")
            elif cart_time and cart_time < 3.0:
                print(f"  ⚠️  Cart Performance: Acceptable ({cart_time:.4f}s < 3.0s)")
            elif cart_time:
                print(f"  ❌ Cart Performance: Needs optimization ({cart_time:.4f}s >= 3.0s)")
        
        if 'Application Startup' in self.results:
            startup_times = self.results['Application Startup']['result']
            if startup_times and isinstance(startup_times, list):
                avg_startup = statistics.mean(startup_times)
                if avg_startup < 0.5:
                    print(f"  ✅ Startup Performance: Excellent ({avg_startup:.4f}s < 0.5s)")
                elif avg_startup < 2.0:
                    print(f"  ⚠️  Startup Performance: Acceptable ({avg_startup:.4f}s < 2.0s)")
                else:
                    print(f"  ❌ Startup Performance: Needs optimization ({avg_startup:.4f}s >= 2.0s)")
        
        print("=" * 60)
        
        return passed_tests == total_tests

def main():
    """Run performance testing suite"""
    print("🔬 PERFORMANCE TEST SUITE - Window Quotation App")
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    perf_tests = PerformanceTests()
    success = perf_tests.run_all_performance_tests()
    
    if success:
        print("\n🎉 ALL PERFORMANCE TESTS PASSED!")
        print("📈 Application performance is within acceptable limits.")
    else:
        print("\n⚠️  Some performance tests failed.")
        print("🔧 Consider optimizing the application for better performance.")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 