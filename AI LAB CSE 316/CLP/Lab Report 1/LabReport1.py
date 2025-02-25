import random

class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = random.randint(4, 7)
        self.source = None
        self.goal = None
        self.goal_level = 999999
        self.state = 0
        self.path = []
        self.topological_order = []

    def generate_grid(self):
        grid = [[random.randint(0, 1) for _ in range(self.N)] for _ in range(self.N)]
        return grid

    def find_valid_position(self, grid):
        while True:
            x, y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            if grid[x][y] == 1:
                return x, y

    def init(self):
        graph = self.generate_grid()
        self.N = len(graph)

        source_x, source_y = self.find_valid_position(graph)
        goal_x, goal_y = self.find_valid_position(graph)
        while (source_x, source_y) == (goal_x, goal_y):
            goal_x, goal_y = self.find_valid_position(graph)

        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, self.goal_level)
        
        print("Generated Grid:")
        for row in graph:
            print(row)
        print("\nSource:", (source_x, source_y))
        print("Goal:", (goal_x, goal_y))

        self.st_dfs(graph, self.source)

        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal.depth)
            print("DFS Path:", self.path)
            print("Topological Order:", self.topological_order)
        else:
            print("Goal cannot be reached from the starting block")

    def print_direction(self, m, x, y):
        if m == 0:
            print("Moving Down ({}, {})".format(x, y))
        elif m == 1:
            print("Moving Up ({}, {})".format(x, y))
        elif m == 2:
            print("Moving Right ({}, {})".format(x, y))
        else:
            print("Moving Left ({}, {})".format(x, y))

    def st_dfs(self, graph, u):
        graph[u.x][u.y] = 0
        self.path.append((u.x, u.y))
        self.topological_order.append((u.x, u.y))
        
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            
            if (0 <= v_x < self.N) and (0 <= v_y < self.N) and graph[v_x][v_y] == 1:
                v_depth = u.depth + 1
                self.print_direction(j, v_x, v_y)
                
                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal.depth = v_depth
                    return
                
                child = Node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)
            
            if self.found:
                return


def main():
    d = DFS()
    d.init()

if __name__ == "__main__":
    main()
