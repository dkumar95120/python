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

    # function to get all nodes of the graph
    def getNodes(self):
        nodes = []
        for node in self.graph:
            if node not in nodes:
                nodes.append(node)
            for neighbour in self.graph[node]:
                if neighbour not in nodes:
                    nodes.append(neighbour)
        return nodes

    def findShortestPath(self, start, end):
        if start == end:
            return [start]
        # this uses parent hashmap to back track path to the starting node
        parent = {start: None}
        visited = set()
        q = [start]
        while q:
            s = q.pop(0)
            visited.add(s)

            # explore s if it has any neighbors
            if s not in self.graph:
                continue

            for n in self.graph[s]:
                if n not in visited:
                    parent[n] = s
                    q.append(n)
                # if this is the end node compute path by back tracing its ancestors
                if n == end:
                    path=[]
                    while n:
                        path.append(n)
                        n = parent[n]
                    return path[::-1]
        # apparently end is not reachable from s so return -1
        return -1

    def dfsVisit (self, node, visited, path):
        visited.add(node)
        # traverse neighbors if it has any
        if node in self.graph:
            for v in self.graph[node]:
                if v not in visited:
                    self.dfsVisit(v, visited, path)
        path.insert(0,node)


    def topologicalSort (self):
        visited = set()
        path = []
        for v in self.graph:
            if v not in visited:
                self.dfsVisit(v, visited, path)
        return path

    # getting sutck in the while loop over stack - will need to revisit this later
    def iterative_topological_sort(self):
        toporder = [] # overall topological order, a sum of order of each unvisited starting node
        visited = set()
        for node in self.graph:
            if node in visited:
                continue
            stack = []    # 
            order = []    # order will be in reverse order at first
            q = [node]    # seed q with the current node of the graph
            while q:
                v = q.pop()
                if v not in visited:
                    visited.add(v)
                    q.extend(self.graph[v])

                    while stack:
                        if v not in self.graph[stack[-1]]:
                            order.append(stack.pop())

                    stack.append(v)
            # deposit this order into the overall topological order
            toporder = stack + order[::-1] + toporder
        return toporder

    # Function to print a BFS/DFS traversal of a graph 
    def traverse_bfs(self):   
        #create a queue for path
        path = []

        # Mark all the vertices as not visited 
        visited = set()
  
        for s in self.graph:
            if s in visited:
                continue
            # create a queue for the subpath from this vertex
            print('visiting node', s)
            subpath = []

            # Mark the source node as visited and enqueue it 
            queue = [s]
      
            while bool(queue): 
      
                # Dequeue a vertex from queue and add to our subpath for the starting node
                s = queue.pop(0)
                if s not in visited:
                    subpath.append(s)
                    visited.add(s)
      
                # If dequeued vertex has adjascent vertices, visit them
                # If a adjacent vertex has not been visited, mark it visited and enqueue it 
                if s in self.graph:
                    for i in self.graph[s]: 
                        if i not in visited: 
                            queue.append(i) 
            # prepend this subpath to the overall path
            path.extend(subpath)
        return path

    def find_shortest_path(self, start, end):
        # return path if start is end
        if start == end:
            return "Start = end"
     
        # keep track of visited nodes
        visited = set()
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
                visited.add(node)
     
        # in case there's no path between the 2 nodes
        return -1

def isSorted(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False 
    return True

def getLetterSequenceInWord(word):
    letterSeq = [word[0]]
    prev = word[0]
    for ch in word[1:]:
        if ch != prev:
            letterSeq.append(ch)
            prev = ch
    return letterSeq

def alphaSequence(words):
    graph = Graph()
    for word in words:
        letterSeq = getLetterSequenceInWord(word)
        for i in range(len(letterSeq)-1):
            graph.addEdge(letterSeq[i],letterSeq[i+1])

    sequence = graph.topologicalSort()
    for word in words:
        indices=[]
        for c in getLetterSequenceInWord(word):
            indices.append(sequence.index(c))
        if not isSorted(indices):
            print(sequence)
            return -1
    return sequence


