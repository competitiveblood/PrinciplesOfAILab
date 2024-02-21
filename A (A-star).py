def astar(initial_state, problem, heuristic):
    priority_queue = [(heuristic(initial_state, problem), initial_state, [])]
    visited = set()

    while priority_queue:
        _, current_state, path = heapq.heappop(priority_queue)

        if problem.is_goal_state(current_state):
            return path

        if current_state not in visited:
            visited.add(current_state)
            next_states = problem.successors(current_state)
            for next_state in next_states:
                cost = len(path) + heuristic(next_state, problem)
                heapq.heappush(priority_queue, (cost, next_state, path + [next_state]))

    return None
