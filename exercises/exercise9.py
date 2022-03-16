# 8-3 T-Shirt Positional argument
def make_shirt(size, message):
    print(f'I have a {size} t-shirt.')
    print(f'It says {message}.')


# make_shirt('large', 'Elden Ring')
# 8-3 Keyword Argument
# make_shirt(size='small', message='Python is frustrating')


# 8-4 large shirts
def make_shirt1(size='large', message='I love python'):
    print(f'I have a {size} t-shirt, It says {message}')


# make_shirt1()
# make_shirt1(size='medium')
# make_shirt1('small', 'I always forget quotes')


# 8-5 Cities
def describe_city(city, country='Ireland'):
    message = f'{city.title()} is in {country.title()}.'
    print(message)


# describe_city('Dublin')
# describe_city('Cork')
# describe_city('Stockholm', 'Sweden')

# 8-9 Messages
messages = ['What are you up to?', 'How is it going', 'Where are you']


def show_messages(messages):
    for message in messages:
        print(message)


# show_messages(messages)

# 8-10 Sending Messages
sent_messages = []
send_messages = (messages, sent_messages)
messages = ['What are you up to?', 'How is it going', 'Where are you']


def show_messages(messages):
    print('Show Message')
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    print('Sending messages')
    while messages:
        message_1 = messages.pop()
        print(message_1)
        sent_messages.append(message_1)
        print(messages)
        print(sent_messages)


send_messages(messages, sent_messages)
show_messages(messages)

# print(messages)
# print(sent_messages)

# 8-11 Archived messages

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)

# 9-1 Restaurant


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f'{self.name} has great {self.cuisine_type}.'
        print(msg)
        return self.cuisine_type

    def open_restaurant(self):
        msg = f'{self.name} is open.'
        print(msg)
        return self.name


my_restaurant = Restaurant('baja', 'tacos')
print(my_restaurant.name)
print(my_restaurant.cuisine_type)
Restaurant.describe_restaurant(my_restaurant)
Restaurant.open_restaurant(my_restaurant)

# 9-2 Three Restaurants
baja = Restaurant('Baja', 'tacos')
baja.describe_restaurant()
luigis = Restaurant('Luigis', 'italian')
luigis.describe_restaurant()
rolls = Restaurant('Rolls', 'sushi')
rolls.describe_restaurant()

# 9-3 Users


class User:

    def __init__(self, first_name, last_name, address, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.address = address
        self.email = email

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}')
        print(f'{self.address}')
        print(f'{self.email}')

    def greet_user(self):
        print(f'Good Morning, {self.first_name}.')


jesse = User('jesse', 'hibarger', '112 1st St', 'me@yahoo.com')
jesse.greet_user()
jesse.describe_user()

barbara = User('barbara', 'matthews', '456 Penny Lane', 'barb@gmail.com')
barbara.greet_user()
barbara.describe_user()

# 9-4 Number served


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f'{self.name} has great {self.cuisine_type}.'
        print(msg)
        return self.cuisine_type

    def open_restaurant(self):
        msg = f'{self.name} is open.'
        print(msg)
        return self.name

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, more_served):
        self.number_served += more_served


restaurant = Restaurant('Baja', 'Tacos')
restaurant.describe_restaurant()
print(f'Number served: {restaurant.number_served}')
restaurant.number_served = 270
print(f'Number served: {restaurant.number_served}')
restaurant.set_number_served(342)
print(f'Number served: {restaurant.number_served}')
restaurant.increment_number_served(675)
print(f'Number served: {restaurant.number_served}')

# 9-5 Login Attempts


class User:

    def __init__(self, first_name, last_name, address, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.address = address
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}')
        print(f'{self.address}')
        print(f'{self.email}')

    def greet_user(self):
        print(f'Good Morning, {self.first_name}.')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


barbara = User('barbara', 'matthews', '456 Penny Lane', 'barb@gmail.com')
barbara.greet_user()
print(f'Making 2 login attempts')
barbara.increment_login_attempts()
barbara.increment_login_attempts()
print(f'log in attempts: {barbara.login_attempts}')
barbara.reset_login_attempts()
print(f'login attempts: {barbara.login_attempts}')



