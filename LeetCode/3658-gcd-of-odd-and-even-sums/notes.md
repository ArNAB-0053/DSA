# GCD of Odd and Even Sums

### Sum of the first n odd numbers

1 + 3 + 5 + ... + (2n - 1) = n²

### Sum of the first n even numbers

2 + 4 + 6 + ... + 2n

Factor out 2:

= 2(1 + 2 + 3 + ... + n)

Using the formula:

1 + 2 + 3 + ... + n = n(n + 1) / 2

Substitute:

= 2 × n(n + 1) / 2

= n(n + 1)

### Compute the GCD

gcd(n², n(n + 1))

Factor out n:

= n × gcd(n, n + 1)

Since n and n + 1 are consecutive integers:

gcd(n, n + 1) = 1

Therefore:

gcd(n², n(n + 1))
= n × 1
= n

### Final Answer

```python
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
```