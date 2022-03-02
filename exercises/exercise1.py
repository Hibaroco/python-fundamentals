print("Hello World!")
# Can you make a typo that doesnt make an error?
# I was able to make it work but put in a O instead of the o in hello.
# Why do you think it didnt make an error?
# The code works but it does not read correctly
# Can you make a type that generates an error?
# I was able to make an error by making the command misspelled "pprint"
# The error message made it easy to decode, it actually offered the answer
# NameError: name 'pprint' is not defined. Did you mean 'print'?

# Python console
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea
# Name spaces are one honking great idea -- let's do more of those!

message_1 = "I am starting to get this!"
print(message_1)


# My first message is I am starting to get this! the printing worked.
# I then assigned a variable to it using an underscore and the number 1.

def display_message():
    """Displays a simple message"""
    print("I am learning about functions and how to use them.")


display_message()
# Here I created the function to print out a string.

def favorite_book(username):
    """Displays your favorite book"""
    print(f"One of my favorite books is {username.title()}.")


favorite_book('doctor sleep')

# This one took me some time because I didn't quite understand it at first
# It took some reading and a lot of checking the code to see why it didnt work.
# But luckily reading the error messages and checking over and over
# The program helped me fix my own code. Thanks Python!
