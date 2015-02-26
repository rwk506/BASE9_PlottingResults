### Built with Python 2.6
# The gridspec module in matplotlib is necessary and may have to be installed prior to use

### Import other packages
from matplotlib import *
import matplotlib.pylab as pylab
from pylab import *
from numpy import *
from scipy import *
import numpy as np
import matplotlib.gridspec as gs
from matplotlib.ticker import MaxNLocator

### Import BASE plotting functions
import plotresY
import plotres_multi


### Plotting singlePopMcmc results
print 'singlePopMcmc results:'
res_single=loadtxt('NGC1261.single.res',skiprows=1)             ## load file
plotresY.plotresY(res_single,startn=1000,color1='forestgreen',lw1=2)     ## plot results with function, customizing some default parameters
savefig('Singlepop.png')                                        ## save figure output to .png file
#plt.show()


### Plotting multiPopMcmc results
print ''
print 'multiPopMcmc results:'
res_multi=loadtxt('NGC1261.multi.res',skiprows=1)                                     ## load file
plotres_multi.plotres_multi(res_multi,startn=1000,priors=[10.08,-1.35,16.18,0.09,0.26,0.32,0.])     ## plot results, include prior lines
savefig('Multipop.png')                                                               ## save figure output to .png file
#plt.show()
