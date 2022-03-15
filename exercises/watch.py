class Watch:
    def __init__(self, band_size, face_color, display_type):
        self._band_size = band_size
        self._face_color = face_color
        self._display_type = display_type

    def ticking(self):
        print(str.format('Watch starts ticking'))

    @property
    def band_size(self):
        return self._band_size

    @band_size.setter
    def band_size(self, num):
        self._band_size = num

    @property
    def face_color(self):
        return self._face_color

    @face_color.setter
    def face_color(self, color):
        self._face_color = color

    @property
    def display_type(self):
        return self._display_type

    @display_type.setter
    def display_type(self, type):
        self._display_type = type


my_watch = Watch('large', 'red', 'digital')
print(my_watch.display_type)
print(my_watch.face_color)
print(my_watch.band_size)
print(my_watch.ticking())
