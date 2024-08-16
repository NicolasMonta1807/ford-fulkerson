from graph import Graph
import sys

def read_graph(filename):
  g = []
  try:
    with open(filename, "r") as f:  
      lines = f.readlines()
      for line in lines:
        row = list(map(int, line.strip().split(",")))
        if len(row) != len(lines):
          print("Invalid graph file. Not a square matrix.")
          sys.exit(1)
        g.append(row)
    return g
  except FileNotFoundError:
    print("File not found.")
    sys.exit(1)
  
def print_result(result):
  print("\nMax flow: ", result[0])
  print("Paths:")
  for path in result[1]:
    print(" -> ".join(map(str, [x + 1 for x in path[0]])), f"Flow: {path[1]}")
  print("\n")

def main():
  if len(sys.argv) < 2:
    print("Usage: python main.py <graph_file> verbose")
    sys.exit(1)
  
  matrix = read_graph(sys.argv[1])
  
  graph = Graph(len(matrix))
  graph.matrix = matrix
  
  verbose = False
  
  if len(sys.argv) == 3:
    if sys.argv[2] == "verbose":
      verbose = True
      graph.print_matrix()
    else :
      print("Invalid argument. Use 'verbose' to print intermediate steps.")
      sys.exit(1)
  
  print("Running Ford Fulkerson algorithm...")
  result = graph.ford_fulkerson(0, len(matrix) - 1, verbose)
  
  print_result(result)

if __name__ == "__main__":
  main()
