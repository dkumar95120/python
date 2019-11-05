
class Graph: 
  
    # Constructor 
    def __init__(self, dict): 
  
        # default dictionary to store graph 
        self.graph = dict

    def dfsVisit (self, node, ancestry, visited, path):
        visited.add(node)
        # traverse neighbors if it has any
        if node in self.graph:
            for v in self.graph[node]:
                if v in ancestry:
                    raise ValueError('Circular dependency on ' + v)
                if v not in visited:
                    self.dfsVisit(v, ancestry +' ' + v, visited, path)
        
        path.append(node)


def buildOrder (node, depList):
    if not bool(node) or not bool(depList):
        return 'Please provide a valid build object and dependency list'

    if node not in depList:
        return node + ' has no dependencies'

    graph = Graph(depList)
    path = []
    visited = set()
    
    try:
        graph.dfsVisit(node, node, visited, path)

    except ValueError as err:
        return err.args

    return path 

print('test case 1: with common dependencies on trees for commercial and parks')
depList = {'city': ['roads','commercial','parks','residential'],
           'roads': ['sewar', 'electrical_lines', 'gas_lines'],
           'commercial': ['building','parking_lot','trees'],
           'parks': ['play_ground', 'kids_play_area','trees'],
           'play_ground': ['grass', 'baseball_diamond', 'walk_way','residential'],
           'residential':['building', 'parking_lot','grass']
           }

print(buildOrder('city', depList))

print('\ntest case 2: with circular dependency among parks, play_ground, and residential')
depList = {'city': ['roads','commercial','parks','residential'],
           'roads': ['sewar', 'electrical_lines', 'gas_lines'],
           'commercial': ['building','parking_lot','trees'],
           'parks': ['play_ground', 'kids_play_area','trees'],
           'play_ground': ['grass', 'baseball_diamond', 'walk_way','residential'],
           'residential':['building', 'parking_lot','grass','parks']
           }

print(buildOrder('city', depList))

print('\ntest case 3: build object witout dependency')
print(buildOrder('library', depList))

print('\ntest case 4: null build object')
print(buildOrder(None, depList))

print('\ntest case 5: null dependency list')
print(buildOrder('city', None))
