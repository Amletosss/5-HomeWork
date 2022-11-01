print('Введите число:')
number = int(input())

if ((number%2) == 1):
    print('Плохо')
elif (number%2 == 0) and (2 <= number <= 5):
    print('Неплохо')
elif (number%2) == 0 and (6 <= number <= 20):
    print('Так себе')
elif (number%2 == 0) and (number > 20):
    print('Отлично')