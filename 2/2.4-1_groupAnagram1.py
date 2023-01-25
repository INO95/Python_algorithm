from collections import defaultdict

strs = ['eat', 'repaid', 'paired', 'tea', 'bat']


def groupAnagrams(strs) -> list:
    hashmap = defaultdict(list)

    for s in strs:
        hashmap["".join(sorted(s))].append(s)

    return hashmap.values()


print(groupAnagrams(strs))
