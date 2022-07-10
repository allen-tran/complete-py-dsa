def solve_knapsack(profits, weights, capacity):
    return recursive_knapsack(profits, weights, capacity, 0)


def recursive_knapsack(profits, weights, capacity, index):
    if capacity <= 0 or index >= len(profits):
        return 0
    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profits[index] + recursive_knapsack(
            profits, weights, capacity-weights[index], index+1)

    profit2 = recursive_knapsack(profits, weights, capacity, index+1)

    return max(profit1, profit2)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
