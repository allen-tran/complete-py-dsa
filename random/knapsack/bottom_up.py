def solve_knapsack(profits, weights, capacity):

    n = len(profits)

    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for i in range(capacity + 1)] for i in range(n)]

    for i in range(0, n):
        dp[i][0] = 0

    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for j in range(1, capacity + 1):
            profit1, profit2 = 0, 0

            if weights[i] <= j:
                profit1 = profits[i] + dp[i - 1][j - weights[i]]
            profit2 = dp[i-1][j]
            dp[i][j] = max(profit1, profit2)

    return dp[n-1][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
