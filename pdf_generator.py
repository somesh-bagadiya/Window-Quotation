from fpdf import FPDF
from datetime import date
from babel.numbers import format_currency
from num2words import num2words
import pandas as pd
import os

# --- Constants ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "Images")

# Image dimensions for PDF output
SlidingWindowWidth = 45
SlidingWindowHeight = 55
SilidingDoorWidth = 45
SilidingDoorHeight = 55
FixLouverWidth = 40
FixLouverHeight = 55
PattiLouverWidth = 40
PattiLouverHeight = 55
OpenableWindowWidth = 45
OpenableWindowHeight = 55
SlidingfoldingdoorWidth = 45
SlidingfoldingdoorHeight = 55
CasementWindowWidth = 40
CasementWindowHeight = 55
AluminiumpartitionWidth = 45
AluminiumpartitionHeight = 55
CompositepannelWidth = 45
CompositepannelHeight = 55
CurtainwallWidth = 45
CurtainwallHeight = 55
FixWindowWidth = 45
FixWindowHeight = 55
ExhaustFanWindowWidth = 45
ExhaustFanWindowHeight = 55

RATIO = {
    "Sliding Window": [SlidingWindowWidth, SlidingWindowHeight],
    "Sliding Door": [SilidingDoorWidth, SilidingDoorHeight],
    "Fix Louver": [FixLouverWidth, FixLouverHeight],
    "Patti Louver": [PattiLouverWidth, PattiLouverHeight],
    "Openable Window": [OpenableWindowWidth, OpenableWindowHeight],
    "Sliding folding door": [SlidingfoldingdoorWidth, SlidingfoldingdoorHeight],
    "Casement Window": [CasementWindowWidth, CasementWindowHeight],
    "Aluminium partition": [AluminiumpartitionWidth, AluminiumpartitionHeight],
    "Toughened partition": [AluminiumpartitionWidth, AluminiumpartitionHeight],
    "Toughened Door": [AluminiumpartitionWidth, AluminiumpartitionHeight],
    "Composite pannel": [CompositepannelWidth, CompositepannelHeight],
    "Curtain wall": [CurtainwallWidth, CurtainwallHeight],
    "Fix Window": [FixWindowWidth, FixWindowHeight],
    "Exhaust Fan Window": [ExhaustFanWindowWidth, ExhaustFanWindowHeight],
}

VAR_NAME = {
    "trackVar": "Type",
    "aluMatVar": "Aluminium Material",
    "glaThicVar": "Glass Thickness",
    "glaTypVar": "Glass Type",
    "hardLocVar": "Hardware Lock",
    "hardBeaVar": "Hardware Bearing",
    "rubbTypVar": "Rubber Type",
    "rubbThicVar": "Rubber Thickness",
    "woolFileVar": "Wool File",
    "aluNetVar": "Aluminium Net",
    "fraColVar": "Frame Colour",
    "silColVar": "Silicon",
    "lowBladVar": "Louver Blade",
    "handleVar": "Handle",
    "acrSheVar": "Acrylic Sheet Colour",
    "hardwaVar": "Hardware",
    "compSheVar": "Composite Sheet Colour",
    "maskTapVar": "Masking Tape Colour",
    "acpSheVar": "ACP Sheet",
}


# --- Public API ---


def create_quotation_pdf(filename, customer_details, cart_items, final_costs):
    """
    Generates a quotation PDF.

    Args:
        filename (str): The path to save the PDF file.
        customer_details (dict): A dictionary with customer information.
        cart_items (pd.DataFrame): A DataFrame with the items in the cart.
        final_costs (dict): A dictionary with the final calculated costs.
    """
    pdf = PDF(customer_details, cart_items, final_costs)
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.driver_code()
    pdf.output(filename)
    print(f"PDF '{filename}' generated successfully.")


# --- PDF Generation Class ---


class PDF(FPDF):

    fileName = None
    printDoneFlag = False

    def __init__(self, customer_details, cart_items, final_costs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer_details = customer_details
        self.cart_items = cart_items
        self.final_costs = final_costs
        self.print_done_flag = False
        
        # Use custom date if provided, otherwise use today's date
        if "quotation_date" in final_costs and final_costs["quotation_date"]:
            self.today = final_costs["quotation_date"].date()
        else:
            self.today = date.today()
            
        # A unique quotation number can be generated here or passed in
        if "quotation_number" in final_costs and final_costs["quotation_number"]:
            self.quotation_number = final_costs["quotation_number"]
        else:
            self.quotation_number = (
                f"QUO/{self.today.strftime('%d%m-%Y')}/{pd.Timestamp.now().microsecond}"
            )

            

    def header(self):
        self.set_font("helvetica", "B", 15)

    def footer(self):
        self.set_y(-17)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(169, 169, 169)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

        self.set_y(-12)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(169, 169, 169)
        self.cell(
            0,
            10,
            "All Images shown are Illustrations, not actual product and not upto scale. Actual product may vary.",
            align="C",
        )

    def driver_code(self):
        self.homePage()

        # Column X positions
        design_x = 27
        specs_x = 92
        cost_x = 137
        quantity_x = 157
        amount_x = 167

        for i, row in self.cart_items.iterrows():
            # Check if a full item block fits, if not, create a new page
            if self.get_y() + 90 > self.page_break_trigger:
                self.new_page()

            current_y = self.get_y()
            self.print_in_pdf(
                current_y, design_x, specs_x, cost_x, quantity_x, amount_x, row
            )

        self.total_display()
        self.pdf_end()

    def homePage(self):
        # Add MGA logo and company header section (matching legacy exactly)
        try:
            self.image(os.path.join(IMAGE_DIR, "MGA_1.png"), x=20, y=10, w=55, h=35.9)
        except Exception as e:
            print(f"Logo image not found: {e}")
            # Add placeholder text if logo image not found
            self.set_y(10)
            self.set_x(20)
            self.set_font("helvetica", "B", 16)
            self.cell(w=55, h=35.9, txt="MGA WINDOWS", align="C", border=1)
        
        # Vertical separator line
        self.line(85, 6, 85, 48)
        
        # Company contact icons and information (matching legacy layout)
        try:
            # Maps icon with link
            self.image(
                os.path.join(IMAGE_DIR, "Mapslogo.png"),
                x=95,
                y=12,
                w=5,
                h=7,
                link="https://www.google.com/maps/place/Madhav+Glass+and+Aluminium/@19.8758195,75.3916281,18.5z/data=!4m5!3m4!1s0x0:0x6466e4a2d6fec24c!8m2!3d19.8759565!4d75.3913081",
            )
            # Phone icon
            self.image(os.path.join(IMAGE_DIR, "PhoneIcon.png"), x=95, y=24, w=5, h=5)
            # Email icon
            self.image(os.path.join(IMAGE_DIR, "EmailIcon.png"), x=95, y=35, w=5, h=3.8)
        except Exception as e:
            print(f"Contact icons not found: {e}")

        # Company address with link
        self.set_y(15)
        self.set_x(102)
        self.set_font("helvetica", "", 8)
        self.cell(
            w=0,
            txt="Chikalthana MIDC, Opp Ajantha Pharma, Aurangabad - 431001",
            link="https://www.google.com/maps/place/Madhav+Glass+and+Aluminium/@19.8758195,75.3916281,18.5z/data=!4m5!3m4!1s0x0:0x6466e4a2d6fec24c!8m2!3d19.8759565!4d75.3913081",
        )

        # Phone numbers
        self.set_y(27)
        self.set_x(102)
        self.cell(w=0, txt="7875115371, 8149440829")

        # Email address
        self.set_y(37)
        self.set_x(102)
        self.cell(w=0, txt="madhavglassandaluminium@gmail.com")

        # Horizontal separator lines
        self.line(15, 52, 195, 52)
        self.dashed_line(15, 53, 195, 53)

        # Date section (right side)
        self.set_y(60)
        self.set_x(170)
        self.set_font("helvetica", "B", 8)
        self.cell(w=0, txt="Date:")

        self.set_y(60.1)
        self.set_x(179)
        self.set_font("helvetica", "", 9)
        self.cell(w=0, txt=f"{self.today.day}/{self.today.month}/{self.today.year}")

        # Quotation number section (right side)
        self.set_y(67)
        self.set_x(140)
        self.set_font("helvetica", "B", 8)
        self.cell(w=0, txt="Quotation Number: ")

        wi = self.get_string_width("Quotation Number: ")

        self.set_y(67)
        self.set_x(140 + wi)
        self.set_font("helvetica", "", 9)
        self.cell(w=0, txt=self.quotation_number)

        # Customer details section (left side)
        self.set_y(60)
        self.set_x(15)
        self.set_font("helvetica", "B", 8)
        self.cell(w=0, txt="To,")

        self.set_y(67)
        self.set_x(15)
        self.set_font("helvetica", "B", 8)
        self.cell(w=0, txt=f"{self.customer_details.get('custNamVar', '')}")

        self.set_y(70)
        self.set_x(15)
        self.set_font("helvetica", "B", 8)
        self.multi_cell(
            w=60, h=3.5, txt=f"{self.customer_details.get('custAddVar', '')}"
        )

        self.ln(h=7)
        title_level_y = self.get_y()
        self.draw_lines_home(title_level_y, 10)  # Draw header lines

        # Table Header
        headers = [
            ("Sr.No", 12),
            ("DESIGN", 65),
            ("SPECIFICATIONS", 45),
            ("RATE", 20),
            ("QTY", 10),
            ("AMOUNT", 28),
        ]
        self.set_y(title_level_y)
        self.set_x(15)
        self.set_font("helvetica", "B", 8)
        self.set_fill_color(229, 233, 243)
        for header, width in headers:
            self.cell(w=width, h=10, txt=header, fill=True, border=1, align="C")
        self.ln()

    def new_page(self):
        self.add_page()
        title_level_y = self.get_y()
        self.draw_lines_home(title_level_y, 10)  # Draw header lines

        # Table Header
        headers = [
            ("Sr.No", 12),
            ("DESIGN", 65),
            ("SPECIFICATIONS", 45),
            ("RATE", 20),
            ("QTY", 10),
            ("AMOUNT", 28),
        ]
        self.set_y(title_level_y)
        self.set_x(15)
        self.set_font("helvetica", "B", 8)
        self.set_fill_color(229, 233, 243)
        for header, width in headers:
            self.cell(w=width, h=10, txt=header, fill=True, border=1, align="C")
        self.ln()

    def print_in_pdf(
        self, text_level, design_x, specs_x, cost_x, quantity_x, amount_x, item_row
    ):
        key = item_row["Particulars"]

        self.draw_lines(text_level)
        
        # Print Sr.No in the first column with proper vertical centering
        self.set_y(text_level + 5)  # Add some top padding
        self.set_x(15)
        self.set_font("helvetica", "B", 8)  # Slightly larger font for better visibility
        self.cell(w=12, h=10, txt=str(item_row["Sr.No"]), align="C")
        
        self.insert_image(item_row, design_x, text_level)

        # Position product title below the image with better spacing
        if RATIO.get(key) and RATIO[key][0] < 50:
            title_y = text_level + 70  # More space for larger images
        else:
            title_y = text_level + 60  # Standard spacing
        
        self.set_y(title_y)
        self.set_x(design_x)
        self.set_font("helvetica", "B", 7)  # Slightly larger font for product title
        self.cell(w=65, h=8, txt=key, align="C")

        self.print_specs(text_level, specs_x, item_row)

        # Cost column - vertically centered
        self.set_y(text_level + 5)
        self.set_x(cost_x)
        self.set_font("helvetica", "B", 7)
        self.cell(w=20, h=10, txt=str(item_row["Cost (INR)"]), align="C")

        # Quantity column - vertically centered
        self.set_y(text_level + 5)
        self.set_x(quantity_x)
        self.set_font("helvetica", "", 7)
        self.cell(w=10, h=10, txt=str(item_row["Quantity"]), align="C")

        # Amount column - vertically centered
        self.set_y(text_level + 5)
        self.set_x(amount_x)
        self.set_font("helvetica", "B", 7)
        self.cell(w=28, h=10, txt=str(item_row["Amount"]), align="C")
        
        self.ln(90)

    def insert_image(self, item_row, design_x, text_level):
        key = item_row["Particulars"]
        if key not in RATIO:
            print(f"Warning: No ratio information for {key}, skipping image insertion.")
            return

        img_w, img_h = RATIO[key]

        try:
            self.image(
                os.path.join(IMAGE_DIR, f"{key}.png"),
                x=design_x + 7.5,
                y=text_level + 8,  # Start image a bit lower to avoid overlapping
                w=img_w,
                h=img_h,
            )
        except RuntimeError as e:
            print(f"Could not load image for {key}: {e}. Skipping.")
            # Draw a placeholder box instead
            self.rect(design_x + 7.5, text_level + 8, img_w, img_h)
            self.set_xy(design_x + 7.5, text_level + 8 + img_h / 2)
            self.cell(w=img_w, txt="Image not found", align="C")

        # Width dimension text (below image) - with better spacing
        str_width = self.get_string_width(str(item_row["Width"]))
        self.set_y(text_level + 12 + img_h)  # More space below image
        self.set_x(design_x + (65 - str_width) / 2)  # Center in the column
        self.set_font("helvetica", "", 7)  # Slightly larger font
        self.cell(w=str_width + 4, h=4, txt=str(item_row["Width"]), align="C")

        # Height dimension text (left side of image) - with better positioning
        str_height = self.get_string_width(str(item_row["Height"]))
        self.set_y(text_level + 8 + (img_h / 2) - 2)  # Center vertically with image
        self.set_x(design_x + 2)  # Small margin from column edge
        self.set_font("helvetica", "", 7)  # Slightly larger font
        self.cell(w=str_height + 4, h=4, txt=str(item_row["Height"]), align="C")

    def print_specs(self, text_level, specs_x, item_row):
        # Start specifications with some top padding to avoid overlapping
        spec_start_y = text_level + 8
        
        # Print area information first
        self.set_y(spec_start_y)
        self.set_x(specs_x)
        self.set_font("helvetica", "", 7)  # Slightly larger font
        self.set_text_color(0, 0, 0)
        self.cell(w=40, h=4, txt=f"Area: {item_row.get('Total Sq.ft', '')} Sq.Ft.")
        spec_start_y += 6

        # Print each specification with proper spacing
        for key, display_name in VAR_NAME.items():
            if (
                key in item_row
                and item_row[key]
                and str(item_row[key]) not in ["0", "nan", ""]
            ):
                self.set_y(spec_start_y)
                self.set_x(specs_x)
                self.set_font("helvetica", "", 6)
                self.set_text_color(0, 0, 0)
                self.multi_cell(w=40, h=3.5, txt=f"{display_name}: {item_row[key]}")
                spec_start_y = self.get_y() + 1  # Add small gap between specs

    def draw_lines(self, title_level_y):
        # This draws the row lines for a single item
        self.line(15, title_level_y, 195, title_level_y)  # Top
        self.line(15, title_level_y + 89, 195, title_level_y + 89)  # Bottom

        x_coords = [15, 27, 92, 137, 157, 167, 195]
        for x in x_coords:
            self.line(x, title_level_y, x, title_level_y + 89)

    def draw_lines_home(self, title_level_y, no_of_div):
        # This draws the header lines
        self.line(15, title_level_y, 195, title_level_y) # Top
        self.line(15, title_level_y + no_of_div, 195, title_level_y + no_of_div)

        x_coords = [15, 27, 92, 137, 157, 167, 195]
        for x in x_coords:
            self.line(x, title_level_y, x, title_level_y + no_of_div)

    def total_display(self):
        """Display totals exactly as legacy totalDisplay() method"""
        if self.get_y() > 200:  # Threshold to create a new page
            self.add_page()

        y_level = self.get_y()
        
        # Helper function to format currency for PDF (like legacy)
        def format_for_pdf(amount):
            formatted = format_currency(amount, "INR", locale="en_IN").replace("\xa0", " ")
            # Replace rupee symbol with Rs. for PDF compatibility like legacy
            if formatted.startswith('₹'):
                formatted = "Rs. " + formatted[1:]
            return formatted

        # Calculate totals from cart data like legacy
        total_amounts = []
        total_sqft = []
        total_quantities = []
        
        for _, row in self.cart_items.iterrows():
            # Extract amount (remove currency symbols and convert to float)
            amount_str = str(row.get('Amount', '0'))
            if amount_str.startswith('₹'):
                amount_str = amount_str[1:]
            amount = float(amount_str.replace(',', ''))
            total_amounts.append(amount)
            
            # Extract square footage
            sqft = float(row.get('Total Sq.ft', 0))
            total_sqft.append(sqft)
            
            # Extract quantity
            qty = float(row.get('Quantity', 1))
            total_quantities.append(qty)

        cart_total = sum(total_amounts)
        
        # Get discount and installation from final_costs
        discount = self.final_costs.get("discount", 0)
        installation = self.final_costs.get("installation", 0)
        gst_percent = self.final_costs.get("gst_percent", 18)

        # Calculate as legacy: discount applied before GST, installation after GST
        subtotal = cart_total
        after_discount = subtotal - discount
        gst_amount = after_discount * gst_percent / 100
        after_gst = after_discount + gst_amount
        final_total = after_gst + installation

        # Display total area
        wi = self.get_string_width("Total Area: ")
        self.set_y(y_level)
        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=wi + 2, h=6, txt="Total Area: ", align="L")
        
        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=20, h=6, txt="{} Sq.Ft.".format(round(sum(total_sqft), 2)), align="L")

        # Display cart total
        self.set_y(y_level)
        self.set_x(100)
        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=45, h=6, txt="Total", fill=True, border=True, align="C")

        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=10, h=6, txt=" : ", fill=True, border=True, align="C")

        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=40, h=6, txt=format_for_pdf(subtotal), fill=True, border=True, align="C")

        y_level += 6

        # Display total windows
        wi = self.get_string_width("Total Windows: ")
        self.set_y(y_level)
        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=wi, h=6, txt="Total Windows: ", align="L")

        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=20, h=6, txt="{} Nos".format(round(sum(total_quantities), 2)), align="L")

        # Display discount if applicable
        if discount > 0:
            self.set_y(y_level)
            self.set_x(100)
            self.set_font("helvetica", "B", 7)
            self.set_fill_color(229, 233, 243)
            self.cell(w=45, h=7, txt="Discount", fill=True, border=True, align="C")

            self.set_font("helvetica", "B", 7)
            self.set_fill_color(229, 233, 243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align="C")

            self.set_font("helvetica", "B", 7)
            self.set_fill_color(229, 233, 243)
            self.cell(w=40, h=7, txt=format_for_pdf(discount), fill=True, border=True, align="C")

            y_level += 7

        # Display pre-tax total
        self.set_y(y_level)
        self.set_x(100)
        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=45, h=6, txt="Pre-Tax Total", fill=True, border=True, align="C")

        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=10, h=6, txt=" : ", fill=True, border=True, align="C")

        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=40, h=6, txt=format_for_pdf(after_discount), fill=True, border=True, align="C")

        y_level += 6

        # Display CGST @9%
        cgst = after_discount * 9 / 100
        self.set_y(y_level)
        self.set_x(100)
        self.set_font("helvetica", "", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=45, h=7, txt="CGST @9%", fill=True, border=True, align="C")

        self.set_font("helvetica", "", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align="C")

        self.set_font("helvetica", "", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=40, h=7, txt=format_for_pdf(cgst), fill=True, border=True, align="C")

        y_level += 7

        # Display SGST @9%
        sgst = after_discount * 9 / 100
        self.set_y(y_level)
        self.set_x(100)
        self.set_font("helvetica", "", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=45, h=7, txt="SGST @9%", fill=True, border=True, align="C")

        self.set_font("helvetica", "", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align="C")

        self.set_font("helvetica", "", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=40, h=7, txt=format_for_pdf(sgst), fill=True, border=True, align="C")

        y_level += 7

        # Display post-tax total
        self.set_y(y_level)
        self.set_x(100)
        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=45, h=7, txt="Post-Tax Total", fill=True, border=True, align="C")

        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align="C")

        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=40, h=7, txt=format_for_pdf(after_gst), fill=True, border=True, align="C")

        y_level += 7

        # Display installation charges if applicable
        if installation > 0:
            self.set_y(y_level)
            self.set_x(100)
            self.set_font("helvetica", "", 7)
            self.set_fill_color(229, 233, 243)
            self.cell(w=45, h=7, txt="Installation Charges", fill=True, border=True, align="C")

            self.set_font("helvetica", "", 7)
            self.set_fill_color(229, 233, 243)
            self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align="C")

            self.set_font("helvetica", "", 7)
            self.set_fill_color(229, 233, 243)
            self.cell(w=40, h=7, txt=format_for_pdf(installation), fill=True, border=True, align="C")

            y_level += 7

        # Display grand total
        self.set_y(y_level)
        self.set_x(100)
        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=45, h=7, txt="Grand Total", fill=True, border=True, align="C")

        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=10, h=7, txt=" : ", fill=True, border=True, align="C")

        self.set_font("helvetica", "B", 7)
        self.set_fill_color(229, 233, 243)
        self.cell(w=40, h=7, txt=format_for_pdf(final_total), fill=True, border=True, align="C")

        self.set_y(self.get_y() + 15)  # Set endLevel for next section

    def pdf_end(self):
        self.set_y(-45)
        self.set_font("helvetica", "B", 9)
        self.cell(w=0, txt="Terms and Conditions:")

        self.set_y(-40)
        self.set_font("helvetica", "", 7)
        self.multi_cell(
            w=180,
            h=3,
            txt="1. Material once sold will not be taken back or exchanged.\n2. Our responsibility ceases immediately after the goods leave our premises.\n3. Payment should be made by A/C Payee Cheque or Draft in favour of 'Madhav Glass & Aluminium'.\n4. All disputes are subject to Aurangabad Jurisdiction only.",
        )

        self.set_y(-25)
        self.set_x(145)
        self.set_font("helvetica", "B", 9)
        self.cell(w=0, txt="For, Madhav Glass & Aluminium")


# ==============================================================================
# INVOICE PDF GENERATOR
# ==============================================================================


def create_invoice_pdf(
    filename, customer_details, invoice_details, cart_items_with_hsn, final_costs
):
    """
    High-level function to generate the complete invoice PDF exactly as legacy.
    This is the only function that should be called from the UI.
    """
    try:
        pdf = PDFInvoice(
            customer_details=customer_details,
            invoice_details=invoice_details,
            cart_items_with_hsn=cart_items_with_hsn,
            final_costs=final_costs,
            orientation="P",
            unit="mm",
            format="A4",
        )
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # Use legacy-style driver code
        pdf.invoice_driver_code()
        pdf.output(filename)
        
        return True, None
    except Exception as e:
        print(f"Error in create_invoice_pdf: {e}")  # Added for debugging
        return False, str(e)


class PDFInvoice(FPDF):
    def __init__(
        self,
        customer_details,
        invoice_details,
        cart_items_with_hsn,
        final_costs,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.customer_details = customer_details
        self.invoice_details = invoice_details
        self.cart_items = cart_items_with_hsn
        self.final_costs = final_costs
        
        # Use custom date if provided, otherwise use today's date
        if "invoice_date" in invoice_details and invoice_details["invoice_date"]:
            self.today = invoice_details["invoice_date"].date()
        else:
            self.today = date.today()
            
        self.print_count = 0
        self.tax_print_count = 0
        self.end_print_level = 0
        self.amt_sum = 0

    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "TAX INVOICE", align="C")

        # Draw page borders exactly as legacy
        self.line(15, 20, 15, 280)
        self.line(195, 20, 195, 280)
        self.line(15, 20, 195, 20)
        self.line(15, 280, 195, 280)

    def footer(self):
        self.set_y(-17)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, "This is a Computer Generated Invoice.", align="C")

    def draw_lines(self, title_level_y=10):
        """Draw section separator lines exactly as legacy"""
        self.line(105, 20, 105, 65)
        self.line(15, 65, 195, 65)
        self.line(15, 80, 195, 80)
        self.line(15, 95, 195, 95)

        for i in range(1, 4):
            self.line(15 + (60 * i), 65, 15 + (60 * i), 95)

        self.line(15, 96, 195, 96)

    def draw_lines_info(self, print_level):
        """Draw item section lines exactly as legacy"""
        self.line(15, 105, 195, 105)
        self.line(23, 96, 23, print_level)
        self.line(88, 96, 88, print_level)
        self.line(108, 96, 108, print_level)
        self.line(132, 96, 132, print_level)
        self.line(157, 96, 157, print_level)
        self.line(167.5, 96, 167.5, print_level)

    def draw_lines_tax(self, start_tax_level, tax_level):
        """Draw tax section lines exactly as legacy"""
        self.line(40, start_tax_level, 40, tax_level + 7)
        self.line(70, start_tax_level, 70, tax_level + 7)
        self.line(120, start_tax_level, 120, tax_level + 7)
        self.line(170, start_tax_level, 170, tax_level + 7)
        self.line(70, start_tax_level + 8, 170, start_tax_level + 8)
        self.line(90, start_tax_level + 8, 90, tax_level + 7)
        self.line(140, start_tax_level + 8, 140, tax_level + 7)
        self.line(15, start_tax_level + 16, 195, start_tax_level + 16)

    def home_page(self):
        """Create home page layout exactly as legacy"""
        # Seller section (left side)
        self.set_y(23)
        self.set_x(17.5)
        self.set_font("helvetica", "B", 10)
        self.cell(w=12, txt="Seller", align="C")

        self.set_y(30)
        self.set_x(17)
        self.set_font("helvetica", "BI", 8)
        self.cell(w=0, txt="Madhav Glass and Aluminium")

        self.set_y(34)
        self.set_x(17)
        self.set_font("helvetica", "", 8)
        self.cell(
            w=0,
            txt="Chikalthana MIDC, Opp Ajantha Pharma,",
            link="https://www.google.com/maps/place/Madhav+Glass+and+Aluminium/@19.8758195,75.3916281,18.5z/data=!4m5!3m4!1s0x0:0x6466e4a2d6fec24c!8m2!3d19.8759565!4d75.3913081",
        )

        self.set_y(38)
        self.set_x(17)
        self.set_font("helvetica", "", 8)
        self.cell(
            w=0,
            txt="Aurangabad - 431001",
            link="https://www.google.com/maps/place/Madhav+Glass+and+Aluminium/@19.8758195,75.3916281,18.5z/data=!4m5!3m4!1s0x0:0x6466e4a2d6fec24c!8m2!3d19.8759565!4d75.3913081",
        )

        self.set_y(42)
        self.set_x(17)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt="State Name : ")

        wi = self.get_string_width("State Name : ")

        self.set_y(42)
        self.set_x(17 + wi)
        self.set_font("helvetica", "I", 8)
        self.cell(w=0, txt="Maharashtra, Code : 27")

        self.set_y(46)
        self.set_x(17)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt="Contact : ")

        wi = self.get_string_width("Contact : ")

        self.set_y(46)
        self.set_x(17 + wi)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt="7875115371, 8149440829")

        self.set_y(50)
        self.set_x(17)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt="Email-ID : ")

        wi = self.get_string_width("Email-ID : ")

        self.set_y(50)
        self.set_x(17 + wi)
        self.set_font("helvetica", "I", 8)
        self.cell(w=0, txt="madhavglassandaluminium@gmail.com")

        self.set_y(54)
        self.set_x(17)
        self.set_font("helvetica", "B", 8)
        self.cell(w=0, txt="GST Registration No : ")

        wi = self.get_string_width("GST Registration No : ")

        self.set_y(54)
        self.set_x(17 + wi)
        self.set_font("helvetica", "I", 8)
        self.cell(w=0, txt="27CURPB8193C1ZC")

        self.set_y(58)
        self.set_x(17)
        self.set_font("helvetica", "B", 8)
        self.cell(w=0, txt="PAN No : ")

        wi = self.get_string_width("PAN No : ")

        self.set_y(58)
        self.set_x(17 + wi)
        self.set_font("helvetica", "I", 8)
        self.cell(w=0, txt="CURPB8193C")

        # Buyer section (right side) - Fixed spacing
        self.set_y(23)
        self.set_x(107)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="Buyer")

        self.set_y(30)
        self.set_x(107)
        self.set_font("helvetica", "BI", 8)
        self.cell(w=0, txt=f"{self.customer_details.get('custNamVar', '')}")

        # Customer address with proper spacing
        self.set_y(34)
        self.set_x(107)
        self.set_font("helvetica", "", 8)
        self.multi_cell(w=70, h=4, txt=f"{self.customer_details.get('custAddVar', '')}")
        
        # Get current Y position after address and add spacing
        address_end_y = self.get_y()
        contact_y = address_end_y + 2  # Add 2mm spacing after address

        # Contact information with proper positioning
        self.set_y(contact_y)
        self.set_x(107)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt="Contact : ")

        wi = self.get_string_width("Contact : ")
        self.set_y(contact_y)
        self.set_x(107 + wi)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt=f"{self.customer_details.get('custConVar', '')}")

        # GST Registration with proper spacing
        gst_y = contact_y + 4
        self.set_y(gst_y)
        self.set_x(107)
        self.set_font("helvetica", "B", 8)
        self.cell(w=0, txt="GST Registration No : ")

        wi = self.get_string_width("GST Registration No : ")
        self.set_y(gst_y)
        self.set_x(107 + wi)
        self.set_font("helvetica", "I", 8)
        self.cell(w=0, txt=f"{self.invoice_details.get('custGstVar', '')}")

        # PAN Number with proper spacing
        pan_y = gst_y + 4
        self.set_y(pan_y)
        self.set_x(107)
        self.set_font("helvetica", "B", 8)
        self.cell(w=0, txt="PAN No : ")

        wi = self.get_string_width("PAN No : ")
        self.set_y(pan_y)
        self.set_x(107 + wi)
        self.set_font("helvetica", "I", 8)
        self.cell(w=0, txt=f"{self.invoice_details.get('custPanVar', '')}")

        # Invoice details section
        self.set_y(67)
        self.set_x(17)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="Invoice No.")

        self.set_y(73)
        self.set_x(17)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt=f"{self.invoice_details.get('invNumbVar', '')}")

        self.set_y(67)
        self.set_x(77)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="Quotation No.")

        self.set_y(73)
        self.set_x(77)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt=f"{self.invoice_details.get('quotNumbVar', '')}")

        self.set_y(67)
        self.set_x(137)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="Date")

        self.set_y(73)
        self.set_x(137)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt=f"{self.today.day}/{self.today.month}/{self.today.year}")

        self.set_y(82)
        self.set_x(17)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="Mode/Terms of Payment")

        self.set_y(88)
        self.set_x(17)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt=f"{self.invoice_details.get('modeTermVar', '')}")

        self.set_y(82)
        self.set_x(77)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="Terms of Delivery")

        self.set_y(88)
        self.set_x(77)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt=f"{self.invoice_details.get('termOfDelVar', '')}")

        self.set_y(82)
        self.set_x(137)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="Destination")

        self.set_y(88)
        self.set_x(137)
        self.set_font("helvetica", "", 8)
        self.cell(w=0, txt=f"{self.invoice_details.get('destinVar', '')}")

        self.draw_lines()

    def info_section_title(self):
        """Create item section headers exactly as legacy"""
        self.set_y(97.5)
        self.set_x(15.5)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="Sr.")

        self.set_y(101.5)
        self.set_x(15.5)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="No.")

        self.set_y(99)
        self.set_x(23)
        self.set_font("helvetica", "B", 10)
        self.cell(w=65, txt="Description of Goods", align="C")

        self.set_y(99)
        self.set_x(88)
        self.set_font("helvetica", "B", 10)
        self.cell(w=20, txt="HSN/SAC", align="C")

        self.set_y(99)
        self.set_x(110)
        self.set_font("helvetica", "B", 10)
        self.cell(w=23, txt="Rate/Sq Ft.", align="C")

        self.set_y(99)
        self.set_x(133)
        self.set_font("helvetica", "B", 10)
        self.cell(w=24, txt="Amount", align="C")

        self.set_y(99)
        self.set_x(158)
        self.set_font("helvetica", "B", 10)
        self.cell(w=10, txt="Qty.", align="C")

        self.set_y(99)
        self.set_x(167.5)
        self.set_font("helvetica", "B", 10)
        self.cell(w=30, txt="Total Amount", align="C")

    def print_info(self, x, print_level):
        """Print single item info exactly as legacy"""
        self.set_y(print_level)
        self.set_x(15.5)
        self.set_font("helvetica", "", 8)
        self.cell(w=7, txt=f"{x + 1}", align="C")

        # Extract item data
        item_row = self.cart_items.iloc[x]
        width = float(str(item_row["Width"]).replace("ft", ""))
        height = float(str(item_row["Height"]).replace("ft", ""))
        area = width * height
        area_str = f"{round(area, 2)} Sq Ft."

        desc = item_row["Particulars"]
        desc1 = f" ({item_row['Width']} x {item_row['Height']} = {area_str})"

        w = self.get_string_width(desc)

        self.set_y(print_level)
        self.set_x(24)
        self.set_font("helvetica", "BI", 8)
        self.cell(w=w + 2, txt=f"{desc}", align="L")
        self.set_font("helvetica", "", 7)
        self.cell(w=77, txt=f"{desc1}", align="L")

        self.set_y(print_level)
        self.set_x(88)
        self.set_font("helvetica", "", 8)
        self.cell(w=20, txt=f"{item_row.get('hsn_sac', '')}", align="C")

        rate = item_row["Cost (INR)"]
        amount = item_row["Amount"]

        self.set_y(print_level)
        self.set_x(115)
        self.set_font("helvetica", "", 8)
        self.cell(w=22.5, txt=f"{rate}", align="L")

        self.set_y(print_level)
        self.set_x(133)
        self.set_font("helvetica", "", 8)
        self.cell(w=25, txt=f"Rs. {amount}", align="L")

        self.set_y(print_level)
        self.set_x(160)
        self.set_font("helvetica", "", 8)
        self.cell(w=8, txt=f"{item_row['Quantity']}", align="C")

        self.set_y(print_level)
        self.set_x(168)
        self.set_font("helvetica", "B", 8)
        self.cell(w=22.5, txt=f"Rs. {amount}", align="L")

    def info_section(self):
        """Create item section exactly as legacy"""
        print_level = 108
        self.info_section_title()
        
        # Calculate totals
        total_amount = 0
        for _, item in self.cart_items.iterrows():
            amount = float(str(item["Amount"]).replace("Rs.", "").replace(",", ""))
            total_amount += amount

        # Print all items
        for i in range(len(self.cart_items)):
            if print_level <= 200:
                self.print_count += 1
                self.print_info(i, print_level)
                print_level += 7
            else:
                # Handle pagination if needed
                break

        # Draw total line
        self.set_y(print_level - 4)
        self.set_x(168)
        self.set_font("helvetica", "", 8)
        self.cell(w=22.5, txt="_______________", align="L")

        self.set_y(print_level + 1)
        self.set_x(168)
        self.set_font("helvetica", "B", 8)
        self.cell(w=22.5, txt=f"Rs. {total_amount:,.2f}", align="L")

        # Helper function for currency formatting
        def ind_curr(x):
            return format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")

        bill = total_amount
        print_level += 10

        # Apply discount if any
        discount = self.final_costs.get("discount", 0)
        if discount > 0:
            bill -= discount
            disc_amount = ind_curr(round(discount, 2))

            self.set_y(print_level)
            self.set_x(60)
            self.set_font("helvetica", "B", 8)
            self.cell(w=22.5, txt="Discount", align="R")

            self.set_y(print_level)
            self.set_x(168)
            self.set_font("helvetica", "B", 8)
            self.cell(w=22.5, txt=f"(-) Rs. {disc_amount[1:]}", align="L")

            print_level += 5

        # CGST @9%
        cgst_amount = bill * 9 / 100
        cgst = ind_curr(cgst_amount)

        self.set_y(print_level)
        self.set_x(60)
        self.set_font("helvetica", "B", 8)
        self.cell(w=22.5, txt="CGST @9%", align="R")

        self.set_y(print_level)
        self.set_x(168)
        self.set_font("helvetica", "B", 8)
        self.cell(w=22.5, txt=f"Rs. {cgst[1:]}", align="L")

        print_level += 5

        # SGST @9%
        self.set_y(print_level)
        self.set_x(60)
        self.set_font("helvetica", "B", 8)
        self.cell(w=22.5, txt="SGST @9%", align="R")

        self.set_y(print_level)
        self.set_x(168)
        self.set_font("helvetica", "B", 8)
        self.cell(w=22.5, txt=f"Rs. {cgst[1:]}", align="L")

        bill += (bill * 18 / 100)

        # Installation charges if any
        installation = self.final_costs.get("installation", 0)
        if installation > 0:
            inst_amount = ind_curr(round(installation, 2))

            print_level += 5

            self.set_y(print_level)
            self.set_x(59)
            self.set_font("helvetica", "B", 8)
            self.cell(w=22.5, txt="Installation Charges", align="R")

            self.set_y(print_level)
            self.set_x(168)
            self.set_font("helvetica", "B", 8)
            self.cell(w=22.5, txt=f"Rs. {inst_amount[1:]}", align="L")

            bill += installation

        print_level += 7

        # Round off calculation
        from math import floor
        round_off = bill - floor(bill)
        round_off = round(round_off, 2)

        if round_off != 0:
            self.set_y(print_level)
            self.set_x(60)
            self.set_font("helvetica", "B", 8)
            self.cell(w=22, txt="Round Off", align="R")

            self.set_y(print_level)
            self.set_x(168)
            self.set_font("helvetica", "B", 8)
            self.cell(w=22, txt=f"(-) Rs. {round_off}", align="L")

            print_level += 8

        bill = bill - round_off
        bill = round(bill)
        curr = ind_curr(bill)

        self.set_y(print_level)
        self.set_x(60)
        self.set_font("helvetica", "B", 8)
        self.cell(w=22, txt="Total", align="R")

        self.set_y(print_level)
        self.set_x(168)
        self.set_font("helvetica", "B", 8)
        self.cell(w=22, txt=f"Rs. {curr[1:]}", align="L")

        print_level += 5

        # Amount in words
        try:
            bill_words = num2words(bill, lang="en_IN").title()
        except:
            # Fallback if num2words is not available
            bill_words = f"{bill:,.2f}"

        self.set_y(print_level + 3)
        self.set_x(16)
        self.set_font("helvetica", "", 10)
        self.cell(w=22, txt="Amount Chargeable (in words)", align="L")

        self.set_y(print_level + 10)
        self.set_x(16)
        self.set_font("helvetica", "B", 10)
        self.multi_cell(
            w=160, h=5, txt=f"Indian Rupees {bill_words} Only", align="L"
        )

        self.set_y(print_level + 3)
        self.set_x(168)
        self.set_font("helvetica", "", 10)
        self.cell(w=22, txt="E. & O.E", align="L")

        self.draw_lines_info(print_level)
        self.line(15, print_level, 195, print_level)
        self.line(15, print_level + 23, 195, print_level + 23)

    def taxable_amount_title(self):
        """Create tax breakdown section headers exactly as legacy"""
        tax_level = 97
        self.set_y(tax_level + 2)
        self.set_x(15)
        self.set_font("helvetica", "B", 10)
        self.cell(w=25, txt="HSN/SAC", align="C")

        self.set_y(tax_level + 2)
        self.set_x(40)
        self.set_font("helvetica", "B", 10)
        self.cell(w=30, txt="Taxable Value", align="C")

        self.set_y(tax_level + 1)
        self.set_x(70)
        self.set_font("helvetica", "B", 10)
        self.cell(w=50, txt="Central Tax", align="C")

        self.set_y(tax_level + 8)
        self.set_x(70)
        self.set_font("helvetica", "B", 10)
        self.cell(w=20, txt="Rate", align="C")

        self.set_y(tax_level + 8)
        self.set_x(90)
        self.set_font("helvetica", "B", 10)
        self.cell(w=30, txt="Amount", align="C")

        self.set_y(tax_level + 1)
        self.set_x(120)
        self.set_font("helvetica", "B", 10)
        self.cell(w=50, txt="State Tax", align="C")

        self.set_y(tax_level + 8)
        self.set_x(120)
        self.set_font("helvetica", "B", 10)
        self.cell(w=20, txt="Rate", align="C")

        self.set_y(tax_level + 8)
        self.set_x(140)
        self.set_font("helvetica", "B", 10)
        self.cell(w=30, txt="Amount", align="C")

        self.set_y(tax_level)
        self.set_x(170)
        self.set_font("helvetica", "B", 10)
        self.cell(w=25, txt="Total Tax", align="C")

        self.set_y(tax_level + 5)
        self.set_x(170)
        self.set_font("helvetica", "B", 10)
        self.cell(w=25, txt="Amount", align="C")

    def print_tax_info(self, tax_level, x, tax_sum):
        """Print tax information for each item exactly as legacy"""
        def ind_curr(x):
            return format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")

        self.set_y(tax_level + 2)
        self.set_x(15)
        self.set_font("helvetica", "", 8)
        item_row = self.cart_items.iloc[x]
        self.cell(w=25, txt=f"{item_row.get('hsn_sac', '')}", align="C")

        # Calculate amount after discount
        amount = float(str(item_row["Amount"]).replace("Rs.", "").replace(",", ""))
        discount = self.final_costs.get("discount", 0)
        
        # Apply discount proportionally per item
        if discount > 0:
            discount_per_item = discount / len(self.cart_items)
            amount = amount - discount_per_item

        self.amt_sum += amount
        amount_formatted = ind_curr(round(amount, 2))

        self.set_y(tax_level + 2)
        self.set_x(40)
        self.set_font("helvetica", "", 8)
        self.cell(w=30, txt=f"Rs. {amount_formatted[1:]}", align="C")

        self.set_y(tax_level + 2)
        self.set_x(70)
        self.set_font("helvetica", "", 8)
        self.cell(w=20, txt="9%", align="C")

        # Calculate CGST
        cgst_amount = amount * 9 / 100
        cgst_formatted = ind_curr(cgst_amount)
        self.set_y(tax_level + 2)
        self.set_x(90)
        self.set_font("helvetica", "", 8)
        self.cell(w=30, txt=f"Rs. {cgst_formatted[1:]}", align="C")

        self.set_y(tax_level + 2)
        self.set_x(120)
        self.set_font("helvetica", "", 8)
        self.cell(w=20, txt="9%", align="C")

        # Calculate SGST
        sgst_amount = amount * 9 / 100
        sgst_formatted = ind_curr(sgst_amount)
        self.set_y(tax_level + 2)
        self.set_x(140)
        self.set_font("helvetica", "", 8)
        self.cell(w=30, txt=f"Rs. {sgst_formatted[1:]}", align="C")

        # Total tax
        total_tax = cgst_amount + sgst_amount
        total_tax_formatted = ind_curr(total_tax)
        self.set_y(tax_level + 2)
        self.set_x(170)
        self.set_font("helvetica", "", 8)
        self.cell(w=25, txt=f"Rs. {total_tax_formatted[1:]}", align="C")

        return tax_sum + cgst_amount

    def taxable_amount(self):
        """Create comprehensive tax breakdown section exactly as legacy"""
        tax_level = 97
        start_tax_level = tax_level - 2
        tax_level += 15
        tax_sum = 0
        
        self.taxable_amount_title()

        # Print tax info for each item
        for i in range(len(self.cart_items)):
            if tax_level <= 230:
                self.tax_print_count += 1
                tax_sum = self.print_tax_info(tax_level, i, tax_sum)
                tax_level += 7

        # Draw tax section lines
        self.draw_lines_tax(start_tax_level, tax_level - 7)
        self.line(15, tax_level, 195, tax_level)

        tax_level += 4

        # Tax totals
        def ind_curr(x):
            return format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")

        amt_sum_formatted = ind_curr(round(self.amt_sum, 2))

        self.set_y(tax_level + 2)
        self.set_x(15)
        self.set_font("helvetica", "B", 8)
        self.cell(w=25, txt="Total  ", align="R")

        self.set_y(tax_level + 2)
        self.set_x(40)
        self.set_font("helvetica", "B", 8)
        self.cell(w=30, txt=f"Rs. {amt_sum_formatted[1:]}", align="C")

        tax_amount_formatted = ind_curr(tax_sum)

        self.set_y(tax_level + 2)
        self.set_x(90)
        self.set_font("helvetica", "B", 8)
        self.cell(w=30, txt=f"Rs. {tax_amount_formatted[1:]}", align="C")

        self.set_y(tax_level + 2)
        self.set_x(140)
        self.set_font("helvetica", "B", 8)
        self.cell(w=30, txt=f"Rs. {tax_amount_formatted[1:]}", align="C")

        final_tax = tax_sum * 2
        final_tax = round(final_tax, 2)
        final_tax_formatted = ind_curr(final_tax)

        self.set_y(tax_level + 2)
        self.set_x(170)
        self.set_font("helvetica", "B", 8)
        self.cell(w=25, txt=f"Rs. {final_tax_formatted[1:]}", align="C")

        # Tax amount in words
        try:
            bill_words = num2words(final_tax, lang="en_IN").title()
        except:
            bill_words = f"{final_tax:,.2f}"

        self.set_y(tax_level + 9)
        self.set_x(16)
        self.set_font("helvetica", "", 10)
        self.cell(w=22, txt="Tax Amount (in words)", align="L")

        self.set_y(tax_level + 16)
        self.set_x(16)
        self.set_font("helvetica", "B", 10)
        self.multi_cell(
            w=160, h=5, txt=f"Indian Rupees {bill_words} Only", align="L"
        )

        self.draw_lines_tax(start_tax_level, tax_level)
        self.line(15, tax_level + 7, 195, tax_level + 7)
        self.line(15, tax_level, 195, tax_level)
        self.line(15, tax_level + 28, 195, tax_level + 28)

        self.end_print_level = tax_level

    def end_print(self):
        """Create end section with bank details exactly as legacy"""
        # Check if we have enough space for bank details (approximately 60mm needed)
        current_y = self.get_y()
        page_height = self.h - self.b_margin  # Available page height
        
        if current_y + 60 > page_height:
            # Not enough space, add new page
            self.add_page()
            self.home_page()
            end_print_level = 100
        else:
            # Enough space, continue on current page
            end_print_level = current_y + 10

        # Hardcoded values exactly as legacy
        name = "Madhav Glass & Aluminium"
        bank = "Punjab National Bank"
        account = "0650050015525"
        ifsc = "PUNB0065020"

        # Draw bank details section
        self.dashed_line(15, end_print_level, 195, end_print_level)
        self.line(15, end_print_level + 28, 195, end_print_level + 28)
        self.line(15, end_print_level + 55, 195, end_print_level + 55)
        self.line(105, end_print_level + 28, 105, end_print_level + 55)

        end_print_level += 2

        self.set_y(end_print_level)
        self.set_x(16)
        self.set_font("helvetica", "B", 10)
        self.cell(w=22, txt="Bank Details", align="L")

        end_print_level += 7

        self.set_y(end_print_level)
        self.set_x(16)
        self.set_font("helvetica", "", 10)
        self.cell(w=22, txt="Recipient Name : ", align="L")

        wi = self.get_string_width("Recipient Name : ")

        self.set_y(end_print_level)
        self.set_x(16 + wi)
        self.set_font("helvetica", "B", 10)
        self.cell(w=22, txt=f"{name}", align="L")

        end_print_level += 5

        self.set_y(end_print_level)
        self.set_x(16)
        self.set_font("helvetica", "", 10)
        self.cell(w=22, txt="BANK NAME : ", align="L")

        wi = self.get_string_width("BANK NAME : ")

        self.set_y(end_print_level)
        self.set_x(16 + wi)
        self.set_font("helvetica", "B", 10)
        self.cell(w=22, txt=f"{bank}", align="L")

        end_print_level += 5

        self.set_y(end_print_level)
        self.set_x(16)
        self.set_font("helvetica", "", 10)
        self.cell(w=22, txt="Account No : ", align="L")

        wi = self.get_string_width("Account No : ")

        self.set_y(end_print_level)
        self.set_x(16 + wi)
        self.set_font("helvetica", "B", 10)
        self.cell(w=22, txt=f"{account}", align="L")

        end_print_level += 5

        self.set_y(end_print_level)
        self.set_x(16)
        self.set_font("helvetica", "", 10)
        self.cell(w=22, txt="IFSC CODE : ", align="L")

        wi = self.get_string_width("IFSC CODE : ")

        self.set_y(end_print_level)
        self.set_x(16 + wi)
        self.set_font("helvetica", "B", 10)
        self.cell(w=22, txt=f"{ifsc}", align="L")

        end_print_level += 5

        self.set_y(end_print_level + 22)
        self.set_x(16)
        self.set_font("helvetica", "B", 10)
        self.cell(w=22, txt="Madhav Glass & Aluminium (Seal and Signature)", align="L")

        self.set_y(end_print_level + 22)
        self.set_x(106)
        self.set_font("helvetica", "B", 10)
        self.cell(w=90, txt="Customers Signature  ", align="R")

    def dashed_line(self, x1, y1, x2, y2):
        """Draw dashed line"""
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)
        dash_length = 2
        gap_length = 1
        current_x = x1
        
        while current_x < x2:
            end_x = min(current_x + dash_length, x2)
            self.line(current_x, y1, end_x, y2)
            current_x = end_x + gap_length

    def invoice_driver_code(self):
        """Main driver code exactly as legacy"""
        self.alias_nb_pages()
        self.set_left_margin(15)
        self.set_right_margin(15)
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_y(15)

        # Create the main invoice page
        self.home_page()
        self.info_section()
        
        # Add tax breakdown page as in legacy
        self.add_page()
        self.home_page()
        self.taxable_amount()
        self.end_print()

        return True
