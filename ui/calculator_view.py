import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename
from babel.numbers import format_currency
from datetime import datetime
from random import randint
from pdf_generator import create_quotation_pdf
from global_state import get_global_state


class CalculatorView(tk.Toplevel):
    def __init__(self, parent, data_manager):
        super().__init__(parent)
        self.parent = parent
        self.data_manager = data_manager
        self.global_state = get_global_state()
        
        self.title("Calculation")
        
        # Set window position exactly as legacy
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        x = (screen_width - (screen_width / 2.8)) / 2 + 30
        y = ((screen_height / 1.5)) / 2
        self.geometry("+%d+%d" % (x, y))
        
        self.attributes("-topmost", True)

        # Variables exactly as legacy
        self.discount_var = tk.StringVar()
        self.installation_var = tk.StringVar()
        self.gst_var = tk.StringVar(value="18")
        
        self.cost_total_var = tk.StringVar()
        self.discount_total_var = tk.StringVar()
        self.installation_total_var = tk.StringVar()
        self.gst_total_var = tk.StringVar()
        
        # Flags exactly as legacy
        self.calculation_done = False

        self.create_widgets()
        self.load_initial_data()

    def create_widgets(self):
        """Create calculator layout exactly as legacy costPage()"""
        # Headers exactly as legacy
        entLab = ttk.Label(self, text="Enter Values")
        entLab.grid(column=1, row=0, padx=10, pady=10, sticky="W")
        totLab = ttk.Label(self, text="Total")
        totLab.grid(column=3, row=0, padx=10, pady=10, sticky="W")

        # Total Cost row
        cost = ttk.Label(self, text="Total Cost")
        cost.grid(column=0, row=2, padx=10, pady=10, sticky="W")
        
        self.cost_total_entry = tk.Entry(
            self, textvariable=self.cost_total_var, relief="solid", 
            width=16, state="disabled"
        )
        self.cost_total_entry.grid(column=3, row=2, padx=10, pady=10, sticky="W")

        # Discount row
        discount = ttk.Label(self, text="Enter Discount Amount")
        discount.grid(column=0, row=4, padx=10, pady=10, sticky="W")
        
        self.discount_entry = tk.Entry(
            self, textvariable=self.discount_var, relief="solid", width=16
        )
        self.discount_entry.grid(column=1, row=4, padx=10, pady=10, sticky="W")
        
        discount_total_label = ttk.Label(self, text="Cost After Discount")
        discount_total_label.grid(column=2, row=4, padx=10, pady=10, sticky="W")
        
        self.discount_total_entry = tk.Entry(
            self, textvariable=self.discount_total_var, relief="solid", 
            width=16, state="disabled"
        )
        self.discount_total_entry.grid(column=3, row=4, padx=10, pady=10, sticky="W")

        # GST row
        gst = ttk.Label(self, text="GST (In Percentage)")
        gst.grid(column=0, row=5, padx=10, pady=10, sticky="W")
        
        self.gst_entry = tk.Entry(
            self, textvariable=self.gst_var, relief="solid", width=16
        )
        self.gst_entry.grid(column=1, row=5, padx=10, pady=10, sticky="W")
        
        gst_total_label = ttk.Label(self, text="Final bill amout with GST")
        gst_total_label.grid(column=2, row=5, padx=10, pady=10, sticky="W")
        
        self.gst_total_entry = tk.Entry(
            self, textvariable=self.gst_total_var, relief="solid", 
            width=16, state="disabled"
        )
        self.gst_total_entry.grid(column=3, row=5, padx=10, pady=10, sticky="W")

        # Installation row
        install = ttk.Label(self, text="Enter Installation Charges")
        install.grid(column=0, row=6, padx=10, pady=10, sticky="W")
        
        self.installation_entry = tk.Entry(
            self, textvariable=self.installation_var, relief="solid", width=16
        )
        self.installation_entry.grid(column=1, row=6, padx=10, pady=10, sticky="W")
        
        install_total_label = ttk.Label(self, text="Cost with Installation Charges")
        install_total_label.grid(column=2, row=6, padx=10, pady=10, sticky="W")
        
        self.installation_total_entry = tk.Entry(
            self, textvariable=self.installation_total_var, relief="solid", 
            width=16, state="disabled"
        )
        self.installation_total_entry.grid(column=3, row=6, padx=10, pady=10, sticky="W")

        # Buttons exactly as legacy
        calculate = tk.Button(
            self, text="Calculate", width=20, command=self.calculate_cost
        )
        calculate.grid(column=0, row=7, columnspan=2, padx=10, pady=15, sticky="W")

        genPdf = tk.Button(
            self, text="Generate PDF", width=20, command=self.generate_pdf
        )
        genPdf.grid(column=1, row=7, columnspan=2, padx=10, pady=15, sticky="N")

        invoice = tk.Button(
            self, text="Invoice Page", width=20, command=self.open_invoice
        )
        invoice.grid(column=2, row=7, columnspan=2, padx=10, pady=15, sticky="E")

    def load_initial_data(self):
        """Load initial data exactly as legacy"""
        # Get total cost from cart
        total_cost = self.data_manager.get_cart_total_amount()
        indCurr = lambda x: format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")
        self.cost_total_var.set(indCurr(total_cost))

    def calculate_cost(self):
        """Calculate costs exactly as legacy calculateCost() method"""
        self.calculation_done = True

        if self.gst_var.get() == "":
            messagebox.showerror(
                "Invalid", "Please fill GST percentage", parent=self
            )
            return False

        indCurr = lambda x: format_currency(x, "INR", locale="en_IN").replace("\xa0", " ")

        # Get total cost and convert to float
        total_cost_str = self.cost_total_var.get()
        totalcost = float(total_cost_str[1:].replace(",", ""))

        print(totalcost)
        discountedCost = 0.0
        installationCost = 0.0
        gstCost = 0.0
        
        # Get GST percentage from input
        gst_percent = float(self.gst_var.get())

        # Logic exactly as legacy
        if self.discount_var.get() != "" and self.installation_var.get() != "":
            discountedCost = totalcost - float(self.discount_var.get())
            gstCost = discountedCost + (discountedCost * gst_percent / 100)
            installationCost = gstCost + float(self.installation_var.get())

            self.discount_total_var.set(indCurr(discountedCost))
            self.installation_total_var.set(indCurr(installationCost))
            self.gst_total_var.set(indCurr(gstCost))

        else:
            gstCost = totalcost + (totalcost * gst_percent / 100)
            self.gst_total_var.set(indCurr(gstCost))

            if self.discount_var.get() != "":
                discountedCost = totalcost - float(self.discount_var.get())
                gstCost = discountedCost + (discountedCost * gst_percent / 100)
                self.discount_total_var.set(indCurr(discountedCost))
                self.gst_total_var.set(indCurr(gstCost))
            else:
                self.discount_total_var.set("")

            if self.installation_var.get() != "":
                gstCost = totalcost + (totalcost * gst_percent / 100)
                installationCost = gstCost + float(self.installation_var.get())
                self.installation_total_var.set(indCurr(installationCost))
                self.gst_total_var.set(indCurr(gstCost))
            else:
                self.installation_total_var.set("")

        print(totalcost, discountedCost, installationCost)

    def generate_pdf(self):
        """Generate PDF exactly as legacy generatePDF() method"""
        if not self.calculation_done:
            messagebox.showerror(
                "Invalid", "Please press calculate button", parent=self
            )
            return False

        self.attributes("-topmost", False)

        # Generate quotation number exactly as legacy
        today = datetime.now()
        quotation_number = (
            "QUO"
            + "/"
            + str(today.day)
            + str(today.month)
            + "-"
            + str(today.year)
            + "/"
            + str(randint(100, 999))
        )

        prog = tk.Toplevel()

        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        x = (screen_width - (screen_width / 2.8)) / 2
        y = ((screen_height / 1.5)) / 2 + 100
        prog.geometry("+%d+%d" % (x, y))
        prog.title("Wait")

        labour = ttk.Label(
            prog,
            text="PDF is generating might take a minute or two. This window would close automatically once done.",
            font=("", 10, "bold"),
        )
        labour.grid(column=0, row=3, padx=20, pady=20, sticky="W")
        
        files = [("PDF Files", "*.pdf"), ("All Files", "*.*")]
        file = asksaveasfilename(filetypes=files, defaultextension=".pdf", parent=self)
        
        if not file:
            prog.destroy()
            self.attributes("-topmost", True)
            return

        try:
            customer_details = self.data_manager.get_customer_details()
            cart_items = self.data_manager.get_cart_data()

            # Prepare final costs
            final_costs = {
                "discount": float(self.discount_var.get()) if self.discount_var.get() else 0,
                "installation": float(self.installation_var.get()) if self.installation_var.get() else 0,
                "gst_percent": float(self.gst_var.get()),
                "quotation_number": quotation_number
            }

            prog.attributes("-topmost", True)
            
            # Generate PDF using the pdf_generator
            create_quotation_pdf(file, customer_details, cart_items, final_costs)
            
            print("Finished")
            prog.destroy()
            self.attributes("-topmost", True)
            
            messagebox.showinfo("Success", "PDF generated successfully!", parent=self)

        except Exception as e:
            prog.destroy()
            self.attributes("-topmost", True)
            messagebox.showerror("Error", f"Error generating PDF: {str(e)}", parent=self)

    def open_invoice(self):
        """Open invoice exactly as legacy callInvoice() method"""
        if not self.calculation_done:
            messagebox.showerror(
                "Invalid", "Please press calculate button", parent=self
            )
            return False

        # Import InvoiceView here to avoid circular import
        try:
            from ui.invoice_view import InvoiceView
            
            # Prepare final costs data for invoice
            final_costs = {
                "discount": float(self.discount_var.get()) if self.discount_var.get() else 0,
                "installation": float(self.installation_var.get()) if self.installation_var.get() else 0,
                "gst_percent": float(self.gst_var.get()),
                "discount_total": self.discount_total_var.get(),
                "installation_total": self.installation_total_var.get(), 
                "gst_total": self.gst_total_var.get(),
                "total_cost": self.cost_total_var.get()
            }
            
            self.destroy()
            invoice_view = InvoiceView(self.parent, self.data_manager, final_costs)
        except ImportError:
            messagebox.showinfo("Coming Soon", "Invoice functionality will be available soon.", parent=self)
