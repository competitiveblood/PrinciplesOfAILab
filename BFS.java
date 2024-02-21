from collections import deque

def bfs(initial_state, problem):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if problem.is_goal_state(current_state):
            return path

        if current_state not in visited:
            visited.add(current_state)
            next_states = problem.successors(current_state)
            for next_state in next_states:
                queue.append((next_state, path + [next_state]))

    return None
