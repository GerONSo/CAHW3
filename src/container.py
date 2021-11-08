from .figure import Figure

class Container():

    def __init__(self) -> None:
        self._current_size = 0
        self._figures = []

    def add_figure(self, figure: Figure):
        self._figures.append(figure)
        self._current_size += 1
    
    def get_figure_at(self, position: int) -> Figure:
        return self._figures[position]

    def sort(self):
        for i in range(1, self._current_size):
            j = i
            while j > 0 and self._figures[j].square() < self._figures[j - 1].square():
                (self._figures[j - 1], self._figures[j]) = (self._figures[j], self._figures[j - 1])
                j -= 1
    
    def size(self) -> int:
        return self._current_size
