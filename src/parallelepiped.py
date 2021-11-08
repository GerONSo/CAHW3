from .figure import Figure

class Parallelepiped(Figure):
    
    def __init__(self, density: float, length: int, width: int, height: int) -> None:
        super().__init__(density)
        self._length = length
        self._width = width
        self._height = height

    def square(self) -> float:
        return 2 * (self._length * self._width + self._width * self._height + self._length * self._height)

    @classmethod
    def read(cls, file, density):
        (length, width, height) = map(int, file.readline().split())
        return Parallelepiped(length=length, width=width, height=height, density=density)

    def print(self, file):
        file.write('Parallelepiped {\n')
        params = f'\tlength = {self._length}\n\twidth = {self._width}\n\theight = {self._height}\n\tsquare() = {self.square()}\n'
        file.write(params)
        file.write('}\n')