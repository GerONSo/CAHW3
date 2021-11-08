import sys
import abc

class Figure:

    def __init__(self, density: float) -> None:
        self.density = density

    @classmethod
    def read(cls, file):
        from .sphere import Sphere
        from .parallelepiped import Parallelepiped
        from .tetrahedron import Tetrahedron
        something = file.readline()
        if something == '':
            return 'EOF'
        figure_name = something.split()[0]
        density = int(file.readline())
        if figure_name == 'Sphere':
            return Sphere.read(file, density)
        elif figure_name == 'Parallelepiped':
            return Parallelepiped.read(file, density)
        elif figure_name == 'Tetrahedron':
            return Tetrahedron.read(file, density)
        else:
            print('Incorrect figure name')
            sys.exit()

    @abc.abstractmethod
    def square() -> float:
        # returns square of Figure
        return
    
    @abc.abstractmethod
    def print(file):
        # prints Figure
        return