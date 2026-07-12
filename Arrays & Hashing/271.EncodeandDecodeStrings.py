class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st+=str(len(s))+"#"+s
        return st

    def decode(self, s: str) -> List[str]:
        Lists = []
        i=0 
        while i < len(s):
            j=i
            while s[j]!="#":
                j+=1
            
            ln = int(s[i:j])

            i = j+1

            word = s[i:i+ln]

            Lists.append(word)

            i+=ln

        return Lists