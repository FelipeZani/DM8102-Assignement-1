import random as rd 
import math
import heapq

def dfs_connected_components(adj, n):
    size = len(adj.keys())
    visited = [False] * (size+1) 
    all_components = []
    print(visited)
    for current_node in range(n, size):
        if visited[current_node]:
            break
        # Start a fresh DFS for a new component
        component = []
        stack = [current_node]

        while stack:
            node = stack.pop()
            if visited[node]:
                break

            visited[node] = True
            component.append(node)
            
            if node not in adj:
                break
            
            for neighbor in list(adj[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)
        heapq.heappush_max(all_components,(len(component),component))
        heapq.heapify_max(all_components)
    
    if(len(all_components) == 1):
        heapq.heappush_max(all_components,(0,[]))
    return all_components

def get_first_False_index(marked):

    for i in range(len(marked)):
        if marked[i] == False:
            return i
    return -1

def dfs(adj,initial_node):
    n = len(adj)
    print(adj)
    visited = [False] * n
    print(visited)
    cc = []
    # Start DFS from node 0.
    st = []
    st.append(initial_node)
    #extracts a connected component 
    last_true_index = 0

    while st:
        res = []

        node = st.pop()

        # If node is already visited, continue
        if visited[node] == True:
            continue

        # Mark this node as visited 
        visited[node] = True
        last_true_index+=1
        res.append(node)

        # Traverse all edges (as stack is used, so 
        # push from right to left)
        size = len(adj[node])
        for i in range(size - 1, -1, -1):
            v = list(adj[node])[i]
            if not visited[v]:
                st.append(v)
        heapq.heappush_max(cc,(len(res),res))
        heapq.heapify_max(cc)
        node_to_add = get_first_False_index(visited)
        if(node_to_add != -1):
            st.append(node_to_add)

    return cc                

def draw_skip_distance(p):
    if(p == 0):
        return -1
    if(p == 1):
        return 0
    
    u = rd.random()
    jump_val = math.ceil((math.log(1-u))/math.log(1-p))
    return jump_val
    
def generate_GNP_graph(n, p) :
    E = {i+1 : set() for i in range(n)}
    
    k = -1
    total_possible_edges = int(n * (n - 1)//2)
    # The bellow code is slower than the uncommented code
    # while True:
    #
    #     l = draw_skip_distance(p)
    #     if (l == float("inf")):
    #         return E;
    #     k = k+l+1
    #     if k < total_possible_edges:
    #         i = math.floor((1+math.sqrt(1+8*k))*0.5) #Solving i for the triangular matrix
    #         j = k - int(i*(i-1)*0.5) 
    #         E[i+1].add(j+1)
    #         E[j+1].add(i+1)
    #     else:
    #         return E

    i = 1             # Current row index
    row_boundary = 0  # Total edges in rows BEFORE row i

    while True:
        l = draw_skip_distance(p)
        k = k + l + 1
        if k >= total_possible_edges or k==-1:
            return E
        
        #Increment i whenever k exceeds the current row
        # A row 'i' has exactly 'i' edges (0, 1, ..., i-1)
        while k >= row_boundary + i:
            row_boundary += i
            i += 1

        j = k - row_boundary
        v_i,v_j = i+1,j+1 
        E[v_i].add(v_j)
        E[v_j].add(v_i)
sample = generate_GNP_graph(5,0.5)
print(sample)
print(dfs_connected_components(sample,1))
# print(dfs(sample,list(sample.keys())[0]))
