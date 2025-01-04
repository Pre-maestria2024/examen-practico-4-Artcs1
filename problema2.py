from queue import PriorityQueue
from queue import Queue

def bfs(source):

    queue = Queue(maxsize = 100005)
    queue.put(source)
    vis[source] = 1

    while not queue.empty():
        u = queue.get()
        for v in adj[u]:
            if vis[v] == 0:
                vis[v]   = 1
                level[v] = level[u]+1
                queue.put(v)
                parent[v] = u

def main():

    n, k = map(int, input().split())

    global adj
    adj = [[] for i in range(n)]
    global level
    level  = [0 for i in range(n)]
    global degree
    degree = [0 for i in range(n)]
    global vis
    vis = [0 for i in range(n)]
    global parent
    parent = [-1 for i in range(n)]

    for i in range(n-1):
        u,v = map(int,input().split())
        degree[u]+=1
        degree[v]+=1
        adj[u].append(v)
        adj[v].append(u)

    bfs(0)
    nodes = PriorityQueue()

    for i in range(1,n):
        if degree[i] == 1:
            nodes.put((-level[i],i))

    vis = [False] * n
    cottages = 0

    while not nodes.empty():
    
        node = nodes.get()
        nivel, key = -node[0], node[1]
        
        if (nivel+1) >= k:
            
            flag = True
            for num in range(k):
                if vis[key] == False:
                    vis[key] = True
                else:
                    flag = False
                    break
                if num != k-1:
                    key = parent[key]

            if flag == True:
                cottages+=1
                nodes.put((-level[parent[key]], parent[key]))


    print(cottages)


        

if __name__  == '__main__':
    main()

