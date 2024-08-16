class Graph:
  def __init__(self, vertices):
    self.vertices = vertices
    self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
  
  def print_matrix(self):
    for row in self.matrix:
      print(" ".join(map(str, row)))
    print("\n")
    
  def dfs(self, s, t, parent):
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
    parent = [-1] * self.vertices
    max_flow = 0
    final_paths = []
    
    it = 1
    while self.dfs(source, sink, parent):
      path_flow = float("Inf")
      s = sink
      path = []
      
      while s != source:
        path.append(s)
        path_flow = min(path_flow, self.matrix[parent[s]][s])
        s = parent[s]
      
      path.append(source)
      path = path[::-1]
      final_paths.append((path, path_flow))
      
      if verbose:
        print(f"It {it}:")
        print(f"Found path: {' - '.join(map(str, path))}")
        print(f"Path flow: {path_flow}")
        
        print(f"Matrix before using path: ")
        self.print_matrix()
      
      max_flow += path_flow
      v = sink
      
      while v != source:
        u = parent[v]
        self.matrix[u][v] -= path_flow
        self.matrix[v][u] += path_flow
        v = parent[v]
      
      if verbose:
        print("Matrix after using path:")
        self.print_matrix()
      
      it += 1
      
    return [max_flow, final_paths]
