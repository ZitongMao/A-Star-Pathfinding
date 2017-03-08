# A-Star-Pathfinding
An efficient A* (A-Star) pathfinding algorithm implemented in Python.

A* algorithm is like an ‘upgrade’ of Dijkstra’s algorithm. It calculates not only the cost on the route, but also the “heuristic”, the expected cost to the goal.

Among all the path-finding algorithms, A* is one of the fastest. It’s usually faster than Dijkstra, and better than greedy. It always returns the optimal results.

It searches a way smaller area than Dijkstra does, when the location of the goal is known. However, when the location of the goal is unknown, we should still use Dijkstra to do the “blind search”.

There are three examples with pictures. The code was attached and included in the package.

Implementation example:

```python


#setting up gamemap

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

```
