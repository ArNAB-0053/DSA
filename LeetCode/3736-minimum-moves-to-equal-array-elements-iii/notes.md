### Intuition
As we can increase only, to match all the element on minimum moves, we have to match all elements to maximum among them. 

**For example,** nums = [2, 1, 3]; to match all of them with minimum moves, we can convert 2 and 1 to 3 as 3 is the max. 

**How many moves it will take ?**

Ans: `max = 3`
- max - 2 = 3 - 2 = 1
- max - 1 = 3 - 1 = 2
- max - 3 = 3 - 3 = 0

So, `(1+2+0) = 3` moves is the answer