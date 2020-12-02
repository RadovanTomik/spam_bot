import tkinter as tk
from tkinter import Label, ttk

from spam_bot import CustomClient


class LoginPage(tk.Tk):
    """A login page GUI for submitting email and password"""

    def __init__(self):
        """Create an instance of LoginPage"""
        tk.Tk.__init__(self)
        self.geometry("300x250")
        Label(self, text="Please enter your facebook credentials:").pack()
        Label(self, text="").pack()
        Label(self, text="Email").pack()
        self.username_entry = tk.Entry(self, textvariable="Email", width=30)
        self.username_entry.pack()
        Label(self, text="").pack()
        Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, textvariable="Password", show='*')
        self.password_entry.pack()
        Label(self, text="").pack()
        self.button = tk.Button(self, text="Login", width=10, height=1, command=self.submit)
        self.button.pack()
        self.password = None
        self.username = None
        self.mainloop()

    def submit(self):
        """Command to submit the entered data after the button is clicked"""
        self.withdraw()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.quit()


class MainPage(tk.Tk):
    """Main page GUI for operations"""
    def __init__(self):
        """Create an instance of MainPage"""
        tk.Tk.__init__(self)
        self.geometry("500x500")
        self.message = None
        self.target = None
        self.user = CustomClient
        self.list = ttk.Combobox(textvariable=self.target).grid(row=1, column=0)
        Label(self, text="Search for user:").grid(row=0, column=0)
        #self.text = tk.Text(self, height=5, width=30, textvariable=self.message).grid(row=2, column=1)
        #self.send_message = tk.Button(self, text="Send Message", width=12, height=1, command=self.user.send_message)\
            #.grid(row=3, column=0)
        self.mainloop()
