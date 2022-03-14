# 5-8 Hello Admin

usernames = ['admin', 'jerry', 'adam', 'katie', 'chris']


def hello():
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again.')


hello()

# 5-9 No users
names = []


def none():
    for name in names:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'hello {name}, thank you for logging in again')
    else:
     print('We need to find some users!')


none()

# 5-10 Checking usernames

current_users = ['tim', 'james', 'cody', 'tilly', 'bob']
new_users = ['eric', 'billy', 'Cody', 'juan', 'carl']


def checking():
    current_users_lower = [user.lower() for user in current_users]
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print(f'Whoops {new_user}, that name has been used.')
        else:
            print(f'Good {new_user}, that name is available.')


checking()

# 5-11 Ordinal Numbers

numbers = list(range(1,10))


def places():
    for number in numbers:
        if number == 1:
            print('1st')
        elif number == 2:
            print('2nd')
        elif number == 3:
            print('3rd')
        else:
            print(f'{number}th')


places()


# 6-1 Person

person = {'first_name': 'Valerie', 'last_name': 'Lillich', 'age': 37, 'city': 'Wichita'}


def wife():
    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])


wife()

# 6-7 People
people = []

person = {'first_name': 'Janice', 'last_name': 'Hibarger', 'age': 58, 'city': 'Mulvane'}
people.append(person)
person = {'first_name': 'Joey', 'last_name': 'Stephens', 'age': 35, 'city': 'Portland'}
people.append(person)


def listing():
    for person in people:
        print(person['first_name'])
        print(person['last_name'])
        print(person['age'])
        print(person['city'])


listing()



