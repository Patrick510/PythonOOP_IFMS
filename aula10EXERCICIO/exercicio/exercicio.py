class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    @property
    def name(self):
        '''o nome da cor'''
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise Exception("Invalid Name")
        self._name = value

    @name.deleter
    def name(self):
        print(f"Deleting name: {self._name}")
        del self._name


c = Color("#ff0000", "bright red")
print(c.name)
c.name = "red"
print(c.name)
del c.name  # Agora isso funcionará corretamente
