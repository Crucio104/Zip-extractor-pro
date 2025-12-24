import zipfile
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class ZipExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zip Extractor Pro")
        self.root.geometry("750x500")
        self.root.resizable(False, False)
        
        self.bg_color = "#f0f2f5"
        self.primary_color = "#4A90E2"
        self.secondary_color = "#50C878"
        self.text_color = "#2c3e50"
        self.card_color = "#ffffff"
        
        self.root.configure(bg=self.bg_color)

        self.zip_path = tk.StringVar()
        self.extract_path = tk.StringVar()

        self.zip_path.trace_add("write", self.check_inputs)
        self.extract_path.trace_add("write", self.check_inputs)

        self.create_widgets()
        self.extract_button.config(state=tk.DISABLED)

    def create_widgets(self):
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="📦 Zip Extractor Pro",
            font=("Segoe UI", 24, "bold"),
            bg=self.primary_color,
            fg="white"
        )
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Extract ZIP files quickly and easily",
            font=("Segoe UI", 10),
            bg=self.primary_color,
            fg="#e8f4f8"
        )
        subtitle_label.pack()

        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill="both", expand=True, padx=30, pady=30)

        zip_card = tk.Frame(main_container, bg=self.card_color, relief="flat", bd=0)
        zip_card.pack(fill="x", pady=(0, 20))
        
        zip_inner = tk.Frame(zip_card, bg=self.card_color)
        zip_inner.pack(padx=25, pady=20)
        
        tk.Label(
            zip_inner,
            text="📁 ZIP File to Extract",
            font=("Segoe UI", 12, "bold"),
            bg=self.card_color,
            fg=self.text_color
        ).grid(row=0, column=0, sticky="w", columnspan=3, pady=(0, 10))
        
        self.zip_entry = tk.Entry(
            zip_inner,
            textvariable=self.zip_path,
            width=50,
            font=("Segoe UI", 10),
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightcolor=self.primary_color
        )
        self.zip_entry.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        
        self.zip_browse_btn = tk.Button(
            zip_inner,
            text="🔍 Browse",
            command=self.browse_zip,
            bg=self.primary_color,
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.zip_browse_btn.grid(row=1, column=1)
        self.zip_browse_btn.bind("<Enter>", lambda e: self.on_hover(e, self.zip_browse_btn, "#3a7bc8"))
        self.zip_browse_btn.bind("<Leave>", lambda e: self.on_leave(e, self.zip_browse_btn, self.primary_color))

        extract_card = tk.Frame(main_container, bg=self.card_color, relief="flat", bd=0)
        extract_card.pack(fill="x", pady=(0, 20))
        
        extract_inner = tk.Frame(extract_card, bg=self.card_color)
        extract_inner.pack(padx=25, pady=20)
        
        tk.Label(
            extract_inner,
            text="📂 Destination Folder",
            font=("Segoe UI", 12, "bold"),
            bg=self.card_color,
            fg=self.text_color
        ).grid(row=0, column=0, sticky="w", columnspan=3, pady=(0, 10))
        
        self.extract_entry = tk.Entry(
            extract_inner,
            textvariable=self.extract_path,
            width=50,
            font=("Segoe UI", 10),
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightcolor=self.primary_color
        )
        self.extract_entry.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        
        self.extract_browse_btn = tk.Button(
            extract_inner,
            text="🔍 Browse",
            command=self.browse_extract,
            bg=self.primary_color,
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.extract_browse_btn.grid(row=1, column=1)
        self.extract_browse_btn.bind("<Enter>", lambda e: self.on_hover(e, self.extract_browse_btn, "#3a7bc8"))
        self.extract_browse_btn.bind("<Leave>", lambda e: self.on_leave(e, self.extract_browse_btn, self.primary_color))

        self.progress = ttk.Progressbar(
            main_container,
            orient="horizontal",
            length=500,
            mode="determinate"
        )
        
        self.progress_label = tk.Label(
            main_container,
            text="",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        
        button_frame = tk.Frame(main_container, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        self.extract_button = tk.Button(
            button_frame,
            text="✨ Extract ZIP File",
            command=self.extract_zip,
            bg=self.secondary_color,
            fg="white",
            font=("Segoe UI", 14, "bold"),
            relief="flat",
            cursor="hand2",
            padx=40,
            pady=15,
            width=20
        )
        self.extract_button.pack()
        self.extract_button.bind("<Enter>", lambda e: self.on_hover(e, self.extract_button, "#3da865"))
        self.extract_button.bind("<Leave>", lambda e: self.on_leave(e, self.extract_button, self.secondary_color))

        self.status_label = tk.Label(
            main_container,
            text="",
            font=("Segoe UI", 9, "italic"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.status_label.pack(pady=(10, 0))

    def on_hover(self, event, button, color):
        button.config(bg=color)

    def on_leave(self, event, button, color):
        if button["state"] != "disabled":
            button.config(bg=color)

    def browse_zip(self):
        file_path = filedialog.askopenfilename(
            title="Select a ZIP file",
            filetypes=[("ZIP Files", "*.zip"), ("All Files", "*.*")]
        )
        if file_path:
            self.zip_path.set(file_path)
            self.status_label.config(text="✓ ZIP file selected", fg=self.secondary_color)

    def browse_extract(self):
        dir_path = filedialog.askdirectory(title="Select destination folder")
        if dir_path:
            self.extract_path.set(dir_path)
            self.status_label.config(text="✓ Destination folder selected", fg=self.secondary_color)

    def check_inputs(self, *args):
        if self.zip_path.get() and self.extract_path.get():
            self.extract_button.config(state=tk.NORMAL)
            self.status_label.config(text="✓ Ready to extract!", fg=self.secondary_color)
        else:
            self.extract_button.config(state=tk.DISABLED, bg="#cccccc")
            if not self.zip_path.get() and not self.extract_path.get():
                self.status_label.config(text="Select a ZIP file and a destination folder", fg="#95a5a6")

    def extract_zip(self):
        zip_file = self.zip_path.get()
        extract_to = self.extract_path.get()

        self.progress['value'] = 0
        self.progress.pack(pady=10)
        self.progress_label.pack()
        self.extract_button.config(state=tk.DISABLED)
        self.root.update()

        try:
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                file_list = zip_ref.namelist()
                total_files = len(file_list)
                
                for index, file in enumerate(file_list, 1):
                    zip_ref.extract(file, extract_to)
                    
                    progress_percent = (index / total_files) * 100
                    self.progress['value'] = progress_percent
                    
                    file_name = os.path.basename(file) if os.path.basename(file) else "folder"
                    self.status_label.config(
                        text=f"⏳ Extracting: {file_name}",
                        fg=self.primary_color
                    )
                    self.progress_label.config(text=f"{int(progress_percent)}%")
                    
                    self.root.update_idletasks()
            
            self.progress.pack_forget()
            self.progress_label.pack_forget()
            self.extract_button.config(state=tk.NORMAL)
            
            self.status_label.config(text="Extraction completed successfully!", fg=self.secondary_color)
            messagebox.showinfo(
                "Success",
                f"Files extracted successfully to:\n{extract_to}\n\nTotal files: {total_files}",
                icon="info"
            )
        except Exception as e:
            self.progress.pack_forget()
            self.progress_label.pack_forget()
            self.extract_button.config(state=tk.NORMAL)
            
            self.status_label.config(text="Error during extraction", fg="#e74c3c")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ZipExtractorApp(root)
    root.mainloop()