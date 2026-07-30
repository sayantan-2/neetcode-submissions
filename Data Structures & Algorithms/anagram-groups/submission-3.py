class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = [[strs[0]]]  # Initialize with first word
        for i in range(1, len(strs)):
            s = strs[i]
            added = False  # Flag to track if `s` is grouped

            for j in output:
                if Counter(s) == Counter(j[0]):  # Compare with first word in group
                    j.append(s)
                    added = True
                    break  # Stop checking once added

            if not added:  # If not grouped, create a new group
                output.append([s])

        return output

                    
        