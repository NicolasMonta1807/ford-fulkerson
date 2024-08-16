class Graph:
  """Class to represent a graph using adjacency matrix.
  
  Attributes:
    vertices (int): Number of vertices in the graph.
    matrix (list): Adjacency matrix representation of the graph.
  """
  
  def __init__(self, vertices):
    self.vertices = vertices
    self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
  
  def print_matrix(self):
    """Prints the matrix representation of the graph.
    """
    
    for row in self.matrix:
      print(" ".join(map(str, row)))
    print("\n")
    
  def dfs(self, s, t, parent):
    """ Depth First Search to find a path from source to sink.

    Parameters:
        s (int): index of the source vertex.
        t (int): index of the sink vertex.
        parent (int): index of the parent vertex.

    Returns:
        boolean: whether a path from source to sink exists.
    """
    
    
    visited = [False] * self.vertices
    stack = [s]
    visited[s] = True
    
    while stack:
      u = stack.pop()
      
      for i, val in enumerate(self.matrix[u]):
        if not visited[i] and val > 0:
          stack.append(i)
          visited[i] = True
          parent[i] = u
    
    return True if visited[t] else False
  
  def ford_fulkerson(self, source, sink, verbose = False):
    """Finds the maximum flow in the graph using Ford Fulkerson algorithm.

    Args:
        source (int): index of the source vertex.
        sink (int): index of the sink vertex.
        verbose (bool, optional): show matrix before and after each iteration. Defaults to False.

    Returns:
        list: paths and their flow values.
    """
    
    # Initialize parent array to store path
    parent = [-1] * self.vertices
    max_flow = 0
    final_paths = []
    it = 1
    
    # While there is a path from source to sink
    while self.dfs(source, sink, parent):
      path_flow = float("Inf")
      s = sink
      path = []
      
      # Find the minimum flow in the path by backtracking
      while s != source:
        path.append(s)
        path_flow = min(path_flow, self.matrix[parent[s]][s])
        s = parent[s]
      
      # Add source to the path
      path.append(source)
      path = path[::-1]
      final_paths.append((path, path_flow))
      
      # Add path flow to max flow
      max_flow += path_flow
      v = sink
      
      # Print path,flow and matrix transformation
      if verbose:
        print(f"It {it}:")
        print(f"Found path: {' - '.join(map(str, path))}")
        print(f"Path flow: {path_flow}")
        
        print(f"Matrix before using path: ")
        self.print_matrix()
      
      # Update the residual capacities of the edges and reverse edges
      while v != source:
        u = parent[v]
        self.matrix[u][v] -= path_flow
        self.matrix[v][u] += path_flow
        v = parent[v]
    
      if verbose:
        print("Matrix after using path:")
        self.print_matrix()
      
      it += 1
    
    # Return max flow and paths 
    return [max_flow, final_paths]
