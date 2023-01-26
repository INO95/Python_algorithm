from collections import defaultdict

strs = ['eat', 'repaid', 'paired', 'tea', 'bat']
# strs = ['ab', 'cd', 'ef']
# strs = ['abc', 'bca', 'cba']


def groupAnagrams(strs) -> list:
    hashmap = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1
        hashmap[tuple(count)].append(s)

    return hashmap.values()


print(groupAnagrams(strs))
