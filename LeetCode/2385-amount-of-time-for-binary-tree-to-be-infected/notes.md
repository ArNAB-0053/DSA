### Intuition

> Kind of same as https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
> can visit this for proper breakdown for how actually solve this kinda problem, as mostly follows kinda same process

- store child in parent map `parent -> map`
- with this you will have the path a node can follow that will be `left`, `right` and `it's parent`
- so try to form an undirected graph using Graph BFS with this and get the `height`