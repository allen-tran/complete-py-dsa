def containsDuplicate(self, nums) -> bool:
    distinct = set()

    for i in nums:
        if i in distinct:
            return True
        distinct.add(i)
    return False
