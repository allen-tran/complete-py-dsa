from group_anagrams import *


def test():
    print('---------------Leetcode Problem 49---------------')
    input = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        ["racecar", "carrace"]
    ]
    output = [
        [['bat'], ['tan', 'nat'], ['eat', 'tea', 'ate']],
        [['racecar', 'carrace']]
    ]
    for i in range(len(input)):
        print(f"Expected: {output[i]} and got: {groupAnagrams(input[i])}")
        if groupAnagrams(input[i]) == output[i]:
            print('PASS')
        else:
            print('FAIL')


if __name__ == "__main__":
    test()
