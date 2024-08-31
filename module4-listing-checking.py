for char in 'happy message': 
    print(char)

    invited_guest = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
    name = input('What is your name? ')
    if name in invited_guest: 
        print('Welcome!')
    else:
        print('You are not invited!')

        invited_guest = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie',]
        name = input('what is your name? ')
        if name not in invited_guests:
            print('You are not invited!')
        else:
            print('welcome!')
