from datetime import datetime
numbers=[]
brth=input("Введите дату родения(ГГГГ-ММ-ДД): ")
birth=datetime.strptime(brth,'%Y-%m-%d')
if birth.year < 1950 and birth.year > 1899:
    num_1=1
    numbers.append(num_1)
elif birth.year < 2000 and birth.year > 1949:
    num_1=2
    numbers.append(num_1)
elif birth.year < 1850 and birth.year > 1799:
    num_1 = 3
    numbers.append(num_1)
elif birth.year < 1900 and birth.year > 1849:
    num_1 = 4
    numbers.append(num_1)
elif birth.year < 2050 and birth.year > 1999:
    num_1 = 5
    numbers.append(num_1)
elif birth.year < 2100 and birth.year > 2049:
    num_1 = 6
    p=str(num_1).zfill(2)
    for idx in  p:
        numbers.append(int(idx))
#2
num_2=str(birth)[2:4]
for idx in num_2:
    numbers.append(int(idx))
#3
num_3=str(birth.month)
num_3=num_3.zfill(2)
for idx in num_3:
    numbers.append(int(idx))
#4
num_4=str(birth.day)
num_4=num_4.zfill(2)
for idx in num_4:
    numbers.append(int(idx))
#5
with open("Roman.csv",'r',encoding='utf-8') as file:
    data=file.readlines()
    for i in range(len(data)):
        data[i]= data[i].strip().replace('\xa0','').split(';')
    code_city=input("Введите код города: ")
    num_5=None
    for i in range(len(data)):
        if code_city in data[i]:
            num_5=data[i][0]
            a = str(num_5).zfill(2)
for idx in a:
    numbers.append(int(idx))

#6
num_6=input("Введите пол(M/F): ")
if num_6 == "M":
    num_6=str(1)
else:
    num_6=str(1)
for idx in num_6:
    numbers.append(int(idx))
#7
surname=input("Введите фамилию: ")
name=input("Введите имя: ")
num_7=str(ord(surname[0].upper()))
for idx in num_7:
    numbers.append(int(idx))
#8
result=0
cnp_numbers="279146358279"
for i in range(12):
    result+=numbers[i]*int(cnp_numbers[i])
result=result%9
numbers.append(result)
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
numbers = ''.join(numbers)
romanian=dict()
romanian[numbers] = {'Фамилия': surname, 'Имя':name,'Пол':num_6, 'Дата рождения':birth.strftime('%Y-%m-%d')}
for k,v in romanian.items():
    print(f'{k} - {v}')