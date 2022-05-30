from maximum_subarray import *


def test():
    print('---------------Leetcode Problem 53---------------')
    input = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ]
    output = [
        6
    ]

    for i in range(len(input)):
        print(f"Expected: {output[i]} and got: {maxSubArray(input[i])}")
        if maxSubArray(input[i]) == output[i]:
            print('PASS')
        else:
            print('FAIL')


if __name__ == "__main__":
    test()
