import mimetypes
import os
from app.services.exceptions.exceptions import FileNotReadyError
from django.core.mail import EmailMessage

def send_email_with_attachment(subject,body,from_email,to_email,file_path):
    email = EmailMessage(subject, body, from_email, to_email)
    try:
        with open(file_path, "rb") as file:

            file_name = os.path.basename(file_path)
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type is None:
                mime_type = "application/octet-stream"
            email.attach(file_name, file.read(), mime_type)
            email.send()
    except FileNotFoundError:
        raise FileNotReadyError("Please create your files first!")

