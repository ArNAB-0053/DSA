## Core Idea

The problem consists of **two separate tasks**:

1. **Find the shortest distance** from `beginWord` to every reachable word.
2. **Print all shortest transformation sequences.**

Since these are different problems, we use two different algorithms:

* **BFS** → Finds the shortest paths.
* **DFS + Backtracking** → Reconstructs every shortest path.

---

# Step 1: Convert Word List to a Set

Convert the given `wordList` into a `set`.

### Why?

* Searching inside a list takes **O(N)**.
* Searching inside a set takes **O(1)**.

The set also acts as the **visited structure** for BFS.

---

# Step 2: Perform BFS

Run BFS starting from `beginWord`.

During BFS maintain:

* **Queue** → Level-order traversal.
* **Distance Map (`dist`)** → Stores the shortest distance from `beginWord`.
* **Parent Dictionary (`parentdict`)** → Stores every parent of a word on a shortest path.

Example:

```text
der
├── des
└── dfr
```

Both reach

```text
dfs
```

Store

```text
parents = {
    "dfs": ["des", "dfr"]
}
```

instead of only one parent.

---

# Step 3: Process Every Generated Word

For every newly generated word:

### Case 1: First Time Discovered

If the word is **not present in `dist`**:

* Store its shortest distance.
* Store its parent.
* Push it into the queue.

Reason:

This is the first (therefore shortest) way to reach this word.

---

### Case 2: Another Shortest Path Found

If

```text
dist[newWord] == dist[currentWord] + 1
```

then another shortest path reaches the same word.

Only add another parent.

Example:

```text
des ---> dfs
dfr ---> dfs
```

Store

```text
parents["dfs"] = ["des", "dfr"]
```

Do **not** push it into the queue again because its shortest distance is already known.

---

# Step 4: Remove Words Level by Level

Do **not** remove words immediately after discovering them.

Instead:

* Finish processing the entire BFS level.
* Remove all words discovered in that level together.

### Why?

If removed immediately, another node in the same level may lose the chance to become an additional parent, causing some shortest paths to disappear.

---

# Step 5: Stop BFS

Once `endWord` has been assigned a shortest distance, finish the current BFS level and stop.

Reason:

BFS guarantees the first discovered distance is the minimum.

Any deeper level cannot produce another shortest path.

---

# Step 6: Build All Paths Using DFS

After BFS, we already know:

* The shortest distance.
* Every valid parent for every shortest path.

Now perform DFS starting from `endWord`.

Maintain:

```text
path = Current transformation sequence
```

For every parent:

1. Append parent to the current path.
2. Recurse.
3. Pop the parent (Backtrack).

---

# Step 7: Base Case

When

```text
currentWord == beginWord
```

a complete shortest path has been found.

Store a **reversed copy** of the current path because DFS was built from `endWord` to `beginWord`.

---

# Overall Flow

```text
Convert wordList to Set
        │
        ▼
Run BFS
        │
        ▼
Compute Shortest Distances
        │
        ▼
Build Parent Dictionary
        │
        ▼
Run DFS + Backtracking
        │
        ▼
Generate All Shortest Transformation Sequences
```

---

# Memory Trick

> **BFS discovers the shortest-path graph.**

> **DFS reconstructs every shortest path from that graph.**

Or even shorter:

```text
BFS → Discover
DFS → Reconstruct
```
