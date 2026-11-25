
import math

def alpha_beta(depth, node, is_max, values, alpha, beta):

    if depth == math.log2(len(values)):
        return values[node], [values[node]]

    if is_max:
        best = float('-inf')
        best_path = []

        for i in range(2):
            val, path = alpha_beta(
                depth + 1, node * 2 + i,
                False, values, alpha, beta)

            if val > best:
                best = val
                best_path = path

            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best, [best] + best_path

    else:
        best = float('inf')
        best_path = []

        for i in range(2):
            val, path = alpha_beta(
                depth + 1, node * 2 + i,
                True, values, alpha, beta)

            if val < best:
                best = val
                best_path = path

            beta = min(beta, best)

            if alpha >= beta:
                break

        return best, [best] + best_path


# User input
n = int(input("Enter number of leaf nodes: "))

if n > 0 and (n & (n - 1)) == 0:

    values = list(map(int, input(
        "Enter leaf node values: ").split()))

    if len(values) == n:

        result, path = alpha_beta(
            0, 0, True, values,
            float('-inf'), float('inf'))

        print("\nLeaf Node Values:", values)
        print("Optimal Value:", result)
        print("Optimal Path:", " -> ".join(map(str, path)))

    else:
        print("Please enter exactly", n, "values.")

else:
    print("Number of leaf nodes must be a power of 2.")
