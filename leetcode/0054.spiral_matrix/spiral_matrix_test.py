from spiral_matrix import *


def test():
    print('---------------Leetcode Problem 54---------------')
    input = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ]
    output = [
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
    ]

    for i in range(len(input)):
        print(f"Expected: {output[i]} and got: {spiralOrder(input[i])}")
        if spiralOrder(input[i]) == output[i]:
            print('PASS')
        else:
            print('FAIL')


if __name__ == "__main__":
    test()
