class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_amount):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_amount = target_amount

    def is_goal_state(self, state):
        return state[0] == self.target_amount or state[1] == self.target_amount

    def successors(self, state):
        jug1, jug2 = state
        next_states = []

        # Fill jug1
        next_states.append((self.jug1_capacity, jug2) if jug1 < self.jug1_capacity else state)

        # Fill jug2
        next_states.append((jug1, self.jug2_capacity) if jug2 < self.jug2_capacity else state)

        # Empty jug1
        next_states.append((0, jug2))

        # Empty jug2
        next_states.append((jug1, 0))

        # Pour from jug1 to jug2
        pour_amount = min(jug1, self.jug2_capacity - jug2)
        next_states.append((jug1 - pour_amount, jug2 + pour_amount))

        # Pour from jug2 to jug1
        pour_amount = min(self.jug1_capacity - jug1, jug2)
        next_states.append((jug1 + pour_amount, jug2 - pour_amount))

        return next_states
