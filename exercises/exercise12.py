# 10-6 Addition

def simple_add():
    print('Let\'s do some addition!')
    try:
        first = input('Put your first number:')
        second = input('And add it with:')
        solution = int(first) + int(second)
        print(solution)
    except ValueError:
        print('You gotta use numbers dude!')


simple_add()

# 10-7 Addition Calculator


def simple_add():
    print('Let\'s do some addition!')
    try:
        first = input('Put your first number:')
        second = input('And add it with:')
        solution = int(first) + int(second)
        print(solution)
    except ValueError:
        print('You gotta use numbers dude!')
        simple_add()


simple_add()

# 10-8 Cats and Dogs

filenames = ['cats.txt', 'dogs.txt']


def simple_search():

    for filename in filenames:
        print(f'Reading {0}....')
        try:
            with open(filename) as f:
                contents = f.read()
                print(contents)
        except FileNotFoundError:
            print('Whoops!, where did that go?')


simple_search()

# 10-9 Silent Cats and Dogs


def simple_search():

    for filename in filenames:
        print(f'Reading {0}....')
        try:
            with open(filename) as f:
                contents = f.read()
                print(contents)
        except FileNotFoundError:
            pass