# 8-15 Printing Models

import printing_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

# 8-16 Imports

import happier
from happier import express
happier.express(True)
from happier import express as ex
express = ex()
import happier as hp
happier == hp


# 9-10 Imported Restaurant

from exercise11 import Restaurant

spruce_goose = Restaurant('Spruce Goose', 'Game Meats')
spruce_goose.describe_restaurant()
spruce_goose.open_restaurant()

# 9-11 Imported Admin

from exercise11 import Admin

homer = Admin('Homer', 'Simpson', '72 Marge Lane', 'Homey@burnsco.com', 'special')
homer.show_privileges()
print(homer.describe_user())

# 9-12 Multiple Modules

from admin import Admin
from user import User

chris = User
chris = Admin('Chris', 'Anderson', '66th First St', 'canderson@yahoo.com', privileges='Can rewrite program'\
              'Can ban user')
chris.show_privileges()
print(chris.show_privileges())

# 9-16 Python module of the week

import random

for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()


