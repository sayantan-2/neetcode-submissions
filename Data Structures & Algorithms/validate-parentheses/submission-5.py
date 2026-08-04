class Solution:
    def isValid(self, s: str) -> bool:
        vp={")":"(","}":"{","]":"["}
        arr=[]
        for ch in s:
            if ch in vp:
                if not arr:
                    return False
                if vp[ch]!=arr.pop():
                    return False
            else:
                arr.append(ch)

        return not arr