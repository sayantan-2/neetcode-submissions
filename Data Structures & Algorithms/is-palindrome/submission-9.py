class Solution:
    def isPalindrome(self, s: str) -> bool:
        single = ""
        for c in s:
            if c.isalnum():
                single+=c.lower()

        return single==single[::-1]