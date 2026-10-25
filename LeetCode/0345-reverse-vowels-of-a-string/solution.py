class Solution:
    # VOWELS = set("aeiouAEIOU")
    # def isVowel(self, ch: str) -> bool:
    #     return ch in self.VOWELS

    # def reverseVowels(self, s: str) -> str:
    #     i, j = 0, len(s) - 1
    #     arr = list(s)

    #     while i < j:
    #         if not self.isVowel(arr[i]) and not self.isVowel(arr[j]):
    #             # advance both
    #             i += 1
    #             j -= 1
    #         elif self.isVowel(arr[i]) and self.isVowel(arr[j]):
    #             # swap and advance both
    #             arr[i], arr[j] = arr[j], arr[i]
    #             i += 1
    #             j -= 1
    #         elif not self.isVowel(arr[i]):
    #             i += 1
    #         else:
    #             j -= 1
        
    #     return "".join(arr)

    # SHORTER and GOOD LOOKING version
    def reverseVowels(self, s: str) -> str:
        VOWELS = set("aeiouAEIOU")
        i, j= 0, len(s) - 1
        chars = list(s)

        while i < j:
            while i < j and chars[i] not in VOWELS:
                i += 1
            while i < j and chars[j] not in VOWELS:
                j -= 1
            # swap
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        
        return "".join(chars)