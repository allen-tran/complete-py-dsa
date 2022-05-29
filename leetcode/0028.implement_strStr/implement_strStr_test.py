from implement_strStr import *


def test():
    print('---------------Leetcode Problem 28---------------')
    input = [
        ["hello", 'll'],
        ["aaaa", "bba"]
    ]
    output = [
        2,
        -1
    ]
    for i in range(len(input)):
        print(
            f"Expected: {output[i]} and got: {strStr(input[i][0], input[i][1])}")
        if strStr(input[i][0], input[i][1]) == output[i]:
            print('PASS')
        else:
            print('FAIL')


if __name__ == "__main__":
    test()
