import pytest
from driving_center_data import email
from driving_center_data import secret_code
from driving_center_data import missing_student
from driving_center_data import student_data
def main():
    test_email()
    test_code()
    test_missing_student()
    test_value_error_checks()

def test_email():
    try:
        assert email("rAMya2@gmail.com") == "rAMya2@gmail.com"
        assert email("Ramya@kent.ac.uk") == "Email is not valid."
    except (AssertionError):
        print("The email given is not correct.")

def test_code():
    try:
        assert secret_code('10') == True
        assert secret_code('9') == False
        assert secret_code('35') == False
    except (AssertionError):
        print("The code does not match the response expected.")

def test_missing_student():
    try:
        assert missing_student("theory") == True
        assert missing_student("TheoRy") == True
        assert missing_student("pRactical") == True
    except AssertionError:
        print("Choice given is not equal to expected response.")

def test_value_error_checks():
    with pytest.raises(ValueError):
        missing_student("random") 
    with pytest.raises(ValueError):
        missing_student("prs35!") 
    with pytest.raises(ValueError):
        student_data("wha2t")

if __name__ == "__name__":
    main()