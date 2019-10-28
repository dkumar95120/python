# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s, bfs=True): 
  
        # Mark all the vertices as not visited 
        visited = []
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited.append(s)
        path = []
  
        while bool(queue): 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) if bfs else queue.pop(-1)
            path.append(s)
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if i not in visited: 
                    queue.append(i) 
                    visited.append(i)
        print(path)

    def find_shortest_path(self, start, end):
        # return path if start is end
        if start == end:
            return "Start = end"
     
        # keep track of visited nodes
        visited = []
        # keep track of all the paths to be checked
        queue = [start]
     
        # keeps looping until all possible paths have been explored
        while queue:
            # pop the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            if node not in visited:
                neighbours = self.graph[node]
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    # return path if neighbour is goal
                    if neighbour == end:
                        return new_path
     
                # mark node as visited
                visited.append(node)
     
        # in case there's no path between the 2 nodes
        return -1