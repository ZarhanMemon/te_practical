# Greedy Best First Search (GBFS) and A* Search Algorithm Implementation


import heapq
import time

graph = {
    'A': [('B', 7) , ('C' , 12)],
    'B':[('G',5)],
    'C':[('G',8)],
    'G':[]
}

heuristic = {
    'A':5,
    'B':6,
    'C':3,
    'G':0
}


#Greedy Best First Search Algorithm
# f(n) = h(n)
# priority queue will be sorted based on h(n) value

def gbfs( graph , heuristic , start , goal):
    
    priority_queue = []
    
    heapq.heappush( priority_queue , (heuristic[start], start ,[start] , 0))
    
    visited = set()
    node_explored = 0
    
    while priority_queue :
        
        h_value , current , path , cost = heapq.heappop(priority_queue)
        
        
        if current in visited:
            continue
        
        visited.add(current)
        node_explored += 1
        
        if current == goal :
            return path , cost , node_explored
        
        for  nieghbour , edge_cost in graph[current]:
            
            if nieghbour not in visited:
                heapq.heappush( priority_queue ,
                               (heuristic[nieghbour] ,
                                nieghbour ,
                                path + [nieghbour],
                                cost + edge_cost))
                
    return None , None , node_explored


t = time.time()
path , cost , node_explored = gbfs(graph , heuristic , 'A' , 'G')

gbfs_time = time.time() - t

print("Path:", path)
print("Cost:", cost)
print("Nodes Explored:", node_explored)
print("GBFS Time:", gbfs_time)


#=================================


# Astar search algorithm
# f(n) = g(n) + h(n)
# priority queue will be sorted based on f(n) value


# A* selects the next node using the evaluation function:
#     f(n) = g(n) + h(n)

# where:
#   - g(n) is the actual cost from the start node to node n.
#   - h(n) is the estimated cost from node n to the goal.
#   - f(n) is the estimated total cost of a path through node n.



def astar( graph , heuristic , start , goal ):
    
    priority_queue = []
    
    heapq.heappush( priority_queue , ( heuristic[start] , 0 , start , [start] ))
    
    best_cost = { start:0 }
    nodes_explored = 0


    while priority_queue :
                        
        f_value , g_value , current , path  = heapq.heappop(priority_queue)
        
        if g_value > best_cost.get(current):
            continue
        
        nodes_explored += 1
        
        if current == goal :
            return path , g_value , nodes_explored
        
        
        for neighbour , edge_cost in graph[current]:
            
            new_g = g_value + edge_cost
            
            if new_g < best_cost.get( neighbour , float('inf')):                
                
                best_cost[neighbour] = new_g
                new_f = new_g + heuristic[neighbour]
                
                heapq.heappush( priority_queue , ( new_f ,
                                                  new_g ,
                                                  neighbour ,
                                                  path + [neighbour] ))
                
    return None , None , nodes_explored


t = time.time()

astar_path , astar_cost , astar_nodes_explored = astar(graph , heuristic , 'A' , 'G')

astar_time = time.time() - t

print("\nA* Search:")
print("Path:", astar_path)
print("Cost:", astar_cost)
print("Nodes Explored:", astar_nodes_explored)
print("A* Time:", astar_time)



# Explanation of A* Search:

# Start at node A:
# 1. Add A to the priority queue with f(A) = g(A) + h(A) = 0 + 5 = 5.
# 2. Remove A from the queue. Explore its neighbours B and C.
# 3. For B: g(B) = g(A) + cost(A, B) = 0 + 7 = 7, f(B) = g(B) + h(B) = 7 + 6 = 13.
# 4. For C: g(C) = g(A) + cost(A, C) = 0 + 12 = 12, f(C) = g(C) + h(C) = 12 + 3 = 15.
# 5. Add B and C to the priority queue. The queue now contains [(13, B), (15, C)].
# 6. Remove B from the queue (smallest f-value). Explore its neighbour G.
# 7. For G: g(G) = g(B) + cost(B, G) = 7 + 5 = 12, f(G) = g(G) + h(G) = 12 + 0 = 12.
# 8. Add G to the priority queue. The queue now contains [(12, G), (15, C)].
# 9. Remove G from the queue (smallest f-value). Since G is the goal, return the path [A, B, G] and cost 12.    

