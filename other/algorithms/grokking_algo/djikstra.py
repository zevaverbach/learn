"""
For each of these graphs, what is the weight of the shorten path from start to finish?
"""

INFINITY = float("inf")


class Graph:
    graph: dict
    parents: dict
    costs: dict


class A(Graph):
    graph = {
        "start": {
            "a": 5,
            "b": 2,
        },
        "a": {
            "b": 8,
            "c": 4,
            "d": 2,
        },
        "b": {
            "d": 7,
        },
        "c": {
            "d": 6,
            "finish": 3,
        },
        "d": {
            "finish": 1,
        },
        "finish": {},
    }

    parents = {
        "a": "start",
        "b": "start",
        "c": None,
        "d": None,
        "finish": None,
    }

    costs = {
        "a": 5,
        "b": 2,
        "c": INFINITY,
        "d": INFINITY,
        "finish": INFINITY,
    }



class B(Graph):
    graph = {
        "start": {
            "a": 10,
        },
        "a": {
            "b": 20,
        },
        "b": {
            "c": 1,
            "finish": 30,
        },
        "c": {
            "a": 1,
        },
        "finish": {},
    }

    parents = {
        "a": "start",
        "b": None,
        "c": "b",
        "finish": "b",
    }

    costs = {
        "a": 10,
        "b": INFINITY,
        "c": INFINITY,
        "finish": INFINITY,
    }


class C(Graph):
    graph = {
        "start": {
            "a": 2,
            "b": 2,
        },
        "a": {
            "c": 2,
            "finish": 2,
        },
        "b": {
            "d": 7,
        },
        "c": {
            "d": 6,
            "finish": 3,
        },
        "d": {
            "finish": 1,
        },
        "finish": {},
    }

    parents = {
        "a": "start",
        "b": "start",
        "c": None,
        "d": None,
        "finish": None,
    }

    costs = {
        "a": 5,
        "b": 2,
        "c": INFINITY,
        "d": INFINITY,
        "finish": INFINITY,
    }




def find_cheapest_path(graph: Graph) -> tuple[list[str], int]:
    processed = []

    def find_lowest_cost_node(costs: dict[str, int]) -> tuple[str, int | float]: 
        lowest_cost = INFINITY
        lowest_cost_node = ""
        for node, cost in costs.items():
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node, lowest_cost

    node, cost = find_lowest_cost_node(graph.costs)
    while node:
        neighbors = graph.graph[node]
        for n, c in neighbors.items():
            new_cost = cost + c
            if graph.costs[n] > new_cost:
                graph.costs[n] = new_cost
                graph.parents[n] = node
        processed.append(node)
        node, cost = find_lowest_cost_node(graph.costs)
    path = ["finish"]
    item = graph.parents["finish"]
    while item != "start":
        path.append(item)
        item = graph.parents[item]
    path.append('start')
    print(graph.costs)
    return path[::-1], sum(graph.costs.values())


parents, total_cost = find_cheapest_path(A)
print(parents, total_cost)
parents, total_cost = find_cheapest_path(B)
print(parents, total_cost)
