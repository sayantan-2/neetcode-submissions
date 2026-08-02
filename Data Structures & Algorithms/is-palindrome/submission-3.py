class Solution:
    def isPalindrome(self, s: str) -> bool:
        single = ""
        for c in s:
            if c.isalnum():
                single+=c.lower()
        left = 0
        right = len(single)-1
        while left < right:
            if single[left]!=single[right]:
                return False
            left+=1
            right-=1
        return True