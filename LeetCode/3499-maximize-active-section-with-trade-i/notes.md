### Approach

1. count the number of `1`s
2. store the number of `0`s appearing before `1`
3. _edge case:_ if that length of that list is < 2 then just return number of ones present in the original string
3. get the highest pair from the stored 0s(by adding pairs)
4. return max_pairs + no. of ones present in the original string

---------

#### Note:

The problem statement mentions treating the string as: `t = '1' + s + '1'`

to handle boundary cases. However, **this is not required for this approach**. By simply storing all contiguous `0`-runs from the original string, we naturally obtain the same result, so the padding can be omitted.
