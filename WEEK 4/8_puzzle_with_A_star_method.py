
import heapq

# Calculate Manhattan distance heuristic
def heuristic(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_index = goal.index(state[i])

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Generate possible next states
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# Check whether the puzzle is solvable
def is_solvable(state, goal):
    def inversions(arr):
        arr = [x for x in arr if x != 0]
        count = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    count += 1

        return count

    return inversions(state) % 2 == inversions(goal) % 2


# A* search algorithm
def astar(start, goal):
    if start == goal:
        return [start]

    if not is_solvable(start, goal):
        return None

    # Priority queue: (f(n), g(n), state)
    open_list = []
    heapq.heappush(
        open_list,
        (heuristic(start, goal), 0, start)
    )

    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = [current]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            return path[::-1]

        for neighbor in get_neighbors(current):
            tentative_g = g + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current

                f_score = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(
                    open_list,
                    (f_score, tentative_g, neighbor)
                )

    return None


# Display the puzzle board
def print_board(state):
    for i in range(0, 9, 3):
        print(" ".join(
            "_" if x == 0 else str(x)
            for x in state[i:i + 3]
        ))
    print()


# Main program: take user input
print("8-Puzzle Problem using A* Algorithm")
print("Enter the 9 numbers from 0 to 8.")
print("Use 0 to represent the blank tile.\n")

start = tuple(map(
    int, input("Enter initial state (e.g. 1 2 3 4 0 6 7 5 8): ").split()
))

goal = tuple(map(
    int, input("Enter goal state (e.g. 1 2 3 4 5 6 7 8 0): ").split()
))

if (len(start) != 9 or len(goal) != 9
        or set(start) != set(range(9))
        or set(goal) != set(range(9))):
    print("Invalid input! Enter each number from 0 to 8 exactly once.")
else:
    solution = astar(start, goal)

    if solution is None:
        print("No solution exists for the given initial and goal states.")
    else:
        print("\nSolution found!")
        print("Number of moves:", len(solution) - 1)
        print("Path:\n")

        for step, state in enumerate(solution):
            print("Step", step)
            print_board(state)
