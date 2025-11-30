from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

class Segment(NamedTuple):
    start: Point
    end: Point

class Circle(NamedTuple):
    ctr: Point
    r: float
