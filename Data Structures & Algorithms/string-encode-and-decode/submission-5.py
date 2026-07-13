class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans
    def decode(self, s: str) -> List[str]:
        if s is None or len(s) == 0:
            return []
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            content=s[j+1:j+1+length]
            ans.append(content)
            i=j+1+length
        return ans