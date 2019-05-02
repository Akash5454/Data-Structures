def bfs(graph, node):
    visited = []
    queue = [node]
    while(len(queue)>0):
        node = queue.pop(0) 
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited        
          

            
            
        
        
        