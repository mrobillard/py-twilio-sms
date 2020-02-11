import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("ACCOUNT_ID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages \
               .create(
                    body="This is a test.",
                    from_='+1XXXXXXXXXX',
                    to='+1XXXXXXXXXX'
                )

print(message.sid)
