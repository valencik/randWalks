import jinja2
import json
import numpy as np
import matplotlib.pyplot as plt

import mpld3

# Parameters
N_paths = 400
N_steps = 400
figureWidth = 24

# 100 evenly-spaced values from 0 to 10
x = np.linspace(0, N_steps, N_steps)

# Generate matrix of -1's and 1's, then take their cumulative sum
y = 2* np.floor(2 * (np.random.random((N_paths, N_steps)) )) -1
y = np.cumsum(y, axis=1)

# Calculate the average distance from zero
avg = np.mean(np.absolute(y), axis=0)
ysqrt = np.sqrt(2*x/3.14159265)


# Plotting Jazz
fig, ax = plt.subplots(figsize=(figureWidth,figureWidth/2), dpi=80, subplot_kw={'xticks': [], 'yticks': []})
lines = ax.plot(x, y.transpose(), color='blue', lw=1, alpha=0.1)

plt.savefig('foo1.pdf')
avgPlot = plt.plot(x, avg, color='red', lw=2, alpha=1)
plt.savefig('foo2.pdf')
sqrtPlot = plt.plot(x, ysqrt, color='green', lw=2, alpha=1)
plt.savefig('foo3.pdf')

#mpld3.save_html(fig, "randomWalkBig.html")

