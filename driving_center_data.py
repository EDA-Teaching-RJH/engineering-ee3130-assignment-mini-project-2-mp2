import re 
import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from making_csv_file import csv_main    #made my own library and import here to create csv files. 

score_list = []             #Empty list to collect score data from csv and insert here.
days_list = []              #Empty list to collect score data from csv and insert here.
days_score_coord_list = []  #Empty list to combine score_list and days_list to get coordinated to plot and show correlation.

def main():
    print(f"DRIVERING CENTER INSTRUCTOR REPORT DATA \nHello, please enter your gmail and create a password to sign up.")
    instructor_email = input("Email: ").strip()
    email(instructor_email)
    password("")
    code = input("Write a two digit number between 10-40:(P.S the code is any value below 30): ")   #Type a number between 10-29 to access data.
    secret_code(code)
    csv_main()              #Data only opened/created after secret code is passed.
    choice = input(f"There are two types of exams.\nDo you want Theory or Practical student results: ")
    choice = choice.capitalize()
    plot(student_data(missing_student(choice)))
    
def email(instructor_email):
    """
    This function handles the email given and checks input validation.

    Parameters:
    email(instructor_email)) : The user email

    Returns:
    instructor_email (str): User email saved
    """
    while True:
        if re.search(r"^[a-zA-Z0-9]+@gmail.com$", instructor_email):
            print(instructor_email)
            break
        else:
            print("Email is not valid.")
            instructor_email = input("Email: ").strip()

def password(password):
    """
    This function takes the password given and sees the match of two inputs.

    Parameters:
    password(password) : Password the user want to set

    Returns:
    password (str): User password saved
    """
    while True:
        password = input("Enter the password: ")
        password2 = input("Enter password again: ")
        if password != password2:
            print("The passwords don't match.")
        else:
            return password

def secret_code(code):
    """
    This function lets the user type a number and if it's in range, they can access data.
    """
    check = re.findall("[1-2][0-9]", code)
    if check:
        print("You entered the right code! You can access the data.")
    else:
        print("Incorrect code. You will not be permitted to view data.")
        exit()

def missing_student(choice):
    """
    This function looks at which data the user wants to access.

    Parameters:
    missing_student(choice) : Choose between two datas

    Returns:
    choice (str): The data chosen to view
    """
    if choice == "Theory":
        return choice
    elif choice == "Practical":
        print(f"There is a student's name and email missing in the data.\nThey had score of 99 and no of days 73. \nComplete the missing data.")
        missing_student_name = input("Type first name of student: ").capitalize()
        missing_student_email = input("Type in first part of email(part before @). This has to start with NaMi: ")
        if re.search(r"^\ANaMi\w", missing_student_email):
            pass
        else:
            raise ValueError("Invalid email so student record will be deleted.")
        mse_full = missing_student_email + "@gmail.com"
        with open("student_practical_data.csv", 'a', newline='') as csvfile:
            row_names = ['Name','Email','Days','Score']
            writer = csv.DictWriter(csvfile, fieldnames=row_names)
            writer.writerow({'Name': f'{missing_student_name}', 'Email':f'{mse_full}', 'Days':'73', 'Score':'99'})
            return choice
    else:
        raise ValueError("Invalid Test Type.")
    

def student_data(choice):
    """
    This function handles the data chosen and collects the data onto a list.

    Parameters:
    student_data(choice) : The data chosen to view
    """
    if choice == "Theory":
        print("Here are the names of people and score:")
        with open('student_theory_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("Name: " + row['Name'] + ", Days:" + row["Days"] + ", Score:" +row['Score'])
                score_list.append(row['Score'])
                days_list.append(row["Days"])
            for a, b in zip(days_list, score_list):
                days_score_coord_list.append([a, b])
    elif choice == "Practical":
        with open('student_practical_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("Name: " + row['Name'] + ", Days:" + row["Days"] + ", Score:" +row['Score'])
                score_list.append(row['Score'])
                days_list.append(row["Days"])
            for a, b in zip(days_list, score_list):
                days_score_coord_list.append([a, b])
    else:
        raise ValueError("Invalid Test Type.")

def plot(choice):
    """
    This function takes data on list to plot a graph for user to view.
    """
    data = np.array(days_score_coord_list)
    x, y = data.T
    plt.plot(x,y)
    if choice == 'Theory':
        plt.title("Theory Exam Score with days of practice")
    else:
        plt.title("Practical Exam Score with days of practice")
    plt.xlabel("Days")
    plt.ylabel("Score (%)")
    plt.show()



if __name__ == "__main__":
    main()