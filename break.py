a = input('Enter a string or word: ')

for i in a:
    if i == 'A' or i == 'a':
        print('A is found')
        break
    else:
        print('A is not found')