import tkinter as tk
from tkinter import Label


class LoginPage(tk.Tk):
    """A login page object with for submitting email and password"""

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

    def submit(self):
        """Command to submit the entered data after the button is clicked"""
        self.withdraw()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.quit()
