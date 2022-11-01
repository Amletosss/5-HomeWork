print('Введите любую строку: ')
text = input()
count = 0
word = text.split()
triple = []
for i in word:
    if i.isalpha():
        triple.append(i)
        if len(triple) == 3:
            print('True')
            break
    else:
        del triple[:]
else:
    print('False')