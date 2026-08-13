class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        for i in s:
            if i in "!@#$%^&*()?,.;:'":
                s = s.replace(i, "")
        s= s.lower()
        temp = s[::-1]
        return temp == s