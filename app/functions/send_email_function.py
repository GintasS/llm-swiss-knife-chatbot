import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.constants import EMAIL_FUNCTION

def send_email(subject, body, to_email):
  """
  Send an email using the specified subject, body, and recipient email address.

  :param subject: str, the subject of the email
  :param body: str, the body content of the email
  :param to_email: str, the recipient's email address
  :return: str, a message indicating the result of the email sending operation

  This function constructs an email message using the provided subject and body,
  and sends it to the specified recipient email address using Gmail's SMTP server.
  It requires a valid Gmail account and app password for authentication.
  """

  msg = MIMEMultipart()
  msg['From'] = EMAIL_FUNCTION.EMAIL_ADDRESS
  msg['To'] = to_email
  msg['Subject'] = subject

  # Attach the body with the msg instance
  msg.attach(MIMEText(body, 'plain'))

  try:
    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the server
    server.login(msg['From'], EMAIL_FUNCTION.EMAIL_PASSWORD)

    # Send the email
    server.sendmail(msg['From'], to_email, msg.as_string())

    # Disconnect from the server
    server.quit()

    return "Email sent successfully."
  except Exception as e:
    print(f"Failed to send email. Error: {e}")
    return None
