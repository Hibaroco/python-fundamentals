# 5-3 Alien Colors #1

alien_color = 'yellow'

if alien_color == 'yellow':
    print("Player just earned 5 points.")

# This one works

alien_color = 'green'

if alien_color == 'yellow':
    print("Player just earned 5 points.")

# This one does not - because the color does not match the desired output.

# 5-4 Alien Colors #2
# If block executes
alien_color = 'green'

if alien_color == 'green':
    print("Player just earned 5 points.")
else:
    print("Player just earned 10 points.")

# Else block executes.
alien_color = 'red'

if alien_color == 'yellow':
    print("Player just earned 5 points.")
else:
    print("Player just earned 10 points.")

# 5-5 Alien Colors #3
# Green Alien output
alien_color = 'green'

if alien_color == 'green':
    print("Player just earned 5 points.")
elif alien_color == 'yellow':
    print("Player just earned 10 points.")
else:
    print("Player just earned 15 points.")

# Yellow Alien output
alien_color = 'yellow'

if alien_color == 'green':
    print("Player just earned 5 points.")
elif alien_color == 'yellow':
    print("Player just earned 10 points.")
else:
    print("Player just earned 15 points.")

# Red Alien output
alien_color = 'red'

if alien_color == 'green':
    print("Player just earned 5 points.")
elif alien_color == 'yellow':
    print("Player just earned 10 points.")
else:
    print("Player just earned 15 points.")

# 5-6 Stages of life

age = 35

if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

# 5 part 5 Boolean code


def method_1(arg1):
    print(bool(arg1))


method_1(0.0)

# 12 is true
# 1.2 is true
# 0 is false
# 0.4 is true
# 0.0 is false



