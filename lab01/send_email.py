#pip install gmail
from gmail import GMail, Message

body= '''
'''

mail = GMail("c4e21.nam@gmail.com","a2811994")
msg = Message("Xin nghi", to="phamquynam94@gmail.com", html= body)
mail.send(msg)