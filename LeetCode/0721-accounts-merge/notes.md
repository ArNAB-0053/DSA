### Intuition
- Two accounts belong to the same person if they share at least one email.
- If Account A shares an email with B, and B shares an email with C,
  then all three accounts belong to the same person.
- This forms groups of connected accounts.
- The problem is essentially finding connected components.
- DSU helps us merge accounts that belong to the same component.

### DSU Approach`Better + Simple`
1. Treat each account as a node.
2. Store:
      email -> account index
3. If an email is seen for the first time:
      store its account index.
4. If the email already exists:
      union(current account, stored account).
5. After all unions:
      accounts belonging to the same person will have the same root parent.
6. Group all emails by their root parent.
7. Sort emails and attach the account name.

### DFS/BFS Approach (Alternative)
1. Treat each account as a node.
2. If two accounts share an email, create an edge between them.
3. Build a graph of connected accounts.
4. Run DFS/BFS to find connected components.
5. Merge emails within each component.
6. Sort emails and attach the account name.