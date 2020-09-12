a = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
#1
print(a + ('\n') + f"1.Количество символов - {len(a)}")
#2
print(f"2.{a[::-1]}")
#3
print(f"3.{str.title(a)}")
#4
print(f"4.{str.capitalize(a)}")
#5.1
print(f"5.1.Количество \"нд\": {a.count('нд')}")
#5.2
print(f"5.2.Количество \"ам\": {a.count('ам')}")
#5.3
print(f"5.3.Количество \"о\": {a.count('о')}")
#5.4
print(f"5.4.'нд' больше чем 'ор' : {a.count('нд') > a.count('ор')}")

#6
print(f"6.1.Метод \"isdigit\":{str.isdigit(a)}")
print(f"6.2.Метод \"upper\":{str.upper(a)}")
print(f"6.3.Метод \"lower\":{str.lower(a)}")
print(f"6.4.Метод \"swapcase\":{str.swapcase(a)}")
print(f"6.5.Метод \"istitle\":{str.istitle(a)}")
x = a.split(',')
print(f"6.6.Метод \"split\":{(x)}")
