import tkinter as tk
from tkinter import Label, Button, Entry
from spam_bot import sign_in
from fbchat import Client
from fbchat.models import *


def login_page():
    login_screen = tk.Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    tk.Label(login_screen, text="Please enter login details").pack()
    tk.Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable="username")
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password__login_entry = Entry(login_screen, textvariable="password", show= '*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=password__login_entry.get()).pack()
    login_screen.mainloop()


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("300x250")
        tk.Label(self, text="Please enter login details:").pack()
        tk.Label(self, text="").pack()
        Label(self, text="Email").pack()
        self.username_entry = tk.Entry(self, textvariable="Email", width=30)
        self.username_entry.pack()
        tk.Label(self, text="").pack()
        Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, textvariable="Password", show='*')
        self.password_entry.pack()
        tk.Label(self, text="").pack()
        self.button = tk.Button(self, text="Login", width=10, height=1, command=self.on_button)
        self.button.pack()
        self.password = None
        self.username = None

    def on_button(self):
        self.username=self.username_entry.get()
        self.password=self.password_entry.get()
        self.quit()
