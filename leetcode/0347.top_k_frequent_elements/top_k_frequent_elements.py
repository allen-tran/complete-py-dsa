def topKFrequent(self, nums, k: int):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for i in nums:
        count[i] = 1 + count.get(i, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
