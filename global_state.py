import tkinter as tk


class GlobalState:
    """
    Global state management for Window Quotation Application
    Ports all legacy global variables and options from MGA Window Quotaion.py
    """
    
    def __init__(self):
        # Initialize all legacy global variables
        self._init_basic_variables()
        self._init_specification_variables()
        self._init_calculation_variables()
        self._init_customer_variables()
        self._init_options()
        
    def _init_basic_variables(self):
        """Initialize basic window dimension and type variables"""
        self.Width = tk.StringVar()
        self.Height = tk.StringVar()
        self.windowTypeVar = tk.StringVar()
        
    def _init_specification_variables(self):
        """Initialize all product specification variables"""
        # Track and material specifications
        self.trackVar = tk.StringVar()
        self.aluMatVar = tk.StringVar()
        
        # Glass specifications  
        self.glaThicVar = tk.StringVar()
        self.glaTypVar = tk.StringVar()
        
        # Hardware specifications
        self.hardLocVar = tk.StringVar()
        self.hardBeaVar = tk.StringVar()
        self.handleVar = tk.StringVar()
        self.hardwaVar = tk.StringVar()
        
        # Rubber specifications
        self.rubbTypVar = tk.StringVar()
        self.rubbThicVar = tk.StringVar()
        
        # Other components
        self.woolFileVar = tk.IntVar()
        self.aluNetVar = tk.StringVar()
        self.fraColVar = tk.StringVar()
        self.silColVar = tk.StringVar()
        
        # Screw variables (6 checkboxes as in legacy)
        self.screwVar1 = tk.IntVar()
        self.screwVar2 = tk.IntVar()
        self.screwVar3 = tk.IntVar()
        self.screwVar4 = tk.IntVar()
        self.screwVar5 = tk.IntVar()
        self.screwVar6 = tk.IntVar()
        
        # Louver and partition specific
        self.lowBladVar = tk.StringVar()
        self.acrSheVar = tk.StringVar()
        self.compSheVar = tk.StringVar()
        self.maskTapVar = tk.StringVar()
        self.acpSheVar = tk.StringVar()
        
    def _init_calculation_variables(self):
        """Initialize cost calculation variables"""
        self.totSqftEntVar = tk.StringVar()
        self.cstAmtInr = tk.StringVar()
        self.costEntVar = tk.StringVar()
        self.instEntVar = tk.StringVar()
        self.discountEntVar = tk.StringVar()
        self.gstEntVar = tk.StringVar()
        
        # Total calculation variables
        self.costTotVar = tk.StringVar()
        self.instTotVar = tk.StringVar()
        self.discTotVar = tk.StringVar()
        self.gstTotVar = tk.StringVar()
        
        # State flags
        self.finalCost = 0
        self.quantity = 1
        self.profitAmnt = 0
        self.calculateFlag = False
        self.calcQuantFlag = False
        self.discFlag = False
        self.pressedCalcFlag = False
        
    def _init_customer_variables(self):
        """Initialize customer detail variables"""
        self.custNamVar = tk.StringVar()
        self.custAddVar = tk.StringVar()
        self.custConVar = tk.StringVar()
        self.address = ""
        self.custName = None
        
    def _init_options(self):
        """Initialize all option lists exactly as legacy"""
        # Window options
        self.window_options = [
            "Sliding Window",
            "Sliding Door", 
            "Fix Louver",
            "Patti Louver",
            "Openable Window",
            "Sliding folding door",
            "Casement Window",
            "Aluminium partition",
            "Toughened partition",
            "Toughened Door",
            "Composite pannel",
            "Curtain wall",
            "Fix Window",
            "Exhaust Fan Window",
        ]
        
        # Track options
        self.track_options = ["2 Track", "3 Track", "4 Track"]
        
        # Material options
        self.aluminium_material = [
            "Regular Section",
            "Domal Section (JINDAL)",
            "UPVC Section", 
            "Profile Aluminium Section",
        ]
        
        # Glass options
        self.glass_thickness = ["3.5mm", "4mm", "5mm", "8mm", "12mm"]
        self.glass_type = ["Plain", "Frosted", "One-way", "Tinted", "Bajra"]
        
        # Hardware options
        self.hardware_lock = ["3/4th inch", "1 inch", "Domal full metal body (ARIES)"]
        self.hardware_bear = ["3/4th inch", "1 inch", "Domal teflon bearing (ARIES)"]
        self.handle_options = ["C Type", "S Type"]
        
        # Rubber options
        self.rubber_type = ["Clear", "Jumbo", "Powder Jumbo"]
        self.rubber_thick = ["4mm", "5mm"]
        
        # Other component options
        self.aluminium_net = ["14 x 14 Aluminium net", "Fiber Net"]
        self.frame_colour = ["Black", "White", "Ivory", "Brown"]
        self.silicon_colour = ["Black", "Clear", "White"]
        
        # Louver and partition options
        self.Louver_blade = [str(i) for i in range(3, 13)]
        self.acrylic_options = ["Black", "White", "Ivory", "Brown"]
        self.composite_options = ["Black", "White", "Ivory"]
        self.masktape_options = ["Red", "Green"]
        self.acpsheet_options = ["Black", "White", "Ivory"]
        
        # Create options dictionary exactly as legacy
        self.options = {
            "track_options": self.track_options,
            "aluminium_material": self.aluminium_material,
            "glass_thickness": self.glass_thickness,
            "glass_type": self.glass_type,
            "hardware_lock": self.hardware_lock,
            "hardware_bear": self.hardware_bear,
            "rubber_type": self.rubber_type,
            "rubber_thick": self.rubber_thick,
            "aluminium_net": self.aluminium_net,
            "frame_colour": self.frame_colour,
            "silicon_colour": self.silicon_colour,
            "Louver_blade": self.Louver_blade,
            "handle_options": self.handle_options,
            "acrylic_options": self.acrylic_options,
            "composite_options": self.composite_options,
            "masktape_options": self.masktape_options,
            "acpsheet_options": self.acpsheet_options,
        }
        
        # Legacy validation pattern
        self.digVerify = "1234567890.,"
        
        # Product image ratios (width, height) as in legacy
        self.ratio = {
            "Sliding Window": [45, 40],
            "Sliding Door": [45, 41],
            "Fix Louver": [40, 48],
            "Patti Louver": [40, 48],
            "Openable Window": [45, 43.5],
            "Sliding folding door": [45, 36],
            "Casement Window": [40, 48],
            "Aluminium partition": [45, 36],
            "Toughened partition": [45, 36],
            "Toughened Door": [45, 45],
            "Composite pannel": [45, 36],
            "Curtain wall": [45, 36],
            "Fix Window": [45, 45],
            "Exhaust Fan Window": [45, 49.5],
        }
        
    def get_all_specification_vars(self):
        """Return dictionary of all specification variables for easy access"""
        return {
            'trackVar': self.trackVar,
            'aluMatVar': self.aluMatVar,
            'glaThicVar': self.glaThicVar,
            'glaTypVar': self.glaTypVar,
            'hardLocVar': self.hardLocVar,
            'hardBeaVar': self.hardBeaVar,
            'rubbTypVar': self.rubbTypVar,
            'rubbThicVar': self.rubbThicVar,
            'woolFileVar': self.woolFileVar,
            'aluNetVar': self.aluNetVar,
            'fraColVar': self.fraColVar,
            'silColVar': self.silColVar,
            'screwVar1': self.screwVar1,
            'screwVar2': self.screwVar2,
            'screwVar3': self.screwVar3,
            'screwVar4': self.screwVar4,
            'screwVar5': self.screwVar5,
            'screwVar6': self.screwVar6,
            'lowBladVar': self.lowBladVar,
            'handleVar': self.handleVar,
            'acrSheVar': self.acrSheVar,
            'hardwaVar': self.hardwaVar,
            'compSheVar': self.compSheVar,
            'maskTapVar': self.maskTapVar,
            'acpSheVar': self.acpSheVar,
        }
        
    def reset_specification_vars(self):
        """Reset all specification variables to empty/default values"""
        spec_vars = self.get_all_specification_vars()
        for var_name, var in spec_vars.items():
            if isinstance(var, tk.IntVar):
                var.set(0)
            else:
                var.set("")
                
    def validate_digits(self, value):
        """Legacy checkDigits equivalent - validate numeric input"""
        if not value:
            return False
        return all(c in self.digVerify for c in value)


# Global instance (singleton pattern)
_global_state = None

def get_global_state():
    """Get the singleton global state instance"""
    global _global_state
    if _global_state is None:
        _global_state = GlobalState()
    return _global_state 