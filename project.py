import csv
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Global Data = Class data
students_with_grades = [
    {'Name': 'Roger Rabbit', 'Grade': '72', 'Class': 'Math'},
    {'Name': 'The Rock', 'Grade': '95', 'Class': 'English'},
    {'Name': 'Slenderman', 'Grade': '40', 'Class': 'Film'},
    {'Name': 'Thor - God of Thunder', 'Grade': '60', 'Class': 'Math'},
    {'Name': 'Zelda', 'Grade': '98', 'Class': 'Journalism'},
    {'Name': 'Winnie the Pooh', 'Grade': '80', 'Class': 'Chemistry'},
    {'Name': 'John Doe', 'Grade': '77', 'Class': 'AP Chemistry'},
    {'Name': 'Gandalf', 'Grade': '100', 'Class': 'AP Literature'},
    {'Name': 'Amber Adamson', 'Grade': '90', 'Class': 'History'},
    {'Name': 'Jon Snow', 'Grade': '85', 'Class': 'Physics'},
]

# Convert to CSV file
def convert_to_csv(csv_file):
    try:
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            # Extract the headers from the keys of the first dictionary in the dataset
            headers = list(students_with_grades[0].keys())
            writer.writerow(headers)
            # Write the values for each dictionary
            for data in students_with_grades:
                writer.writerow(data.values())
    except IOError as e:
        print(f"Error occurred while converting dataset to CSV: {e}")

# Send email with CSV file as attachment
def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_file):
    try:
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
    except smtplib.SMTPException as e:
        print(f"Error occurred while sending email: {e}")

# Add a curve to the grades
def add_the_curve():
    try:
        # Each student has an additional 10 points from a curve
        for data in students_with_grades:
            data['Grade'] = str(int(data['Grade']) + 10)
    except Exception as e:
        print(f"Error occurred while processing the dataset: {e}")

def add_to_grades():
    new_data = {}
    new_data["Name"] = input("Enter a new student's name: ")
    new_data["Grade"] = input("Enter a new student's grade: ")
    new_data["Class"] = input("Enter a new student's class: ")
    students_with_grades.append(new_data)


# Sender & Recipient Addresses + Subject and body
sender_email = 'amber.renee.adamson@gmail.com'
sender_password = '[pass]'
receiver_email = 'amber.renee.adamson@gmail.com'
subject = 'CSV file'
Date = datetime.datetime.now()
body = (f"'Attached is the report for {Date}'")

# Run the functions
try:
    add_to_grades()
    add_the_curve()
except Exception as e:
    print(f"Error occurred while processing the dataset: {e}")

# Generate a CSV file
csv_file_path = 'output.csv'
convert_to_csv(csv_file_path)

# Send the CSV file via email
try:
    send_email(sender_email, sender_password, receiver_email, subject, body, csv_file_path)
except Exception as e:
    print(f"Error occurred while sending email: {e}")

