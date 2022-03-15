class Horse:
    def __init__(self, coat_color, mane_length, size):
        self._coat_color = coat_color
        self._mane_length = mane_length
        self._size = size

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
    def size(self):
        return self._size

    @size.setter
    def size(self, height):
        self._size = height


my_horse = Horse('black', '36', '5ft')
print(my_horse.size)
print(my_horse.mane_length)
print(my_horse.coat_color)
print(my_horse.gallop())
