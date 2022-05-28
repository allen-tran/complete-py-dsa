def longestCommonPrefix(strs) -> str:
    # sort the list by length so the first index is the smallest word
    strs.sort()
    # start res out by taking the entire smallest word
    res = strs[0]
    # scan through the rest of the words
    for i in range(1, len(strs)):
        # if the word is not equal to res, we need to subtract res by 1
        while res != strs[i][:len(res)]:
            res = res[:-1]
    return res
