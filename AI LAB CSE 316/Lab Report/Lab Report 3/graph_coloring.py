def is_safe(graph, vertex, colors, color, V):
    for i in range(V):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True

def graph_coloring_util(graph, k, colors, vertex, V):
    if vertex == V:
        return True

    for color in range(1, k + 1):
        if is_safe(graph, vertex, colors, color, V):
            colors[vertex] = color
            if graph_coloring_util(graph, k, colors, vertex + 1, V):
                return True
            colors[vertex] = 0
    return False

def solve_graph_coloring():
    print("Enter the number of vertices (N), edges (M), and colors (K):")
    N, M, K = map(int, input().split())
    
    graph = [[0] * N for _ in range(N)]
    
    print("\nEnter the edges (u v):")
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1
    
    colors = [0] * N
    
    if graph_coloring_util(graph, K, colors, 0, N):
        print(f"\nColoring Possible with {K} Colors")
        print(f"Color Assignment: {colors}")
    else:
        print(f"\nColoring Not Possible with {K} Colors")

if __name__ == "__main__":
    solve_graph_coloring() 