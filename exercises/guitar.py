class Guitar:

    def __init__(self, body_type, fret_size, strings,):
        self._body_type = body_type
        self._fret_size = fret_size
        self._strings = strings

    def strum(self):
        print(str.format('Guitar strings vibrate'))

    @property
    def body_type(self):
        return self._body_type

    @body_type.setter
    def body_type(self, material):
        self._body_type = material

    @property
    def fret_size(self):
        return self._fret_size

    @fret_size.setter
    def fret_size(self, num):
        self._fret_size = num

    @property
    def strings(self):
        return self._strings

    @strings.setter
    def strings(self, num1):
        self._strings = num1


my_guitar = Guitar('wood', 16, 5)
print(my_guitar.body_type)
print(my_guitar.strings)
print(my_guitar.fret_size)
print(my_guitar.strum)

