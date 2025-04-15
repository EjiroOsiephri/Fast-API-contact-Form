import os
from twilio.rest import Client

def send_sms(data):
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    message = f"New message from {data.name} via {data.preferred_contact}. Email: {data.email}. Msg: {data.message}"
    try:
        client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=os.getenv("RECEIVER_PHONE")
        )
    except Exception as e:
        print(f"Twilio error: {e}")
