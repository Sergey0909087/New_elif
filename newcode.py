# x = 5
# if x == 5:
#     print('ravno')
# else:
#     print('ne ravno')

# x == 5 # znak ravenstva
# x > 5 # bolshe
# x < 5 # menshe
# x >= 5 # bolshe ili ravno
# x <= 5 # menshe ili ravno
# x != 5 # ne ravno

# num_1 = 3
# num_2 = 7
# if num_1 < num_2:
#     print('Menshe')
# else:
#     print('Bolshe')

# x = 15
# if x > 2:
#     if x < 10:
#         print('x bolshe 2, no menshe 10')


# and - logicheskoe umnojenie
# or - logicheskoe slojenie
# not - logicheskoe otritsanie

# age = 12
# user_class = 7
# if age >= 12 and user_class == 7:
#     print('Uslovie verno')

# age = 11
# user_class = 5
# if age >= 12 or user_class == 7:
#     print('Uslovie verno')


# age = 11
# if not age == 12:
#     print('Vozrast ne raven 12')

# x = 5
# if x >= 5:
#     print('YES')
# if x == 5:
#     print('YES')
# if x != 10:
#     print('YES')
# else:
#     print('NO')

# age = int(input('Vvedi svoi vozrast: '))
# if 18 > age >= 14:
#     print('Vam bolshe 14 ili 14 let')
# elif 21 > age >= 18:
#     print('Vam bolshe 18 ili 18 let')
# elif 45 > age >= 21:
#     print('Vam bolshe 21 ili 21 god')
# elif age >= 45:
#     print('Vam bolshe 45 ili 45 let')


"""
Starshei mi 11 i mladshe 15 let
"""

# Cherez vlozhenie usloviya
# age = 12
# if age > 11:
#     if age < 15:
#         print('DA')

# Ispolzuya operatori and i or
# age = 12
# if age > 11 and age < 15:
#     print('DA')

# Ispolzuya proverku po diapozonu
# age = 12
# if 11 < age < 15:
#     print('Da')

# ternarnii operator

# num = int(input('Vvedi chislo'))

# Esli uslovie verno Uslovie inache Esli ne verno
# print('Chetnoe' if num % 2 == 0 else 'Nechetnoe')

# if num % 2 == 0:
#     print('Chetnoe')
# else:
#     print('nechetnoe')

# Zadanie 1

age = int(input('Введи свою температуру: '))
if 20 <= age <= 35:
    print('Низкая')
elif 36 < age <= 37:
    print('Здоров')
elif 38 < age <= 40:
    print('Высокая температура')

# Zadanie 2

age = int(input('веди число: '))
if age > 100 or age < -100:
    print('-')
else:
    print('+')

# Zadanie 3

x = int(input('введи первое число: '))
y = int(input('введи второе число: '))
z = int(input('введи третье число: '))
if x > 10 and y > 10 and z > 10:
    print('ДА')
else:
    print('Нет')
