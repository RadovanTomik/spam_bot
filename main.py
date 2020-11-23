from GUI import *
from spam_bot import sign_in


login = SampleApp()
login.mainloop()

client = sign_in(login.username, login.password)
client.send(Message(text="message"), thread_id=client.uid, thread_type=ThreadType.USER)