from .figure import Figure
from math import sqrt

class Tetrahedron(Figure):

    def __init__(self, density: float, edge_length: int) -> None:
        super().__init__(density)
        self._edge_length = edge_length

    def square(self) -> float:
        return sqrt(3) * self._edge_length ** 2

    @classmethod
    def read(cls, file, density):
        edge_length = int(file.readline().split()[0])
        return Tetrahedron(edge_length=edge_length, density=density)
    
    def print(self, file):
        file.write('Tetrahedron {\n')
        file.write(f'\tedge_length = {self._edge_length}\n\tsquare() = {self.square()}\n')
        file.write('}\n')