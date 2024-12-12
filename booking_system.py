import datetime
import cowsay

class Diary:
    def __init__(self, festival, birthday, holiday):
        self.festival = festival
        self.birthday = birthday
        self.holiday = holiday
    
    @staticmethod
    def format_date(date):
        return date.strftime('%d/%m/%y')
    def show_festival(self):
        return self.format_date(self.festival)
    def show_birthday(self):
        return self.format_date(self.birthday)
    def show_holiday(self):
        return self.format_date(self.holiday)
    def book_appointment(self, date):
        cowsay.tux(f"Booking appointment for date {date} \nBooking Successful!")
    
class Member:
    def __init__(self, first_name):
        self.first_name = first_name
class Teen(Member):
    def speak(self):
        print(f"Hey! I'm {self.first_name} and I need to make a hair appointment.")
class Adult(Member):
    def speak(self):
        print(f"Good afternoon, My name is {self.first_name} and I want to make a spa appointment.")

class   CustomerDiary(Diary):
    def __init__(self, festival, birthday, holiday, date_format):
        self.date_format = date_format
        super().__init__(festival, birthday, holiday)
    def format_date(self, date):
        return date.strftime(self.date_format)

person = input("Which customer's diary do you want to see: Kris, Maki, Rasi, Varun: ").capitalize().strip()
Kris_diary = CustomerDiary(datetime.date(2024,8,31), datetime.date(2005,12,12), datetime.date(2024,12,25), '%d/%m/%y')
Maki_diary = CustomerDiary(datetime.date(2024,7,12), datetime.date(2007,5,13), datetime.date(2025,1,1), '%d/%m/%y')
Rasi_diary = CustomerDiary(datetime.date(2024,2,29), datetime.date(1973,2,3), datetime.date(2024,12,31), '%d/%m/%y')
Varun_diary = CustomerDiary(datetime.date(2024,4,23), datetime.date(1975,8,4), datetime.date(2025,2,28), '%d/%m/%y')

class PlannedTeen(Teen, Diary):
    pass
class PlannedAdult(Adult, Diary):
    pass

# Quick runthrough to see what the customer request is. This depends on if they are teen or adult. 

if person == 'Kris':
    Kris = PlannedTeen('Kris')
    Kris.speak()
elif person == 'Maki':
    Maki = PlannedTeen('Maki')
    Maki.speak()
elif person == 'Rasi':
    Rasi = PlannedAdult('Rasi')
    Rasi.speak()
elif person == 'Varun':
    Varun = PlannedAdult('Varun')
    Varun.speak()
else:
    raise ValueError("Customer doesn't exist.")

class Expose(Diary):
    def __init__(self, festival, birthday, holiday):
        super().__init__(festival, birthday, holiday)
    event = input(f"Let's see what days they are busy.\nDo you want to see birthday, festival or holiday: ").lower()
    if person == 'Kris':
        if event == 'birthday':
            print("Birthday: " + Kris_diary.show_birthday()+ f"\nThey are free on 2025/1/14")
        elif event == 'festival':
            print("Festival: " + Kris_diary.show_festival()+ f"\nThey are free on 2025/1/14")
        elif event == 'holiday':
            print("Holiday: " + Kris_diary.show_holiday()+ f"\nThey are free on 2025/1/14")
        else:
            raise ValueError("That event doesn't exist.")
        Kris.book_appointment(datetime.date(2025,1,14))
    elif person == 'Maki':
        if event == 'birthday':
            print("Birthday: " + Maki_diary.show_birthday()+ f"\nThey are free on 2025/1/14")
        elif event == 'festival':
            print("Festival: " + Maki_diary.show_festival()+ f"\nThey are free on 2025/1/14")
        elif event == 'holiday':
            print("Holiday: " + Maki_diary.show_holiday()+ f"\nThey are free on 2025/1/14")
        else:
            raise ValueError("That event doesn't exist.")
        Maki.book_appointment(datetime.date(2025,1,14))
    elif person == 'Rasi':
        if event == 'birthday':
            print("Birthday: " + Rasi_diary.show_birthday()+ f"\nThey are free on 2025/1/14")
        elif event == 'festival':
            print("Festival: " + Rasi_diary.show_festival()+ f"\nThey are free on 2025/1/14")
        elif event == 'holiday':
            print("Holiday: " + Rasi_diary.show_holiday()+ f"\nThey are free on 2025/1/14")
        else:
            raise ValueError("That event doesn't exist.")
        Rasi.book_appointment(datetime.date(2025,1,14))
    elif person == 'Varun':
        if event == 'birthday':
            print("Birthday: " + Varun_diary.show_birthday()+ f"\nThey are free on 2025/1/14")
        elif event == 'festival':
            print("Festival: " + Varun_diary.show_festival()+ f"\nThey are free on 2025/1/14")
        elif event == 'holiday':
            print("Holiday: " + Varun_diary.show_holiday()+ f"\nThey are free on 2025/1/14")
        else:
            raise ValueError("That event doesn't exist.")
        Varun.book_appointment(datetime.date(2025,1,14))
    else:
        pass
    



