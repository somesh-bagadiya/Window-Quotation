import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename
from pdf_generator import create_invoice_pdf


class InvoiceView(tk.Toplevel):
    def __init__(self, parent, data_manager, final_costs):
        super().__init__(parent)
        self.parent = parent
        self.data_manager = data_manager
        self.final_costs = final_costs

        self.title("Generate Invoice")
        self.geometry("900x700")

        # --- Invoice Specific Variables ---
        self.invNumbVar = tk.StringVar()
        self.quotNumbVar = tk.StringVar()
        self.modeTermVar = tk.StringVar()
        self.termOfDelVar = tk.StringVar()
        self.destinVar = tk.StringVar()
        self.custGstVar = tk.StringVar()
        self.custPanVar = tk.StringVar()
        self.hsn_vars = [
            tk.StringVar() for _ in range(len(self.data_manager.get_cart_data()))
        ]

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill="both", expand=True)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # --- Top Frame for Customer and Invoice Details ---
        top_frame = ttk.Frame(main_frame)
        top_frame.grid(row=0, column=0, sticky="ew", pady=5)
        top_frame.columnconfigure(1, weight=1)

        # Customer Details
        cust_details_frame = ttk.LabelFrame(
            top_frame, text="Customer Details", padding="10"
        )
        cust_details_frame.grid(row=0, column=0, padx=5, pady=5, sticky="ns")

        ttk.Label(cust_details_frame, text="Name:").grid(
            row=0, column=0, sticky="w", pady=2
        )
        ttk.Entry(
            cust_details_frame,
            textvariable=self.parent.parent.custNamVar,
            state="readonly",
        ).grid(row=0, column=1, sticky="ew")
        ttk.Label(cust_details_frame, text="Address:").grid(
            row=1, column=0, sticky="w", pady=2
        )
        ttk.Entry(
            cust_details_frame,
            textvariable=self.parent.parent.custAddVar,
            state="readonly",
        ).grid(row=1, column=1, sticky="ew")
        ttk.Label(cust_details_frame, text="Contact:").grid(
            row=2, column=0, sticky="w", pady=2
        )
        ttk.Entry(
            cust_details_frame,
            textvariable=self.parent.parent.custConVar,
            state="readonly",
        ).grid(row=2, column=1, sticky="ew")
        ttk.Label(cust_details_frame, text="Customer GST No.:").grid(
            row=3, column=0, sticky="w", pady=2
        )
        ttk.Entry(cust_details_frame, textvariable=self.custGstVar).grid(
            row=3, column=1, sticky="ew"
        )
        ttk.Label(cust_details_frame, text="Customer PAN No.:").grid(
            row=4, column=0, sticky="w", pady=2
        )
        ttk.Entry(cust_details_frame, textvariable=self.custPanVar).grid(
            row=4, column=1, sticky="ew"
        )

        # Invoice Details
        inv_details_frame = ttk.LabelFrame(
            top_frame, text="Invoice Details", padding="10"
        )
        inv_details_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        ttk.Label(inv_details_frame, text="Invoice Number:").grid(
            row=0, column=0, sticky="w", pady=2
        )
        ttk.Entry(inv_details_frame, textvariable=self.invNumbVar).grid(
            row=0, column=1, sticky="ew"
        )
        ttk.Label(inv_details_frame, text="Quotation Number:").grid(
            row=1, column=0, sticky="w", pady=2
        )
        ttk.Entry(inv_details_frame, textvariable=self.quotNumbVar).grid(
            row=1, column=1, sticky="ew"
        )
        ttk.Label(inv_details_frame, text="Mode/Terms of Payment:").grid(
            row=2, column=0, sticky="w", pady=2
        )
        ttk.Entry(inv_details_frame, textvariable=self.modeTermVar).grid(
            row=2, column=1, sticky="ew"
        )
        ttk.Label(inv_details_frame, text="Terms of Delivery:").grid(
            row=3, column=0, sticky="w", pady=2
        )
        ttk.Entry(inv_details_frame, textvariable=self.termOfDelVar).grid(
            row=3, column=1, sticky="ew"
        )
        ttk.Label(inv_details_frame, text="Destination:").grid(
            row=4, column=0, sticky="w", pady=2
        )
        ttk.Entry(inv_details_frame, textvariable=self.destinVar).grid(
            row=4, column=1, sticky="ew"
        )

        # --- Cart Items Frame (Scrollable) ---
        cart_canvas_frame = ttk.LabelFrame(
            main_frame, text="Cart Items & HSN/SAC Codes", padding="10"
        )
        cart_canvas_frame.grid(row=1, column=0, sticky="nsew", pady=5)
        cart_canvas_frame.rowconfigure(0, weight=1)
        cart_canvas_frame.columnconfigure(0, weight=1)

        canvas = tk.Canvas(cart_canvas_frame)
        scrollbar = ttk.Scrollbar(
            cart_canvas_frame, orient="vertical", command=canvas.yview
        )
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Headers
        headers = [
            "Sr.No",
            "Description of Goods",
            "HSN/SAC",
            "Rate",
            "Quantity",
            "Amount",
        ]
        for i, header in enumerate(headers):
            ttk.Label(
                scrollable_frame,
                text=header,
                font="TkDefaultFont 10 bold",
                relief="groove",
                padding=5,
            ).grid(row=0, column=i, padx=5, pady=5, sticky="ew")

        # Cart Data
        cart_data = self.data_manager.get_cart_data()
        for i, cart_row in cart_data.iterrows():
            ttk.Label(scrollable_frame, text=cart_row["Sr.No"]).grid(
                row=i + 1, column=0
            )
            desc = f"{cart_row['Particulars']} ({cart_row['Width']} x {cart_row['Height']})"
            ttk.Label(scrollable_frame, text=desc).grid(row=i + 1, column=1, sticky="w")
            ttk.Entry(scrollable_frame, textvariable=self.hsn_vars[i], width=15).grid(
                row=i + 1, column=2
            )
            ttk.Label(scrollable_frame, text=cart_row["Cost (INR)"]).grid(
                row=i + 1, column=3
            )
            ttk.Label(scrollable_frame, text=cart_row["Quantity"]).grid(
                row=i + 1, column=4
            )
            ttk.Label(scrollable_frame, text=cart_row["Amount"]).grid(
                row=i + 1, column=5
            )

        # --- Bottom Frame for Action Button ---
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.grid(row=2, column=0, sticky="e", pady=10)

        generate_btn = ttk.Button(
            bottom_frame, text="Generate Invoice PDF", command=self.generate_invoice_pdf
        )
        generate_btn.pack()

    def generate_invoice_pdf(self):
        # 1. Collect all data from StringVars
        invoice_details = {
            "invNumbVar": self.invNumbVar.get(),
            "quotNumbVar": self.quotNumbVar.get(),
            "modeTermVar": self.modeTermVar.get(),
            "termOfDelVar": self.termOfDelVar.get(),
            "destinVar": self.destinVar.get(),
            "custGstVar": self.custGstVar.get(),
            "custPanVar": self.custPanVar.get(),
        }

        # 2. Get cart data from data_manager and add HSN codes
        cart_data_with_hsn = self.data_manager.get_cart_data().copy()
        hsn_codes = [var.get() for var in self.hsn_vars]
        cart_data_with_hsn["hsn_sac"] = hsn_codes

        # 3. Get customer data from data_manager (via main app)
        customer_details = self.data_manager.get_customer_details()

        # 4. Prompt for filename
        try:
            filename = asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Documents", "*.pdf"), ("All Files", "*.*")],
                title="Save Invoice As...",
                parent=self,
            )
            if not filename:
                return  # User cancelled

            # 5. Call create_invoice_pdf
            success, message = create_invoice_pdf(
                filename,
                customer_details,
                invoice_details,
                cart_data_with_hsn,
                self.final_costs,
            )

            if success:
                messagebox.showinfo(
                    "Success", f"Successfully saved invoice to {filename}", parent=self
                )
                self.destroy()
            else:
                messagebox.showerror(
                    "Error", f"Failed to generate invoice PDF:\n{message}", parent=self
                )

        except Exception as e:
            messagebox.showerror(
                "Error", f"An unexpected error occurred:\n{e}", parent=self
            )
