from distlib.compat import raw_input
from fbchat import Client
from fbchat.models import *
import json
import time


def sign_in():
    """Sign in, if no previous session please provide F2A authentication when prompted"""
    email = raw_input("Your email: ")
    password = raw_input("Password: ")
    user = Client(email, password, session_cookies=load_cookies())
    return user


def send_message(sender, recipient):
    """Sending messages to a specific user"""
    message = raw_input("Your message:")
    times = int(input("How many times would you like to send the message:"))
    for i in range(times):
        sender.send(Message(text=message), thread_id=recipient.uid, thread_type=ThreadType.USER)
        time.sleep(2)


def find_user():
    """Find and choose a specific user"""
    users = []
    place = -1
    not_found = True
    # until a user is chosen
    while not_found:
        name = raw_input("Name: ")
        users = client.searchForUsers(name)
        # Printout 4 best matches
        for i, user in enumerate(users[:4], 1):
            print(f'#{i}    {user.name}')
        place = int(input("Enter number, in case the user is not listed, press enter and try their name again:"))
        if 0 <= place <= 3:
            not_found = False
    return users[place-1]


def load_cookies():
    """Load cookies from a json file"""
    try:
        with open('session.json', 'r') as f:
            cookies = json.load(f)
            return cookies
    except:
        pass


def save_cookies(client2):
    """Save cookies after a session, for faster login"""
    with open('session.json', 'w') as f:
        json.dump(client2.getSession(), f)


def send_text_file(file):
    pass


client = sign_in()
session_cookies = client.getSession()
target_user = find_user()
send_message(client, target_user)
save_cookies(client)
