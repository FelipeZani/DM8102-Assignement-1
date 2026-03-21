import random as rd 
import math

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
        if k >= total_possible_edges:
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
generate_GNP_graph(15000,0.5)
