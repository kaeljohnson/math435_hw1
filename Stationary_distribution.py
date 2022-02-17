import numpy as np

def findDistribution(A):
    # add stationary vector
    
    stationary = np.ones(len(A[0])+1)
    zeros = np.zeros(len(A))

    # extract 1 from each probablity in transition matrix
    identity = np.identity(len(A)
    
    A = A - I

    A = np.append(A, zeros, axis=1)

    A = np.append(A,[stationary],axis= 0)
    
        
    
    
    
