from numpy import *
from time import time

def error_given_pts(c, m, points):
    '''
    It gives us a insight into whether
    gradient descent actually happened and also tells us the
    presicion of the line of best fit.
    The total error is computed by the mean-squared error
    method. Here we use the equation of a straight line
    y = mx + c
    '''
    total_error = 0
    for i in xrange(0,len(points)):
        x = points[i,0]
        y = points[i,1]
        total_error += (y - (m*x + c))**2
    return total_error / float(len(points))

def step_grad(c_cur, m_cur, learningRate, points):
    '''
    Most of this function can be understood from a mathematical
    background.These results come from partial differentiation.
    We differentiate the loss function with respect to c and m 
    seperately.
    '''
    c_grad = 0
    m_grad = 0
    N = float(len(points))
    for i in xrange(0,len(points)):
        x = points[i,0]
        y = points[i,1]
        c_grad += -(2/N) * (y - (m_cur*x + c_cur))
        m_grad += -(2/N) * x * (y - (m_cur*x + c_cur))
    #Here the learning rate becomes useful as it decides the convergence rate
    new_c = c_cur - (learningRate * c_grad)
    new_m  = m_cur - (learningRate * m_grad)
    return [new_c, new_m]

def grad_descent_run(pts,start_c, start_m, num_iterations, learning_rate):
    #Performs gradient descent over the given number of iterations to
    # get the line of best fit
    c = start_c
    m = start_m
    for i in xrange(num_iterations):
        c, m  = step_grad(c, m, learning_rate, pts)
    return [c, m]


def main_fun():
    #Let's import out dataset
    pts = genfromtxt('inet.csv', delimiter = ',')
    #First we define the Hyperparameters
    initial_c = 0
    initial_m = 0
    num_iter = 10000
    learning_rate = 0.0001
    print 'Beginning gradient decent initial c = {0}, initial m = {1} and the current error is: {2}'.format(initial_c, initial_m, error_given_pts(initial_c,initial_m,pts))
    print 'Running'
    start = time()
    [c, m] = grad_descent_run(pts,initial_c,initial_m, num_iter, learning_rate)
    end = time()
    print 'After performing gradient descent for {0} iterations we have c = {1}, m = {2} and error = {3}'.format(num_iter, c, m, error_given_pts(c, m, pts))
    print 'The time taken was:', end-start, 'Seconds'
if __name__ == '__main__':
    main_fun()
