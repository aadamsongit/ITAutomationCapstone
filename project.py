#first, import the modules:

import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#function to convert to csv file
def convert_to_csv(dataset, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dataset)

#function to send email
def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_file):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    with open(attachment_file, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {attachment_file}')

        message.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(message)
    server.quit()

# placeholder details (to be modified)
dataset = [
    ['Name', 'Age', 'City'],
    ['John Doe', '25', 'New York'],
    ['Jane Smith', '30', 'Los Angeles'],
    ['Mike Johnson', '40', 'Chicago']
]

# Placeholder details (to be modified)
sender_email = 'amber.renee.adamson@gmail.com'
sender_password = 'jqpdqjsyxvugozle'
receiver_email = 'amber.renee.adamson@gmail.com'
subject = 'CSV file'
body = 'Please find the attached CSV file.'

# for loop for data
accumulated_data = []
for data in dataset:
    accumulated_data.append(data)

# generate csv file
csv_file_path = 'output.csv'
convert_to_csv(accumulated_data, csv_file_path)

# send the csv file
send_email(sender_email, sender_password, receiver_email, subject, body, csv_file_path)

