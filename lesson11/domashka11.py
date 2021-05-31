from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record] = record
        
    def __next__(self):
        keys = tuple(self.data.keys())
        if self.index == len(keys):
            raise StopIteration
        
        key = keys[self.index]
        item = self.data[key]
        self.index += 1
        return item.name, item.birthday.birthday
        
    def __iter__(self):
        self.index = 0
        return self
    
        
class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name

        
class Phone(Field):
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone):
        if len(phone) >= 10:
            self.__phone = phone
        else:
            print('Not correct phone number')
            

class Birthday(Field):
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday
    @property
    def birthday(self):
        return self.__birthday
    @birthday.setter
    def birthday(self, birthday):
        a = birthday.split('-')
        if len(a) == 3 and len(a[0]) == 4 and len(a[1]) == 2 and len(a[2]) == 2:
            self.__birthday = birthday
        else:
            print('Not correct birthday, please input YYYY-MM-DD')
            
        
class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.new_phone = ''
        self.birthday = None
        
    def add_phone(self, phone):
        self.phones.append(phone)
        
    def edit_phone(self, phone, new_phone):
        for i in self.phones:
            if i == phone:
                idx = self.phones.index(i)
                self.phones[idx] = new_phone
                
    def remove_phone(self, phone):
        self.phones.remove(phone)

    def add_birthday(self, birthday):
        self.birthday = birthday

    def days_to_birthday(self):
        result = None
        if self.birthday.birthday != None:
            a = self.birthday.birthday
            a = a.split('-')
            a = datetime(int(a[0]),int(a[1]),int(a[2]))
            now = datetime.now()
            first_date = datetime(now.year, a.month, a.day)
            result = (first_date - now.today()).days
            if result < 0:
                second_date = datetime(now.year+1, a.month, a.day)
                result = (second_date - now.today()).days
            return result







abon_1 = Name('Vasya')
phone_1 = Phone('+380999999')
birthday_1 = Birthday('1988-03-30')
phone_2 = Phone('+380972222222')
record_1 = Record(f'{abon_1.name}')
record_1.add_phone(phone_1)
record_1.add_phone(phone_2)
record_1.add_birthday(birthday_1)

abon_2 = Name('Petya')
phone_3 = Phone('+380666666666')
birthday_2 = Birthday('2000-06-30')
record_2 = Record(f'{abon_2.name}')
record_2.add_phone(phone_3)
record_2.add_birthday(birthday_2)

print(record_1.name, record_1.birthday.birthday, record_1.phones[0].phone, record_1.phones[1].phone)
print(record_2.name, record_2.birthday.birthday, record_2.phones[0].phone)
print(record_1.days_to_birthday())
print(record_2.days_to_birthday())

AB = AddressBook()
AB.add_record(record_1)
AB.add_record(record_2)
