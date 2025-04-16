import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_email(data):
    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {os.getenv('RESEND_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "from": "Contact Form <onboarding@resend.dev>",  
        "to": [os.getenv("RECEIVER_EMAIL")],
        "subject": "New Contact Form Submission",
        "html": f"""
            <strong>Name:</strong> {data.name}<br>
            <strong>Email:</strong> {data.email}<br>
            <strong>Phone:</strong> {data.phone}<br>
            <strong>WhatsApp:</strong> {data.whatsapp}<br>
            <strong>Message:</strong> {data.message}<br>
            <strong>Preferred Contact:</strong> {data.preferred_contact}
        """
    }

    response = requests.post(url, json=payload, headers=headers)
    print("Resend status:", response.status_code)
    if response.status_code >= 400:
        print("Resend error:", response.text)
