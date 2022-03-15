class Boat:

    def __init__(self, hull_size, motor, cargo):
        self._hull_size = hull_size
        self._motor = motor
        self._cargo = cargo

    def propulsion(self):
        print(str.format('Boat moves on water'))

    @property
    def hull_size(self):
        return self._hull_size

    @hull_size.setter
    def hull_size(self, num):
        self._hull_size = num

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, hp):
        self._motor = hp

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, manifest):
        self._cargo = manifest


my_boat = Boat(500, 'electric', 'shrimp')
print(my_boat.motor)
print(my_boat.hull_size)
print(my_boat.cargo)
print(my_boat.propulsion())
