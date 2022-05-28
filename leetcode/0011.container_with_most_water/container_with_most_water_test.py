from container_with_most_water import *


def test():
    print('---------------Leetcode Problem 11---------------')
    numbers = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1]
    ]

    for i in range(len(numbers)):
        print(maxArea(numbers[i]))


if __name__ == "__main__":
    test()
