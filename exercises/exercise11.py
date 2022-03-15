# 9-6 Ice cream
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


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print('A few flavors left:'.format(self.flavors))


ice_cream = IceCreamStand('Cool Stuff', 'Ice Cream', 'Chocolate & Tres Leches')
print(ice_cream.name)
print(ice_cream.cuisine_type)
print(ice_cream.flavors)

# 9-7 Admin
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


class Admin(User):
    def __init__(self, first_name, last_name, address, email, privileges):
        super().__init__(first_name, last_name, address, email)
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'Can create posts, Can delete posts, Can ban user'.format(self.privileges))


jeff = Admin('Jeff', 'Davis', '321 Bidding', 'lajefe@gmail.com', privileges='Can add a post, Delete a post,\
 Can ban user')
print(jeff.first_name)
print(jeff.last_name)
print(jeff.email)
print(jeff.address)
print(jeff.privileges)

# 9-8 Privilege


class Privileges(Admin):
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'Can add user, Can delete post, Can ban user')


james = Admin('James', 'Baker', '65 West St', 'Jimmy@aol.com', 'privileges')
print(james.privileges)
print(james.email)
print(james.address)
print(james.first_name)
print(james.last_name)

# Horse child objects


class Horse:
    def __init__(self, coat_color, mane_length, shape):
        self._coat_color = coat_color
        self._mane_length = mane_length
        self._shape = shape

    def gallop(self):
        print(str.format('Runs through the pasture'))

    @property
    def coat_color(self):
        return self._coat_color

    @coat_color.setter
    def coat_color(self, color):
        self._coat_color = color

    @property
    def mane_length(self):
        return self._mane_length

    @mane_length.setter
    def mane_length(self, num):
        self._mane_length = num

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, height):
        self._shape = height


class Pony(Horse):
    def __init__(self, coat_color, mane_length, body_shape, horse_shoes, saddle):
        super().__init__(coat_color, mane_length, body_shape)
        self._horse_shoes = horse_shoes
        self._saddle = saddle

    @property
    def horse_shoes(self):
        return self._horse_shoes

    @horse_shoes.setter
    def horse_shoes(self, mat):
        self._horse_shoes = mat

    @property
    def saddle(self):
        return self._saddle

    @saddle.setter
    def saddle(self, stirrups):
        self._saddle = stirrups

    def whinny(self):
        print('Shakes head and stomps'.format(self.saddle))


greg = Pony('black', '2', 'small', 'brass', 'leather')
print(greg.saddle)
print(greg.horse_shoes)
print(greg.whinny())
print(greg.gallop())


class Clydesdale(Horse):
    def __init__(self, coat_color, mane_length, body_shape, harness, rider):
        super().__init__(coat_color, mane_length, body_shape)
        self._harness = harness
        self._rider = rider

    @property
    def harness(self):
        return self._harness

    @harness.setter
    def harness(self, clips):
        self._harness = clips

    @property
    def rider(self):
        return self._rider

    @rider.setter
    def rider(self, jockey):
        self.rider = jockey

    def pull_cart(self):
        print('Hyah!'.format(self.rider))


buster = Clydesdale('red', '65', 'muscular', 'bones', 'steven')
print(buster.coat_color)
print(buster.rider)
print(buster.shape)
print(buster.harness)
print(buster.gallop())
print(buster.pull_cart())
