import sys

from knapsack import knapsack

class dp(knapsack):
    def __init__(self, filename):
        knapsack.__init__(self, filename)
        
    def DP(self, solution):
        # Renaming things to keep track of them wrt. names used in algorithm
        v = self.item_values
        wv = self.item_weights
        n = self.Nitems
        W = self.Capacity
        
        # the dynamic programming function for the knapsack problem
        # the code was adapted from p17 of http://www.es.ele.tue.nl/education/5MC10/solutions/knapsack.pdf

        # v array holds the values / profits / benefits of the items
        # wv array holds the sizes / weights of the items
        # n is the total number of items
        # W is the constraint (the weight capacity of the knapsack)
        # solution: True in position n means pack item number n+1. False means do not pack it.
        
        # V and Keep should be 2d arrays for use in the dynamic programming solution
        # The are both of size (n + 1)*(W + 1)
        
        # Initialise V and keep
        # ADD CODE HERE
        # two dimensional array. All other values in the array we initialise with null or None
        V = [[None for _ in range((W + 1))] for j in range((n + 1))]
        keep = [[None for _ in range((W + 1))] for j in range((n + 1))]
        
        # Set the values of the zeroth row of the partial solutions table to False
        # ADD CODE HERE
        for w in range(0, W + 1):
            V[0][w] = 0
        
        # main dynamic programming loops, adding on item at a time and looping through weights from 0 to W
        # ADD CODE HERE
        for i in range(1, n + 1):
            for w in range(0, W + 1):
                if (wv[i] <= w) and ((v[i]+V[i-1][w-wv[i]]) > V[i-1][w]):
                    V[i][w] = v[i] + V[i-1][w-wv[i]]
                    keep[i][w] = 1
                else:
                    V[i][w] = V[i-1][w]
                    keep[i][w] = 0
        
        # now discover which iterms were in the optimal solution
        # ADD CODE HERE
        optimal_solution = []
        K = W
        for i in range(n, 0, -1):
            if keep[i][K] == 1:
                optimal_solution.append(i)
                K = K - wv[i]

        for index in optimal_solution:
            solution[index] = True
        
        
knapsk = dp(sys.argv[1])
solution = [False]*(knapsk.Nitems + 1)
knapsk.DP(solution)
knapsk.check_evaluate_and_print_sol(solution)
