# Experiment - 2
# Implement the BFS - DFS for Route solving problem

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['I'],
    'G': [],
    'H': ['J'],
    'I': [],
    'J': []
}

#===============================================

from collections import deque

def bfs(graph, start, goal):
    
    queue = deque([[start]])    # Queue stores paths (FIFO)
    visited = set()             # Track visited nodes
    nodes_explored = 0          # Counter for explored nodes

    while queue:                        # Loop until queue is empty
        path = queue.popleft()          # Get oldest path from front
        current = path[-1]               # Get last node of path

        if current in visited:       # Skip if already visited
            continue
        
        visited.add(current)        # Mark node as visited
        nodes_explored += 1             # Increment counter
        print("Explored:", current)

        if current == goal:             # Check if goal is reached
            return path, nodes_explored
        
        for childrens in graph[current]:         # Check all neighbour/childrens
            if childrens not in visited:            # If childrens is new
                queue.append(path + [childrens])     # Add new path to back
        
    return None, nodes_explored # Return if no path found




def dfs(graph, start, goal):
    stack = [[start]]                # Stack stores paths (LIFO)
    visited = set()                  # Track visited nodes
    nodes_explored = 0               # Counter for explored nodes

    while stack:                     # Loop until stack is empty
        path = stack.pop()           # Get newest path from top
        current = path[-1]           # Get last node of path

        if current in visited:      # Skip if already visited
            continue

        visited.add(current)        # Mark node as visited
        nodes_explored += 1         # Increment counter
        print("Explored:", current)

        if current == goal:                 # Check if goal is reached
            return path, nodes_explored
        
        for childrens in graph[current]:            # Check all neighbour/childrens
            if childrens not in visited:            # If childrens is new
                stack.append(path + [childrens])    # Push new path to top
        
    return None, nodes_explored                  # Return if no path found



#===========================================

import time


print("----- BFS -----")  
# from left -> right 

t = time.perf_counter()

path1, nodes_explored1 = bfs(graph, 'A', 'J')

bfs_time = time.perf_counter() - t

print("Path:", path1)
print("Nodes explored:", nodes_explored1)
print("Time taken by bfs:", bfs_time, "sec")


#====

print("\n----- DFS -----")   
# starts from (A) - Rightmost branch (C) --> Leftmost branch (B) 

t = time.perf_counter()

path2, nodes_explored2 = dfs(graph, 'A', 'J')

dfs_time = time.perf_counter() - t

print("Path:", path2)
print("Nodes explored:", nodes_explored2)
print("Time taken by dfs:", dfs_time, "sec")

