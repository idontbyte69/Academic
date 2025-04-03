# Maze Solver using IDDFS

## Sample Test Cases

### Case#1
Input:
```
4 4
0 0 1 0
1 0 1 0
0 0 0 0
1 1 0 1
Start: 0 0
Target: 2 3
```

Output:
```
Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (1,0), (1,1), (0,1), (2,1), (2,2), (2,3)]
```

### Case#2
Input:
```
3 3
0 1 0
0 1 0
0 1 0
Start: 0 0
Target: 2 2
```

Output:
```
Path not found at max depth 6 using IDDFS
``` 