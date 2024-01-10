from collections import deque

# Function to solve the water jug problem using BFS
def water_jug_problem(capacity_a, capacity_b, target):
    # Initial state: both jugs are empty
    state = (0, 0)
    visited = set()  # To track visited states
    queue = deque([(state, [])])  # Queue to perform BFS

    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)

        # Check if the target amount of water is achieved
        if target in current_state:
            if target == current_state[0]:
                print(f"Solution found! Pour water from Jug A to get {target} units.")
            else:
                print(f"Solution found! Pour water from Jug B to get {target} units.")
            print("Path:", path)
            return

        # Possible operations: fill, empty, or transfer water between jugs
        a, b = current_state
        next_states = [
            (capacity_a, b),  # Fill jug A
            (a, capacity_b),  # Fill jug B
            (0, b),  # Empty jug A
            (a, 0),  # Empty jug B
            (min(a + b, capacity_a), max(0, a + b - capacity_a)),  # Pour from B to A
            (max(0, a + b - capacity_b), min(a + b, capacity_b)),  # Pour from A to B
        ]

        for next_state in next_states:
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    print("No solution found.")

# Define jug capacities and target amount of water
capacity_jug_a = 3
capacity_jug_b = 4
target_amount = 2

# Solve the water jug problem
water_jug_problem(capacity_jug_a, capacity_jug_b, target_amount)
