def dfs(graph, explored,parents,u,visited,path,edges):
    explored[u]=0
    # print(u)
    for v in graph[u]:
        if explored[v]==1:
            parents[v]=u
            path.append((u,v))
            edges.remove((u,v))
            dfs(graph, explored,parents,v,visited,path,edges)
    
    for v in graph[u]:
        if parents[u] is not  v:
            # print('here',(u,v),(v,u))
            if (u,v) in edges:
                print((u,v))
                path.append((u,v))
                edges.remove((u,v))
            if (v,u) in edges:
                # print((v,u))
                path.append((v,u))
                edges.remove((v,u))

    if sum(explored)==0:
        x = parents[u]
        if (u,x) in edges:
            path.append((u,x))
            edges.remove((u,x))
        
            


if __name__ == "__main__":
    graph = [[1,4],[0,2,3],[1,6],[1,4,6],[0,3,5],[4],[2,3]]
    visited = set()
    explored=[1]*7
    parents = [None]*7
    # dfs(graph, visited_v,0)
    edges = set()
    path=[]
    temp = set()
    for i,u in enumerate(graph):
        for v in u:
            edges.add((i,v))
            edges.add((v,i))
            # if (i,v) not in edges:
            #     edges.append((i,v))
            # if (v,i) not in edges:
            #     edges.append((v,i))
            
    print(edges)
    dfs(graph,explored,parents,0,visited,path,edges)
    print(path)
    
    
        
