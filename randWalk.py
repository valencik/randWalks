import numpy as np
import matplotlib.pyplot as plt


def saveFigure(name):
    print("Saving pdf of " + name + "...")
    plt.savefig(name + '.np' + str(nPaths) + '.ns' + str(nSteps) + '.pdf',
                bbox_inches='tight')
#  print("Saving " +name +" png")
#  plt.savefig(name+'.png', bbox_inches='tight')

# Parameters
nPaths = 400
nSteps = 400
figureWidth = 24

# Set x to evenly-spaced values from 0 to nSteps
x = np.linspace(0, nSteps, nSteps)

# Generate matrix of -1's and 1's, then take their cumulative sum
y = 2 * np.floor(2 * (np.random.random((nPaths, nSteps)))) - 1
y = np.cumsum(y, axis=1)

# Calculate the average distance from zero
avg = np.mean(np.absolute(y), axis=0)
ysqrt = np.sqrt(2 * x / np.pi)

# Initial figure
fig, ax = plt.subplots(figsize=(figureWidth, figureWidth/2))

# Plot!
ax.plot(x, y.transpose(), color='blue', lw=0, alpha=0.0)
ax.plot(x, y[1].transpose(), color='blue', lw=3, alpha=1)
saveFigure("rWalkSingle")
ax.cla()

ax.plot(x, y[1].transpose(), color='blue', lw=3, alpha=1)
ax.plot(x, y.transpose(), color='blue', lw=1, alpha=0.1)
saveFigure("rWalkAll")

avgPlot = plt.plot(x, avg, color='red', lw=2, alpha=1)
saveFigure("rWalkAvg")

sqrtPlot = plt.plot(x, ysqrt, color='green', lw=2, alpha=1)
saveFigure("rWalkAvgSqrt")
