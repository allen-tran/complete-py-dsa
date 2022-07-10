def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]
    return recursive_knapsack(dp, profits, weights, capacity, 0)


def recursive_knapsack(dp, profits, weights, capacity, index):
    if capacity <= 0 or index >= len(profits):
        return 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]
    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profits[index] + recursive_knapsack(
            dp, profits, weights, capacity-weights[index], index+1)

    profit2 = recursive_knapsack(dp, profits, weights, capacity, index+1)

    dp[index][capacity] = max(profit1, profit2)
    return dp[index][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
