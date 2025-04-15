import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(data):
    message = Mail(
        from_email='your_verified_email@example.com',
        to_emails=os.getenv("RECEIVER_EMAIL"),
        subject='New Contact Form Submission',
        html_content=f"""
        <strong>Name:</strong> {data.name}<br>
        <strong>Email:</strong> {data.email}<br>
        <strong>Message:</strong> {data.message}<br>
        <strong>Phone:</strong> {data.phone}<br>
        <strong>WhatsApp:</strong> {data.whatsapp}<br>
        <strong>Preferred Contact:</strong> {data.preferred_contact}
        """,
    )
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(f"SendGrid error: {e}")
