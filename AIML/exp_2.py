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


#===================================================================================================
# DRY RUN
#===================================================================================================
# 
# 1. BFS (Queue & Visited Set Track)
# 
# Initialization:
# * queue: [['A']]
# * visited: set()
# 
# Step 1:
# * Queue Action: queue.popleft() -> path = ['A']
# * Current Node: current = 'A'
# * State Updates: visited = {'A'}, nodes_explored = 1
# * Childrens Added: ['A', 'B'] and ['A', 'C'] added to back of path['A']
# * End of Step: queue = [['A', 'B'], ['A', 'C']]
# 
# Step 2:
# * Queue Action: queue.popleft() -> path = ['A', 'B']
# * Current Node: current = 'B'
# * State Updates: visited = {'A', 'B'}, nodes_explored = 2
# * Childrens Added: ['A', 'B', 'D'] and ['A', 'B', 'E'] added to back
# * End of Step: queue = [['A', 'C'], ['A', 'B', 'D'], ['A', 'B', 'E']]
# 
# Step 3:
# * Queue Action: queue.popleft() -> path = ['A', 'C']
# * Current Node: current = 'C'
# * State Updates: visited = {'A', 'B', 'C'}, nodes_explored = 3
# * Childrens Added: ['A', 'C', 'F'] added to back
# * End of Step: queue = [['A', 'B', 'D'], ['A', 'B', 'E'], ['A', 'C', 'F']]
# 
# Step 4:
# * Queue Action: queue.popleft() -> path = ['A', 'B', 'D']
# * Current Node: current = 'D'
# * State Updates: visited = {'A', 'B', 'C', 'D'}, nodes_explored = 4
# * Childrens Added: ['A', 'B', 'D', 'G'] added to back
# * End of Step: queue = [['A', 'B', 'E'], ['A', 'C', 'F'], ['A', 'B', 'D', 'G']]
# 
# Step 5:
# * Queue Action: queue.popleft() -> path = ['A', 'B', 'E']
# * Current Node: current = 'E'
# * State Updates: visited = {'A', 'B', 'C', 'D', 'E'}, nodes_explored = 5
# * Childrens Added: ['A', 'B', 'E', 'H'] added to back
# * End of Step: queue = [['A', 'C', 'F'], ['A', 'B', 'D', 'G'], ['A', 'B', 'E', 'H']]
# 
# Step 6:
# * Queue Action: queue.popleft() -> path = ['A', 'C', 'F']
# * Current Node: current = 'F'
# * State Updates: visited = {'A', 'B', 'C', 'D', 'E', 'F'}, nodes_explored = 6
# * Childrens Added: ['A', 'C', 'F', 'I'] added to back
# * End of Step: queue = [['A', 'B', 'D', 'G'], ['A', 'B', 'E', 'H'], ['A', 'C', 'F', 'I']]
# 
# Step 7:
# * Queue Action: queue.popleft() -> path = ['A', 'B', 'D', 'G']
# * Current Node: current = 'G'
# * State Updates: visited = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}, nodes_explored = 7
# * Childrens Added: None (G has no Childrens)
# * End of Step: queue = [['A', 'B', 'E', 'H'], ['A', 'C', 'F', 'I']]
# 
# Step 8:
# * Queue Action: queue.popleft() -> path = ['A', 'B', 'E', 'H']
# * Current Node: current = 'H'
# * State Updates: visited = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}, nodes_explored = 8
# * Childrens Added: ['A', 'B', 'E', 'H', 'J'] added to back
# * End of Step: queue = [['A', 'C', 'F', 'I'], ['A', 'B', 'E', 'H', 'J']]
# 
# Step 9:
# * Queue Action: queue.popleft() -> path = ['A', 'C', 'F', 'I']
# * Current Node: current = 'I'
# * State Updates: visited = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'}, nodes_explored = 9
# * Childrens Added: None (I has no Childrens)
# * End of Step: queue = [['A', 'B', 'E', 'H', 'J']]
# 
# Step 10:
# * Queue Action: queue.popleft() -> path = ['A', 'B', 'E', 'H', 'J']
# * Current Node: current = 'J'
# * Goal Check: J == J is True!
# * Return Statement: Returns (['A', 'B', 'E', 'H', 'J'], 10)


#---

# 
# 2. DFS (Stack & Visited Set Track)
# 
# Initialization:
# * stack: [['A']]
# * visited: set()
# 
# Step 1:
# * Stack Action: stack.pop() -> path = ['A']
# * Current Node: current = 'A'
# * State Updates: visited = {'A'}, nodes_explored = 1
# * Childrens Added: ['A', 'B'] and ['A', 'C'] pushed to top of path['A']
# * End of Step: stack = [['A', 'B'], ['A', 'C']]
# 
# Step 2:
# * Stack Action: stack.pop() -> path = ['A', 'C'] (Rightmost item branch)
# * Current Node: current = 'C'
# * State Updates: visited = {'A', 'C'}, nodes_explored = 2
# * Childrens Added: ['A', 'C', 'F'] pushed to top
# * End of Step: stack = [['A', 'B'], ['A', 'C', 'F']]
# 
# Step 3:
# * Stack Action: stack.pop() -> path = ['A', 'C', 'F']
# * Current Node: current = 'F'
# * State Updates: visited = {'A', 'C', 'F'}, nodes_explored = 3
# * Childrens Added: ['A', 'C', 'F', 'I'] pushed to top
# * End of Step: stack = [['A', 'B'], ['A', 'C', 'F', 'I']]
# 
# Step 4:
# * Stack Action: stack.pop() -> path = ['A', 'C', 'F', 'I']
# * Current Node: current = 'I'
# * State Updates: visited = {'A', 'C', 'F', 'I'}, nodes_explored = 4
# * Childrens Added: None (I has no Childrens)
# * End of Step: stack = [['A', 'B']]
# 
# Step 5:
# * Stack Action: stack.pop() -> path = ['A', 'B'] (Back to B branch)
# * Current Node: current = 'B'
# * State Updates: visited = {'A', 'B', 'C', 'F', 'I'}, nodes_explored = 5
# * Childrens Added: ['A', 'B', 'D'] and ['A', 'B', 'E'] pushed to top
# * End of Step: stack = [['A', 'B', 'D'], ['A', 'B', 'E']]
# 
# Step 6:
# * Stack Action: stack.pop() -> path = ['A', 'B', 'E']
# * Current Node: current = 'E'
# * State Updates: visited = {'A', 'B', 'C', 'E', 'F', 'I'}, nodes_explored = 6
# * Childrens Added: ['A', 'B', 'E', 'H'] pushed to top
# * End of Step: stack = [['A', 'B', 'D'], ['A', 'B', 'E', 'H']]
# 
# Step 7:
# * Stack Action: stack.pop() -> path = ['A', 'B', 'E', 'H']
# * Current Node: current = 'H'
# * State Updates: visited = {'A', 'B', 'C', 'E', 'F', 'H', 'I'}, nodes_explored = 7
# * Childrens Added: ['A', 'B', 'E', 'H', 'J'] pushed to top
# * End of Step: stack = [['A', 'B', 'D'], ['A', 'B', 'E', 'H', 'J']]
# 
# Step 8:
# * Stack Action: stack.pop() -> path = ['A', 'B', 'E', 'H', 'J']
# * Current Node: current = 'J'
# * Goal Check: J == J is True!
# * Return Statement: Returns (['A', 'B', 'E', 'H', 'J'], 8)
#===================================================================================================
