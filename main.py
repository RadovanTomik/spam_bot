from fbchat.models import *
from GUI import *
from spam_bot import sign_in


login = LoginPage()
login.mainloop()
client = sign_in(login.username, login.password)
