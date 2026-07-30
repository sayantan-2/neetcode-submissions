class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=len(strs)
        ml=[]
        cache=[]
        for i in range(l):
            s = strs[i]
            if s not in cache:
                il=[]
                il.append(s)
                for j in range(i+1,l):
                    t=strs[j]
                    if Counter(s) == Counter(t):
                        il.append(t)
                        cache.append(t)
                ml.append(il)

        return ml