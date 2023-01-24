s = "Abbc, c, bb, a"


def isPalindrome(s) -> bool:
    s = "".join(list(filter(str.isalnum, s))).lower()

    return s == s[::-1]


print(isPalindrome(s))
