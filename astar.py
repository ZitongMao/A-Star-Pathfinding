import heapq

#using built-in heaps to generate a priority queue, storing open lists 
class PriorityQueue:
    def __init__(self):
        self.elements = []
        
    #empty queue
    def empty(self):
        return len(self.elements) == 0
    
    def add(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
        
    def pop(self):
        return heapq.heappop(self.elements)[1]

#This is the preparation section for the gamp map. All the nodes are square grids. 
class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.mountains = []
    
    #make sure that nodes are in the map
    def in_bound(self, node):
        (x, y) = node
        return 0 <= x < self.width and 0 <= y < self.height
    
    #make sure that charaters cannot pass through the mountains
    def passable(self, node):
        return node not in self.mountains
    
    #I'm using Manhattan Method here - the character can only move 4 directions 'up, down, left, right'
    def neighbors(self, node):
        (x, y) = node
        results = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        results = filter(self.in_bound, results)
        results = filter(self.passable, results)
        return results

#preparation for adding the weight to the map. Normal grounds cost 1, and trees cost 2 (will add later)
class WeightedGrid(SquareGrid):
    def __init_(self, width, height):
        super().__init__(width, height)
        self.weights = {}
    
    def cost(self, from_node, to_node):
        #normal ground cost 1
        return self.weights.get(to_node, 1)

#For actually visualizing the map
def draw_tile(graph, node, style, width):
    #Default tile looks like '.'
    t = '.'
    if 'number' in style and node in style['number']: t = "%d" % style['number'][node]
    if 'point_to' in style and style['point_to'].get(node, None) is not None:
        (x1, y1) = node
        (x2, y2) = style['point_to'][node]
        #For different directions, arrowheads
        if x2 == x1 + 1: t = "\u2192"
        if x2 == x1 - 1: t = "\u2190"
        if y2 == y1 + 1: t = "\u2193"
        if y2 == y1 - 1: t = "\u2191"
    #Start point with 'S', Goal point with 'G', paths are '@', mountains are '#'
    if 'start' in style and node == style['start']: t = "S"
    if 'goal' in style and node == style['goal']: t = "G"
    if 'path' in style and node in style['path']: t = "@"
    if node in graph.mountains: t = "#" * width
    return t

#generating the map
def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()
        
#go backward from the goal. Following the parent node to construct the path.
def reconstruct_path(parent_node, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = parent_node[current]
        path.append(current)
    return path

#Finally the main searching algorithm!

#What separates A* from Dijkstra is the heuristic function
#it calculates not only the cost so far but also the 'expected' cost to the goal point

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    openlist = PriorityQueue()
    openlist.add(start, 0)
    parent_node = {}
    cost_so_far = {}
    parent_node[start] = None
    cost_so_far[start] = 0
    
    while not openlist.empty():
        current = openlist.pop()
        
        if current == goal:
            break
            
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if new_cost < cost_so_far.get(next, float('inf')):
                cost_so_far[next] = new_cost
                #F = G + H
                priority = new_cost + heuristic(next, goal)
                openlist.add(next, priority)
                parent_node[next] = current
                
    return parent_node, cost_so_far

#setting up gamemap

#example 1

gamemap = WeightedGrid(10, 10)

gamemap.mountains = [(2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

gamemap.weights = {tree: 2 for tree in [(5,1),(5,2),(5,3),(5,4),(5,5),
                                        (5,6),(5,7),(5,8),(7,2),(7,3),
                                        (7,4),(7,5),(7,6),(7,7)]}

#main
parent_node, cost_so_far = a_star_search(gamemap, (0, 4), (9, 4))

#draw
draw_grid(gamemap, width=3, point_to=parent_node, start=(0, 4), goal=(9, 4))
print()
draw_grid(gamemap, width=3, number=cost_so_far, start=(0, 4), goal=(9, 4))
print()
draw_grid(gamemap, width=3, path=reconstruct_path(parent_node, start=(0, 4), goal=(9, 4)))

#example 2

gamemap = WeightedGrid(10, 10)

gamemap.mountains = [(5, 6), (6, 7), (7, 4), (8, 5)]

gamemap.weights = {tree: 2 for tree in [(6,5),(6,6),(7,6),(9,5),(9,6),
                                        (9,7)]}

#main
parent_node, cost_so_far = a_star_search(gamemap, (5, 7), (9, 4))

#draw
draw_grid(gamemap, width=3, point_to=parent_node, start=(5, 7), goal=(9, 4))
print()
draw_grid(gamemap, width=3, number=cost_so_far, start=(5, 7), goal=(9, 4))
print()
draw_grid(gamemap, width=3, path=reconstruct_path(parent_node, start=(5, 7), goal=(9, 4)))

#example 3

gamemap = WeightedGrid(10, 10)

gamemap.mountains = [(8, 0), (8, 1), (8, 2), (8, 4),(9, 5)]

gamemap.weights = {tree: 2 for tree in [(8,3)]}

#main
parent_node, cost_so_far = a_star_search(gamemap, (5, 7), (9, 4))

#draw
draw_grid(gamemap, width=3, point_to=parent_node, start=(5, 7), goal=(9, 4))
print()
draw_grid(gamemap, width=3, number=cost_so_far, start=(5, 7), goal=(9, 4))
print()
draw_grid(gamemap, width=3, path=reconstruct_path(parent_node, start=(5, 7), goal=(9, 4)))
