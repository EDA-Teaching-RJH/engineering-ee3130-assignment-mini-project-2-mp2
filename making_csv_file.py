import pandas as pd
import seaborn as sns

student_theory_dict = [
    { 'Name': 'Croca', 'Email': '54Croca@gmail.com', 'Days': '14', 'Score': '34'},
    { 'Name': 'Chris', 'Email': 'chr1s2@gmail.com', 'Days': '21', 'Score': '37'},
    { 'Name': 'Arthur', 'Email': 'Arthur2@gmail.com', 'Days': '27', 'Score': '43'},
    { 'Name': 'Sharon', 'Email': 'Shar0n@gmail.com', 'Days': '32', 'Score': '65'},
    { 'Name': 'Ruby', 'Email': 'ruby12@gmail.com', 'Days': '43', 'Score': '76'},
    { 'Name': 'Touca', 'Email': '11touCa@gmail.com', 'Days': '44', 'Score': '83'},
    { 'Name': 'Michelle', 'Email': 'mimmi@gmail.com', 'Days': '57', 'Score': '84'},
    { 'Name': 'Ramya', 'Email': 'Ramya@gmail.com', 'Days': '65', 'Score': '85'},
    { 'Name': 'Kris', 'Email': 'kris65@gmail.com', 'Days': '66', 'Score': '89'},
    { 'Name': 'Rahul', 'Email': 'Rahul564@gmail.com', 'Days': '75', 'Score': '90'},
    { 'Name': 'Vilas', 'Email': 'Vilas26@gmail.com', 'Days': '89', 'Score': '99'}
]
    


student_practical_dict = [
    { 'Name': 'Bob', 'Email': 'bobRoss@gmail.com','Days': '15', 'Score': '21'},
    { 'Name': 'Gina', 'Email': 'ginawill4@gmail.com','Days': '20', 'Score': '23'},
    { 'Name': 'Warner', 'Email': 'bRos@gmail.com','Days': '23', 'Score': '23'},
    { 'Name': 'Prisha', 'Email': 'prishvish@gmail.com','Days': '32', 'Score': '53'},
    { 'Name': 'Sung', 'Email': 'sungSing@gmail.com','Days': '34', 'Score': '54'},
    { 'Name': 'Mark', 'Email': 'markie@gmail.com','Days': '55', 'Score': '56'},
    { 'Name': 'Misca', 'Email': 'misca4@gmail.com','Days': '59', 'Score': '67'},
    { 'Name': 'Ophelia', 'Email': 'ophelia34@gmail.com','Days': '67', 'Score': '74'},
    { 'Name': 'Tia', 'Email': '12tia5@gmail.com','Days': '69', 'Score': '89'},
    { 'Name': 'Konilaven', 'Email': 'konimw@gmail.com','Days': '72', 'Score': '99'}
]

def csv_main():
    df = pd.DataFrame(student_theory_dict)
    df.to_csv('student_theory_data.csv', index = False)

    dff = pd.DataFrame(student_practical_dict)
    dff.to_csv('student_practical_data.csv', index = False)

if __name__ == "__csv_main__":
    csv_main()