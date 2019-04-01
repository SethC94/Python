from twilio.rest import Client
import time
list = ['8', 'D']
def message_troll():
    global message

    # Your Account SID from twilio.com/console
    account_sid = "AC89d9735b0452435c9ec49b7ab4c07d8e"
    # Your Auth Token from twilio.com/console
    auth_token  = "b6b5fa49c4fa14719c614b43fe991c71"

    client = Client(account_sid, auth_token)

    package = client.messages.create(
        to="+12092211140",
        from_="+16504575970",
        body= message)

    print(package.sid)
while True:
    list.insert(1, '=')
    message = ''.join(list)
    message_troll()
