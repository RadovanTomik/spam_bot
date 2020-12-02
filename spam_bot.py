from distlib.compat import raw_input
from fbchat import Client
from fbchat.models import *
from tkinter import simpledialog
import json
import time


class CustomClient(Client):
    """Custom subclass for overriding"""
    def on2FACode(self):
        """Override method for submitting 2FA code"""
        return simpledialog.askstring("2FA", 'Please enter your 2FA code')

    @staticmethod
    def sign_in(email, password):
        """Sign in, if no previous session please provide 2FA authentication when prompted"""
        user = CustomClient(str(email), str(password))
        return user

    def send_message(self, recipient):
        """Sending messages to a specific user"""
        message = raw_input("Your message:")
        times = int(input("How many times would you like to send the message:"))
        for i in range(times):
            self.send(Message(text=message), thread_id=recipient.uid, thread_type=ThreadType.USER)
            time.sleep(2)

    def find_user(self):
        """Find and choose a specific user"""
        users = []
        place = -1
        not_found = True
        # until a user is chosen
        while not_found:
            name = raw_input("Name: ")
            users = self.searchForUsers(name)
            # Printout 4 best matches
            for i, user in enumerate(users[:4], 1):
                print(f'#{i}    {user.name}')
            place = int(input("Enter number, in case the user is not listed, press enter and try their name again:"))
            if 0 <= place <= 3:
                not_found = False
        return users[place - 1]

    @staticmethod
    def load_cookies():
        """Load cookies from a json file"""
        try:
            with open('session.json', 'r') as f:
                cookies = json.load(f)
                return cookies
        except FileNotFoundError:
            pass

    def save_cookies(self):
        """Save cookies after a session, for faster login"""
        with open('session.json', 'w') as f:
            json.dump(self.getSession(), f)
