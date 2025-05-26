import os
import zipfile
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import tkinter as tk
from datetime import datetime

from compress import compress_file
from decompress import decompress_file
from cleanup import delete_file

# Fixed output directory
OUTPUT_DIR = r"C:\Users\matei\Desktop\Algoritm\LZMA"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def unique_path(path):
    """
    Return a unique file path by appending a counter if the file exists.
    E.g., file.txt -> file(1).txt, file(2).txt, etc.
    """
    base, ext = os.path.splitext(path)
    counter = 1
    new_path = path
    while os.path.exists(new_path):
        new_path = f"{base}({counter}){ext}"
        counter += 1
    return new_path

class DarkApp(ttk.Window):
    def __init__(self):
        super().__init__(themename='darkly')
        self.title('Aplicație de Compresie & Decompresie')
        self.geometry('700x500')
        self.resizable(False, False)

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill=BOTH, padx=20, pady=20)

        self.comp_tab = ttk.Frame(notebook)
        self.decomp_tab = ttk.Frame(notebook)

        notebook.add(self.comp_tab, text='Comprimare')
        notebook.add(self.decomp_tab, text='Decompresare')

        self.setup_comp()
        self.setup_decomp()

    def setup_comp(self):
        frame = ttk.Frame(self.comp_tab)
        frame.pack(pady=20)

        ttk.Label(frame, text='Fișier de comprimat', font=('Helvetica', 14)).grid(row=0, column=0, pady=5)
        ttk.Button(frame, text='Selectează...', bootstyle=INFO, command=self.upload_comp).grid(row=0, column=1, padx=10)

        self.comp_input = None
        self.comp_output = None

        ttk.Button(self.comp_tab, text='Comprimă', bootstyle=SUCCESS, command=self.run_comp).pack(pady=10)
        ttk.Button(self.comp_tab, text='Șterge Comprimat', bootstyle=DANGER, command=self.clean_comp).pack()

    def upload_comp(self):
        f = filedialog.askopenfilename(
            title='Selectează fișier',
            filetypes=[('Toate fișierele', '*.*'), ('Fișiere Text', '*.txt'), ('PDF', '*.pdf'), ('Word', '*.doc;*.docx')]
        )
        if f:
            self.comp_input = f
            input_filename = os.path.basename(f)
            name_wo_ext, _ = os.path.splitext(input_filename)
            # Compressed output always in OUTPUT_DIR
            out_path = os.path.join(OUTPUT_DIR, f"{name_wo_ext}_compressed.zip")
            self.comp_output = unique_path(out_path)

    def run_comp(self):
        if not self.comp_input:
            messagebox.showerror('Eroare', 'Selectează un fișier')
            return
        try:
            compress_file(self.comp_input, self.comp_output)
            messagebox.showinfo('Succes', f'Comprimat în: {self.comp_output}')
        except Exception as e:
            messagebox.showerror('Eroare', str(e))

    def clean_comp(self):
        if not self.comp_output:
            messagebox.showwarning('Avertisment', 'Nimic de șters')
            return
        delete_file(self.comp_output)

    def setup_decomp(self):
        frame = ttk.Frame(self.decomp_tab)
        frame.pack(pady=20)

        ttk.Label(frame, text='Fișier de decompresat', font=('Helvetica', 14)).grid(row=0, column=0, pady=5)
        ttk.Button(frame, text='Selectează...', bootstyle=INFO, command=self.upload_decomp).grid(row=0, column=1, padx=10)

        self.decomp_input = None
        self.decomp_output = None

        ttk.Button(self.decomp_tab, text='Decomprima', bootstyle=SUCCESS, command=self.run_decomp).pack(pady=10)
        ttk.Button(self.decomp_tab, text='Șterge Decomprimat', bootstyle=DANGER, command=self.clean_decomp).pack()

    def upload_decomp(self):
        f = filedialog.askopenfilename(
            title='Selectează arhivă ZIP',
            filetypes=[('ZIP', '*.zip'), ('Toate fișierele', '*.*')]
        )
        if f:
            self.decomp_input = f
            input_filename = os.path.basename(f)
            base_name, _ = os.path.splitext(input_filename)
            # Determine extension of file inside archive
            with zipfile.ZipFile(f, 'r') as zipf:
                names = zipf.namelist()
                ext = os.path.splitext(names[0])[1] if names else ''
            # Proposed decompressed file path
            proposed = os.path.join(OUTPUT_DIR, f"{base_name}_decompressed{ext}")
            self.decomp_output = unique_path(proposed)

    def run_decomp(self):
        if not self.decomp_input:
            messagebox.showerror('Eroare', 'Selectează arhivă')
            return
        try:
            decompress_file(self.decomp_input, self.decomp_output)
            messagebox.showinfo('Succes', f'Decomprimat în: {self.decomp_output}')
        except Exception as e:
            messagebox.showerror('Eroare', str(e))

    def clean_decomp(self):
        if not self.decomp_output:
            messagebox.showwarning('Avertisment', 'Nimic de șters')
            return
        delete_file(self.decomp_output)

if __name__ == '__main__':
    app = DarkApp()
    app.mainloop()