def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
            if neighbor not in visited:
                 dfs(graph, neighbor, visited)


from collections import deque

def bfs(graph, start):
     visited= set()
     queue = deque([start])
     visited.add(start)

     while queue:
          vertex = queue.popleft()
          print(vertex, end=' ')
          for neighbor in graph[vertex]:
               if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS (recursive):")
dfs(graph, 'A')

print("\n BFS:")
bfs(graph, 'A')


