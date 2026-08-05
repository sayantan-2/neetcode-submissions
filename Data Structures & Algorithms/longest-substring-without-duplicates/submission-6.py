class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l=0
        window=s[l]
        result=1
        for r in range(1,len(s)):
            ch=s[r]
            if ch not in window:
                window=window+ch
                result=max(result,len(window))
            else:
                l=window.find(ch)+1
                window=window[l:]+ch
        return result