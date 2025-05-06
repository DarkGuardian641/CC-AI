import heapq

# Directions the blank (0) can move
moves = {
    'Up': -3,
    'Down': 3,
    'Left': -1,
    'Right': 1
}

# Goal state
goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]

# Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        goal_idx = goal_state.index(tile)
        distance += abs(goal_idx // 3 - i // 3) + abs(goal_idx % 3 - i % 3)
    return distance

# Get possible moves
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)

    for move, pos in moves.items():
        new_idx = idx + pos
        if move == 'Left' and idx % 3 == 0:
            continue
        if move == 'Right' and idx % 3 == 2:
            continue
        if move == 'Up' and idx < 3:
            continue
        if move == 'Down' and idx > 5:
            continue

        new_state = state.copy()
        new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
        neighbors.append((new_state, move))
    return neighbors

# A* Search
def a_star(start):
    frontier = []
    heapq.heappush(frontier, (0 + manhattan_distance(start), 0, start, []))
    explored = set()

    while frontier:
        estimated_cost, cost, state, path = heapq.heappop(frontier)
        state_tuple = tuple(state)
        if state == goal_state:
            return path + [state]
        if state_tuple in explored:
            continue
        explored.add(state_tuple)

        for neighbor, move in get_neighbors(state):
            if tuple(neighbor) not in explored:
                heapq.heappush(frontier, (
                    cost + 1 + manhattan_distance(neighbor),
                    cost + 1,
                    neighbor,
                    path + [state]
                ))
    return None

# Pretty print state
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Example usage
if __name__ == "__main__":
    start_state = [1, 2, 3,
                   4, 0, 6,
                   7, 5, 8]

    solution = a_star(start_state)
    if solution:
        print("Solution found in", len(solution) - 1, "moves:")
        for step in solution:
            print_state(step)
    else:
        print("No solution found.")
