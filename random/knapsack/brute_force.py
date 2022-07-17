class Solution:
    def solve_knapsack(self, profits, weights, capacity):
        return self.recursive_knapsack(profits, weights, capacity, 0)

    def recursive_knapsack(self, profits, weights, capacity, index):
        if capacity <= 0 or index >= len(profits):
            return 0
        profit1 = 0
        if weights[index] <= capacity:
            profit1 = profits[index] + self.recursive_knapsack(
                profits, weights, capacity-weights[index], index+1)

        profit2 = self.recursive_knapsack(profits, weights, capacity, index+1)

        return max(profit1, profit2)


if __name__ == "__main__":
    s = Solution()
    print(s.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(s.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(s.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
