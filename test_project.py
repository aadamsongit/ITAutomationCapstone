import pytest
from project import main, add_to_grades, add_the_curve, csv_file_sort, average_the_grades, students_with_grades

def test_add_to_grades():
    # Set up test data and inputs
    new_data = {
        "Name": "Test Student",
        "Grade": "90",
        "Class": "Math"
    }

    students_with_grades.clear()

    # Call the function
    add_to_grades(new_data)

    # Check if test student was added
    assert {'Name': 'Test Student', 'Grade': '90', 'Class': 'Math'} in students_with_grades

def test_add_the_curve():
    # Set up test data and inputs
    test_data = [
        {'Name': 'Student 1', 'Grade': '80', 'Class': 'Math'},
        {'Name': 'Student 2', 'Grade': '70', 'Class': 'Math'},
    ]
    expected_data = [
        {'Name': 'Student 1', 'Grade': '90', 'Class': 'Math'},
        {'Name': 'Student 2', 'Grade': '80', 'Class': 'Math'},
    ]

    students_with_grades.clear()
    students_with_grades.extend(test_data)

    # Call the function
    add_the_curve()

    # Check if the grades were curved correctly
    assert test_data == expected_data

def test_csv_file_sort():
    # Set up test data and inputs
    test_data = [
        {'Name': 'Student 1', 'Grade': '80', 'Class': 'Math'},
        {'Name': 'Student 2', 'Grade': '90', 'Class': 'English'},
        {'Name': 'Student 3', 'Grade': '70', 'Class': 'History'},
    ]
    expected_csv_files = ['math_grades.csv', 'english_grades.csv', 'history_grades.csv']

    students_with_grades.clear()
    students_with_grades.extend(test_data)

    # Call the function
    csv_file_paths = csv_file_sort()

    # Check if the CSV files were created correctly
    assert csv_file_paths == expected_csv_files

def test_average_the_grades():
    # Set up test data and inputs
    test_data = [
        {'Name': 'Student 1', 'Grade': '80', 'Class': 'Math'},
        {'Name': 'Student 2', 'Grade': '90', 'Class': 'Math'},
        {'Name': 'Student 3', 'Grade': '70', 'Class': 'English'},
        {'Name': 'Student 4', 'Grade': '85', 'Class': 'English'},
    ]
    expected_averages = {
        'Math': 85.0,
        'English': 77.5,
    }

    students_with_grades.clear()
    students_with_grades.extend(test_data)

    # Call the function
    class_averages = average_the_grades()

    # Check if the class averages were calculated correctly
    assert class_averages == expected_averages

def test_main_function(capsys):

    # Call the main function
    main()

    # Check if the expected output is printed
    captured = capsys.readouterr()  # Capture the printed output
    assert 'Math email sent successfully.' in captured.out

# Run the tests
if __name__ == '__main__':
    pytest.main()
