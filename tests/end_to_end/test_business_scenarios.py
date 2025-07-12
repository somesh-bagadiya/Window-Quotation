"""
End-to-End Business Scenario Tests
Window Quotation Application

Tests real-world business scenarios:
- Residential home quotations
- Commercial office projects  
- Industrial facility quotations
- High-value complex projects
- Rush order workflows
- Budget-constrained scenarios
"""

import pytest
import tkinter as tk
import os
import tempfile
from unittest.mock import patch, MagicMock

from ui.main_app import MainApplication
from ui.product_frames import *  # Import all product frames
from data_manager import DataManager


class TestResidentialScenarios:
    """Test residential home quotation scenarios"""
    
    @pytest.mark.end_to_end
    @pytest.mark.residential
    def test_small_apartment_quotation(self, tk_root, clean_data_manager, clean_global_state, temp_test_directory):
        """Test quotation for small apartment with basic windows"""
        app = MainApplication(tk_root)
        
        # Small apartment customer
        customer_data = {
            'custNamVar': 'John & Mary Apartment',
            'custAddVar': 'Flat 3B, Sunrise Apartments\nSector 15, New Town',
            'custConVar': '+91-9876543210'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.global_state.custAddVar.set(customer_data['custAddVar'])
        app.global_state.custConVar.set(customer_data['custConVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Typical apartment requirements
        apartment_products = [
            {
                'frame_class': FixWindowFrame,
                'particulars': 'Fix Window',
                'width': '4',
                'height': '3',
                'quantity': 3,  # Living room, bedrooms
                'specs': {
                    'aluMatVar': 'Regular Section',
                    'glaThicVar': '4mm',
                    'glaTypVar': 'Plain'
                }
            },
            {
                'frame_class': SlidingWindowFrame,
                'particulars': 'Sliding Window',
                'width': '6',
                'height': '4',
                'quantity': 2,  # Main bedroom, kitchen
                'specs': {
                    'trackVar': '2 Track',
                    'aluMatVar': 'Regular Section',
                    'glaThicVar': '5mm',
                    'glaTypVar': 'Plain'
                }
            },
            {
                'frame_class': SlidingDoorFrame,
                'particulars': 'Sliding Door',
                'width': '3',
                'height': '7',
                'quantity': 1,  # Balcony door
                'specs': {
                    'trackVar': '2 Track',
                    'aluMatVar': 'Regular Section',
                    'glaThicVar': '8mm',
                    'glaTypVar': 'Tinted'
                }
            }
        ]
        
        total_products = 0
        
        for product in apartment_products:
            for qty_instance in range(product['quantity']):
                product_window = tk.Toplevel(tk_root)
                product_window.withdraw()
                
                try:
                    frame = product['frame_class'](product_window, app.data_manager)
                    
                    # Set dimensions
                    frame.global_state.Width.set(product['width'])
                    frame.global_state.Height.set(product['height'])
                    
                    # Set specifications
                    for spec_key, spec_value in product['specs'].items():
                        if hasattr(frame.global_state, spec_key):
                            getattr(frame.global_state, spec_key).set(spec_value)
                    
                    # Calculate cost
                    frame.calculate_cost()
                    
                    # Create cart item
                    width = float(product['width'])
                    height = float(product['height'])
                    area = width * height
                    
                    specs = frame.global_state.get_all_specification_vars()
                    spec_values = {key: var.get() if hasattr(var, 'get') else var 
                                  for key, var in specs.items()}
                    
                    total_products += 1
                    cart_item = {
                        'Sr.No': total_products,
                        'Particulars': product['particulars'],
                        'Width': f"{product['width']}ft",
                        'Height': f"{product['height']}ft",
                        'Total Sq.ft': area,
                        'Cost (INR)': 1200.0,  # Budget-friendly apartment pricing
                        'Quantity': 1,
                        'Amount': 1200.0 * area,
                        **spec_values
                    }
                    
                    frame.data_manager.add_item_to_cart(cart_item)
                    
                finally:
                    frame.destroy()
                    product_window.destroy()
        
        # Verify apartment quotation
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 6, "Apartment should have 6 window/door items"
        
        total_amount = app.data_manager.get_cart_total_amount()
        assert 50000 <= total_amount <= 200000, "Apartment quotation should be in reasonable range"
        
        # Save apartment quotation
        excel_filename = os.path.join(temp_test_directory, "apartment_quotation.xlsx")
        success, message = app.data_manager.save_quotation_to_excel(excel_filename)
        assert success, f"Apartment quotation save should succeed: {message}"
    
    @pytest.mark.end_to_end
    @pytest.mark.residential
    def test_luxury_villa_quotation(self, tk_root, clean_data_manager, clean_global_state, temp_test_directory):
        """Test quotation for luxury villa with premium features"""
        app = MainApplication(tk_root)
        
        # Luxury villa customer
        customer_data = {
            'custNamVar': 'Mr. & Mrs. Premium Villa',
            'custAddVar': 'Villa No. 7, Green Valley Estate\nPremium Hills, Metro City',
            'custConVar': '+91-9000000001'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.global_state.custAddVar.set(customer_data['custAddVar'])
        app.global_state.custConVar.set(customer_data['custConVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Premium villa products
        luxury_products = [
            {
                'frame_class': SlidingFoldingDoorFrame,
                'particulars': 'Sliding Folding Door',
                'width': '12',
                'height': '8',
                'quantity': 2,  # Main entrance, garden access
                'specs': {
                    'aluMatVar': 'Domal Section (JINDAL)',
                    'glaThicVar': '12mm',
                    'glaTypVar': 'Tinted'
                }
            },
            {
                'frame_class': CasementWindowFrame,
                'particulars': 'Casement Window',
                'width': '8',
                'height': '6',
                'quantity': 4,  # Bedrooms
                'specs': {
                    'aluMatVar': 'Domal Section (JINDAL)',
                    'glaThicVar': '8mm',
                    'glaTypVar': 'One-way'
                }
            },
            {
                'frame_class': CurtainWallFrame,
                'particulars': 'Curtain Wall',
                'width': '15',
                'height': '10',
                'quantity': 1,  # Living room feature wall
                'specs': {
                    'aluMatVar': 'Profile Aluminium Section',
                    'glaThicVar': '12mm',
                    'glaTypVar': 'Tinted'
                }
            }
        ]
        
        total_products = 0
        
        for product in luxury_products:
            for qty_instance in range(product['quantity']):
                product_window = tk.Toplevel(tk_root)
                product_window.withdraw()
                
                try:
                    frame = product['frame_class'](product_window, app.data_manager)
                    
                    # Set dimensions
                    frame.global_state.Width.set(product['width'])
                    frame.global_state.Height.set(product['height'])
                    
                    # Set luxury specifications
                    for spec_key, spec_value in product['specs'].items():
                        if hasattr(frame.global_state, spec_key):
                            getattr(frame.global_state, spec_key).set(spec_value)
                    
                    # Calculate premium cost
                    frame.calculate_cost()
                    
                    # Create premium cart item
                    width = float(product['width'])
                    height = float(product['height'])
                    area = width * height
                    
                    specs = frame.global_state.get_all_specification_vars()
                    spec_values = {key: var.get() if hasattr(var, 'get') else var 
                                  for key, var in specs.items()}
                    
                    total_products += 1
                    cart_item = {
                        'Sr.No': total_products,
                        'Particulars': product['particulars'],
                        'Width': f"{product['width']}ft",
                        'Height': f"{product['height']}ft",
                        'Total Sq.ft': area,
                        'Cost (INR)': 2500.0,  # Premium luxury pricing
                        'Quantity': 1,
                        'Amount': 2500.0 * area,
                        **spec_values
                    }
                    
                    frame.data_manager.add_item_to_cart(cart_item)
                    
                finally:
                    frame.destroy()
                    product_window.destroy()
        
        # Verify luxury villa quotation
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 7, "Villa should have 7 premium items"
        
        total_amount = app.data_manager.get_cart_total_amount()
        assert total_amount >= 500000, "Luxury villa should be high-value quotation"
        
        # Save luxury quotation
        excel_filename = os.path.join(temp_test_directory, "luxury_villa_quotation.xlsx")
        success, message = app.data_manager.save_quotation_to_excel(excel_filename)
        assert success, f"Luxury villa quotation save should succeed: {message}"


class TestCommercialScenarios:
    """Test commercial office and business quotations"""
    
    @pytest.mark.end_to_end
    @pytest.mark.commercial
    def test_office_building_quotation(self, tk_root, clean_data_manager, clean_global_state, temp_test_directory):
        """Test quotation for commercial office building"""
        app = MainApplication(tk_root)
        
        # Commercial customer
        customer_data = {
            'custNamVar': 'TechCorp Office Solutions Pvt Ltd',
            'custAddVar': 'Tech Tower, IT Park Phase 2\nCyber City, Business District',
            'custConVar': '+91-8000000001'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.global_state.custAddVar.set(customer_data['custAddVar'])
        app.global_state.custConVar.set(customer_data['custConVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Commercial office products
        office_products = [
            {
                'frame_class': AluminiumPartitionFrame,
                'particulars': 'Aluminium Partition',
                'width': '10',
                'height': '8',
                'quantity': 8,  # Office cabins
                'specs': {
                    'aluMatVar': 'Profile Aluminium Section',
                    'glaThicVar': '8mm',
                    'glaTypVar': 'Frosted'
                }
            },
            {
                'frame_class': ToughenedPartitionFrame,
                'particulars': 'Toughened Partition',
                'width': '12',
                'height': '8',
                'quantity': 4,  # Conference rooms
                'specs': {
                    'aluMatVar': 'Domal Section (JINDAL)',
                    'glaThicVar': '12mm',
                    'glaTypVar': 'Plain'
                }
            },
            {
                'frame_class': ToughenedDoorFrame,
                'particulars': 'Toughened Door',
                'width': '3',
                'height': '7',
                'quantity': 12,  # Office doors
                'specs': {
                    'aluMatVar': 'Regular Section',
                    'glaThicVar': '12mm',
                    'glaTypVar': 'Plain'
                }
            },
            {
                'frame_class': FixWindowFrame,
                'particulars': 'Fix Window',
                'width': '6',
                'height': '4',
                'quantity': 20,  # External windows
                'specs': {
                    'aluMatVar': 'Regular Section',
                    'glaThicVar': '8mm',
                    'glaTypVar': 'Tinted'
                }
            }
        ]
        
        total_products = 0
        
        for product in office_products:
            for qty_instance in range(product['quantity']):
                product_window = tk.Toplevel(tk_root)
                product_window.withdraw()
                
                try:
                    frame = product['frame_class'](product_window, app.data_manager)
                    
                    # Set dimensions
                    frame.global_state.Width.set(product['width'])
                    frame.global_state.Height.set(product['height'])
                    
                    # Set commercial specifications
                    for spec_key, spec_value in product['specs'].items():
                        if hasattr(frame.global_state, spec_key):
                            getattr(frame.global_state, spec_key).set(spec_value)
                    
                    # Calculate commercial cost
                    frame.calculate_cost()
                    
                    # Create commercial cart item
                    width = float(product['width'])
                    height = float(product['height'])
                    area = width * height
                    
                    specs = frame.global_state.get_all_specification_vars()
                    spec_values = {key: var.get() if hasattr(var, 'get') else var 
                                  for key, var in specs.items()}
                    
                    total_products += 1
                    cart_item = {
                        'Sr.No': total_products,
                        'Particulars': product['particulars'],
                        'Width': f"{product['width']}ft",
                        'Height': f"{product['height']}ft",
                        'Total Sq.ft': area,
                        'Cost (INR)': 1800.0,  # Commercial bulk pricing
                        'Quantity': 1,
                        'Amount': 1800.0 * area,
                        **spec_values
                    }
                    
                    frame.data_manager.add_item_to_cart(cart_item)
                    
                finally:
                    frame.destroy()
                    product_window.destroy()
        
        # Verify commercial quotation
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 44, "Office building should have 44 items total"
        
        total_amount = app.data_manager.get_cart_total_amount()
        assert total_amount >= 1000000, "Commercial project should be high-value"
        
        # Save commercial quotation
        excel_filename = os.path.join(temp_test_directory, "office_building_quotation.xlsx")
        success, message = app.data_manager.save_quotation_to_excel(excel_filename)
        assert success, f"Commercial quotation save should succeed: {message}"
        
        # Verify file is substantial for large commercial project
        file_size = os.path.getsize(excel_filename)
        assert file_size > 5000, f"Commercial Excel file should be substantial, got {file_size} bytes"
    
    @pytest.mark.end_to_end
    @pytest.mark.commercial  
    def test_retail_showroom_quotation(self, tk_root, clean_data_manager, clean_global_state):
        """Test quotation for retail showroom with display features"""
        app = MainApplication(tk_root)
        
        # Retail customer
        customer_data = {
            'custNamVar': 'Premium Retail Showroom Ltd',
            'custAddVar': 'Ground Floor, Shopping Mall\nCommercial Complex, City Center',
            'custConVar': '+91-7000000001'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Retail showroom products - focus on visibility and aesthetics
        showroom_products = [
            {
                'frame_class': CurtainWallFrame,
                'particulars': 'Curtain Wall',
                'width': '20',
                'height': '10',
                'quantity': 1,  # Street-facing display
                'specs': {
                    'aluMatVar': 'Profile Aluminium Section',
                    'glaThicVar': '12mm',
                    'glaTypVar': 'Plain'  # Maximum visibility
                }
            },
            {
                'frame_class': SlidingDoorFrame,
                'particulars': 'Sliding Door',
                'width': '4',
                'height': '8',
                'quantity': 2,  # Customer entrances
                'specs': {
                    'trackVar': '3 Track',
                    'aluMatVar': 'Domal Section (JINDAL)',
                    'glaThicVar': '12mm',
                    'glaTypVar': 'Plain'
                }
            },
            {
                'frame_class': AluminiumPartitionFrame,
                'particulars': 'Aluminium Partition',
                'width': '8',
                'height': '8',
                'quantity': 3,  # Display sections
                'specs': {
                    'aluMatVar': 'Profile Aluminium Section',
                    'glaThicVar': '8mm',
                    'glaTypVar': 'Plain'
                }
            }
        ]
        
        for i, product in enumerate(showroom_products):
            for qty_instance in range(product['quantity']):
                product_window = tk.Toplevel(tk_root)
                product_window.withdraw()
                
                try:
                    frame = product['frame_class'](product_window, app.data_manager)
                    
                    frame.global_state.Width.set(product['width'])
                    frame.global_state.Height.set(product['height'])
                    
                    for spec_key, spec_value in product['specs'].items():
                        if hasattr(frame.global_state, spec_key):
                            getattr(frame.global_state, spec_key).set(spec_value)
                    
                    frame.calculate_cost()
                    
                    width = float(product['width'])
                    height = float(product['height'])
                    area = width * height
                    
                    specs = frame.global_state.get_all_specification_vars()
                    spec_values = {key: var.get() if hasattr(var, 'get') else var 
                                  for key, var in specs.items()}
                    
                    cart_item = {
                        'Sr.No': i * 10 + qty_instance + 1,
                        'Particulars': product['particulars'],
                        'Width': f"{product['width']}ft",
                        'Height': f"{product['height']}ft",
                        'Total Sq.ft': area,
                        'Cost (INR)': 2200.0,  # Retail display pricing
                        'Quantity': 1,
                        'Amount': 2200.0 * area,
                        **spec_values
                    }
                    
                    frame.data_manager.add_item_to_cart(cart_item)
                    
                finally:
                    frame.destroy()
                    product_window.destroy()
        
        # Verify showroom quotation
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 6, "Showroom should have 6 display items"
        
        total_amount = app.data_manager.get_cart_total_amount()
        assert total_amount >= 800000, "Retail showroom should be substantial investment"


class TestIndustrialScenarios:
    """Test industrial facility and warehouse quotations"""
    
    @pytest.mark.end_to_end
    @pytest.mark.industrial
    def test_warehouse_facility_quotation(self, tk_root, clean_data_manager, clean_global_state):
        """Test quotation for industrial warehouse facility"""
        app = MainApplication(tk_root)
        
        # Industrial customer
        customer_data = {
            'custNamVar': 'Industrial Logistics Pvt Ltd',
            'custAddVar': 'Warehouse Complex, Industrial Area\nSector 58, Industrial Estate',
            'custConVar': '+91-6000000001'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Industrial warehouse requirements
        warehouse_products = [
            {
                'frame_class': FixWindowFrame,
                'particulars': 'Fix Window',
                'width': '8',
                'height': '6',
                'quantity': 15,  # Ventilation windows
                'specs': {
                    'aluMatVar': 'Regular Section',
                    'glaThicVar': '5mm',
                    'glaTypVar': 'Plain'
                }
            },
            {
                'frame_class': PattiLouverFrame,
                'particulars': 'Patti Louver',
                'width': '10',
                'height': '8',
                'quantity': 8,  # Industrial ventilation
                'specs': {
                    'aluMatVar': 'Regular Section',
                    'glaThicVar': '4mm',
                    'lowBladVar': '8'
                }
            },
            {
                'frame_class': SlidingDoorFrame,
                'particulars': 'Sliding Door',
                'width': '6',
                'height': '8',
                'quantity': 4,  # Loading bay offices
                'specs': {
                    'trackVar': '2 Track',
                    'aluMatVar': 'Regular Section',
                    'glaThicVar': '8mm',
                    'glaTypVar': 'Plain'
                }
            }
        ]
        
        for i, product in enumerate(warehouse_products):
            for qty_instance in range(product['quantity']):
                product_window = tk.Toplevel(tk_root)
                product_window.withdraw()
                
                try:
                    frame = product['frame_class'](product_window, app.data_manager)
                    
                    frame.global_state.Width.set(product['width'])
                    frame.global_state.Height.set(product['height'])
                    
                    for spec_key, spec_value in product['specs'].items():
                        if hasattr(frame.global_state, spec_key):
                            getattr(frame.global_state, spec_key).set(spec_value)
                    
                    frame.calculate_cost()
                    
                    width = float(product['width'])
                    height = float(product['height'])
                    area = width * height
                    
                    specs = frame.global_state.get_all_specification_vars()
                    spec_values = {key: var.get() if hasattr(var, 'get') else var 
                                  for key, var in specs.items()}
                    
                    cart_item = {
                        'Sr.No': i * 20 + qty_instance + 1,
                        'Particulars': product['particulars'],
                        'Width': f"{product['width']}ft",
                        'Height': f"{product['height']}ft",
                        'Total Sq.ft': area,
                        'Cost (INR)': 1000.0,  # Industrial bulk pricing
                        'Quantity': 1,
                        'Amount': 1000.0 * area,
                        **spec_values
                    }
                    
                    frame.data_manager.add_item_to_cart(cart_item)
                    
                finally:
                    frame.destroy()
                    product_window.destroy()
        
        # Verify warehouse quotation
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 27, "Warehouse should have 27 industrial items"
        
        total_amount = app.data_manager.get_cart_total_amount()
        assert total_amount >= 1500000, "Industrial facility should be large-scale"


class TestSpecialScenarios:
    """Test special business scenarios and edge cases"""
    
    @pytest.mark.end_to_end
    @pytest.mark.special
    def test_rush_order_workflow(self, tk_root, clean_data_manager, clean_global_state):
        """Test rush order with quick quotation requirements"""
        app = MainApplication(tk_root)
        
        # Rush order customer
        customer_data = {
            'custNamVar': 'Urgent Construction Ltd - RUSH ORDER',
            'custAddVar': 'Project Site 123, Emergency Repairs',
            'custConVar': '+91-9999999999'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Quick standard products for rush order
        rush_products = [
            {
                'frame_class': FixWindowFrame,
                'particulars': 'Fix Window',
                'width': '6',
                'height': '4',
                'quantity': 10  # Standard size, high quantity
            },
            {
                'frame_class': SlidingDoorFrame,
                'particulars': 'Sliding Door',
                'width': '3',
                'height': '7',
                'quantity': 5  # Standard doors
            }
        ]
        
        import time
        start_time = time.time()
        
        # Process rush order quickly
        for i, product in enumerate(rush_products):
            for qty_instance in range(product['quantity']):
                product_window = tk.Toplevel(tk_root)
                product_window.withdraw()
                
                try:
                    frame = product['frame_class'](product_window, app.data_manager)
                    
                    frame.global_state.Width.set(product['width'])
                    frame.global_state.Height.set(product['height'])
                    
                    # Use default specifications for speed
                    frame.calculate_cost()
                    
                    width = float(product['width'])
                    height = float(product['height'])
                    area = width * height
                    
                    cart_item = {
                        'Sr.No': i * 10 + qty_instance + 1,
                        'Particulars': product['particulars'],
                        'Width': f"{product['width']}ft",
                        'Height': f"{product['height']}ft",
                        'Total Sq.ft': area,
                        'Cost (INR)': 1500.0,  # Standard rush pricing
                        'Quantity': 1,
                        'Amount': 1500.0 * area
                    }
                    
                    frame.data_manager.add_item_to_cart(cart_item)
                    
                finally:
                    frame.destroy()
                    product_window.destroy()
        
        processing_time = time.time() - start_time
        
        # Verify rush order efficiency
        cart_data = app.data_manager.get_cart_data()
        assert len(cart_data) == 15, "Rush order should have 15 standard items"
        assert processing_time < 40.0, f"Rush order took {processing_time:.2f}s - realistic for 15 products"
    
    @pytest.mark.end_to_end
    @pytest.mark.special
    def test_budget_constrained_scenario(self, tk_root, clean_data_manager, clean_global_state):
        """Test budget-conscious customer scenario"""
        app = MainApplication(tk_root)
        
        # Budget customer
        customer_data = {
            'custNamVar': 'Budget Home Solutions',
            'custAddVar': 'Affordable Housing Project, Phase 1',
            'custConVar': '+91-8888888888'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.data_manager.set_customer_details(customer_data)
        
        # Budget-friendly products
        budget_products = [
            {
                'frame_class': FixWindowFrame,
                'particulars': 'Fix Window',
                'width': '4',
                'height': '3',
                'quantity': 5,
                'cost': 600.0  # Budget pricing
            },
            {
                'frame_class': SlidingWindowFrame,
                'particulars': 'Sliding Window',
                'width': '5',
                'height': '4',
                'quantity': 3,
                'cost': 800.0  # Budget sliding
            }
        ]
        
        for i, product in enumerate(budget_products):
            for qty_instance in range(product['quantity']):
                product_window = tk.Toplevel(tk_root)
                product_window.withdraw()
                
                try:
                    frame = product['frame_class'](product_window, app.data_manager)
                    
                    frame.global_state.Width.set(product['width'])
                    frame.global_state.Height.set(product['height'])
                    
                    # Budget specifications - basic options
                    if hasattr(frame.global_state, 'aluMatVar'):
                        frame.global_state.aluMatVar.set('Regular Section')
                    if hasattr(frame.global_state, 'glaThicVar'):
                        frame.global_state.glaThicVar.set('4mm')
                    if hasattr(frame.global_state, 'glaTypVar'):
                        frame.global_state.glaTypVar.set('Plain')
                    
                    frame.calculate_cost()
                    
                    width = float(product['width'])
                    height = float(product['height'])
                    area = width * height
                    
                    cart_item = {
                        'Sr.No': i * 10 + qty_instance + 1,
                        'Particulars': product['particulars'],
                        'Width': f"{product['width']}ft",
                        'Height': f"{product['height']}ft",
                        'Total Sq.ft': area,
                        'Cost (INR)': product['cost'],
                        'Quantity': 1,
                        'Amount': product['cost'] * area
                    }
                    
                    frame.data_manager.add_item_to_cart(cart_item)
                    
                finally:
                    frame.destroy()
                    product_window.destroy()
        
        # Verify budget scenario
        cart_data = app.data_manager.get_cart_data()
        total_amount = app.data_manager.get_cart_total_amount()
        
        assert len(cart_data) == 8, "Budget project should have 8 items"
        assert total_amount <= 100000, "Budget quotation should stay within limits"
        
        # Verify all items use budget specifications
        for _, item in cart_data.iterrows():
            if 'aluMatVar' in item and pd.notna(item['aluMatVar']):
                assert item['aluMatVar'] == 'Regular Section', "Budget items should use regular sections"
    
    @pytest.mark.end_to_end
    @pytest.mark.performance
    def test_high_volume_quotation_performance(self, tk_root, clean_data_manager):
        """Test system performance with high-volume quotations"""
        import time
        
        app = MainApplication(tk_root)
        
        # High-volume customer
        customer_data = {
            'custNamVar': 'Mega Construction Corp - Bulk Order',
            'custAddVar': 'Multiple Project Sites',
            'custConVar': '+91-7777777777'
        }
        
        app.global_state.custNamVar.set(customer_data['custNamVar'])
        app.data_manager.set_customer_details(customer_data)
        
        start_time = time.time()
        
        # Add 50 items (high volume)
        for i in range(50):
            cart_item = {
                'Sr.No': i + 1,
                'Particulars': f'Bulk Item {i + 1}',
                'Width': '8ft',
                'Height': '6ft',
                'Total Sq.ft': 48.0,
                'Cost (INR)': 1200.0,
                'Quantity': 1,
                'Amount': 57600.0  # 1200 * 48
            }
            app.data_manager.add_item_to_cart(cart_item)
        
        # Perform bulk operations
        cart_data = app.data_manager.get_cart_data()
        total_amount = app.data_manager.get_cart_total_amount()
        
        # Update quantities in bulk
        for i in range(1, 11):  # Update first 10 items
            app.data_manager.update_item_quantity(i, 2)
        
        processing_time = time.time() - start_time
        
        # Performance assertions
        assert len(cart_data) == 50, "Should handle 50 items"
        assert total_amount > 2000000, "High-volume quotation should be substantial"
        assert processing_time < 20.0, f"High-volume processing took {processing_time:.2f}s"
        
        # Verify updates worked
        updated_cart = app.data_manager.get_cart_data()
        for i in range(10):
            assert updated_cart.iloc[i]['Quantity'] == 2, f"Item {i+1} quantity should be updated" 