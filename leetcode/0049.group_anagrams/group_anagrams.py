def groupAnagrams(strs):
    # key: sorted word, value: words in original form
    word_dictionary = {}

    for word in strs:
        # sort the word
        temp = "".join(sorted(word))
        if temp not in word_dictionary:
            word_dictionary[temp] = list([word])
        else:
            word_dictionary[temp].append(word)
    res = [word for word in word_dictionary.values()]
    res.sort(key=len)
    return res
