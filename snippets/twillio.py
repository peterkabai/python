from twilio.rest import Client
import os
import set_environ

account_sid = os.environ.get("twillio_sid")
auth_token  = os.environ.get("twillio_token")

client = Client(account_sid, auth_token)

to = os.environ.get("my_number")
twillio = os.environ.get("twillio_number")

text = "Hello, again!"

message = client.messages.create(
    to = to, 
    from_ = twillio,
    body = text
)

print(message.sid)