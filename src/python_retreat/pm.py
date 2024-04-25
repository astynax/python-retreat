from dataclasses import dataclass
from typing import TypeAlias, Any


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    start: Point
    stop: Point


@dataclass
class Circle:
    center: Point
    radius: int


Shape: TypeAlias = Circle | Line


def is_vertical(shape: Shape | dict) -> Any:
    match shape:
        case {"shape": "line", "start": Point(x=int(x)), "end": Point(x=int(x2))}:
            return x == x2
        case Circle():
            return "circle can't be vertical"
        case Line(Point(x=int(x1)), Point(x=x2)) if x1 == x2:
            return True
    return False


class C:
    __match_args__ = ('x',)

    def __getattr__(self, item):
        if item == 'x':
            return 42
        raise AttributeError('oops')


def x_of_c():
    match C():
        case C(42 as x):
            print('C.x =', x)


if __name__ == '__main__':
    for x in (
            Line(Point(10, 10), Point(10, 100)),
            {"shape": "line", "start": Point(10, 10), "end": Point(10, 100)}
    ):
        print(f'is_vertical({x!r}) => {is_vertical(x)}')

    x_of_c()
