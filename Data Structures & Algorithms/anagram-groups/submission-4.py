class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs={}
        for word in strs:
            sortedWord="".join(sorted(word))
            if sortedWord not in sortedStrs:
                sortedStrs[sortedWord] = []
            sortedStrs[sortedWord].append(word)
        
        final = []
        for v in sortedStrs.values():
            final.append(v)

        return final