class Solution:
    def isValid(self, s: str) -> bool:
        vp={")":"(","}":"{","]":"["}
        op=['(','{','[']
        cl=[')','}',']']
        l=len(s)
        arr=[]
        for i in range(l):
            ch=s[i]
            if ch in op:
                arr.append(ch)
            if ch in cl:
                if not arr:
                    return False
                if vp[ch]!=arr.pop():
                    return False

        return not arr
                