from tkinter import ttk
import tkinter as tk
from .base_product_frame import BaseProductFrame
from tkinter import messagebox
from babel.numbers import format_currency

# A dictionary to hold common options, can be expanded
OPTIONS = {
    "track_options": ["2 Track", "3 Track", "4 Track"],
    "aluminium_material": ["Regular Section", "Domal Section (JINDAL)", "UPVC Section", "Profile Aluminium Section"],
    "glass_thickness": ["3.5mm", "4mm", "5mm", "8mm", "12mm"],
    "glass_type": ["Plain", "Frosted", "One-way", "Tinted", "Bajra"],
    "hardware_lock": ["3/4th inch", "1 inch", "Domal full metal body (ARIES)"],
    "hardware_bearing": ["3/4th inch", "1 inch", "Domal teflon bearing (ARIES)"],
    "rubber_type": ["Clear", "Jumbo", "Powder Jumbo"],
    "rubber_thickness": ["4mm", "5mm"],
    "aluminium_net": ["14 x 14 Aluminium net", "Fiber Net"],
    "frame_colour": ["Black", "White", "Ivory", "Brown"],
    "silicon_colour": ["Black", "Clear", "White"],
    "louver_blade": [str(i) for i in range(3, 13)],
    "handle_options": ["C Type", "S Type"],
    "hardware_options": ["Regular", "Premium"],
    "acrylic_sheet_colour": ["Black", "White", "Ivory", "Brown"],
    "composite_sheet_colour": ["Black", "White", "Ivory"],
    "masking_tape_colour": ["Red", "Green"],
    "acp_sheet": ["Black", "White", "Ivory"],
}

class SlidingWindowFrame(BaseProductFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)

    def create_specifications(self):
        """Create specifications exactly as legacy SlidingWindow"""
        # Add specifications title
        selectWinLabel = ttk.Label(
            self.frame1, text="Specifications", font=("", 10, "bold")
        )
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        
        # Add large product image (600x400 as in legacy)
        self.add_product_image("Sliding Window.png")
        
        # Create specification labels exactly as legacy
        self.create_specification_labels()
        
        # Create specification widgets exactly as legacy  
        self.create_specification_widgets()
        
        # Add Next button
        self.add_next_button()

    def create_specification_labels(self):
        """Create specification labels exactly as legacy variableTitles()"""
        row = 5  # Start from row 5 as in legacy
        
        labels = [
            ("Type", row),
            ("Aluminium Material", row + 1),
            ("Glass Thickness", row + 2),
            ("Glass Type", row + 3),
            ("Hardware Lock", row + 4),
            ("Hardware Bearing", row + 5),
            ("Rubber Type", row + 6),
            ("Rubber Thickness", row + 7),
            ("Wool File", row + 8),
            ("Aluminium Net", row + 9),
            ("Frame Colour", row + 10),
            ("Silicon", row + 11),
            ("Screw", row + 12),
        ]
        
        for label_text, row_num in labels:
            label = ttk.Label(self.frame1, text=label_text)
            label.grid(column=0, row=row_num, padx=10, pady=10, sticky="W")

    def create_specification_widgets(self):
        """Create specification widgets exactly as legacy variables()"""
        row = 5  # Start from row 5 to match labels
        
        # Track (Type)
        track = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.trackVar, 
            width=30, 
            values=self.global_state.track_options
        )
        track.grid(column=1, row=row, padx=10, pady=10, sticky="W")
        track.bind("<Key>", lambda event: self.handleWait(event, track, "track_options"))
        
        # Aluminium Material
        aluMat = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.aluMatVar, 
            width=30, 
            values=self.global_state.aluminium_material
        )
        aluMat.grid(column=1, row=row + 1, padx=10, pady=10, sticky="W")
        aluMat.bind("<Key>", lambda event: self.handleWait(event, aluMat, "aluminium_material"))

        # Glass Thickness
        glaThic = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.glaThicVar, 
            width=30, 
            values=self.global_state.glass_thickness
        )
        glaThic.grid(column=1, row=row + 2, padx=10, pady=10, sticky="W")
        glaThic.bind("<Key>", lambda event: self.handleWait(event, glaThic, "glass_thickness"))

        # Glass Type
        glaTyp = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.glaTypVar, 
            width=30, 
            values=self.global_state.glass_type
        )
        glaTyp.grid(column=1, row=row + 3, padx=10, pady=10, sticky="W")
        glaTyp.bind("<Key>", lambda event: self.handleWait(event, glaTyp, "glass_type"))

        # Hardware Lock
        hardLoc = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.hardLocVar, 
            width=30, 
            values=self.global_state.hardware_lock
        )
        hardLoc.grid(column=1, row=row + 4, padx=10, pady=10, sticky="W")
        hardLoc.bind("<Key>", lambda event: self.handleWait(event, hardLoc, "hardware_lock"))

        # Hardware Bearing
        hardBea = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.hardBeaVar, 
            width=30, 
            values=self.global_state.hardware_bear
        )
        hardBea.grid(column=1, row=row + 5, padx=10, pady=10, sticky="W")
        hardBea.bind("<Key>", lambda event: self.handleWait(event, hardBea, "hardware_bear"))

        # Rubber Type
        rubbTyp = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.rubbTypVar, 
            width=30, 
            values=self.global_state.rubber_type
        )
        rubbTyp.grid(column=1, row=row + 6, padx=10, pady=10, sticky="W")
        rubbTyp.bind("<Key>", lambda event: self.handleWait(event, rubbTyp, "rubber_type"))

        # Rubber Thickness
        rubbThic = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.rubbThicVar, 
            width=30, 
            values=self.global_state.rubber_thick
        )
        rubbThic.grid(column=1, row=row + 7, padx=10, pady=10, sticky="W")
        rubbThic.bind("<Key>", lambda event: self.handleWait(event, rubbThic, "rubber_thick"))

        # Wool File (Checkbox)
        woolFile = ttk.Checkbutton(
            self.frame1, 
            variable=self.global_state.woolFileVar, 
            takefocus=0
        )
        woolFile.grid(column=1, row=row + 8, padx=15, pady=15, sticky="W")

        # Aluminium Net
        aluNet = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.aluNetVar, 
            width=30, 
            values=self.global_state.aluminium_net
        )
        aluNet.grid(column=1, row=row + 9, padx=10, pady=10, sticky="W")
        aluNet.bind("<Key>", lambda event: self.handleWait(event, aluNet, "aluminium_net"))

        # Frame Colour
        fraCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.fraColVar, 
            width=30, 
            values=self.global_state.frame_colour
        )
        fraCol.grid(column=1, row=row + 10, padx=10, pady=10, sticky="W")
        fraCol.bind("<Key>", lambda event: self.handleWait(event, fraCol, "frame_colour"))

        # Silicon Colour
        silCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.silColVar, 
            width=30, 
            values=self.global_state.silicon_colour
        )
        silCol.grid(column=1, row=row + 11, padx=10, pady=10, sticky="W")
        silCol.bind("<Key>", lambda event: self.handleWait(event, silCol, "silicon_colour"))

        # Screw selection (6 checkboxes with labels) exactly as legacy
        self.create_screw_selection(row + 12)

    def create_screw_selection(self, row):
        """Create screw selection widget exactly as legacy"""
        fram1 = tk.LabelFrame(self.frame1, borderwidth=0)
        fram1.grid(column=1, row=row, padx=10, pady=10, sticky="W")
        
        screw_values = ["6.56", "9.56", "25.6", "32.6", "50.8", "75.10"]
        screw_vars = [
            self.global_state.screwVar1, self.global_state.screwVar2, 
            self.global_state.screwVar3, self.global_state.screwVar4, 
            self.global_state.screwVar5, self.global_state.screwVar6
        ]
        
        for i, (value, var) in enumerate(zip(screw_values, screw_vars)):
            # Checkbox
            screw_cb = ttk.Checkbutton(fram1, variable=var, takefocus=0)
            screw_cb.grid(column=i, row=0, sticky="N", padx=5, pady=5)
            
            # Label
            screw_lab = ttk.Label(fram1, text=value)
            screw_lab.grid(column=i, row=1, sticky="N", padx=5, pady=5)

    def calculate_cost(self):
        """Implement exact legacy calculation logic for SlidingWindow"""
        try:
            width = float(self.global_state.Width.get()) if self.global_state.Width.get() else 0
            height = float(self.global_state.Height.get()) if self.global_state.Height.get() else 0
            totSQFt = width * height
            
            # Update total square feet
            self.global_state.totSqftEntVar.set(f"{totSQFt:.2f}")
            
            # Validation exactly as legacy
            cost_str = self.global_state.costEntVar.get()
            if cost_str == "":
                messagebox.showerror(
                    "Invalid", "Please fill in the cost field.", parent=self.parent
                )
                return False
                
            if not self.global_state.validate_digits(cost_str):
                messagebox.showerror(
                    "Invalid", "Please enter numbers in the cost field.", parent=self.parent
                )
                return False
            
            # Calculate cost exactly as legacy
            indCurr = lambda x: format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")
            cstAmt = float(totSQFt) * float(cost_str)
            self.global_state.cstAmtInr.set(indCurr(cstAmt))
            
            return True
            
        except (ValueError, TypeError):
            messagebox.showerror("Invalid Input", "Please enter valid numbers for dimensions and cost.", parent=self.parent)
            return False


class SlidingDoorFrame(SlidingWindowFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)
        
    def create_specifications(self):
        """Create specifications for SlidingDoor (same as SlidingWindow)"""
        super().create_specifications()
        # Override image
        self.add_product_image("Sliding Door.png")


class FixLouverFrame(BaseProductFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)

    def get_automatic_rate(self, product_type, total_sqft):
        """Get automatic rate for FixLouver from data file"""
        try:
            material = self.global_state.aluMatVar.get()
            if not material:
                return None  # No material selected, require manual entry
                
            data_df = self.data_manager.get_data()
            rate_series = data_df.loc[
                (data_df["Material"] == material) &
                (data_df["Type"] == "louver")
            ]["Rate"]

            if not rate_series.empty:
                return float(rate_series.iloc[0])
            else:
                messagebox.showinfo("Rate Not Found", 
                    f"No rate found for {material} louver. Please enter cost manually.", 
                    parent=self.parent)
                return None
                
        except Exception as e:
            print(f"Error looking up rate for FixLouver: {e}")
            return None

    def create_specifications(self):
        """Create specifications for FixLouver"""
        # Add specifications title
        selectWinLabel = ttk.Label(
            self.frame1, text="Specifications", font=("", 10, "bold")
        )
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        
        # Add product image
        self.add_product_image("Fix Louver.png")
        
        # Create specification labels and widgets
        self.create_louver_specifications()
        
        # Add Next button
        self.add_next_button()

    def create_louver_specifications(self):
        """Create louver-specific specifications"""
        row = 5
        
        # Labels
        labels = [
            ("Aluminium Material", row),
            ("Glass Thickness", row + 1),
            ("Glass Type", row + 2),
            ("Louver Blade", row + 3),
            ("Frame Colour", row + 4),
            ("Silicon", row + 5),
        ]
        
        for label_text, row_num in labels:
            label = ttk.Label(self.frame1, text=label_text)
            label.grid(column=0, row=row_num, padx=10, pady=10, sticky="W")
            
        # Widgets
        # Aluminium Material
        aluMat = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.aluMatVar, 
            width=30, 
            values=self.global_state.aluminium_material
        )
        aluMat.grid(column=1, row=row, padx=10, pady=10, sticky="W")
        aluMat.bind("<Key>", lambda event: self.handleWait(event, aluMat, "aluminium_material"))

        # Glass Thickness
        glaThic = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.glaThicVar, 
            width=30, 
            values=self.global_state.glass_thickness
        )
        glaThic.grid(column=1, row=row + 1, padx=10, pady=10, sticky="W")
        glaThic.bind("<Key>", lambda event: self.handleWait(event, glaThic, "glass_thickness"))

        # Glass Type
        glaTyp = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.glaTypVar, 
            width=30, 
            values=self.global_state.glass_type
        )
        glaTyp.grid(column=1, row=row + 2, padx=10, pady=10, sticky="W")
        glaTyp.bind("<Key>", lambda event: self.handleWait(event, glaTyp, "glass_type"))

        # Louver Blade
        lowBlad = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.lowBladVar, 
            width=30, 
            values=self.global_state.Louver_blade
        )
        lowBlad.grid(column=1, row=row + 3, padx=10, pady=10, sticky="W")
        lowBlad.bind("<Key>", lambda event: self.handleWait(event, lowBlad, "Louver_blade"))

        # Frame Colour
        fraCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.fraColVar, 
            width=30, 
            values=self.global_state.frame_colour
        )
        fraCol.grid(column=1, row=row + 4, padx=10, pady=10, sticky="W")
        fraCol.bind("<Key>", lambda event: self.handleWait(event, fraCol, "frame_colour"))

        # Silicon Colour
        silCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.silColVar, 
            width=30, 
            values=self.global_state.silicon_colour
        )
        silCol.grid(column=1, row=row + 5, padx=10, pady=10, sticky="W")
        silCol.bind("<Key>", lambda event: self.handleWait(event, silCol, "silicon_colour"))


class PattiLouverFrame(FixLouverFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)
        
    def get_automatic_rate(self, product_type, total_sqft):
        """Get automatic rate for PattiLouver from data file"""
        try:
            material = self.global_state.aluMatVar.get()
            if not material:
                return None  # No material selected, require manual entry
                
            data_df = self.data_manager.get_data()
            rate_series = data_df.loc[
                (data_df["Material"] == material) &
                (data_df["Type"] == "patti")
            ]["Rate"]

            if not rate_series.empty:
                return float(rate_series.iloc[0])
            else:
                messagebox.showinfo("Rate Not Found", 
                    f"No rate found for {material} patti. Please enter cost manually.", 
                    parent=self.parent)
                return None
                
        except Exception as e:
            print(f"Error looking up rate for PattiLouver: {e}")
            return None
        
    def create_specifications(self):
        """Create specifications for PattiLouver (same as FixLouver but different image)"""
        super().create_specifications()
        # Override image
        self.add_product_image("Patti Louver.png")


class OpenableWindowFrame(BaseProductFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)

    def get_automatic_rate(self, product_type, total_sqft):
        """Get automatic rate for OpenableWindow from data file"""
        try:
            material = self.global_state.aluMatVar.get()
            glass_thickness = self.global_state.glaThicVar.get()
            
            if not material or not glass_thickness:
                return None  # Missing required fields, require manual entry
                
            data_df = self.data_manager.get_data()
            rate_series = data_df.loc[
                (data_df["Material"] == material) &
                (data_df["Type"] == "openable") &
                (data_df["SubType"] == glass_thickness)
            ]["Rate"]

            if not rate_series.empty:
                return float(rate_series.iloc[0])
            else:
                messagebox.showinfo("Rate Not Found", 
                    f"No rate found for {material} openable window with {glass_thickness} glass. Please enter cost manually.", 
                    parent=self.parent)
                return None
                
        except Exception as e:
            print(f"Error looking up rate for OpenableWindow: {e}")
            return None

    def create_specifications(self):
        """Create specifications for OpenableWindow"""
        # Add specifications title
        selectWinLabel = ttk.Label(
            self.frame1, text="Specifications", font=("", 10, "bold")
        )
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        
        # Add product image
        self.add_product_image("Openable Window.png")
        
        # Create specification labels and widgets
        self.create_openable_specifications()
        
        # Add Next button
        self.add_next_button()

    def create_openable_specifications(self):
        """Create openable window specifications"""
        row = 5
        
        # Labels
        labels = [
            ("Aluminium Material", row),
            ("Glass Thickness", row + 1),
            ("Glass Type", row + 2),
            ("Handle", row + 3),
            ("Hardware", row + 4),
            ("Frame Colour", row + 5),
            ("Silicon", row + 6),
        ]
        
        for label_text, row_num in labels:
            label = ttk.Label(self.frame1, text=label_text)
            label.grid(column=0, row=row_num, padx=10, pady=10, sticky="W")
            
        # Widgets
        # Aluminium Material
        aluMat = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.aluMatVar, 
            width=30, 
            values=self.global_state.aluminium_material
        )
        aluMat.grid(column=1, row=row, padx=10, pady=10, sticky="W")
        aluMat.bind("<Key>", lambda event: self.handleWait(event, aluMat, "aluminium_material"))

        # Glass Thickness
        glaThic = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.glaThicVar, 
            width=30, 
            values=self.global_state.glass_thickness
        )
        glaThic.grid(column=1, row=row + 1, padx=10, pady=10, sticky="W")
        glaThic.bind("<Key>", lambda event: self.handleWait(event, glaThic, "glass_thickness"))

        # Glass Type
        glaTyp = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.glaTypVar, 
            width=30, 
            values=self.global_state.glass_type
        )
        glaTyp.grid(column=1, row=row + 2, padx=10, pady=10, sticky="W")
        glaTyp.bind("<Key>", lambda event: self.handleWait(event, glaTyp, "glass_type"))

        # Handle
        handle = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.handleVar, 
            width=30, 
            values=self.global_state.handle_options
        )
        handle.grid(column=1, row=row + 3, padx=10, pady=10, sticky="W")
        handle.bind("<Key>", lambda event: self.handleWait(event, handle, "handle_options"))

        # Hardware (Entry field as in legacy)
        hardwa = tk.Entry(
            self.frame1, 
            textvariable=self.global_state.hardwaVar, 
            width=33, 
            relief="solid"
        )
        hardwa.grid(column=1, row=row + 4, padx=10, pady=10, sticky="W")

        # Frame Colour
        fraCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.fraColVar, 
            width=30, 
            values=self.global_state.frame_colour
        )
        fraCol.grid(column=1, row=row + 5, padx=10, pady=10, sticky="W")
        fraCol.bind("<Key>", lambda event: self.handleWait(event, fraCol, "frame_colour"))

        # Silicon Colour
        silCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.silColVar, 
            width=30, 
            values=self.global_state.silicon_colour
        )
        silCol.grid(column=1, row=row + 6, padx=10, pady=10, sticky="W")
        silCol.bind("<Key>", lambda event: self.handleWait(event, silCol, "silicon_colour"))


class SlidingFoldingDoorFrame(SlidingWindowFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)
        
    def create_specifications(self):
        """Create specifications for SlidingFoldingDoor (same as SlidingWindow)"""
        super().create_specifications()
        # Override image
        self.add_product_image("Sliding folding door.png")


class CasementWindowFrame(SlidingWindowFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)
        
    def create_specifications(self):
        """Create specifications for CasementWindow (same as SlidingWindow)"""
        super().create_specifications()
        # Override image
        self.add_product_image("Casement Window.png")


class AluminiumPartitionFrame(BaseProductFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)

    def create_specifications(self):
        """Create specifications for AluminiumPartition"""
        # Add specifications title
        selectWinLabel = ttk.Label(
            self.frame1, text="Specifications", font=("", 10, "bold")
        )
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        
        # Add product image
        self.add_product_image("Aluminium partition.png")
        
        # Create specification labels and widgets
        self.create_partition_specifications()
        
        # Add Next button
        self.add_next_button()

    def create_partition_specifications(self):
        """Create aluminium partition specifications"""
        row = 5
        
        # Labels
        labels = [
            ("Aluminium Material", row),
            ("Acrylic Sheet Colour", row + 1),
            ("Masking Tape Colour", row + 2),
            ("Silicon Colour", row + 3),
        ]
        
        for label_text, row_num in labels:
            label = ttk.Label(self.frame1, text=label_text)
            label.grid(column=0, row=row_num, padx=10, pady=10, sticky="W")
            
        # Widgets
        # Aluminium Material
        aluMat = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.aluMatVar, 
            width=30, 
            values=self.global_state.aluminium_material
        )
        aluMat.grid(column=1, row=row, padx=10, pady=10, sticky="W")
        aluMat.bind("<Key>", lambda event: self.handleWait(event, aluMat, "aluminium_material"))

        # Acrylic Sheet Colour
        acrShe = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.acrSheVar, 
            width=30, 
            values=self.global_state.acrylic_options
        )
        acrShe.grid(column=1, row=row + 1, padx=10, pady=10, sticky="W")
        acrShe.bind("<Key>", lambda event: self.handleWait(event, acrShe, "acrylic_options"))

        # Masking Tape Colour
        maskTap = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.maskTapVar, 
            width=30, 
            values=self.global_state.masktape_options
        )
        maskTap.grid(column=1, row=row + 2, padx=10, pady=10, sticky="W")
        maskTap.bind("<Key>", lambda event: self.handleWait(event, maskTap, "masktape_options"))

        # Silicon Colour
        silCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.silColVar, 
            width=30, 
            values=self.global_state.silicon_colour
        )
        silCol.grid(column=1, row=row + 3, padx=10, pady=10, sticky="W")
        silCol.bind("<Key>", lambda event: self.handleWait(event, silCol, "silicon_colour"))


class ToughenedPartitionFrame(BaseProductFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)

    def create_specifications(self):
        """Create specifications for ToughenedPartition"""
        # Add specifications title
        selectWinLabel = ttk.Label(
            self.frame1, text="Specifications", font=("", 10, "bold")
        )
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        
        # Add product image
        self.add_product_image("Toughened partition.png")
        
        # Create specification labels and widgets
        self.create_toughened_specifications()
        
        # Add Next button
        self.add_next_button()

    def create_toughened_specifications(self):
        """Create toughened partition specifications"""
        row = 5
        
        # Labels
        labels = [
            ("Glass Thickness", row),
            ("Silicon Colour", row + 1),
        ]
        
        for label_text, row_num in labels:
            label = ttk.Label(self.frame1, text=label_text)
            label.grid(column=0, row=row_num, padx=10, pady=10, sticky="W")
            
        # Widgets
        # Glass Thickness
        glaThic = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.glaThicVar, 
            width=30, 
            values=self.global_state.glass_thickness
        )
        glaThic.grid(column=1, row=row, padx=10, pady=10, sticky="W")
        glaThic.bind("<Key>", lambda event: self.handleWait(event, glaThic, "glass_thickness"))

        # Silicon Colour
        silCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.silColVar, 
            width=30, 
            values=self.global_state.silicon_colour
        )
        silCol.grid(column=1, row=row + 1, padx=10, pady=10, sticky="W")
        silCol.bind("<Key>", lambda event: self.handleWait(event, silCol, "silicon_colour"))


class ToughenedDoorFrame(ToughenedPartitionFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)
        
    def create_specifications(self):
        """Create specifications for ToughenedDoor (same as ToughenedPartition)"""
        super().create_specifications()
        # Override image
        self.add_product_image("Toughened Door.png")


class CompositePanelFrame(BaseProductFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)

    def create_specifications(self):
        """Create specifications for CompositePanel"""
        # Add specifications title
        selectWinLabel = ttk.Label(
            self.frame1, text="Specifications", font=("", 10, "bold")
        )
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        
        # Add product image
        self.add_product_image("Composite pannel.png")
        
        # Create specification labels and widgets
        self.create_composite_specifications()
        
        # Add Next button
        self.add_next_button()

    def create_composite_specifications(self):
        """Create composite panel specifications"""
        row = 5
        
        # Labels
        labels = [
            ("Composite Sheet Colour", row),
            ("Masking Tape Colour", row + 1),
            ("Silicon Colour", row + 2),
        ]
        
        for label_text, row_num in labels:
            label = ttk.Label(self.frame1, text=label_text)
            label.grid(column=0, row=row_num, padx=10, pady=10, sticky="W")
            
        # Widgets
        # Composite Sheet Colour
        compShe = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.compSheVar, 
            width=30, 
            values=self.global_state.composite_options
        )
        compShe.grid(column=1, row=row, padx=10, pady=10, sticky="W")
        compShe.bind("<Key>", lambda event: self.handleWait(event, compShe, "composite_options"))

        # Masking Tape Colour
        maskTap = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.maskTapVar, 
            width=30, 
            values=self.global_state.masktape_options
        )
        maskTap.grid(column=1, row=row + 1, padx=10, pady=10, sticky="W")
        maskTap.bind("<Key>", lambda event: self.handleWait(event, maskTap, "masktape_options"))

        # Silicon Colour
        silCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.silColVar, 
            width=30, 
            values=self.global_state.silicon_colour
        )
        silCol.grid(column=1, row=row + 2, padx=10, pady=10, sticky="W")
        silCol.bind("<Key>", lambda event: self.handleWait(event, silCol, "silicon_colour"))


class CurtainWallFrame(ToughenedPartitionFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)
        
    def create_specifications(self):
        """Create specifications for CurtainWall (same as ToughenedPartition)"""
        super().create_specifications()
        # Override image
        self.add_product_image("Curtain wall.png")


class FixWindowFrame(SlidingWindowFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)
        
    def create_specifications(self):
        """Create specifications for FixWindow (same as SlidingWindow)"""
        super().create_specifications()
        # Override image
        self.add_product_image("Fix Window.png")


class ExhaustFanWindowFrame(BaseProductFrame):
    def __init__(self, parent, data_manager):
        super().__init__(parent, data_manager)

    def create_specifications(self):
        """Create specifications for ExhaustFanWindow"""
        # Add specifications title
        selectWinLabel = ttk.Label(
            self.frame1, text="Specifications", font=("", 10, "bold")
        )
        selectWinLabel.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        
        # Add product image
        self.add_product_image("Exhaust Fan Window.png")
        
        # Create specification labels and widgets
        self.create_exhaust_specifications()
        
        # Add Next button
        self.add_next_button()

    def create_exhaust_specifications(self):
        """Create exhaust fan window specifications"""
        row = 5
        
        # Labels
        labels = [
            ("Aluminium Material", row),
            ("Glass Thickness", row + 1),
            ("Glass Type", row + 2),
            ("ACP Sheet", row + 3),
            ("Frame Colour", row + 4),
            ("Silicon", row + 5),
        ]
        
        for label_text, row_num in labels:
            label = ttk.Label(self.frame1, text=label_text)
            label.grid(column=0, row=row_num, padx=10, pady=10, sticky="W")
            
        # Widgets
        # Aluminium Material
        aluMat = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.aluMatVar, 
            width=30, 
            values=self.global_state.aluminium_material
        )
        aluMat.grid(column=1, row=row, padx=10, pady=10, sticky="W")
        aluMat.bind("<Key>", lambda event: self.handleWait(event, aluMat, "aluminium_material"))

        # Glass Thickness
        glaThic = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.glaThicVar, 
            width=30, 
            values=self.global_state.glass_thickness
        )
        glaThic.grid(column=1, row=row + 1, padx=10, pady=10, sticky="W")
        glaThic.bind("<Key>", lambda event: self.handleWait(event, glaThic, "glass_thickness"))

        # Glass Type
        glaTyp = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.glaTypVar, 
            width=30, 
            values=self.global_state.glass_type
        )
        glaTyp.grid(column=1, row=row + 2, padx=10, pady=10, sticky="W")
        glaTyp.bind("<Key>", lambda event: self.handleWait(event, glaTyp, "glass_type"))

        # ACP Sheet
        acpShe = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.acpSheVar, 
            width=30, 
            values=self.global_state.acpsheet_options
        )
        acpShe.grid(column=1, row=row + 3, padx=10, pady=10, sticky="W")
        acpShe.bind("<Key>", lambda event: self.handleWait(event, acpShe, "acpsheet_options"))

        # Frame Colour
        fraCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.fraColVar, 
            width=30, 
            values=self.global_state.frame_colour
        )
        fraCol.grid(column=1, row=row + 4, padx=10, pady=10, sticky="W")
        fraCol.bind("<Key>", lambda event: self.handleWait(event, fraCol, "frame_colour"))

        # Silicon Colour
        silCol = ttk.Combobox(
            self.frame1, 
            textvariable=self.global_state.silColVar, 
            width=30, 
            values=self.global_state.silicon_colour
        )
        silCol.grid(column=1, row=row + 5, padx=10, pady=10, sticky="W")
        silCol.bind("<Key>", lambda event: self.handleWait(event, silCol, "silicon_colour"))
