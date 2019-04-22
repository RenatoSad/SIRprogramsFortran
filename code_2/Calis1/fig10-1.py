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

with open('Infecp.dat','r') as f:
  Inf1=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          Inf1.append(line)
Inf1 = np.array(Inf1)
Tnf = Inf1[:,0]/365

with open('SIRCla.dat','r') as f:
  f13 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f13.append(line)
	      
f13 = np.array(f13)
T13 = f13[:,0]/365

with open('SIRExp.dat','r') as f:
  f14 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f14.append(line)
	      
f14 = np.array(f14)
T14 = f14[:,0]/365

plt.rcParams['axes.linewidth'] = 3.5 
plt.rcParams['xtick.major.width'] = 3.5
plt.rcParams['ytick.major.width'] = 3.5
plt.rcParams['xtick.major.size'] = 15
plt.rcParams['ytick.major.size'] = 15


rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.51, 0.01, r'$Time \ (year)$', ha='center',fontsize=(30))
fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))
    
plt.subplot(111)
plt.plot(Tnf,Inf1[:,2],'green',label=r'$Polynomial$',linewidth=1.5)
plt.plot(T14,f14[:,2],'orange',label=r'$Exponential$', linewidth=1.5)
plt.plot(T13,f13[:,2],'navy',label=r'$Classic$', linewidth=1.5)

plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(.99, 1.15), shadow = True, loc='upper left', ncol=1,fontsize=(16))

#plt.suptitle(r'$\beta=\frac{2.5}{15}\cos\bigg(\frac{\pi}{365}  t \bigg)$, $\kappa_1=1/15$, $\kappa_2=1/(0.8*365)$' %(data[0]),fontsize=(30))
    
figure_name = './figure.jpg'	# name of the figure to be saved
plt.savefig(figure_name)
plt.show()