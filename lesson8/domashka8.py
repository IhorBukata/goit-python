from datetime import datetime
from collections import defaultdict


users = [{'Ihor':datetime(1988, 3, 13)}, {'Sergiy':datetime(1965, 5, 24)}, {'Anastasiya':datetime(2001, 5, 22)}, {'Valeriy':datetime(1985, 5, 23)}, {'Anna':datetime(1985, 5, 26)}]
# 0:'Monday', 1:'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Monday', 6: 'Monday'


def congratulate(users):
    mon_list = []
    tue_list = []
    wed_list = []
    thu_list = []
    fri_list = []
    result = ''

    now_date = datetime.now()
    now_weekday = datetime.weekday(now_date)
    birth_start = 4 - now_weekday
    birth_end = birth_start + 7
    for i in users:
        for key, value in i.items():
            virtual_value = value.replace(year = now_date.year)
            dif_days = (virtual_value - now_date).days
            if dif_days in range(birth_start, birth_end):
                virtual_weekday = datetime.weekday(virtual_value)
                if virtual_weekday == 0 or virtual_weekday == 5 or virtual_weekday == 6:
                    mon_list.append(key)
                elif virtual_weekday == 1:
                    tue_list.append(key)
                elif virtual_weekday == 2:
                    wed_list.append(key)
                elif virtual_weekday == 3:
                    thu_list.append(key)
                elif virtual_weekday == 4:
                    fri_list.append(key)
                
    if len(mon_list) != 0:
        result += "Monday: " + str(mon_list) + '\n'
    if len(tue_list) != 0:
        result += "Tuesday: " + str(tue_list) + '\n'
    if len(wed_list) != 0:
        result += "Wednesday: " + str(wed_list) + '\n'
    if len(thu_list) != 0:
        result += "Thursday: " + str(wed_list) + '\n'
    if len(fri_list) != 0:
        result += "Friday: " + str(wed_list) + '\n'
    result = result.replace('[', '').replace(']', '').replace("'", '')

    return result


print(congratulate(users))

