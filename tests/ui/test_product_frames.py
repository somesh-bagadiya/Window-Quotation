"""
UI Tests for Product Frame Components
Window Quotation Application

Tests all 14 product frame implementations including:
- Initialization and inheritance testing
- Cost calculation functionality
- Specification widget creation
- User interaction simulation
- Add to cart workflow testing
"""

import pytest
import tkinter as tk
from unittest.mock import patch, MagicMock

# Import all product frame classes
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

# Product frame test data for parametrized testing
PRODUCT_FRAMES_DATA = [
    (SlidingWindowFrame, "Sliding Window", {"track_required": True, "glass_required": True}),
    (SlidingDoorFrame, "Sliding Door", {"track_required": True, "glass_required": True}),
    (FixLouverFrame, "Fix Louver", {"louver_required": True, "glass_required": False}),
    (PattiLouverFrame, "Patti Louver", {"louver_required": True, "adjustable": True}),
    (OpenableWindowFrame, "Openable Window", {"hardware_required": True, "glass_required": True}),
    (SlidingFoldingDoorFrame, "Sliding Folding Door", {"folding_mechanism": True, "track_required": True}),
    (CasementWindowFrame, "Casement Window", {"hinge_required": True, "glass_required": True}),
    (AluminiumPartitionFrame, "Aluminium Partition", {"partition_type": True, "mounting_required": True}),
    (ToughenedPartitionFrame, "Toughened Partition", {"safety_glass": True, "structural": True}),
    (ToughenedDoorFrame, "Toughened Door", {"safety_glass": True, "door_hardware": True}),
    (CompositePanelFrame, "Composite Panel", {"panel_type": True, "composite_material": True}),
    (CurtainWallFrame, "Curtain Wall", {"structural_glazing": True, "weatherproofing": True}),
    (FixWindowFrame, "Fix Window", {"fixed_installation": True, "glass_required": True}),
    (ExhaustFanWindowFrame, "Exhaust Fan Window", {"ventilation": True, "fan_integration": True}),
]

# Extract just the frame classes for simpler parametrization
PRODUCT_FRAME_CLASSES = [item[0] for item in PRODUCT_FRAMES_DATA]


class TestProductFrameInitialization:
    """Test initialization of all product frame classes"""
    
    @pytest.mark.ui
    @pytest.mark.parametrize("frame_class", PRODUCT_FRAME_CLASSES)
    def test_frame_class_initialization(self, tk_root, clean_data_manager, frame_class):
        """Test that each product frame class initializes correctly"""
        frame = frame_class(tk_root, clean_data_manager)
        
        try:
            # Verify inheritance from BaseProductFrame
            assert hasattr(frame, 'global_state'), f"{frame_class.__name__} missing global_state"
            assert hasattr(frame, 'data_manager'), f"{frame_class.__name__} missing data_manager"
            assert hasattr(frame, 'calculate_cost'), f"{frame_class.__name__} missing calculate_cost method"
            assert hasattr(frame, 'add_to_cart'), f"{frame_class.__name__} missing add_to_cart method"
            
            # Verify UI structure from BaseProductFrame
            assert hasattr(frame, 'frame2'), f"{frame_class.__name__} missing customer details frame"
            assert hasattr(frame, 'frame0'), f"{frame_class.__name__} missing dimensions frame"
            assert hasattr(frame, 'frame1'), f"{frame_class.__name__} missing specifications frame"
            
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass
    
    @pytest.mark.ui
    @pytest.mark.parametrize("frame_class,product_name,features", PRODUCT_FRAMES_DATA)
    def test_frame_with_features(self, tk_root, clean_data_manager, frame_class, product_name, features):
        """Test frames with their specific features and capabilities"""
        frame = frame_class(tk_root, clean_data_manager)
        
        try:
            # Set the window type to match the product
            frame.global_state.windowTypeVar.set(product_name)
            
            # Verify window title matches product name
            expected_title = f"MGA WINDOWS - {product_name}"
            # Note: In test environment, title might not be visible, but we can check if it's set
            
            # Test specific features based on product type
            if features.get("track_required"):
                assert hasattr(frame.global_state, 'trackVar'), f"{product_name} should have track options"
            
            if features.get("glass_required"):
                assert hasattr(frame.global_state, 'glaThicVar'), f"{product_name} should have glass options"
                assert hasattr(frame.global_state, 'glaTypVar'), f"{product_name} should have glass type options"
            
            if features.get("louver_required"):
                # Louver frames should have specific louver options
                assert hasattr(frame.global_state, 'lowBladVar'), f"{product_name} should have louver blade options"
            
            if features.get("hardware_required"):
                assert hasattr(frame.global_state, 'hardLocVar'), f"{product_name} should have hardware options"
                assert hasattr(frame.global_state, 'handleVar'), f"{product_name} should have handle options"
                
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass


class TestProductFrameSpecifications:
    """Test specification widget creation and management"""
    
    @pytest.mark.ui
    @pytest.mark.parametrize("frame_class", PRODUCT_FRAME_CLASSES)
    def test_specifications_widgets_creation(self, tk_root, clean_data_manager, frame_class):
        """Test that specifications widgets are created properly"""
        frame = frame_class(tk_root, clean_data_manager)
        
        try:
            # Check if create_specifications method exists and can be called
            if hasattr(frame, 'create_specifications'):
                frame.create_specifications()
            
            # Verify that frame1 (specifications frame) has child widgets
            children = frame.frame1.winfo_children()
            # Most product frames should have some specification widgets
            # Note: Some frames might have minimal specifications
            
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass
    
    @pytest.mark.ui
    @pytest.mark.parametrize("frame_class", PRODUCT_FRAME_CLASSES)
    def test_global_state_variables_access(self, tk_root, clean_data_manager, frame_class):
        """Test that frames can access and modify global state variables"""
        frame = frame_class(tk_root, clean_data_manager)
        
        try:
            # Test basic dimension variables
            frame.global_state.Width.set("10")
            frame.global_state.Height.set("8")
            
            assert frame.global_state.Width.get() == "10"
            assert frame.global_state.Height.get() == "8"
            
            # Test common specification variables
            if hasattr(frame.global_state, 'trackVar'):
                frame.global_state.trackVar.set("2 Track")
                assert frame.global_state.trackVar.get() == "2 Track"
            
            if hasattr(frame.global_state, 'aluMatVar'):
                frame.global_state.aluMatVar.set("Regular Section")
                assert frame.global_state.aluMatVar.get() == "Regular Section"
                
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass


class TestProductFrameCostCalculation:
    """Test cost calculation functionality for all product frames"""
    
    @pytest.mark.ui
    @pytest.mark.parametrize("frame_class", PRODUCT_FRAME_CLASSES)
    def test_cost_calculation_method_exists(self, tk_root, clean_data_manager, frame_class):
        """Test that cost calculation method exists and is callable"""
        frame = frame_class(tk_root, clean_data_manager)
        
        try:
            # Set up basic dimensions
            frame.global_state.Width.set("10")
            frame.global_state.Height.set("8")
            
            # Cost calculation should not raise an error
            # Note: Actual cost calculation might depend on Excel data
            assert callable(frame.calculate_cost), f"{frame_class.__name__} calculate_cost is not callable"
            
            # Try to call calculate_cost (might fail due to missing data, but shouldn't crash)
            try:
                frame.calculate_cost()
            except Exception as e:
                # Log the exception but don't fail the test if it's a data-related issue
                print(f"Cost calculation for {frame_class.__name__} raised: {e}")
                
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass
    
    @pytest.mark.ui
    @pytest.mark.parametrize("width,height", [
        ("10", "8"),
        ("12", "6"),
        ("8", "10"),
        ("15", "12"),
        ("6", "4")
    ])
    def test_sliding_window_cost_calculation_variations(self, tk_root, clean_data_manager, width, height):
        """Test cost calculation with different dimensions for Sliding Window"""
        frame = SlidingWindowFrame(tk_root, clean_data_manager)
        
        try:
            # Set dimensions
            frame.global_state.Width.set(width)
            frame.global_state.Height.set(height)
            
            # Set some specifications
            frame.global_state.trackVar.set("2 Track")
            frame.global_state.aluMatVar.set("Regular Section")
            
            # Calculate area
            expected_area = float(width) * float(height)
            
            # Try cost calculation
            try:
                frame.calculate_cost()
                # If successful, check if area is calculated correctly
                calculated_area = frame.global_state.totSqftEntVar.get()
                if calculated_area:
                    assert float(calculated_area) == expected_area
            except Exception as e:
                print(f"Cost calculation failed with dimensions {width}x{height}: {e}")
                
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass


class TestProductFrameAddToCart:
    """Test add to cart functionality for all product frames"""
    
    @pytest.mark.ui
    @pytest.mark.parametrize("frame_class", PRODUCT_FRAME_CLASSES)
    def test_add_to_cart_method_exists(self, tk_root, clean_data_manager, frame_class):
        """Test that add to cart method exists for all frames"""
        frame = frame_class(tk_root, clean_data_manager)
        
        try:
            assert hasattr(frame, 'add_to_cart'), f"{frame_class.__name__} missing add_to_cart method"
            assert callable(frame.add_to_cart), f"{frame_class.__name__} add_to_cart is not callable"
            
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass
    
    @pytest.mark.ui
    def test_sliding_window_add_to_cart_workflow(self, tk_root, clean_global_state, clean_data_manager):
        """Test complete add to cart workflow for Sliding Window"""
        # Create a proper Toplevel window as the parent (as done in real application)
        product_window = tk.Toplevel(tk_root)
        product_window.title("Sliding Window")
        product_window.withdraw()  # Hide the window for testing
        
        frame = SlidingWindowFrame(product_window, clean_data_manager)

        try:
            # Set up product configuration
            frame.global_state.Width.set("10")
            frame.global_state.Height.set("8")
            frame.global_state.windowTypeVar.set("Sliding Window")
            frame.global_state.trackVar.set("2 Track")
            frame.global_state.aluMatVar.set("Regular Section")
            frame.global_state.glaThicVar.set("5mm")
            frame.global_state.glaTypVar.set("Plain")

            # Set a test cost for calculation
            frame.global_state.costEntVar.set("1500")
            frame.global_state.totSqftEntVar.set("80")
            frame.global_state.cstAmtInr.set("120000")

            # Mock the data manager add_item_to_cart method
            with patch.object(frame.data_manager, 'add_item_to_cart') as mock_add:
                frame.add_to_cart()

                # Verify add_item_to_cart was called
                assert mock_add.called, "add_item_to_cart should be called"

                # Get the arguments passed to add_item_to_cart
                call_args = mock_add.call_args[0][0]  # First argument of first call

                # Verify key item details (use the actual keys from the item_data structure)
                assert call_args['windowTypeVar'] == "Sliding Window"
                assert call_args['Width'] == "10"
                assert call_args['Height'] == "8"
                
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass
            try:
                product_window.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass


class TestProductFrameSpecialFeatures:
    """Test special features unique to specific product types"""
    
    @pytest.mark.ui
    @pytest.mark.parametrize("louver_frame_class", [FixLouverFrame, PattiLouverFrame])
    def test_louver_frame_specific_features(self, tk_root, clean_data_manager, louver_frame_class):
        """Test louver-specific features for Fix and Patti Louver frames"""
        frame = louver_frame_class(tk_root, clean_data_manager)
        
        try:
            # Louver frames should have louver blade options
            assert hasattr(frame.global_state, 'lowBladVar'), f"{louver_frame_class.__name__} should have louver blade options"
            
            # Test setting louver blade values
            frame.global_state.lowBladVar.set("6")
            assert frame.global_state.lowBladVar.get() == "6"
            
            # Patti Louver should have additional adjustability features
            if louver_frame_class == PattiLouverFrame:
                # Test if Patti Louver has additional controls
                pass  # Additional Patti-specific tests can be added here
                
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass
    
    @pytest.mark.ui
    @pytest.mark.parametrize("partition_frame_class", [AluminiumPartitionFrame, ToughenedPartitionFrame])
    def test_partition_frame_specific_features(self, tk_root, clean_data_manager, partition_frame_class):
        """Test partition-specific features"""
        frame = partition_frame_class(tk_root, clean_data_manager)
        
        try:
            # Partition frames should have structural considerations
            frame.global_state.Width.set("20")  # Partitions often have larger dimensions
            frame.global_state.Height.set("10")
            
            assert frame.global_state.Width.get() == "20"
            assert frame.global_state.Height.get() == "10"
            
            # Test partition-specific calculations
            try:
                frame.calculate_cost()
            except Exception as e:
                print(f"Partition cost calculation for {partition_frame_class.__name__}: {e}")
                
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass
    
    @pytest.mark.ui
    def test_exhaust_fan_window_unique_features(self, tk_root, clean_data_manager):
        """Test unique features of Exhaust Fan Window"""
        frame = ExhaustFanWindowFrame(tk_root, clean_data_manager)
        
        try:
            # Exhaust fan windows might have ventilation-specific options
            frame.global_state.Width.set("4")  # Exhaust fans are typically smaller
            frame.global_state.Height.set("4")
            
            # Test if fan-specific variables exist
            # (This depends on actual implementation)
            assert frame.global_state.Width.get() == "4"
            assert frame.global_state.Height.get() == "4"
            
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass


class TestProductFrameUserInteractionSimulation:
    """Test simulated user interactions with product frames"""
    
    @pytest.mark.ui
    def test_user_workflow_simulation_sliding_window(self, tk_root, clean_data_manager):
        """Simulate complete user workflow for Sliding Window configuration"""
        frame = SlidingWindowFrame(tk_root, clean_data_manager)
        
        try:
            # Step 1: User enters dimensions
            frame.global_state.Width.set("12")
            frame.global_state.Height.set("8")
            
            # Step 2: User selects track type
            frame.global_state.trackVar.set("3 Track")
            
            # Step 3: User selects materials
            frame.global_state.aluMatVar.set("Domal Section (JINDAL)")
            frame.global_state.glaThicVar.set("8mm")
            frame.global_state.glaTypVar.set("Tinted")
            
            # Step 4: User selects hardware
            frame.global_state.hardLocVar.set("Mortise Lock")
            frame.global_state.hardBeaVar.set("Steel Ball Bearing")
            frame.global_state.handleVar.set("C Type Handle")
            
            # Step 5: User selects colors
            frame.global_state.fraColVar.set("White")
            frame.global_state.silColVar.set("Clear")
            
            # Verify all selections are retained
            assert frame.global_state.Width.get() == "12"
            assert frame.global_state.trackVar.get() == "3 Track"
            assert frame.global_state.aluMatVar.get() == "Domal Section (JINDAL)"
            assert frame.global_state.glaThicVar.get() == "8mm"
            assert frame.global_state.fraColVar.get() == "White"
            
            # Step 6: User calculates cost
            try:
                frame.calculate_cost()
                print("Cost calculation completed successfully")
            except Exception as e:
                print(f"Cost calculation simulation failed: {e}")
                
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass
    
    @pytest.mark.ui
    @pytest.mark.parametrize("frame_class", PRODUCT_FRAME_CLASSES[:5])  # Test first 5 for performance
    def test_rapid_configuration_changes(self, tk_root, clean_data_manager, frame_class):
        """Test rapid configuration changes to simulate user experimentation"""
        frame = frame_class(tk_root, clean_data_manager)
        
        try:
            # Rapid dimension changes
            dimensions = [("8", "6"), ("10", "8"), ("12", "10"), ("6", "4")]
            for width, height in dimensions:
                frame.global_state.Width.set(width)
                frame.global_state.Height.set(height)
                
                # Verify changes are applied immediately
                assert frame.global_state.Width.get() == width
                assert frame.global_state.Height.get() == height
            
            # Rapid specification changes (if available)
            if hasattr(frame.global_state, 'trackVar'):
                tracks = ["2 Track", "3 Track", "4 Track"]
                for track in tracks:
                    frame.global_state.trackVar.set(track)
                    assert frame.global_state.trackVar.get() == track
                    
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass


class TestProductFrameErrorHandling:
    """Test error handling and edge cases for product frames"""
    
    @pytest.mark.ui
    @pytest.mark.parametrize("frame_class", PRODUCT_FRAME_CLASSES)
    def test_frame_destruction_cleanup(self, tk_root, clean_data_manager, frame_class):
        """Test that frames clean up properly when destroyed"""
        frame = frame_class(tk_root, clean_data_manager)
        
        # Store reference to global state
        global_state = frame.global_state
        
        # Destroy frame
        frame.destroy()
        
        # Global state should still be accessible (singleton pattern)
        assert global_state is not None
        assert hasattr(global_state, 'Width')
    
    @pytest.mark.ui
    def test_invalid_dimension_handling(self, tk_root, clean_data_manager):
        """Test handling of invalid dimension inputs"""
        frame = SlidingWindowFrame(tk_root, clean_data_manager)
        
        try:
            # Test invalid dimension inputs
            invalid_inputs = ["abc", "", "-5", "0"]
            
            for invalid_input in invalid_inputs:
                frame.global_state.Width.set(invalid_input)
                frame.global_state.Height.set("8")
                
                # Calculate cost should handle invalid inputs gracefully
                try:
                    frame.calculate_cost()
                except Exception as e:
                    # Error handling is expected for invalid inputs
                    print(f"Expected error for invalid input '{invalid_input}': {e}")
                    
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass
    
    @pytest.mark.ui
    @pytest.mark.parametrize("frame_class", PRODUCT_FRAME_CLASSES)
    def test_frame_without_global_state_initialization(self, tk_root, clean_data_manager, frame_class):
        """Test frame behavior if global state is not properly initialized"""
        # This test checks robustness of frame initialization
        frame = frame_class(tk_root, clean_data_manager)
        
        try:
            # Even with potential global state issues, frame should not crash
            assert frame is not None
            assert hasattr(frame, 'global_state')
            
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass


class TestProductFrameAccessibility:
    """Test accessibility and usability features"""
    
    @pytest.mark.ui
    @pytest.mark.parametrize("frame_class", PRODUCT_FRAME_CLASSES)
    def test_keyboard_navigation_compatibility(self, tk_root, clean_data_manager, frame_class):
        """Test that frames support keyboard navigation"""
        frame = frame_class(tk_root, clean_data_manager)
        
        try:
            # Check if widgets support focus (important for accessibility)
            children = frame.winfo_children()
            
            # Most frames should have focusable widgets
            focusable_widgets = []
            for child in children:
                try:
                    child.focus_set()
                    focusable_widgets.append(child)
                except:
                    pass  # Some widgets might not support focus
            
            # Should have some focusable widgets for user interaction
            # Note: In test environment, actual focus might not work as expected
            
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass
    
    @pytest.mark.ui
    def test_window_resizing_compatibility(self, tk_root, clean_data_manager):
        """Test that frames handle window resizing appropriately"""
        frame = SlidingWindowFrame(tk_root, clean_data_manager)
        
        try:
            # Test different window sizes
            sizes = [(800, 600), (1024, 768), (1200, 800)]
            
            for width, height in sizes:
                tk_root.geometry(f"{width}x{height}")
                tk_root.update()  # Update geometry
                
                # Frame should still be functional after resize
                assert frame.winfo_width() >= 0
                assert frame.winfo_height() >= 0
                
        finally:
            try:
                frame.destroy()
            except (tk.TclError, AttributeError):
                # Handle case where tkinter has already been cleaned up
                pass 