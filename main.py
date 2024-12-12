import re 
import csv

import numpy as np
import seaborn as sns

score_list = []
days_list = []
theory_grade_list = []
student_theory_count = []
global scorea1 


def main():
    global choice
    print(f"DRIVERING CENTER INSTRUCTOR REPORT DATA \nHello, please enter your gmail and create a password to sign up.")
    # email("")
    # password("")
    student_data(missing_student(""))
    plotting(score_list)
    grade()

def email(instructor_email):
    while True:
        instructor_email = input("Email: ").strip()
        if re.search(r"^[a-zA-Z0-9]+@gmail.com$", instructor_email):
            return instructor_email
        else:
            print("Email is not valid.")

def password(password):
    while True:
        password = input("Enter the password: ")
        password2 = input("Enter password again: ")
        if password != password2:
            print("The passwords don't match.")
        else:
            return password

def missing_student(choice):
    choice = input(f"There are two types of exams.\nDo you want Theory or Practical student results: ").capitalize()
    if choice == "Theory":
        return choice
    elif choice == "Practical":
        print(f"There is a student's name and email missing in the data.\nThey had score of 27. Complete the missing data.")
        missing_student_name = input("Type first name of student: ").capitalize()
        missing_student_email = input("Type in first part of email(part before @): ")
        if re.search(r"^[a-zA-Z0-9]", missing_student_email):
            pass
        else:
            raise ValueError("Invalid email so student record will be deleted.")
        mse_full = missing_student_email + "@gmail.com"
        new_dict = [{'Name': f'{missing_student_name}', 'Email':f'{mse_full}', 'Score':'27'}]
        with open("student_practical_data.csv", 'a') as csvfile:
            writer = csv.writer(csvfile)
            for item in new_dict:
                writer.writerow(new_dict)
            return choice
        # with open("student_practical_data.csv", 'w', newline='') as csvfile:
        #     row_names = ['Name','Email','Score']
        #     writer = csv.DictWriter(csvfile, fieldnames=row_names)
        #     writer.writerow({'Name': f'{missing_student_name}', 'Email':f'{mse_full}', 'Score':'27'})
        #     return choice
    else:
        raise ValueError("Invalid Test Type.")

def student_data(choice):
    if choice == "Theory":
        print("Here are the names of people and score:")
        with open('student_theory_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("Name: " + row['Name'] + ", Days:" + row["Days"] + ", Score:" +row['Score'])
                score_list.append(row['Score'])
                days_list.append(row["Days"])
            print(score_list)
            return score_list, days_list
        print(score_list)
    elif choice == "Practical":
        with open('student_practical_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("Name: " + row['Name'] + ", Days:" + row["Days"] + ", Score:" +row['Score'])
    else:
        raise ValueError("Invalid Test Type.")


def grade():
    for i in score_list:
        i = int(i)
        if i >= 85:
            theory_grade_list.append('A*')
            scorea1 += 1
        elif i >= 70:
            theory_grade_list.append('A')
        elif i >= 60:
            theory_grade_list.append('B')
        elif i >= 50:
            theory_grade_list.append('C')
        elif i >= 40:
            theory_grade_list.append('D')
        else:
            theory_grade_list.append('F')
    print(theory_grade_list)
    print(scorea1)

    




def plotting(score_list):
    import matplotlib.pyplot as plt
    # days = days_list
    # score = score_list
        # days_list = np.arange(1,100)
        # score_list = np.arange(1,100)
        # plt.scatter(days_list,score_list)
        # plt.show()
    # plt.plot(score)
    # plt.title("Score Achieved")
    # plt.xlabel("Days")
    # plt.ylabel("Score(%)")
    # plt.show()
    # plt.title("Scores Achieved")
    # plt.xlabel("Days")
    # plt.ylabel("Score(%)")
    # plt.plot(t, days, score, color ='red')
    # plt.show()

if __name__ == "__main__":
    main()