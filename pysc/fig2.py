import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib import rc


with open('fort.11','r') as f:
  f10 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f10.append(line)
	      
f10 = np.array(f10)

plt.rcParams['axes.linewidth'] = 3.5 
plt.rcParams['xtick.major.width'] = 3.5
plt.rcParams['ytick.major.width'] = 3.5
plt.rcParams['xtick.major.size'] = 15
plt.rcParams['ytick.major.size'] = 15
#pgf_with_rc_fonts = {"font.family":"serif"}
#plt.rcParams.update(pgf_with_rc_fonts)

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True, figsize=(10, 10))
fig.text(0.45, 0.03, r'$\tau_{\mathrm{k}}$', ha='center',fontsize=(40))
#fig.text(0.01, 0.55, r'$\varrho_{ii}$', va='center', rotation='vertical',fontsize=(35))


plt.subplot(111)
plt.plot(f10[:,0],f10[:,1],'navy',marker='o',markevery=200,markersize=10,label=r'$S(\tau)$', linewidth=2.5)
plt.plot(f10[:,0],f10[:,2],'orange',marker='o',markevery=200,markersize=10,label=r'$I(\tau)$', linewidth=2.5)
plt.plot(f10[:,0],f10[:,3],'red',marker='o',markevery=200,markersize=10,label=r'$R(\tau)$', linewidth=2.5)
plt.plot(f10[:,0],f10[:,4],'green',marker='o',markevery=200,markersize=10,label=r'$N(\tau)$', linewidth=2.5)

#plt.xlim(xmax = 1, xmin = 0)
#plt.yticks(np.arange(-200.0, -800-1, -200))
plt.ylabel('Modelo 2',fontsize=(40))
plt.tick_params(labelsize='40',labeltop='off',labelright='off', labelbottom='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(1.015, 1.05), shadow = True, loc='upper left', ncol=1,fontsize=(21))
#xlabels = ['0',r'$\pi$',r'$2\pi$',r'$ 3 \pi $',r'$ 4\pi$']
#x=[0,3.14,2*3.14,3*3.14,4*3.14]
plt.ylim(ymax = 10.1, ymin = -0.1)
#plt.xticks(x,xlabels)
#plt.title('Kicks to A and C',fontsize=(30))
letter = 'b)'	# letter that identifies the figure (for no letter write '')
letter_color = 'black'	# color of the letter that identifies the figure
#plt.text(1, 0.024, letter,fontsize=35, color=letter_color)


figure_name = './figure.jpg'	# name of the figure to be saved

plt.savefig(figure_name)
plt.show()


