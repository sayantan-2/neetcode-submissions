class Solution:
    def isPalindrome(self, s: str) -> bool:
        single = ""
        for c in s:
            if c.isalnum():
                single+=c.lower()

        if single==single[::-1]:
            return True
        else:
            return False