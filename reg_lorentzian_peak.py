import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, differential_evolution
import warnings

#Get the data
pts =  np.genfromtxt('inet.csv', delimiter = ',')

#Split the data into x and y
x_pts = np.array([pts[i,0] for i in xrange(len(pts))])
y_pts = np.array([pts[i,1] for i in xrange(len(pts))])

#Credits : @zunzun
#This is the good stuff

def double_Lorentz(x, a, b, A, w, x_0, A1, w1, x_01):
    return a*x+b+(2*A/np.pi)*(w/(4*(x-x_0)**2 + w**2))+(2*A1/np.pi)*(w1/(4*(x-x_01)**2 + w1**2))

def sumOfSquaredError(parameterTuple):
    warnings.filterwarnings("ignore") # do not print warnings by genetic algorithm
    return np.sum((y_pts - double_Lorentz(x_pts, *parameterTuple)) ** 2)

def generate_Initial_Parameters():
    #min and max used for bounds
    maxX = max(x_pts)
    minX = min(x_pts)
    maxY = max(y_pts)
    minY = min(y_pts)

    parameterBounds = []
    parameterBounds.append([-1.0, 1.0]) # parameter bounds for a
    parameterBounds.append([maxY/-2.0, maxY/2.0]) # parameter bounds for b
    parameterBounds.append([0.0, maxY*100.0]) # parameter bounds for A
    parameterBounds.append([0.0, maxY/2.0]) # parameter bounds for w
    parameterBounds.append([minX, maxX]) # parameter bounds for x_0
    parameterBounds.append([0.0, maxY*100.0]) # parameter bounds for A1
    parameterBounds.append([0.0, maxY/2.0]) # parameter bounds for w1
    parameterBounds.append([minX, maxX]) # parameter bounds for x_01

    # "seed" the numpy random number generator for repeatable results
    result = differential_evolution(sumOfSquaredError, parameterBounds, seed=3)
    return result.x

initial_params = generate_Initial_Parameters()
fitted_params, niepewnosci = curve_fit(double_Lorentz, x_pts, y_pts, initial_params)

a, b, A, w, x_0, A1, w1, x_01 = fitted_params
y_fit = double_Lorentz(x_pts, a, b, A, w, x_0, A1, w1, x_01)

plt.plot(y_pts, c='#42f4c2')
plt.plot(y_fit, c='#f49441')

fig1 = plt.gcf()
fig1.savefig('graph_2.png', bbox_inches='tight')
plt.show()
