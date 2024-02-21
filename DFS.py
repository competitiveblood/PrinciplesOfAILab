def dfs(initial_state, problem):
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()

        if problem.is_goal_state(current_state):
            return path

        if current_state not in visited:
            visited.add(current_state)
            next_states = problem.successors(current_state)
            for next_state in reversed(next_states):
                stack.append((next_state, path + [next_state]))

    return None
