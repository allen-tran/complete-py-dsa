from typing import List


def intersection(nums1: List[str], nums2: List[str]) -> List[str]:
    set1 = set(nums1)
    set2 = set(nums2)

    if len(set1) < len(set2):
        return set_intersection(set1, set2)
    else:
        return set_intersection(set2, set1)


def set_intersection(set1, set2):
    return [x for x in set1 if x in set2]


user0 = ['/purple', '/pink', '/white', 'blue']
user1 = ['/orange', '/yellow', '/pink', '/white', '/purple']

print(intersection(user0, user1))
