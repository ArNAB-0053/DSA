## Approach 1 - General Idea for Approach 1 (Pure Math)
---
### Definitions

* `n` → given number
* `l` → number of digits in `n`

### Formula

The formula can be understood as two main sections:

**Total commas = Complete range contribution + Partial range contribution**

```text
int("9" * (l - 4) + "000") × (l // 3 if l % 3 != 0 else l // 3 - 1)
+
(n - 10^(l - 1)) + 1
```

---

### 1. Complete Range Contribution

```text
int("9" * (l - 4) + "000")
×
(l // 3 if l % 3 != 0 else l // 3 - 1)
```

#### A. Number of complete numbers

```text
int("9" * (l - 4) + "000")
```

This represents the number of integers from `1000` up to the largest number with fewer than `l` digits.

Examples:

```text
l = 5 → 9000   → 1000 to 9999
l = 6 → 99000  → 1000 to 99999
l = 7 → 999000 → 1000 to 999999
```

#### B. Number of commas per number

```text
l // 3 if l % 3 != 0 else l // 3 - 1
```

A comma is inserted after every 3 digits from the right.

Normally, `l // 3` gives the number of comma positions, but when `l` is exactly divisible by `3`, it counts one extra comma.

Examples:

```text
5 digits → 12,345       → 1 comma → 5 // 3 = 1
6 digits → 123,456      → 1 comma → 6 // 3 - 1 = 1
7 digits → 1,234,567    → 2 commas → 7 // 3 = 2
9 digits → 123,456,789  → 2 commas → 9 // 3 - 1 = 2
```

So this expression is equivalent to:

```text
floor((l - 1) / 3)
```

Therefore:

```text
Complete range contribution
=
number of complete numbers × commas per number
```

---

### 2. Partial Range Contribution

```text
(n - 10^(l - 1)) + 1
```

This calculates the number of integers from the **first `l`-digit number** up to `n`.

For example, if:

```text
n = 10005
l = 5
```

then:

```text
10005 - 10^4 + 1
= 10005 - 10000 + 1
= 6
```

The numbers are:

```text
10000, 10001, 10002, 10003, 10004, 10005
```

Since all of them have `1` comma, the contribution is `6`.

---

### Example: `n = 10005`

Here:

```text
l = 5
```

#### Complete range

```text
int("9" * (5 - 4) + "000")
= int("9000")
= 9000
```

Number of commas:

```text
5 // 3 = 1
```

Therefore:

```text
9000 × 1 = 9000
```

#### Partial range

```text
10005 - 10^4 + 1
= 6
```

#### Final answer

```text
9000 + 6 = 9006
```

---

### Final Formula

```python
int("9" * (l - 4) + "000") 
*
(l // 3 if l % 3 != 0 else l // 3 - 1) 
+
(n - 10 ** (l - 1)) + 1
```

#### Overall idea

```text
Total commas
=
Complete range contribution
+
Partial range contribution
```

The complete range counts all smaller numbers with commas, while the partial range counts the remaining `l`-digit numbers from `10^(l-1)` through `n`.

### Complexity

* **Time:** `O(log n)`
* **Space:** `O(log n) - auxiliary space due to converting n to a string`

---

## Approach 2 - Position-Based Approach

### Main Idea

Instead of counting commas by **digit ranges**, count each **comma position independently**.

A comma can appear at positions:

```text
1,000
1,000,000
1,000,000,000
1,000,000,000,000
...
```

So we start with:

```python
p = 1000
```

and keep multiplying `p` by `1000`.

---

### How It Works

For each comma position `p`:

```text
p = 1000, 1,000,000, 1,000,000,000, ...
```

Every number from `p` to `n` contains a comma at that position.

The number of such integers is:

```text
n - p + 1
```

Therefore:

```text
Total commas = Σ (n - p + 1)
```

where `p` takes the values:

```text
1000, 1000000, 1000000000, ...
```

---

### Example: `n = 1,000,005`

#### First comma position

```text
p = 1,000
```

Numbers from `1,000` to `1,000,005`:

```text
1,000,005 - 1,000 + 1 = 999,006
```

So the thousands comma contributes:

```text
999,006
```

#### Second comma position

```text
p = 1,000,000
```

Numbers from `1,000,000` to `1,000,005`:

```text
1,000,005 - 1,000,000 + 1 = 6
```

So the millions comma contributes:

```text
6
```

#### Next position

```text
p = 1,000,000,000
```

Since `p > n`, stop.

#### Final Answer

```text
999,006 + 6 = 999,012
```

---

### Key Insight

> **Don't count commas per number. Count how many numbers contain each possible comma position.**

### Complexity

* **Time:** `O(log n)`
* **Space:** `O(1)`

