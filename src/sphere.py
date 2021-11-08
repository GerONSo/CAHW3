from .figure import Figure
from math import pi

class Sphere(Figure):
    
    def __init__(self, density: float, radius: int) -> None:
        super().__init__(density)
        self._radius = radius

    def square(self) -> float:
        return 4 * pi * (self._radius ** 2)

    @classmethod
    def read(cls, file, density):
        radius = int(file.readline().split()[0])
        return Sphere(radius=radius, density=density)

    def print(self, file):
        file.write('Sphere {\n')
        file.write(f'\tradius = {self._radius}\n\tsquare() = {self.square()}\n')
        file.write('}\n')
