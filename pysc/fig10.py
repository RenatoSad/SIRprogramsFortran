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

with open('Infec.dat','r') as f:
  Inf1=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          Inf1.append(line)
Inf1 = np.array(Inf1)

plt.rcParams['axes.linewidth'] = 3.5 
plt.rcParams['xtick.major.width'] = 3.5
plt.rcParams['ytick.major.width'] = 3.5
plt.rcParams['xtick.major.size'] = 15
plt.rcParams['ytick.major.size'] = 15


rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.51, 0.01, r'$time \ (days)$', ha='center',fontsize=(30))
fig.text(0.04, 0.51, r'$I$', ha='center',fontsize=(30))
    
plt.subplot(111)
plt.plot(Inf1[:,0],Inf1[:,2],'green',label=r'$ConsPoly$',linewidth=3.0)

plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(.99, 1.15), shadow = True, loc='upper left', ncol=1,fontsize=(16))

plt.suptitle(r'$\beta=\frac{2.5}{15}\cos\bigg(\frac{\pi}{365}  t \bigg)$, $\kappa_1=1/15$, $\kappa_2=1/(0.8*365)$' %(data[0]),fontsize=(30))
    
figure_name = './figure.jpg'	# name of the figure to be saved
plt.savefig(figure_name)
plt.show()