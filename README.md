# A-Star-Pathfinding
An efficient A* (A-Star) pathfinding algorithm implemented in Python.

A* algorithm is like an ‘upgrade’ of Dijkstra’s algorithm. It calculates not only the cost on the route, but also the “heuristic”, the expected cost to the goal.

Among all the path-finding algorithms, A* is one of the fastest. It’s usually faster than Dijkstra, and better than greedy. It always returns the optimal results.

It searches a way smaller area than Dijkstra does, when the location of the goal is known. However, when the location of the goal is unknown, we should still use Dijkstra to do the “blind search”.

There are three examples with pictures. The code was attached and included in the package.

Implementation example:

