import tkinter as tk
from ui.main_app import MainApplication
import os

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Window Quotation")
    root.configure(bg="#f0f0f0")  # Match legacy background

    # Set window icon
    try:
        # Correctly determine the base directory from __main__.py
        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "Images", "MGA Logo.ico")
        root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Could not load window icon: {e}")

    # Create the main application - no packing needed as it creates widgets directly on root
    app = MainApplication(root)
    
    root.mainloop()
