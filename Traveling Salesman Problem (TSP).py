from itertools import permutations

def total_distance(path, distances):
    return sum(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))

def traveling_salesman_bruteforce(distances):
    cities = range(len(distances))
    min_path = min(permutations(cities), key=lambda path: total_distance(path, distances))
    return min_path
