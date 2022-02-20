import numpy as np

def findDistribution(A):

    '''
            Stationary Distribution

                   pi = piP

                  pi - piP = 0

                 pi(I - P) = 0

               (I - P).T (pi.T) = 0

    pi describes a probability distribution so:

                 sum(pi_i) = 1

    Which makes this an overdetermined system
    since we need another equation to satisfy
    that condition.

                                            '''

    '''add stationary vector'''
    A = np.transpose(A)
    stationary = np.ones(len(A[0])+1)
    zeros = np.zeros(len(A)).reshape(-1,1)

    '''

    extract 1 from each probablity in transition matrix

                                                    '''

    identity = np.identity(len(A))
    A = A - identity
    A = np.append(A, zeros, axis=1)
    A = np.append(A,[stationary],axis= 0)
    b = A[:, -1].reshape(-1,1)
    A = A[:, :-1]

    

    '''

    Solve Ax = b
    Need QR decomp to solve overdetermined matrix
    QRx = b
        
                                                    '''

    stationary_distribution = np.linalg.lstsq(A, b, rcond=None)[0]
    
    
    return stationary_distribution



file = open("transition_matrix.csv")
A = np. loadtxt(file, delimiter=",")

    
print(findDistribution(A))
