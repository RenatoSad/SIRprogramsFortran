import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib import rc

with open('par.dat','r') as g:
  data = [] 
  for line in g:
     data = line.split()
     if data:
	      data = [float(i) for i in data]
data = np.array(data)

with open('fortb20E.14','r') as f:
  f14 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f14.append(line)
	      
f14 = np.array(f14)

with open('fortb20L.15','r') as f:
  f15 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f15.append(line)
	      
f15 = np.array(f15)

plt.rcParams['axes.linewidth'] = 1.0 
plt.rcParams['xtick.major.width'] = 1.0
plt.rcParams['ytick.major.width'] = 1.0
plt.rcParams['xtick.major.size'] = 7
plt.rcParams['ytick.major.size'] = 7

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.51, 0.04, r'$time \ (days)$', ha='center',fontsize=(30))
#fig.text(0.04, 0.51, r'$I$', ha='center',fontsize=(30))


plt.subplot(311)
plt.plot(f14[:,0],f14[:,4],'black',label=r'$N$',linewidth=1.5)
plt.plot(f14[:,0],f14[:,1],'navy',label=r'$S(t)$',linewidth=1.5)

plt.tick_params(labelsize='12',labeltop='off',labelright='off', labelbottom='off', labelleft='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(1.0, 1.10), shadow = True, loc='upper left', ncol=1,fontsize=(20))
    
plt.subplot(312)
plt.plot(f14[:,0],f14[:,3],'green',label=r'$R(t)$',linewidth=1.5)

plt.tick_params(labelsize='12',labeltop='off',labelright='off', labelbottom='off', labelleft='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(1.0, 1.10), shadow = True, loc='upper left', ncol=1,fontsize=(20))
    
plt.subplot(313)
plt.plot(f14[:,0],f14[:,2],'red',label=r'$I(t)$',linewidth=1.5)

plt.tick_params(labelsize='12',labeltop='off',labelright='off',labelleft='on',labelbottom='on')

plt.legend(borderpad=0.1,bbox_to_anchor=(1.0, 1.10), shadow = True, loc='upper left', ncol=1,fontsize=(20))
    
figure_name = './figure.jpg'	# name of the figure to be saved
plt.savefig(figure_name)
plt.show()



















