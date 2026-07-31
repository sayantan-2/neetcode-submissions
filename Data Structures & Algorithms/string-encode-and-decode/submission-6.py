class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr=""
        for word in strs:
            finalStr+=word+"#-"
        
        return finalStr

    def decode(self, s: str) -> List[str]:
        return s.split("#-")[:-1]