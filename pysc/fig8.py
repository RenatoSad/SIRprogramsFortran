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

with open('fort.13','r') as f:
  f13 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f13.append(line)
	      
f13 = np.array(f13)

with open('fort.14','r') as f:
  f14 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f14.append(line)
	      
f14 = np.array(f14)

with open('fort.15','r') as f:
  f15 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f15.append(line)
	      
f15 = np.array(f15)

with open('fort.16','r') as f:
  f16 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f16.append(line)
	      
f16 = np.array(f16)

plt.rcParams['axes.linewidth'] = 3.5 
plt.rcParams['xtick.major.width'] = 3.5
plt.rcParams['ytick.major.width'] = 3.5
plt.rcParams['xtick.major.size'] = 15
plt.rcParams['ytick.major.size'] = 15


rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.51, 0.01, r'$time \ (days)$', ha='center',fontsize=(30))
fig.text(0.04, 0.51, r'$N(t)$', ha='center',fontsize=(30))

###
#plt.subplot(131)

#plt.plot(f13[:,0],f13[:,2],'orange',label=r'$I(\tau)$', linewidth=2.5)
#plt.tick_params(labelsize='15',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
#plt.title("Planck",fontsize=15)

#plt.subplot(132)

#plt.plot(f14[:,0],f14[:,2],'orange',label=r'$I(\tau)$', linewidth=2.5)
#plt.tick_params(labelsize='15',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
#plt.title("Exponential",fontsize=15)

#plt.subplot(133)

#plt.plot(f15[:,0],f15[:,2],'orange',label=r'$I(\tau)$', linewidth=2.5)
#plt.tick_params(labelsize='15',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
#plt.title("Lineal",fontsize=15)
###

plt.subplot(111)
plt.plot(f13[:,0],f13[:,4],'navy',label=r'$Planck$', linewidth=2.5)
plt.plot(f14[:,0],f14[:,4],'orange',label=r'$Exponential$', linewidth=2.5)
plt.plot(f15[:,0],f15[:,4],'red',label=r'$Lineal$', linewidth=2.5)
plt.plot(f16[:,0],f16[:,4],'green',label=r'$Lineal2$', linewidth=2.5)

plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')

plt.legend(borderpad=0.1,bbox_to_anchor=(.99, 1.15), shadow = True, loc='upper left', ncol=1,fontsize=(16))


plt.suptitle(r'$\beta=$%d$\times 10^{-2}\cos(\omega_o  t )$, $\kappa_1=1/15$, $\kappa_2=1/365$ $\mu=0.0183$' %(data[0]),fontsize=(30))


figure_name = './figure.jpg'	# name of the figure to be saved

plt.savefig(figure_name)
plt.show()