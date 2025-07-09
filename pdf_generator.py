from fpdf import FPDF
from datetime import date
from babel.numbers import format_currency
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
    def __init__(self, customer_details, cart_items, final_costs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer_details = customer_details
        self.cart_items = cart_items
        self.final_costs = final_costs
        self.print_done_flag = False
        self.today = date.today()
        # A unique quotation number can be generated here or passed in
        self.quotation_number = (
            f"QUO/{self.today.strftime('%d%m-%Y')}/{pd.Timestamp.now().microsecond}"
        )

    fileName = None
    printDoneFlag = False

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
        self.set_y(60)
        self.set_x(170)
        self.set_font("helvetica", "B", 8)
        self.cell(w=0, txt="Date:")

        self.set_y(60.1)
        self.set_x(179)
        self.set_font("helvetica", "", 9)
        self.cell(w=0, txt=f"{self.today.day}/{self.today.month}/{self.today.year}")

        self.set_y(67)
        self.set_x(140)
        self.set_font("helvetica", "B", 8)
        self.cell(w=0, txt="Quotation Number: ")

        wi = self.get_string_width("Quotation Number: ")

        self.set_y(67)
        self.set_x(140 + wi)
        self.set_font("helvetica", "", 9)
        self.cell(w=0, txt=self.quotation_number)

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
        self.set_y(text_level)
        self.set_x(15)
        self.set_font("helvetica", "", 6)
        self.cell(w=12, txt=str(item_row["Sr.No"]), align="C")
        self.insert_image(item_row, design_x, text_level)

        if RATIO.get(key) and RATIO[key][0] < 50:
            self.set_y(text_level + 65)
        else:
            self.set_y(text_level + 55)
        self.set_x(design_x)
        self.set_font("helvetica", "B", 6)
        self.cell(w=65, txt=key, align="C")

        self.print_specs(text_level, specs_x, item_row)

        self.set_y(text_level)
        self.set_x(cost_x)
        self.set_font("helvetica", "B", 6)
        self.cell(w=20, txt=str(item_row["Cost (INR)"]), align="C")

        self.set_y(text_level)
        self.set_x(quantity_x)
        self.set_font("helvetica", "", 6)
        self.cell(w=10, txt=str(item_row["Quantity"]), align="C")

        self.set_y(text_level)
        self.set_x(amount_x)
        self.set_font("helvetica", "B", 6)
        self.cell(w=28, txt=str(item_row["Amount"]), align="C")
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
                y=text_level + 5,
                w=img_w,
                h=img_h,
            )
        except RuntimeError as e:
            print(f"Could not load image for {key}: {e}. Skipping.")
            # Draw a placeholder box instead
            self.rect(design_x + 7.5, text_level + 5, img_w, img_h)
            self.set_xy(design_x + 7.5, text_level + 5 + img_h / 2)
            self.cell(w=img_w, txt="Image not found", align="C")

        str_width = self.get_string_width(str(item_row["Width"]))
        str_height = self.get_string_width(str(item_row["Height"]))

        self.set_y(text_level + 8.2 + img_h)
        self.set_x(design_x + (60 - str_width) / 2)
        self.set_font("helvetica", "", 6)
        self.cell(w=str_width + 4, txt=str(item_row["Width"]), align="C")

        self.set_y(text_level + 4 + (img_h / 2))
        self.set_x(design_x + 1.7)
        self.set_font("helvetica", "", 6)
        self.cell(w=str_height + 4, h=5, txt=str(item_row["Height"]), align="C")

    def print_specs(self, text_level, specs_x, item_row):
        self.set_y(text_level)
        self.set_x(specs_x)
        self.set_font("helvetica", "BI", 7)
        self.set_text_color(118, 175, 93)
        # Cost per sqft is not in the cart data, so we comment this out.
        # self.cell(w=10,txt=f"Rate (Rs.): {item_row.get('costEntVar', '')} Sq.Ft.")
        text_level += 4
        self.set_y(text_level)
        self.set_x(specs_x)
        self.set_font("helvetica", "", 6)
        self.set_text_color(0, 0, 0)
        self.cell(w=10, txt=f"Area: {item_row.get('Total Sq.ft', '')} Sq.Ft.")
        text_level += 4

        for key, display_name in VAR_NAME.items():
            if (
                key in item_row
                and item_row[key]
                and str(item_row[key]) not in ["0", "nan", ""]
            ):
                self.set_y(text_level)
                self.set_x(specs_x)
                self.multi_cell(w=40, h=3.5, txt=f"{display_name}: {item_row[key]}")
                text_level = self.get_y()

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
    High-level function to generate the complete invoice PDF.
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
        pdf.add_page()
        pdf.home_page()
        pdf.infosection_title()
        pdf.infosection()
        pdf.end_print()
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
        self.today = date.today()

    def header(self):
        try:
            self.image(os.path.join(IMAGE_DIR, "MGA_1.png"), x=10, y=8, w=33)
        except Exception as e:
            print(f"Header Image Error: {e}")
        self.set_font("helvetica", "B", 15)
        self.cell(80)
        self.cell(30, 10, "Tax Invoice", 1, 0, "C")
        self.cell(80)
        self.set_font("helvetica", "", 10)
        self.cell(30, 10, "Original for Recipient", 0, 0, "C")
        self.ln(20)

    def footer(self):
        self.set_y(-25)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, "This is a computer-generated invoice", 0, 0, "C")
        self.set_y(-20)
        self.set_font("helvetica", "B", 10)
        self.cell(125)
        self.cell(0, 10, "For Madhav Glass & Aluminium", 0, 0, "C")

    def home_page(self):
        # Seller Details
        self.set_xy(12, 35)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="Madhav Glass & Aluminium")
        self.ln(5)
        self.set_x(12)
        self.set_font("helvetica", "", 10)
        self.cell(w=0, txt="Plot no. 5, Chikalthana MIDC,")
        self.ln(5)
        self.set_x(12)
        self.cell(w=0, txt="Opp. Ajantha Pharma, Aurangabad - 431001")
        self.ln(5)
        self.set_x(12)
        self.cell(w=0, txt="Maharashtra")
        self.ln(5)
        self.set_x(12)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="GSTIN/UIN: 27BEXP8978P1Z5")
        self.ln(5)
        self.set_x(12)
        self.cell(w=0, txt="PAN/IT No.: BEXXXXXX7P")

        # Invoice Details
        self.set_xy(110, 35)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt=f"Invoice No.: {self.invoice_details.get('invNumbVar', '')}")
        self.ln(5)
        self.set_x(110)
        self.set_font("helvetica", "", 10)
        self.cell(
            w=0, txt=f"Quotation No.: {self.invoice_details.get('quotNumbVar', '')}"
        )
        self.ln(5)
        self.set_x(110)
        self.cell(
            w=0,
            txt=f"Mode/Terms of Payment: {self.invoice_details.get('modeTermVar', '')}",
        )
        self.ln(5)
        self.set_x(110)
        self.cell(
            w=0,
            txt=f"Terms of Delivery: {self.invoice_details.get('termOfDelVar', '')}",
        )
        self.ln(5)
        self.set_x(110)
        self.cell(w=0, txt=f"Destination: {self.invoice_details.get('destinVar', '')}")

        # Buyer Details
        self.set_xy(12, self.get_y() + 10)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt="Buyer")
        self.ln(5)
        self.set_x(12)
        self.set_font("helvetica", "", 10)
        self.cell(w=0, txt=f"{self.customer_details.get('custNamVar', '')}")
        self.ln(5)
        self.set_x(12)
        self.multi_cell(w=80, h=5, txt=f"{self.customer_details.get('custAddVar', '')}")
        self.ln(5)
        self.set_x(12)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, txt=f"GSTIN/UIN: {self.invoice_details.get('custGstVar', '')}")
        self.ln(5)
        self.set_x(12)
        self.cell(w=0, txt=f"PAN/IT No.: {self.invoice_details.get('custPanVar', '')}")

        self.ln(10)

    def infosection_title(self):
        self.set_x(10)
        self.set_font("helvetica", "B", 9)
        self.set_fill_color(229, 233, 243)
        self.cell(10, 10, "Sr.No", border=1, align="C", fill=True)
        self.cell(80, 10, "Description of Goods", border=1, align="C", fill=True)
        self.cell(20, 10, "HSN/SAC", border=1, align="C", fill=True)
        self.cell(20, 10, "Quantity", border=1, align="C", fill=True)
        self.cell(25, 10, "Rate", border=1, align="C", fill=True)
        self.cell(25, 10, "Amount", border=1, align="C", fill=True)
        self.ln()

    def infosection(self):
        self.set_font("helvetica", "", 9)
        for i, item in self.cart_items.iterrows():
            self.set_x(10)
            desc = f"{item['Particulars']} ({item['Width']} x {item['Height']})"

            # Use self.get_string_width to calculate cell height
            desc_width = 78
            lines = self.multi_cell(
                w=desc_width, h=5, txt=desc, dry_run=True, output="L"
            )
            cell_height = len(lines) * 5

            self.cell(10, cell_height, str(item["Sr.No"]), border=1, align="C")

            x_before_multi = self.get_x()
            y_before_multi = self.get_y()
            self.multi_cell(80, 5, desc, border=1, align="L")
            self.set_xy(x_before_multi + 80, y_before_multi)

            self.cell(
                20, cell_height, str(item.get("hsn_sac", "")), border=1, align="C"
            )
            self.cell(20, cell_height, str(item["Quantity"]), border=1, align="C")
            self.cell(25, cell_height, f"{item['Cost (INR)']:.2f}", border=1, align="R")
            self.cell(25, cell_height, f"{item['Amount']:.2f}", border=1, align="R")
            self.ln()

    def end_print(self):
        # This threshold might need adjustment
        if self.get_y() > 220:
            self.add_page()

        # Totals section
        totals = [
            ("Subtotal:", self.final_costs.get("subtotal", 0)),
            ("Discount:", self.final_costs.get("discount", 0)),
            (
                f"CGST @ {self.final_costs.get('gst_percent', 0)/2}%:",
                self.final_costs.get("gst_amount", 0) / 2,
            ),
            (
                f"SGST @ {self.final_costs.get('gst_percent', 0)/2}%:",
                self.final_costs.get("gst_amount", 0) / 2,
            ),
            ("Installation:", self.final_costs.get("installation", 0)),
        ]

        self.set_font("helvetica", "", 10)
        for label, value in totals:
            self.set_x(130)
            self.cell(40, 8, label, border=1, align="R")
            self.cell(30, 8, f"{value:,.2f}", border=1, align="R")
            self.ln()

        # Grand Total
        self.set_x(130)
        self.set_font("helvetica", "B", 10)
        self.cell(40, 8, "Grand Total:", border=1, align="R")
        self.cell(
            30, 8, f"{self.final_costs.get('final_total', 0):,.2f}", border=1, align="R"
        )
        self.ln()


# Cleanup old classes/functions if they are no longer needed
# Make sure to remove the old invoiceDriverCode method.
