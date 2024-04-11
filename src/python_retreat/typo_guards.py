from typing import TypeGuard, TypeAlias, Any
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


PointTuple: TypeAlias = tuple[float, float]


def is_point_tuple(value: Any) -> TypeGuard[PointTuple]:
    return (
            isinstance(value, tuple) and
            len(value) == 2 and
            isinstance(value[0], (int, float)) and
            isinstance(value[1], (int, float))
    )


def is_point_like(value: Any) -> TypeGuard[Point | PointTuple]:
    return isinstance(value, Point) or is_point_tuple(value)


def at_base(point: Point | PointTuple) -> bool:
    if isinstance(point, Point):
        return point.x == 0 and point.y == 0
    elif is_point_tuple(point):
        return point == (0, 0)
    raise TypeError(f'Is not a point-like: {point}')


if __name__ == '__main__':
    for p in (Point(0, 0), (0, 0), "oops!"):
        if is_point_like(p) and at_base(p):
            if is_point_tuple(p):
                x, y = p
                print(f'({x}, {y}) is on the base')
            elif isinstance(p, Point):  # Just 'else' wouldn't work
                print(f'({p.x}, {p.y}) is on the base')
