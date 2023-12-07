# libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from functools import partial
import sys
import json

# tools
sys.path.insert(0, './tools/')
import amplifydocx as ampdocx
import amplifyImage as ampimg

# Strings
STRINGSFILE = open("strings.json")
STRINGS = json.loads(STRINGSFILE.read())

# Tkinter GUI
fontScale = 3
windowScale = 4

class App:
    def __init__(self, master, font):
        self.font = font
        self.master = master
        master.title(STRINGS["title"])
        master.geometry(str(300*windowScale)+"x"+str(200*windowScale))

        # Create buttons for each function
        self.btn_resize_font = tk.Button(master, text=STRINGS["resize_font_menu"], command=self.open_resize_font_window, font=self.font)
        self.btn_resize_font.pack(pady=10)

        self.btn_amplify_image = tk.Button(master, text=STRINGS["resize_image_menu"], command=self.open_amplify_image_window, font=self.font)
        self.btn_amplify_image.pack(pady=10)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def validate(self, path, factor):
        if path == "" or path == None:
            return STRINGS["error_empty_path"]
        if factor == "" or factor == None:
            return STRINGS["error_empty_factor"]
        try:
            factor = int(factor)
        except Exception as e:
            return STRINGS["error_NaN_factor"]
        if factor <= 0:
            return STRINGS["error_low_factor"]
        return None

    def enable_execution_button(self, button, file_entry, resize_entry):
        button.config(state=tk.NORMAL if file_entry.get() and resize_entry.get() else tk.DISABLED)

    def replace_entry_text(self, entry_widget, fileType, fileExt):
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[(fileType, fileExt), ("All files", "*.*")])
        if file_path:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, file_path)
            self.enable_execution_button(btn_execute, file_path_entry, entry_resize_factor)

    def open_resize_font_window(self):
        self.clear_window()

        # Create a frame to organize widgets
        input_frame = tk.Frame(self.master)
        input_frame.pack(pady=10)

        # File Path Widgets
        lbl_docx_path = tk.Label(input_frame, text=STRINGS["resize_font_path"], font=self.font)
        lbl_docx_path.grid(row=0, column=0, pady=5)

        file_path_entry = tk.Entry(input_frame, font=self.font)
        file_path_entry.grid(row=0, column=1, padx=0, pady=5)

        file_dialog_button = tk.Button(input_frame, text=STRINGS["get_file_path"], command=lambda: self.replace_entry_text(file_path_entry, "Word Documents", "*.docx *.doc"), font=self.font)
        file_dialog_button.grid(row=0, column=2, pady=5)

        # Resize Factor Widgets
        lbl_resize_factor = tk.Label(input_frame, text=STRINGS["resize_font_factor"], font=self.font)
        lbl_resize_factor.grid(row=1, column=0, pady=5)

        entry_resize_factor = tk.Spinbox(input_frame, from_=0, to=1000, textvariable=2, font=self.font)
        entry_resize_factor.grid(row=1, column=1, pady=5)

        # Execution Button
        btn_execute = tk.Button(self.master, text=STRINGS["resize_font_submit"], command=lambda: message_label.config(text=self.execute_resize_font(
            file_path_entry.get(), entry_resize_factor.get())), font=self.font)
        btn_execute.pack(pady=10)

        # Messages Label
        message_label = tk.Label(self.master, text="", font=self.font, fg="green")
        message_label.pack(pady=5)

        # Back Button
        btn_back = tk.Button(self.master, text=STRINGS["back"], command=self.reset_main_menu, font=self.font)
        btn_back.pack(pady=10, side=tk.BOTTOM)

    def execute_resize_font(self, docx_path, resize_factor):
        status = self.validate(docx_path, resize_factor)
        if status != None:
            return status
        ampdocx.resize_font(docx_path, resize_factor)

    def open_amplify_image_window(self):
        self.clear_window()

        # Create a frame to organize widgets
        input_frame = tk.Frame(self.master)
        input_frame.pack(pady=10)

        # File Path Widgets
        lbl_img_path = tk.Label(input_frame, text=STRINGS["resize_image_path"], font=self.font)
        lbl_img_path.grid(row=0, column=0, pady=5)

        file_path_entry = tk.Entry(input_frame, font=self.font)
        file_path_entry.grid(row=0, column=1, padx=0, pady=5)

        file_dialog_button = tk.Button(input_frame, text=STRINGS["get_file_path"], command=lambda: self.replace_entry_text(file_path_entry, "Image Files", "*.png *.jpg *.jpeg *.gif"), font=self.font)
        file_dialog_button.grid(row=0, column=2, pady=5)

        # Resize Factor Widgets
        lbl_resize_factor = tk.Label(input_frame, text=STRINGS["resize_image_factor"], font=self.font)
        lbl_resize_factor.grid(row=1, column=0, pady=5)

        entry_resize_factor = tk.Spinbox(input_frame, from_=0, to=1000, textvariable=2, font=self.font)
        entry_resize_factor.grid(row=1, column=1, pady=5)

        # Execution Button
        btn_execute = tk.Button(self.master, text=STRINGS["resize_image_submit"], command=lambda: message_label.config(text=self.execute_amplify_image(
            file_path_entry.get(), entry_resize_factor.get())), font=self.font)
        btn_execute.pack(pady=10)

        # Messages Label
        message_label = tk.Label(self.master, text="", font=self.font, fg="green")
        message_label.pack(pady=5)

        # Back Button
        btn_back = tk.Button(self.master, text=STRINGS["back"], command=self.reset_main_menu, font=self.font)
        btn_back.pack(pady=10, side=tk.BOTTOM)

    def execute_amplify_image(self, input_path, resize_factor):
        status = self.validate(input_path, resize_factor)
        if status != None:
            return status
        amplify_image(input_path, input_path, amplify_factor)

    def reset_main_menu(self):
        self.clear_window()
        self.__init__(self.master, self.font)

if __name__ == "__main__":
    root = tk.Tk()
    font = font.Font(family="Times New Roman", size=11*fontScale)
    app = App(root, font)
    root.mainloop()
