class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for i, s in enumerate(strs):
            l = len(s)
            encoded_str += str(l) + "#" + s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= "#":
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length

            decoded_str.append(s[start:end])
            i = end
        return decoded_str            
