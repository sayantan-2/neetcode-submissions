class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr=""
        for word in strs:
            finalStr+=word+"-_-"
        
        return finalStr

    def decode(self, s: str) -> List[str]:
        return s.split("-_-")[:-1]