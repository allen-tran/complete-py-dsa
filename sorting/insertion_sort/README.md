# Insertion Sort

- quadratic run time complexity: O(N^2)

We want to seprate the given array in place by creating the left side of it as the sorted portion and the right side as the unsorted portion. Each number that is on the left most of the right poriton will be considered to the sorted side by continouously swapping each index-1 element that it enconters. We continue this process for all of the numbers ranging from 1 -> len(arr).