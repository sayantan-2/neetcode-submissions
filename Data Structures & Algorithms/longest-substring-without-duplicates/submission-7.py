class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        seen = set()
        max_len = 0

        for right in range(len(s)):

            # Shrink the window until s[right] is no longer a duplicate
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add the current character
            seen.add(s[right])

            # Update the maximum window length
            max_len = max(max_len, right - left + 1)

        return max_len