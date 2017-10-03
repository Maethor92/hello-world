from urllib2 import urlopen
import matplotlib.pyplot as plt
import numpy as np


output = urllib.urlopen('http://130.239.81.188:5000/app/api/v1.0/compute').read()

# https://stackoverflow.com/questions/16892072/bar-chart-in-pylab-from-a-dictionary

d = ast.literal_eval(output)
X = np.arange(len(d))

figure(0)
plt.bar(X, d.values(), align='center')
plt.xticks(X, d.keys())
plt.show()
