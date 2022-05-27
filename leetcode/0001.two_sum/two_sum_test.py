from two_sum import *

def test():
    print('---------------Leetcode Problem 1---------------')
    numbers = [
        [1,2,3,4,5],
        [232,435,32,34,6,],
        [-1,-1,-2, -3]
    ]
    targets = [
        9, 78, -4
    ]

    for i in range(len(numbers)):
        print(twoSum(numbers[i], targets[i]))

if __name__ == "__main__":
    test()