import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

data = np.genfromtxt('inet.csv', delimiter=',', skip_header=1,skip_footer=0, names=['x', 'y'])

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Test data")    
ax1.set_xlabel('time')
ax1.set_ylabel('internet Usage per minute')
ax1.scatter(data['x'],data['y'], c='r', label='The dataset')

intercept = 41.1741378707
slope = 1.5838905446
abline_values = [slope * i + intercept for i in data['x']]

ax1.plot(data['x'], abline_values, 'b', linewidth=2.0)
leg = ax1.legend()
#fig1 = plt.gcf()
#fig1.savefig('graph.png', bbox_inches='tight')
plt.show()
plt.draw()

