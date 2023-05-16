# Project Overview

A high school has reported the grades for students in three core subjects. Initially, the grades have been stored in a data dictionary, along with keys for the students' names and for each subject. These final grades will be assessed with a curve of ten points, and there may be an additional student who needs to be added to the final report.

The tasks that this project aims to automate include sorting the data for the grades into CSV files by subject, then e-mailing each file individually, with the recipient being (implicitly) a parent/guardian, or a school administrator. In addition to sorting the data dictionary into CSV files and generating an email, the code needs to have a function to input an additional student, as well as adding the ten point curve to each grade. 

Finally, the code also needs to average the grades for each class, then generate a print statement to comment on the progress of each of the three classes, either by noting that the students are performing very well and meeting or exceeding expectations, or by making a note that the students may need additional tutoring or remedial assistance.


## User Stories

As a teacher, I want to be able to sort my students' grades by class, so I can easily see their performance in each subject.

As a teacher, I want to send grade reports to parents/guardians via email, so they can stay informed about their child's academic progress.

As a teacher, I want to add a curve to the grades, so students can receive an extra boost in their scores and be rewarded for their efforts.

As a teacher, I want to be able to add new students to the grade system, so I can include them in the overall class performance analysis.

As a teacher, I want to generate an average grade for each class, so I can assess the overall performance and identify areas for improvement.

As a teacher, I want to print notes about the students' progress, so I can provide personalized feedback and recommendations for their academic development.

As a school administrator, I want to ensure that grade reports are securely and efficiently sent to parents/guardians, so that sensitive student data is protected and parents receive accurate information.

As a teacher, I want to have an automated system that handles the sorting, grading, and reporting processes, so that I can save time and focus more on teaching and supporting my students.

## Technical challenges and solutions

While writing and debugging the code for this project, I encountered a few technical challenges. Here are the difficulties I faced, and how I solved them:

Initially, I wanted the code to send an email with all three CSV files attached. The code was sending three emails, one with one CSV file, one with two, and a third with all three. Upon consideration, I decided it would be best to send three emails, each with one CSV file attached per subject, so I refactored the main function with a for loop. 

Another technical challenge concerned the handling of the data. At one point, the CSV files were not taking in every entry in the data dictionary, i.e. when I updated the data dictionary with a new entry, it was not being recognized in the CSV output. Additionally, an entry was appearing that I did not add, and the entry I did add (via the input function) was not showing. I believe that this was a result of a prior input which, for some reason, was sticking in the output CSV file. Creating a sorted_data variable and using a lambda sort with two for loops solved the problem, as it re-sorted the data from the data dictionary. I also removed the print statements from the csv_file_sort function, as they were printing based on the output.csv file, not based on the data dictionary, which was causing confusion. Instead, I used return statements with this function.

When implementing the tests with Pytest, I initially ran into some errors. I had to figure out how to pass new_data into the add_to_grades test function while not using a parameter in definining the test function or its corresponding function in the project file, as it was causing an error in terms of integrating with the add_to_grades function as it was set up in the project file. Using data=None as a parameter in the project file for the add_to_grades function and passing in new_data in the function call for the test project file worked to resolve this issue.

When running the test version of the main function, I encountered an error with the function not recognizing the print statement. I had to double-check the capsys parameter and ensure it was passed to the test function so it would run successfully.

The average_the_grades function did not have a return statement, resulting in a None value being returned. To address this, I modified the function to calculate and return the class averages as a dictionary.

Initially, the test_main_function was throwing errors related to accessing the test_data and expected_output variables. To resolve this, I ensured that the variables were properly accessed within the test function.

Finally, I encountered an error when running the tests due to missing imports. I added the necessary import statements to the test file, such as pytest and other required modules, to resolve the import errors.
