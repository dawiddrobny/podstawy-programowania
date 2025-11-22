from emails import email_sender, email_recipient, email_subject, email_body


sender = email_sender()
print(f"Sender: {sender}")

recipient = email_recipient()
print(f"Recipient: {recipient}")

subject = email_subject()
print(f"Subject: {subject}")

body = email_body()
print(f"Body:\n{body}")
