import os
import csv
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

# Global Data = Class data
students_with_grades = [
    {'Name': 'Roger Rabbit', 'Grade': '72', 'Class': 'Math'},
    {'Name': 'The Rock', 'Grade': '95', 'Class': 'English'},
    {'Name': 'Slenderman', 'Grade': '40', 'Class': 'English'},
    {'Name': 'Thor - God of Thunder', 'Grade': '60', 'Class': 'History'},
    {'Name': 'Zelda', 'Grade': '98', 'Class': 'Math'},
    {'Name': 'Winnie the Pooh', 'Grade': '80', 'Class': 'History'},
    {'Name': 'John Doe', 'Grade': '77', 'Class': 'English'},
    {'Name': 'Gandalf', 'Grade': '100', 'Class': 'Math'},
    {'Name': 'Amber Adamson', 'Grade': '90', 'Class': 'History'},
    {'Name': 'Jon Snow', 'Grade': '85', 'Class': 'Math'},
    {'Name': 'Bee Tee Dubs', 'Grade': '70', 'Class': 'English'}
]

# Convert to CSV file
def convert_to_csv(csv_files):
    try:
        for csv_file in csv_files:
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
def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_files):
    try:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        for attachment_file in attachment_files:
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

def add_to_grades(data=None):
    new_data = {}
    new_data["Name"] = input("Enter a new student's name: ")
    new_data["Grade"] = input("Enter a new student's grade: ")
    new_data["Class"] = input("Enter a new student's class: ")
    students_with_grades.append(new_data)

    # Update the class-specific DataFrame
    class_df = pd.DataFrame(students_with_grades)
    class_name_lower = students_with_grades[-1]['Class'].lower()
    class_df.to_csv(f"{class_name_lower}_grades.csv", index=False)

def csv_file_sort():

    # read DataFrame
    data = pd.read_csv("output.csv")
 
    subject_math = data[data['Class'] == 'Math']
    subject_history = data[data['Class'] == 'History']
    subject_english = data[data['Class'] == 'English']
 
    subject_math.to_csv('math_grades.csv', index=False)
    subject_english.to_csv('english_grades.csv', index=False)
    subject_history.to_csv('history_grades.csv', index=False)
 
    return ['math_grades.csv', 'english_grades.csv', 'history_grades.csv']

def average_the_grades():
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(students_with_grades)

    # Convert the 'Grade' column to numeric values
    df['Grade'] = pd.to_numeric(df['Grade'])

    # Calculate the average grades for each class
    class_averages = df.groupby('Class')['Grade'].mean()

    for class_name_byaverage, average in class_averages.items():
        if average > 85:
            print(f"The students of {class_name_byaverage} performed very well!")
        elif 85 > average > 70:
            print(f"The students of {class_name_byaverage} need more practice.")
        else:
            print(f"The students of {class_name_byaverage} need tutoring and remedial lessons. Please closely monitor progress.")

# Convert the class averages to a dictionary
    class_averages_dict = class_averages.to_dict()

    return class_averages_dict

# Sender & Recipient Addresses + Subject and body
sender_email = 'amber.renee.adamson@gmail.com'
sender_password = os.environ.get('SENDER_PASSWORD')
receiver_email = 'amber.renee.adamson@gmail.com'
# subject = 'Grade Report'
# Date = datetime.datetime.now()
# body = (f"'Attached is the report for {Date}'")
# csv_file_paths = csv_file_sort()

def main():
    try:
        add_to_grades()
        add_the_curve()
        csv_file_paths = csv_file_sort()

        # Sort the data by class
        sorted_data = sorted(students_with_grades, key=lambda x: x['Class'].lower())

        # Clear the contents of the CSV files
        for csv_file in csv_file_paths:
            open(csv_file, 'w').close()

        # Update the CSV files with the sorted data
        for data in sorted_data:
            class_name_lower = data['Class'].lower()
            class_df = pd.DataFrame([data])
            class_df.to_csv(f"{class_name_lower}_grades.csv", mode='a', header=False, index=False)

        # Display the sorted data
        for data in sorted_data:
            print(f"Name: {data['Name']}, Grade: {data['Grade']}, Class: {data['Class']}")

        # Send email for each class separately
        for csv_file in csv_file_paths:
            class_name = csv_file.split('_')[0].capitalize()  # Extract class name from file name
            subject = f'{class_name} Grade Report'
            body = f'Attached is the grade report for {class_name}'
            attachment_files = [csv_file]

            # Send the email for the current class
            print(f"Sending {class_name} email...")
            send_email(sender_email, sender_password, receiver_email, subject, body, attachment_files)
            print(f"{class_name} email sent successfully.")

        average_the_grades()

        convert_to_csv(csv_file_paths)

    except Exception as e:
        print(f"Error occurred while processing the dataset: {e}")

main()


