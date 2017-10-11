# Linear Algebra Take Home Quiz #3
# Author: Rocco Haro
# University of Alaska, Anchorage
# Oct '17'
# https://github.com/rocco-haro/Linear-Difference-Eq..git

import numpy as np

class StateMtx(object):
    """ Calculates the k+1 values for a linear difference equation
    """
    def __init__(self, *args):
        self.args = args
        # Converts input arr to matrix, which returns a N by 1 matrix.
        # So I take the transpose of this returned matrix to make it a valid
        # matrix for multiplication against the stateMtx
        self.initParameters = np.mat(self.args[0]).T

        # just hard codoing the matrix vals
        prep = [[0.97, 0.05, 0.10], [0.00, 0.90, 0.05], [0.03, 0.05, 0.85]]
        self.stateMtx = np.mat(prep) # converts array to matrix

    def printClass(self):
        print("Initial Parameters: ")
        print(self.initParameters)
        print("\nState Matrix: ")
        print(self.stateMtx)
        print("\n")

    def getNextK(self, currK):
        return self.stateMtx*currK

    def getKthValueAt(self, targetDay):
        currK = self.initParameters
        for x in range(targetDay):
            nextK = self.getNextK(currK)
            currK = nextK
        return currK

if __name__ == "__main__":
    k0 = [295, 55, 150 ]
    m = StateMtx(k0)
    m.printClass()
    res = m.getKthValueAt(30)
    print(res)
