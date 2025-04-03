def is_valid(x, y, rows, cols, maze, visited):
    return (0 <= x < rows and 
            0 <= y < cols and 
            maze[x][y] == 0 and 
            not visited[x][y])

def dfs(maze, start, target, visited, path, depth, max_depth):
    rows, cols = len(maze), len(maze[0])
    x, y = start
    
    if depth > max_depth:
        return False, path
    if start == target:
        return True, path
    
    visited[x][y] = True
    path.append(start)
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y, rows, cols, maze, visited):
            found, new_path = dfs(maze, (new_x, new_y), target, visited, path.copy(), depth + 1, max_depth)
            if found:
                return True, new_path
    
    visited[x][y] = False
    path.pop()
    return False, path

def iddfs(maze, start, target):
    rows, cols = len(maze), len(maze[0])
    max_depth = rows * cols
    
    for depth in range(max_depth + 1):
        visited = [[False] * cols for _ in range(rows)]
        found, path = dfs(maze, start, target, visited, [], 0, depth)
        if found:
            return True, path, depth
    
    return False, [], max_depth

def solve_maze():
    print("Enter the number of rows and columns (space-separated):")
    rows, cols = map(int, input().split())
    
    print("\nEnter the maze grid (0 for path, 1 for wall):")
    maze = []
    for i in range(rows):
        print(f"Enter row {i+1} ({cols} numbers space-separated):")
        row = list(map(int, input().split()))
        if len(row) != cols:
            print(f"Error: Row {i+1} must contain exactly {cols} numbers")
            return
        maze.append(row)
    
    print("\nYour maze:")
    for row in maze:
        print(" ".join(map(str, row)))
    
    print("\nEnter start position (row column):")
    start_x, start_y = map(int, input().split())
    if not (0 <= start_x < rows and 0 <= start_y < cols):
        print("Error: Start position is out of bounds")
        return
    if maze[start_x][start_y] == 1:
        print("Error: Start position cannot be a wall")
        return
    
    print("Enter target position (row column):")
    target_x, target_y = map(int, input().split())
    if not (0 <= target_x < rows and 0 <= target_y < cols):
        print("Error: Target position is out of bounds")
        return
    if maze[target_x][target_y] == 1:
        print("Error: Target position cannot be a wall")
        return
    
    start = (start_x, start_y)
    target = (target_x, target_y)
    found, path, depth = iddfs(maze, start, target)
    
    print("\nResult:")
    if found:
        print(f"Path found at depth {depth} using IDDFS")
        print(f"Traversal Order: {path}")
        if path[-1] != target:
            path.append(target)
    else:
        print(f"Path not found at max depth {depth} using IDDFS")

if __name__ == "__main__":
    solve_maze() 