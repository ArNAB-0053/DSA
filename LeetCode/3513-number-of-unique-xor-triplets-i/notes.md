## Observation

- For `n >= 3`, the answer is the **smallest power of 2 strictly greater than `n`**.
- The cases `n = 1` and `n = 2` are exceptions, where the answer is simply `n`.

### Why?

- Since `nums` is a **permutation of `[1, 2, ..., n]`**, the largest number determines the maximum number of bits required.
- Let `k` be the number of bits needed to represent `n`.
- XOR **cannot introduce a new higher bit**. If all operands fit within `k` bits, their XOR result will also fit within `k` bits.
- Therefore, every possible XOR value lies in the range:

  ```text
  0 to (2^k - 1)
  ```

- The total number of possible XOR values is:

  ```text
  2^k
  ```

- Since `2^k` is the **smallest power of 2 greater than `n`**, that is the answer.

### Examples

| `n` | Bits Required | Answer |
|----:|:-------------:|-------:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 2 | 4 |
| 4 | 3 | 8 |
| 5 | 3 | 8 |
| 8 | 4 | 16 |
| 15 | 4 | 16 |
| 16 | 5 | 32 |