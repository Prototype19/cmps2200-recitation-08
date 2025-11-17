from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """

    def helper(visited, frontier):
        if len(frontier) == 0:
            return visited
        else:
            node, distance, edge_num = heappop(frontier)
            print(f"Visting {node}, distance {distance}, number edge {edge_num}")
            if node in visited:
                return helper(visited, frontier)
            else:
                visited[node] = (distance, edge_num)
                for neighbor, weight in graph[node]:
                    heappush(frontier, (neighbor, distance + weight, edge_num + 1))
                return helper(visited, frontier)

    frontier = []
    heappush(frontier, (source, 0, 0))
    visited = dict()
    return helper(visited, frontier)
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """

    def bfs_serial_helper(visited, frontier, result):
        if len(frontier) == 0:
            return result  # Return result dictionary

        node = frontier.popleft()
        print(f'Visiting {node}, Dictionary: {result}')
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in frontier:
                frontier.append(neighbor)
                result[neighbor] = node  # Update result dictionary

        return bfs_serial_helper(visited, frontier, result)

    frontier = deque([source])
    visited = set()
    result = {}  # Creating result dictionary

    return bfs_serial_helper(visited, frontier, result)

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = [] # Create list which will be converted to string later
    curr_node = parents[destination] # Start at destination node
    while curr_node != 's':
        path.append(curr_node)
        curr_node = parents[curr_node]
    path.append('s')

    return "".join(map(str, reversed(path)))




