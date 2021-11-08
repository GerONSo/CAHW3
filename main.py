import sys
from src.container import Container
from src.figure import Figure
from typing import List
from random import randint
from src.sphere import Sphere
from src.parallelepiped import Parallelepiped
from src.tetrahedron import Tetrahedron
from time import time

def random_figure() -> Figure:
    figure_number = randint(0, 2)
    MAX_LENGTH = 1000
    density = randint(0, MAX_LENGTH)
    if (figure_number == 0):
        radius = randint(0, MAX_LENGTH)
        return Sphere(radius=radius, density=density)
    elif (figure_number == 1):
        length = randint(0, MAX_LENGTH)
        width = randint(0, MAX_LENGTH)
        height = randint(0, MAX_LENGTH)
        return Parallelepiped(length=length, width=width, height=height, density=density);
    else:
        edge_length = randint(0, MAX_LENGTH)
        return Tetrahedron(edge_length=edge_length, density=density)

def run_with_default_input(argv: List[str]):
    input_file_path = argv[2]
    output_file_path = argv[3]
    output_sorted_file_path = argv[4]

    input_file = open(input_file_path, 'r')
    output_file = open(output_file_path, 'w')
    output_sorted_file = open(output_sorted_file_path, 'w')
    
    container = Container()
    with input_file:
        while True:
            figure = Figure.read(input_file)
            if figure == 'EOF':
                break
            container.add_figure(figure)
    
    for i in range(container.size()):
        container.get_figure_at(i).print(output_file)

    container.sort()
    
    for i in range(container.size()):
        container.get_figure_at(i).print(output_sorted_file)

    input_file.close()
    output_file.close()
    output_sorted_file.close()

def run_with_random_input(argv: List[str]):
    figure_count = int(argv[2])
    output_file_path = argv[3]
    output_sorted_file_path = argv[4]

    output_file = open(output_file_path, 'w')
    output_sorted_file = open(output_sorted_file_path, 'w')
    
    container = Container()
    for i in range(figure_count):
        figure = random_figure()
        container.add_figure(figure)
    
    for i in range(container.size()):
        container.get_figure_at(i).print(output_file)

    container.sort()
    
    for i in range(container.size()):
        container.get_figure_at(i).print(output_sorted_file)

    output_file.close()
    output_sorted_file.close()

def on_incorrect_argument_count(argv: List[str]):
    print("Amount of arguments is incorrect:")
    print(f"Try {argv[0]} -f .../input.txt .../output.txt .../output_sorted.txt")
    print(f"OR\n{argv[0]} -r items_count .../output.txt .../output_sorted.txt")
    sys.exit(1)

def main():
    start_time = time()
    if len(sys.argv) < 2:
        on_incorrect_argument_count(sys.argv)
    flag = sys.argv[1]
    if len(sys.argv) == 5 and flag == '-f':
        run_with_default_input(sys.argv)
        end_time = time()
        print(f'Time elapsed: {end_time - start_time}s')
    elif len(sys.argv) == 5 and flag == '-r':
        run_with_random_input(sys.argv)
        end_time = time()
        print(f'Time elapsed: {end_time - start_time}s')
    else:
        on_incorrect_argument_count(sys.argv)

if __name__ == '__main__':
    main()
