import numpy as np


def fixedPointDistribution(T):


    '''
    We want to solve with fixed point iteration.

    x_* = Ax

    '''
    error = 10e-12
    maxIteration = 300
    n = len(T[0])
    dist = np.ones(n)/n

    for i in range(maxIteration):
        dist_prev = dist
        dist = np.dot(dist, T)

        acc = np.sum(np.abs(dist-dist_prev))/n 

        if acc < error: break
        

    normalized = dist/sum(dist)

    return normalized

def findDistributionMatrixEigenvalues(A):


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

    print(sum(stationary_distribution))
    
    
    return stationary_distribution


if __name__ == "__main__":
    file = open("damped_transition_matrix.csv")
    A = np.loadtxt(file, delimiter=",")

    ranks = fixedPointDistribution(A)
    np.savetxt("rankings.csv", ranks, delimiter=",")
