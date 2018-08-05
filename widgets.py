import tkinter as tk
from tkinter import ttk

class NormalFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.grid(column=0, row=0, sticky="nwse")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

class HLine(ttk.Separator):
    def __init__(self, parent, *args, **kwargs):
        ttk.Separator.__init__(self, parent, *args, **kwargs, orient="horizontal")
        self.grid(sticky="ew", pady=10, columnspan=2)
        
class TextLabel(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        ttk.Label.__init__(self, parent, *args, **kwargs)
        self.grid(sticky="nw", padx=10, pady=10)
        self.grid_columnconfigure(0,weight=0)
        self.grid_rowconfigure(0,weight=1)

class ShortResponse(tk.Text):
    def __init__(self, parent, *args, **kwargs):
        tk.Text.__init__(self, parent, *args, **kwargs, width = 50, height = 1)
        self.grid(sticky="nw", padx=10, pady=10)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

class LongResponse(tk.Text):
    def __init__(self, parent, *args, **kwargs):
        tk.Text.__init__(self, parent, *args, **kwargs, width = 50, height = 3)
        self.grid(sticky="nw", padx=10, pady=10)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        
class CircleButton(ttk.Radiobutton):
    def __init__(self, parent, *args, **kwargs):
        ttk.Radiobutton.__init__(self, parent, *args, **kwargs)
        self.grid(sticky="nw", padx=10, pady=4)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

class SaveButton(tk.Button):
    def __init__(self, parent, *args, **kwargs):
        ttk.Button.__init__(self, parent, *args, **kwargs)
        self.grid(sticky="ns", padx=10, pady=10)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)