### Approach 1: DSU APPROACH 
This will return the actual answer, but for this problem it is a overkill.
But it is a general answer for this kinda questions.

### Approach 2: by creating component ID`Best for this problem`

> this approach is best for this specifix problem because - **nums is sorted, so any gap > maxDiff splits the graph into a new connected component**

#### Intuition

- create an array to store the component ID
- loop in the nums
	- if the difference greater than `maxDiff`, create new ID by adding `1` 
	- else store previous component's ID
- create an answer array
- loop through queries
	- append the truthness of `pre[u]` and `pre[v]`
- return answer array