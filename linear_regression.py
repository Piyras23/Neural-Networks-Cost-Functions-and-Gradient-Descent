import numpy as np
from matplotlib import pyplot
import math
from mpl_toolkit.mplot3d import axes3d


# Load the data
data = np.loadtxt('linear_regression.txt', delimiter = ',')
#separate predictor from target variable
X = np.c_([np.ones(data.shape[0]), data[:,0])
y = np.c_[data[:,1]]


# First appraoch - Normal equation

def normalEquation(#necessary parameters goes here):
    """
    Parameteres: input variables (Table) , Target vector
    Instructions: Complete the code to compute the closed form solution to linear regression and 	save the result in theta.
    Return: coefficinets 
    """
    ## Your codes go here 
  
    return theta


# Iterative Approach - Gradient Descent 

'''
Following paramteres need to be set by you - you may need to run your code multiple times to find the best combination 
'''


def gradient_descent():
    """
    Paramters: input variable , Target variable, theta, number of iteration, learning_rate
    Instructions: Complete the code to compute the iterative solution to linear regression, in each iteration you will 
    add the cost of the iteration to a an empty list name cost_hisotry and update the theta.
    Return: theta, cost_history 
    """
    cost_hisotry = []
    # Your code goes here 
        
    return  theta, cost_hisotry



# Plot the cost over number of iterations
'''
#Your plot should be similar to the provided plot
'''




# Plot the linear regression line for both gradient approach and normal equation in same plot
'''
hints: your x-axis will be your predictor variable and y-axis will be your target variable. plot a
scatter plot and draw the regression line using the theta calculated from both approaches. Your plot
should be similar to what provided.
'''



# Plot contour plot and 3d plot for the gradient descent approach

'''
your plots should be similar to our plots.

'''





