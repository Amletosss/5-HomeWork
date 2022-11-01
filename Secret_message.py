print('Введите свой тест с секретным сообщением: ')
text = input()
message = ''
for i in text:
    if i.isupper() == True:
        message += (i.upper())
print('Секретное сообщение: ', message)
