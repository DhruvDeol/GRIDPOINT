import math
from itertools import combinations


def distance(x1, y1, x2, y2):
    """
    Calculate Euclidean distance between two points.
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calculate_cost(neighborhoods, warehouses, assignments):
    """
    Calculate total weighted delivery cost.

    Cost = distance × number of orders
    """

    total_cost = 0

    for warehouse_index, neighborhood_indices in enumerate(assignments):

        wx = warehouses[warehouse_index]["x"]
        wy = warehouses[warehouse_index]["y"]

        for index in neighborhood_indices:

            neighborhood = neighborhoods[index]

            d = distance(
                wx,
                wy,
                neighborhood["x"],
                neighborhood["y"]
            )

            cost = d * neighborhood["orders"]

            total_cost += cost

    return total_cost


def assign_neighborhoods(neighborhoods, warehouses):
    """
    Assign every neighborhood to its nearest warehouse.
    """

    assignments = [[] for _ in warehouses]

    for i, neighborhood in enumerate(neighborhoods):

        best_warehouse = 0
        best_distance = float("inf")

        for j, warehouse in enumerate(warehouses):

            d = distance(
                neighborhood["x"],
                neighborhood["y"],
                warehouse["x"],
                warehouse["y"]
            )

            if d < best_distance:
                best_distance = d
                best_warehouse = j

        assignments[best_warehouse].append(i)

    return assignments


def optimize_warehouses(data, number_of_warehouses):
    """
    Find warehouse locations that minimize
    weighted delivery cost.

    For a beginner-friendly MVP, warehouse locations
    are selected from existing neighborhood locations.
    """

    neighborhoods = []

    for _, row in data.iterrows():

        neighborhoods.append({
            "name": str(row["Neighborhood"]),
            "x": float(row["X Coordinate"]),
            "y": float(row["Y Coordinate"]),
            "orders": float(row["Orders"])
        })

    n = len(neighborhoods)

    # Cannot have more warehouses than neighborhoods
    number_of_warehouses = min(number_of_warehouses, n)

    best_cost = float("inf")
    best_warehouses = None
    best_assignments = None

    # Try every possible combination of warehouse locations
    for combination in combinations(
        range(n),
        number_of_warehouses
    ):

        warehouses = []

        for index in combination:

            warehouses.append({
                "x": neighborhoods[index]["x"],
                "y": neighborhoods[index]["y"],
                "name": neighborhoods[index]["name"]
            })

        # Assign each neighborhood to nearest warehouse
        assignments = assign_neighborhoods(
            neighborhoods,
            warehouses
        )

        # Calculate weighted cost
        cost = calculate_cost(
            neighborhoods,
            warehouses,
            assignments
        )

        # Keep the best solution
        if cost < best_cost:

            best_cost = cost
            best_warehouses = warehouses
            best_assignments = assignments

    # Convert assignments from indexes to names
    assignment_names = []

    for warehouse_index, indices in enumerate(best_assignments):

        names = []

        for index in indices:
            names.append(
                neighborhoods[index]["name"]
            )

        assignment_names.append(names)

    return (
        best_warehouses,
        assignment_names,
        best_cost
    )