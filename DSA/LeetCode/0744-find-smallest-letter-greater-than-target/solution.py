class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = '{'

        for ch in letters:
            if ord(ch) > ord(target) and ord(ch) < ord(ans):
                ans = ch

        return letters[0] if ans == '{' else ans