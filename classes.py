import datetime

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
    
class FamilyDiary(Diary):
    def __init__(self, festival, birthday, holiday, date_format):
        self.date_format = date_format
        super().__init__(festival, birthday, holiday)
    def format_date(self, date):
        return date.strftime(self.date_format)

person = input("Which family member diary do you want to see: Kris, Maki, Rasi, Varun: ").capitalize()
event = input("Do you want to see birthday, festival or holiday: ").lower()
Kris_diary = FamilyDiary(datetime.date(2024,8,31), datetime.date(2005,12,12), datetime.date(2024,12,25), '%d/%m/%y')
Maki_diary = FamilyDiary(datetime.date(2024,7,12), datetime.date(2007,5,13), datetime.date(2025,1,1), '%d/%m/%y')
Rasi_diary = FamilyDiary(datetime.date(2024,2,29), datetime.date(1973,2,3), datetime.date(2024,12,31), '%d/%m/%y')
Varun_diary = FamilyDiary(datetime.date(2024,4,23), datetime.date(1975,8,4), datetime.date(2025,2,28), '%d/%m/%y')

def main():
    print(looking_dates())
def looking_dates():
    if person == 'Kris':
        if event == 'birthday':
            return "Birthday: " + Kris_diary.show_birthday()
        elif event == 'festival':
            return ("Festival: " + Kris_diary.show_festival())
        elif event == 'holiday':
            return ("Holiday: " + Kris_diary.show_holiday())
        else:
            raise ValueError("That event doesn't exist.")
    elif person == 'Maki':
        if event == 'birthday':
            return ("Birthday: " + Maki_diary.show_birthday())
        elif event == 'festival':
            return ("Festival: " + Maki_diary.show_festival())
        elif event == 'holiday':
            return ("Holiday: " + Maki_diary.show_holiday())
        else:
            raise ValueError("That event doesn't exist.")
    elif person == 'Rasi':
        if event == 'birthday':
            return ("Birthday: " + Rasi_diary.show_birthday())
        elif event == 'festival':
            return ("Festival: " + Rasi_diary.show_festival())
        elif event == 'holiday':
            return ("Holiday: " + Rasi_diary.show_holiday())
        else:
            raise ValueError("That event doesn't exist.")
    elif person == 'Varun':
        if event == 'birthday':
            return ("Birthday: " + Varun_diary.show_birthday())
        elif event == 'festival':
            return ("Festival: " + Varun_diary.show_festival())
        elif event == 'holiday':
            return ("Holiday: " + Varun_diary.show_holiday())
        else:
            raise ValueError("That event doesn't exist.")
