# from collections import deque

# def topological_sort(n,adj,visited,stack):
#     visited[n]=True
#     # print('-->>',n)
#     for e in adj[n]:
#         x = int(e)
#         if x > 0 and visited[x] is False:
#             topological_sort(x,adj,visited,stack)
#     stack.append(n)
        



# if __name__ == "__main__":
#     n = int(input())
#     adj=[0]
#     for _ in range(1,n+1):
#         s = input().split(" ")
#         adj.append(s)
#     time = input().split(" ")
#     time.insert(0,-1)
   
#     visited = [False]*(n+1)
#     stack = deque() 
   
#     topological_sort(1,adj,visited,stack)
   
#     # print(stack)
#     arr=[0 for _ in range(n+1)]
#     while len(stack)>0:
#         v=stack.pop()
#         # print(v)
#         arr[v]+= int(time[v])
#         for e in adj[v]:
#             edge = int(e)   
#             if edge is not -1: 
#                 if arr[edge]<arr[v]:
#                     arr[edge]+=arr[v]
#                 # print('---',v,arr[v],edge,arr[edge])
            
#     for i in range(1,n+1):
#         print(arr[i])





##################################################################################
i=1
def deleteNode(v,adj,in_deg,top_order):
    # print(v,adj,in_deg,top_order)
    
    global i
    top_order[v]=i
    i+=1

    for w in adj[v]:
        if w is not -1:
            in_deg[w]-=1
    

    for w in adj[v]:
        if w is not -1:
            
            if in_deg[w]==0:
                
                in_deg[w]=None
                deleteNode(w,adj,in_deg,top_order)



def fastTopological(adj,top_order):
    n = len(adj)
    in_deg=[0]*n
    
    for v in adj:
        for edge in v:
            if edge is not -1:
                in_deg[edge]+=1
    
    
    queue=[]
    for vertex,val in enumerate(in_deg):
        if val==0:
            queue.append(vertex)
            in_deg[vertex]=None
    
    while len(queue) > 0:
        u=queue.pop(0)
        
        deleteNode(u,adj,in_deg,top_order)

    



if __name__ == "__main__":
    n = int(input())
    adj=[[0]]
    for _ in range(1,n+1):
        s = input().split(" ")
        edges=[]
        for e in s:
            edges.append(int(e))
        adj.append(edges)
    times = input().split(" ")
    time=[]
    for t in times:
        time.append(int(t))
    time.insert(0, -1)

    # print(time)
    # print(adj)
    
    top_order=[None]*(n+1)

    fastTopological(adj,top_order)

    arr=[0 for _ in range(n+1)]

    # print(top_order)

    for i in range(1,n+1):
        u = top_order[i]
        # print(i,u)
        arr[u]+=time[u]
        for edge in adj[u]:
            if edge is not -1:
                t1 = arr[edge]+arr[u]
                t2 = arr[edge]
                if t1>t2:
                    arr[edge]=t1
    
    
    for i in range(1, n+1):
        print(arr[i])    
   