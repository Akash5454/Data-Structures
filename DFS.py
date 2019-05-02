class Graph:
    def __init__(self,g):
        if g is None:
            g = {}
        self.g = g  
    def dfs(self, node, visited):
        if node not in visited:
            visited.append(node)
            for n in self.g[node]:
                self.dfs(n,visited)
        return visited