class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out = []
        for word in words:
            weight = 0
            for ch in word:
                weight += weights[ord(ch) - ord('a')]
            rem = ord('z') - weight % 26 #@ mod 26
            out.append(chr(rem))

        return "".join(out)