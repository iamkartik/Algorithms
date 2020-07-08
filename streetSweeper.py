def dfs(graph, explored,parents,u,visited):
    explored[u]=1
    # print(u,graph[u])
    for v in graph[u]:
        if (u,v) not in visited:
            print('Truck going on',(u,v))
            visited.add((u,v))
            parents[v]=u
            dfs(graph,explored, parents,v,visited)
            


if __name__ == "__main__":
    graph = [[1,3],[0,4,2],[1,3],[0,2,5],[1],[3]]
    visited = set()
    explored=[0]*6
    parents = [None]*6
    # dfs(graph, visited_v,0)
    dfs(graph,explored,parents,0,visited)
    print(visited)
    print(parents)

        
