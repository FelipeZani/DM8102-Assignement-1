
import random 



def sampling_without_replacement(S, k , seed ):
    
    random.seed(seed)

    """
    Universe S = all nodes of the grid graph G(n,m)
    Returns k randomly selected distinct nodes.
    """
    R = []
    while len(R) < k:
        x = random.randint(0, len(S)-1) #indeces
    
        if x not in R:
            R.append(x)
    
    result  = [S[i] for i in R]
    return result

def main(): 
    # Example universe S : list of grid nodes
    S = [ (i,j)for i in range(3) for j in range(4)] # G(3,4)
    k = 5 
    result = sampling_without_replacement(S,k,10)
    print("Sampled nodes:",result)

if __name__ == "__main__":
    main()