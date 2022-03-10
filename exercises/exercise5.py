# 5.1 Conditional Tests


truck = 'Dodge'
print("Is truck == 'Dodge'? I predict True")
print(truck == 'Dodge')
print("Is truck == 'dodge'? I predict False")
print(truck == 'dodge')

card = 'Valentine'
print("Is card == 'Valentine'? I predict True")
print(card == 'Valentine')
print("Is card == 'Baseball'? I predict False")
print(card == 'Baseball')

game = 'Elden Ring'
print("Is game == 'Elden Ring'? I predict True")
print(game == 'Elden Ring')
print("Is game == 'Mario Kart'? I predict False")
print(game == 'Mario Kart')

weapon = 'Sword'
print("Is weapon == 'Sword'? I predict True")
print(weapon == 'Sword')
print("Is weapon == 'Flail' I predict False")
print(weapon == 'Flail')

book = 'comic'
print("Is book == 'comic'? I predict True")
print(book == 'comic')
print("Is book == 'compendium'? I predict False")
print(book == 'compendium')

# 5.2
# Test 1 Equality and Inequality with strings

comic_book = 'Spider-man'
print("Is comic_book == 'spider-man'? False")
print(comic_book == 'spider-man')
print("Is comic_book == 'Spider-man'? True")

# Test 2 Using the lower method

car = 'Volvo'
print("Is car == volvo")
print(car.lower() == 'volvo')

car1 = 'honda'
print("Is car == 'honda'?")
print(car1.lower() == 'honda')

# Test 3 Numerical Tests
# Equality and Inequality first is false 15 is not equal to 25, second is true 15 is not equal to 25


def equal_1(value1, value2):
    result_equal = value1 == value2
    result_not = value1 != value2
    print(result_equal)
    print(result_not)


equal_1(15, 25)
# the first is true 10 is equal to 10, the second is true 10 is not equal to 40

def equal_2(value1, value2, value3):
    result_1 = value1 == value2
    result_2 = value2 != value3
    print(result_1)
    print(result_2)


equal_2(10, 10, 40)

# Greater than: first


def greater_1(value1, value2):
    result_1 = value1 > value2
    result_2 = value2 > value1
    print(result_1)
    print(result_2)


greater_1(56, 23)

# Less than: first is true 14 is less than 28, second one is false 14 is not greater than 28.


def less_1(value1, value2):
    result_1 = value1 < value2
    result_2 = value1 > value2
    print(result_1)
    print(result_2)


less_1(14, 28)


# Greater than or equal to first is true 15 is larger than 5, the second 5 is not greater than 15.


def greater_2(value1, value2):
    result_1 = value1 >= value2
    result_2 = value2 >= value1
    print(result_1)
    print(result_2)


greater_2(15, 5)


# Less than or equal to first is true: 2 is less than 25, second is false 25 is not less than 2


def less_2(value1, value2):
    result_1 = value1 <= value2
    result_2 = value2 <= value1
    print(result_1)
    print(result_2)


less_2(2, 25)

# and or statements: the first is True 15 is larger than 5 and 40 is less than 50
# the second is false 15 is not larger than 17 and 40 is not smaller than 30
alpha = 15
delta = 40


def logic_and():
    result = alpha > 5 and delta < 50
    result_2 = alpha > 17 and delta < 30
    print(result)
    print(result_2)


logic_and()

# using or: result 1 is true 15 > 14 and 40 < 68. result 2 is false 15 is > not < 2, 40 is < not > 140


def logic_or():
    result_1 = alpha > 14 or delta < 68
    result_2 = alpha < 2 or delta > 140
    print(result_1)
    print(result_2)


logic_or()


# in and not in strings first result is true should is inside the string, second is false because phrase is in string.
phrase = "What kind of phrase should I write?"


def sentence(arg):
    result = arg in phrase
    print(result)
    result = arg not in phrase
    print(result)


sentence('should')


# Using the same phrase the first is false because of the capitalization of What inside the phrase. Which means the
# second is True because of the same capitalization.


def sentence_1(arg):
    result = arg in phrase
    print(result)
    result = arg not in phrase
    print(result)


sentence('what')


# 5.3
# Arithmatic Operators: addition, subtraction, multiplication, and division


def basic(value1, value2):
    result = value1 + value2
    print(result)
    result_2 = value1 - value2
    print(result_2)
    result_3 = value1 * value2
    print(result_3)
    result_4 = value1 / value2
    print(result_4)


basic(15, 2)

# 5.4
# Here we have the modulus equals, exponent equals, plus equals, and minus equals.


def math(value):
    value %= 54
    print(value)
    value **= 3
    print(value)
    value += 65
    print(value)
    value -= 77
    print(value)


math(4)

# I tried to use these comments to help out this time. Sorry about before, I just hope this made it clearer and not
# jumbled. Hopefully it helps!

