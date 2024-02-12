# import getpass
# import smtplib

# PROJECT_NAME = "project management tool"

# HOST = "smtp.gmail.com"
# PORT = 587
# FROM_EMAIL = "managementproject12345678@gmail.com"
# TO_EMAIL = "unnimayak109@gmail.com"
# # PASSWORD = getpass.getpass("Enter password: ")
# APP_PASSWORD = {PROJECT_NAME:'dqhq oubw cepe caas'}
# # PASSWORD = "project@9961665408"


# MESSAGE = """Subject: MAil sent using python
# Hi all about python,

# This email is sent using a test account.
# thanks,
# Test Account

# """

# smtp = smtplib.SMTP(HOST,PORT)

# status_code,response =smtp.ehlo()
# print(f"[*]Starting TLS connection: {status_code} {response}")


# status_code,response =smtp.ehlo()
# print(f"[*]Starting TLS connection: {status_code} {response}")

# status_code,response =smtp.starttls()
# print(f"[*]Starting TLS connection: {status_code} {response}")

# status_code,response =smtp.login(FROM_EMAIL,APP_PASSWORD.get(PROJECT_NAME))
# print(f"[*]Starting TLS connection: {status_code} {response}")

# smtp.sendmail(FROM_EMAIL,TO_EMAIL,MESSAGE)
# smtp.quit()


# email = {'members': [{'email': 'athisruthmsatheesh98@gmail.com', 'name': 'Athisruth M Satheesh', 'userType': 'User'}]}

# print(email)
# print(email['members'][0]['email'])
