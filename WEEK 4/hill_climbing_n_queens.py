def conflicts(state, n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                count += 1
    return count

def hill_climbing(state, n):
    while True:
        current = conflicts(state, n)

        if current == 0:
            return state

        best_state = state[:]
        best_score = current

        for col in range(n):
            for row in range(n):
                if row != state[col]:
                    neighbor = state[:]
                    neighbor[col] = row
                    score = conflicts(neighbor, n)

                    if score < best_score:
                        best_score = score
                        best_state = neighbor

        if best_score >= current:
            return None

        state = best_state

def display(state, n):
    for row in range(n):
        for col in range(n):
            print("Q" if state[col] == row else ".", end=" ")
        print()

n = int(input("Enter number of queens: "))
state = list(map(int, input(
    f"Enter initial state ({n} row values, 0 to {n-1}): "
).split()))

if n > 0 and len(state) == n and all(0 <= x < n for x in state):
    solution = hill_climbing(state, n)

    if solution is not None:
        print("Solution found:", solution)
        display(solution, n)
        print("Conflicts:", conflicts(solution, n))
    else:
        print("Local optimum reached. No solution found.")
else:
    print("Invalid input.")