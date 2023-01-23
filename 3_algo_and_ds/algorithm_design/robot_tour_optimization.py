"""
input: a set `S` of `n` points on a plane
output: what is the shortest cycle tour that visits each point in the set `S`?
"""
import typing as t

Point = t.NewType("Point", tuple[int, int])
Points = t.NewType("Points", tuple[Point, ...])
PointPair = t.NewType("PointPair", tuple[Point, Point])


class NotFound(Exception):
    ...


def optimize(points: Points) -> Points:
    distance_lookup = make_distance_lookup(points)
    optimized = points
    shortest = None
    for point in points:
        itinerary = []
        total_distance = 0
        distance = 0
        closest = point
        while True:
            itinerary.append(closest)
            total_distance += distance
            try:
                closest, distance = get_closest_point(
                    closest_to=closest or point,
                    distance_lookup=distance_lookup,
                    itinerary=itinerary,
                )
            except NotFound:
                if len(itinerary) == len(points):
                    break
                else:
                    raise
            # to complete the circuit
        total_distance += get_distance_between_two_points(point, itinerary[-1])
        itinerary.append(point)
        if shortest is None or total_distance < shortest:
            shortest = total_distance
            optimized = itinerary
    return Points(tuple(optimized))


def make_distance_lookup(points: Points) -> dict[PointPair, int]:
    distance_lookup: dict[PointPair, int] = {}
    for idx, point in enumerate(points):
        for idx_prime, point_prime in enumerate(points):
            if (
                idx_prime == idx
                or (point, point_prime) in distance_lookup
                or (point_prime, point) in distance_lookup
            ):
                continue
            distance = get_distance_between_two_points(point, point_prime)
            distance_lookup[PointPair((point, point_prime))] = distance
            distance_lookup[PointPair((point_prime, point))] = distance
    return distance_lookup


def get_closest_point(
    *, closest_to: Point, distance_lookup: dict[PointPair, int], itinerary: list[Point]
) -> tuple[Point, int]:
    next_points = []
    for point_pair, distance in distance_lookup.items():
        if closest_to == point_pair[0]:
            next_points.append((point_pair[1], distance))
    sorted_next_points = sorted(next_points, key=lambda np: np[1])
    for next_point, distance in sorted_next_points:
        if next_point not in itinerary:
            return next_point, distance
    raise NotFound


def get_distance_between_two_points(
    first: tuple[int, int], second: tuple[int, int]
) -> int:
    return (((second[0] - first[0]) ** 2) + ((second[1] - first[1]) ** 2)) ** 0.5


if __name__ == "__main__":
    points: Points = Points(
        (
            Point((5, 10)),
            Point((9, 8)),
            Point((10, 6)),
            Point((9, 2)),
            Point((6, 0)),
            Point((3, 1)),
            Point((1, 3)),
            Point((0, 6)),
            Point((2, 8)),
        )
    )
    print(optimize(points))

    points: Points = Points(
        (
            Point((0, 0)), 
            Point((0, 4)),
            Point((5, 4)),
            Point((5, 0)),
            Point((10, 4)),
            Point((10, 0)),
        )
    )
    print(optimize(points))
