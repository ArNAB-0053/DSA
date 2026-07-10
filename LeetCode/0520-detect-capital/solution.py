class Solution:
    # --------------------------------------------
    #               Naive Approach
    # --------------------------------------------
    # Works and absolutely correct answer but code quality can be improved

    # def getCase(self, ch: str):
    #     if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
    #         return "capital"
    #     return "lower"

    # def detectCapitalUse(self, word: str) -> bool:
    #     n = len(word)

    #     if n == 1:
    #         return True

    #     firstLetter = word[0]
    #     secondLetter = word[1]

    #     if self.getCase(firstLetter) == "capital":
    #         if self.getCase(secondLetter) == "capital":
    #             for i in range(2, n):
    #                 if self.getCase(word[i]) == "lower":
    #                     return False
    #         elif self.getCase(secondLetter) == "lower":
    #             for i in range(2, n):
    #                 if self.getCase(word[i]) == "capital":
    #                     return False

    #     elif self.getCase(firstLetter) == "lower":
    #         for i in range(1, n):
    #             if self.getCase(word[i]) == "capital":
    #                 return False

    #     return True

    # --------------------------------------------
    #           only using in-build methods
    # --------------------------------------------
    # def detectCapitalUse(self, word: str) -> bool:
    #     return (
    #         word.isupper() or
    #         word.islower() or 
    #         word.istitle()
    #     )


    # --------------------------------------------
    #           Slight better version
    #              (for interviews)
    # --------------------------------------------

    # python already has it's buildin isupper() funtion
    # but not using is
    def isUpper(self, ch: str):
        # this also works
        return 'A' <= ch <= 'Z'

    def detectCapitalUse(self, word: str) -> bool:
        # Intuition
        # - will assume uppercase case is 1 and lower is 0
        # - and loop through the word adding the value
        # - if that comes as 
        # - - 0: all lowercase (valid)
        # - - same as len(word): all upper (valid)
        # - - 1: means only one uppercase, in that case we don't know which one is exactly upper, so will case the first letter is upper, if yes -> valid else -> not valid

        summ = 0
        for ch in word:
            if self.isUpper(ch):
                summ += 1

        return summ == 0 or summ == len(word) or (summ == 1 and self.isUpper(word[0]))