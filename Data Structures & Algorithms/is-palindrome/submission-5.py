class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        single = ""
        for c in s:
            if c.isalnum():
                single+=c

        if single==single[::-1]:
            return True
        else:
            return False