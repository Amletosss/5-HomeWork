print('Введите целое число:')
number = int(input())

if (number%15) == 0:
    print('Fizz Buzz')
elif (number%3) == 0:
    print('Fizz')
elif (number%5) == 0:
    print('Buzz')
else:
    print(str(number))

