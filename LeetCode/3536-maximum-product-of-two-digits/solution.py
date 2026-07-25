class Solution:
    def maxProduct(self, n: int) -> int:
        maxx, snd_max = 0, 0

        while n != 0:
            digit = n % 10
            if digit > maxx:
                snd_max = maxx
                maxx = digit
            elif digit > snd_max:
                snd_max = digit
            n //= 10

        return maxx * snd_max