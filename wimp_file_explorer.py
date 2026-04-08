#!/usr/bin/env python3
"""
WIMP File Explorer with Direct Manipulation
Features: Open files, Save files, Display file contents in text area
"""

import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import os

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple File Explorer")
        self.root.geometry("700x600")
        
        # Current file path
        self.current_file = None
        
        # Create menu bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_command(label="Save File", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="New File", command=self.new_file)
        file_menu.add_command(label="Clear", command=self.clear_text)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        # Create toolbar frame
        toolbar = tk.Frame(root, bg="#f0f0f0", height=50)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Toolbar buttons
        open_button = tk.Button(
            toolbar, 
            text="📂 Open File", 
            command=self.open_file,
            font=("Arial", 10),
            padx=10,
            pady=5
        )
        open_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        save_button = tk.Button(
            toolbar,
            text="💾 Save File",
            command=self.save_file,
            font=("Arial", 10),
            padx=10,
            pady=5
        )
        save_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        new_button = tk.Button(
            toolbar,
            text="📄 New File",
            command=self.new_file,
            font=("Arial", 10),
            padx=10,
            pady=5
        )
        new_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        clear_button = tk.Button(
            toolbar,
            text="🗑️ Clear",
            command=self.clear_text,
            font=("Arial", 10),
            padx=10,
            pady=5
        )
        clear_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        # File info label
        self.info_label = tk.Label(
            root,
            text="No file opened",
            bg="#e0e0e0",
            anchor="w",
            padx=10,
            font=("Arial", 9)
        )
        self.info_label.pack(side=tk.TOP, fill=tk.X)
        
        # Create text area with scrollbar
        text_frame = tk.Frame(root)
        text_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.text_area = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            font=("Courier New", 11),
            undo=True
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_bar = tk.Label(
            root,
            text="Ready",
            bg="#d0d0d0",
            anchor="w",
            padx=10,
            font=("Arial", 9)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Bind keyboard shortcuts
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-n>', lambda e: self.new_file())
    
    def open_file(self):
        """Open and display file contents"""
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, content)
                
                self.current_file = file_path
                file_name = os.path.basename(file_path)
                self.info_label.config(text=f"File: {file_name} | Path: {file_path}")
                self.status_bar.config(text=f"Opened: {file_path}")
                self.root.title(f"File Explorer - {file_name}")
                
                print(f"Selected file: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{str(e)}")
                self.status_bar.config(text="Error opening file")
    
    def save_file(self):
        """Save current content to file"""
        if self.current_file:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                self.status_bar.config(text=f"Saved: {self.current_file}")
                messagebox.showinfo("Success", "File saved successfully!")
                print(f"File saved to: {self.current_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{str(e)}")
                self.status_bar.config(text="Error saving file")
        else:
            self.save_as_file()
    
    def save_as_file(self):
        """Save content to a new file"""
        file_path = filedialog.asksaveasfilename(
            title="Save file as",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                self.current_file = file_path
                file_name = os.path.basename(file_path)
                self.info_label.config(text=f"File: {file_name} | Path: {file_path}")
                self.status_bar.config(text=f"Saved: {file_path}")
                self.root.title(f"File Explorer - {file_name}")
                
                messagebox.showinfo("Success", "File saved successfully!")
                print(f"File saved to: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{str(e)}")
                self.status_bar.config(text="Error saving file")
    
    def new_file(self):
        """Create a new file"""
        if self.text_area.get(1.0, tk.END).strip():
            response = messagebox.askyesno(
                "New File",
                "Current content will be cleared. Continue?"
            )
            if not response:
                return
        
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.info_label.config(text="New file (unsaved)")
        self.status_bar.config(text="New file created")
        self.root.title("File Explorer - New File")
    
    def clear_text(self):
        """Clear the text area"""
        response = messagebox.askyesno(
            "Clear Text",
            "Are you sure you want to clear all text?"
        )
        if response:
            self.text_area.delete(1.0, tk.END)
            self.status_bar.config(text="Text cleared")

def main():
    root = tk.Tk()
    app = FileExplorer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
