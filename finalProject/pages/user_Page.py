
import tkinter as tk
class user_page(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.ctp()

    def ctp(self):
        self.label = tk.Label(self,text="Hello")
        self.label.pack()