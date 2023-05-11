#first, import the modules:

import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#function to convert to csv file
def convert_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as file:
        lines = file.readlines()

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for line in lines:
            
            row = line.strip().split(',')
            writer.writerow(row)

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
txt_file_path = 'input.txt'
csv_file_path = 'output.csv'
attachment_file_path = csv_file_path
sender_email = 'amber.renee.adamson@gmail.com'
sender_password = '[savedinfile]'
receiver_email = 'amber.renee.adamson@gmail.com'
subject = 'CSV file'
body = 'Please find the attached CSV file.'

# call convert function
convert_to_csv(txt_file_path, csv_file_path)

# call send function to send the file
send_email(sender_email, sender_password, receiver_email, subject, body, attachment_file_path)
