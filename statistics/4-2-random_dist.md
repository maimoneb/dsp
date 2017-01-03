[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

"""Generate 1000 numbers from random.random and plot their PMF and CDF.
Is the distribution uniform?"""

import random
import numpy as np
import matplotlib.pyplot as plt
import yaml
from datetime import datetime
from scipy.interpolate import UnivariateSpline


def cdf(data):
    data_size=len(data)

    # Set bins edges
    data_set=sorted(set(data))
    bins=np.append(data_set, data_set[-1]+1)

    # Use the histogram function to bin the data
    counts, bin_edges = np.histogram(data, bins=bins, density=False)

    counts=counts.astype(float)/data_size

    # Find the cdf
    cdf = np.cumsum(counts)

    # Plot the cdf
    plt.plot(bin_edges[0:-1], cdf,linestyle='--', marker="o", color='b')
    plt.ylim((0,1))
    plt.ylabel("CDF")
    plt.grid(True)
   # plt.savefig('CDF.png')
    #plt.close()
    plt.show()

def PMF1(hist):
    plt.bar(range(len(hist)), hist.values(), align='center')
    plt.xticks(range(len(hist)), hist.keys())
    #plt.savefig('PMF.png')
    plt.show()

def PMF2(prob):
    p, x = np.histogram(prob, bins=100)  # bin it into n = N/10 bins
    x = x[:-1] + (x[1] - x[0]) / 2  # convert bin edges to centers
    f = UnivariateSpline(x, p, s=100)
    plt.plot(x, f(x))
    #plt.savefig('PMF_CenterEdge.png')
    plt.show()

prob = []
hist = {}
i=0
random.seed(datetime.now())
while i <= 1000:
    # Get random number in range 0 through 1 exclusive.
    p = random.random()
    p2 = "%0.2f" % p
    p2 = float(p2)
    if p2 not in hist:
        hist[p2] = 1
    else:
        hist[p2] += 1
    prob.append(p2)
    i += 1
cdf(prob)
PMF1(hist)
PMF2(prob)
