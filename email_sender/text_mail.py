import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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


data = {'members': [{'email': 'netore2740@oprevolt.com', 'name': 'johnwick', 'userType': 'User'}, {'email': 'netore2740@oprevolt.com', 'name': 'Jesse Pinkman', 'userType': 'User'}]}

for i in data["members"]:
    emails = i["email"]
    name = i["name"]
    usertype = i["userType"]
    print("Email sent to : " + str(name) + " the email is " + str(emails) + " and usertype is " + usertype + ".")



def invite_mail(data):
        try:
            for i in data["members"]:
                EMAIL = i["email"]
                NAME = i["name"]
                USERTYPE = i["userType"]
                PROJECT_NAME = "project management tool"
                HOST = "smtp.gmail.com"
                PORT = 587
                FROM_EMAIL = "managementproject12345678@gmail.com"
                TO_EMAIL = EMAIL
                print(TO_EMAIL)
                print(data)
                APP_PASSWORD = {PROJECT_NAME: 'dqhq oubw cepe caas'}
                PROJECT_LINK = "https://expertzlabin.netlify.app/"

                SUBJECT = f"""Mail sent using Python to {NAME}"""

                BODY = f"""
                Hi all about python,
                This email is sent using a test account.
                thanks,
                Test Account

                Project link: {PROJECT_LINK}
                """

                message = MIMEMultipart()
                message['From'] = FROM_EMAIL
                message['To'] = TO_EMAIL
                message['Subject'] = SUBJECT

                message.attach(MIMEText(BODY, 'plain'))

                smtp = smtplib.SMTP(HOST, PORT)

                status_code, response = smtp.ehlo()
                print(f"[*]Starting TLS connection: {status_code} {response}")

                status_code, response = smtp.starttls()
                print(f"[*]Starting TLS connection: {status_code} {response}")

                status_code, response = smtp.login(FROM_EMAIL, APP_PASSWORD.get(PROJECT_NAME))
                print(f"[*]Starting TLS connection: {status_code} {response}")

                smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
                print("Email sent to : " + str(NAME) + " the email is " + str(EMAIL) + " and usertype is " + USERTYPE)
                smtp.quit()
                return {
                    'message': 'Invitation email sent successfully', 
                    'status': 200
                }

        except Exception as e:
            print(e)
            return {'error': 'Internal Server Error'}, 500
        


invite_mail(data)