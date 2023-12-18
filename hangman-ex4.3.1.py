ltr = input("Guess a letter: ")
if len(ltr) > 1 and not (ltr.isalpha()):
    print('E3')
elif len(ltr) > 1:
    print('E1')
elif not (ltr.isalpha()):
    print('E2')
else:
    print(ltr.lower())
