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

with open('fort.11','r') as f:
  f10 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f10.append(line)
	      
f10 = np.array(f10)

with open('fort.12','r') as f:
  f11 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f11.append(line)
	      
f11 = np.array(f11)

with open('fort.13','r') as f:
  f12 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f12.append(line)
	      
f12 = np.array(f12)

with open('fort.14','r') as f:
  f13 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f13.append(line)
	      
f13 = np.array(f13)

with open('fort.15','r') as f:
  f14 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f14.append(line)
	      
f14 = np.array(f14)


with open('fort.16','r') as f:
  f15 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f15.append(line)
	      
f15 = np.array(f15)




plt.rcParams['axes.linewidth'] = 3.5 
plt.rcParams['xtick.major.width'] = 3.5
plt.rcParams['ytick.major.width'] = 3.5
plt.rcParams['xtick.major.size'] = 15
plt.rcParams['ytick.major.size'] = 15
#pgf_with_rc_fonts = {"font.family":"serif"}
#plt.rcParams.update(pgf_with_rc_fonts)

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

fig, ax = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.47, 0.03, r'$\tau_{\mathrm{k}}$', ha='center',fontsize=(40))
#fig.text(0.01, 0.55, r'$\varrho_{ii}$', va='center', rotation='vertical',fontsize=(35))


plt.subplot(231)
plt.plot(f10[:,0],f10[:,1],'navy',marker='o',markevery=200,markersize=5,label=r'$S(\tau)$', linewidth=2.5)
plt.plot(f10[:,0],f10[:,2],'orange',marker='o',markevery=200,markersize=5,label=r'$I(\tau)$', linewidth=2.5)
plt.plot(f10[:,0],f10[:,3],'red',marker='o',markevery=200,markersize=5,label=r'$R(\tau)$', linewidth=2.5)
plt.plot(f10[:,0],f10[:,4],'green',marker='o',markevery=200,markersize=5,label=r'$N(\tau)$', linewidth=2.5)
plt.tick_params(labelsize='40',labeltop='off',labelright='off', labelbottom='off',labelleft='on')
#plt.legend(borderpad=0.1,bbox_to_anchor=(1.015, 1.05), shadow = True, loc='upper left', ncol=1,fontsize=(21))
#xlabels = ['0',r'$\pi$',r'$2\pi$',r'$ 3 \pi $',r'$ 4\pi$']
#x=[0,3.14,2*3.14,3*3.14,4*3.14]
#plt.xticks(x,xlabels)
#plt.ylabel('Modelo 4',fontsize=(40))
#plt.xlim(xmax = 5.01, xmin = 0)
plt.xticks(np.arange(0., 15 + 0.01, 5.))
plt.ylim(ymax = 10.1, ymin = -0.1)
plt.yticks(np.arange(0., 10 + 0.1, 5))
#plt.title('Kicks to A and C',fontsize=(30))
letter = '1)'	# letter that identifies the figure (for no letter write '')
letter_color = 'black'	# color of the letter that identifies the figure
plt.text(0.1, 8, letter,fontsize=35, color=letter_color)


plt.subplot(232)
plt.plot(f11[:,0],f11[:,1],'navy',marker='o',markevery=200,markersize=5,label=r'$S(\tau)$', linewidth=2.5)
plt.plot(f11[:,0],f11[:,2],'orange',marker='o',markevery=200,markersize=5,label=r'$I(\tau)$', linewidth=2.5)
plt.plot(f11[:,0],f11[:,3],'red',marker='o',markevery=200,markersize=5,label=r'$R(\tau)$', linewidth=2.5)
plt.plot(f11[:,0],f11[:,4],'green',marker='o',markevery=200,markersize=5,label=r'$N(\tau)$', linewidth=2.5)
plt.tick_params(labelsize='40',labeltop='off',labelright='off', labelbottom='off', labelleft='off')
#plt.legend(borderpad=0.1,bbox_to_anchor=(1.015, 1.05), shadow = True, loc='upper left', ncol=1,fontsize=(21))
#xlabels = ['0',r'$\pi$',r'$2\pi$',r'$ 3 \pi $',r'$ 4\pi$']
#x=[0,3.14,2*3.14,3*3.14,4*3.14]
#plt.xticks(x,xlabels)
#plt.ylabel('Modelo 4',fontsize=(40))
#plt.xlim(xmax = 5.01, xmin = 0)
plt.xticks(np.arange(0., 15 + 0.01, 5.))
plt.ylim(ymax = 10.1, ymin = -0.1)
plt.yticks(np.arange(0., 10 + 0.1, 5))
#plt.title('Kicks to A and C',fontsize=(30))
letter = '2)'	# letter that identifies the figure (for no letter write '')
letter_color = 'black'	# color of the letter that identifies the figure
plt.text(0.1, 8, letter,fontsize=35, color=letter_color)


plt.subplot(233)
plt.plot(f12[:,0],f12[:,1],'navy',marker='o',markevery=200,markersize=5,label=r'$S(\tau)$', linewidth=2.5)
plt.plot(f12[:,0],f12[:,2],'orange',marker='o',markevery=200,markersize=5,label=r'$I(\tau)$', linewidth=2.5)
plt.plot(f12[:,0],f12[:,3],'red',marker='o',markevery=200,markersize=5,label=r'$R(\tau)$', linewidth=2.5)
plt.plot(f12[:,0],f12[:,4],'green',marker='o',markevery=200,markersize=5,label=r'$N(\tau)$', linewidth=2.5)
plt.tick_params(labelsize='40',labeltop='off',labelright='off', labelbottom='off', labelleft='off')
plt.legend(borderpad=0.1,bbox_to_anchor=(1.015, 1.05), shadow = True, loc='upper left', ncol=1,fontsize=(21))
#xlabels = ['0',r'$\pi$',r'$2\pi$',r'$ 3 \pi $',r'$ 4\pi$']
#x=[0,3.14,2*3.14,3*3.14,4*3.14]
#plt.xticks(x,xlabels)
#plt.ylabel('Modelo 4',fontsize=(40))
#plt.xlim(xmax = 5.01, xmin = 0)
plt.xticks(np.arange(0., 15 + 0.01, 5.))
plt.ylim(ymax = 10.1, ymin = -0.1)
plt.yticks(np.arange(0., 10 + 0.1, 5))
#plt.title('Kicks to A and C',fontsize=(30))
letter = '3)'	# letter that identifies the figure (for no letter write '')
letter_color = 'black'	# color of the letter that identifies the figure
plt.text(0.1, 8, letter,fontsize=35, color=letter_color)

plt.subplot(234)
plt.plot(f13[:,0],f13[:,1],'navy',marker='o',markevery=200,markersize=5,label=r'$S(\tau)$', linewidth=2.5)
plt.plot(f13[:,0],f13[:,2],'orange',marker='o',markevery=200,markersize=5,label=r'$I(\tau)$', linewidth=2.5)
plt.plot(f13[:,0],f13[:,3],'red',marker='o',markevery=200,markersize=5,label=r'$R(\tau)$', linewidth=2.5)
plt.plot(f13[:,0],f13[:,4],'green',marker='o',markevery=200,markersize=5,label=r'$N(\tau)$', linewidth=2.5)
plt.tick_params(labelsize='40',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
#xlabels = ['0',r'$\pi$',r'$2\pi$',r'$ 3 \pi $',r'$ 4\pi$']
#x=[0,3.14,2*3.14,3*3.14,4*3.14]
#plt.xticks(x,xlabels)
#plt.ylabel('Modelo 4',fontsize=(40))
plt.xlim(xmax = 5.01, xmin = 0)
plt.xticks(np.arange(0., 15 + 0.01, 5.))
plt.ylim(ymax = 10.1, ymin = -0.1)
plt.yticks(np.arange(0., 10 + 0.1, 5))
#plt.title('Kicks to A and C',fontsize=(30))
letter = '4)'	# letter that identifies the figure (for no letter write '')
letter_color = 'black'	# color of the letter that identifies the figure
plt.text(0.1, 8, letter,fontsize=35, color=letter_color)


plt.subplot(235)
plt.plot(f14[:,0],f14[:,1],'navy',marker='o',markevery=200,markersize=5,label=r'$S(\tau)$', linewidth=2.5)
plt.plot(f14[:,0],f14[:,2],'orange',marker='o',markevery=200,markersize=5,label=r'$I(\tau)$', linewidth=2.5)
plt.plot(f14[:,0],f14[:,3],'red',marker='o',markevery=200,markersize=5,label=r'$R(\tau)$', linewidth=2.5)
plt.plot(f14[:,0],f14[:,4],'green',marker='o',markevery=200,markersize=5,label=r'$N(\tau)$', linewidth=2.5)
plt.tick_params(labelsize='40',labeltop='off',labelright='off', labelbottom='on', labelleft='off')
#xlabels = ['0',r'$\pi$',r'$2\pi$',r'$ 3 \pi $',r'$ 4\pi$']
#x=[0,3.14,2*3.14,3*3.14,4*3.14]
#plt.xticks(x,xlabels)
#plt.ylabel('Modelo 4',fontsize=(40))
plt.xlim(xmax = 5.01, xmin = 0)
plt.xticks(np.arange(0., 15 + 0.01, 5.))
plt.ylim(ymax = 10.1, ymin = -0.1)
plt.yticks(np.arange(0., 10 + 0.1, 5))
#plt.title('Kicks to A and C',fontsize=(30))
letter = '5)'	# letter that identifies the figure (for no letter write '')
letter_color = 'black'	# color of the letter that identifies the figure
plt.text(0.1, 8, letter,fontsize=35, color=letter_color)


plt.subplot(236)
plt.plot(f15[:,0],f15[:,1],'navy',marker='o',markevery=200,markersize=5,label=r'$S(\tau)$', linewidth=2.5)
plt.plot(f15[:,0],f15[:,2],'orange',marker='o',markevery=200,markersize=5,label=r'$I(\tau)$', linewidth=2.5)
plt.plot(f15[:,0],f15[:,3],'red',marker='o',markevery=200,markersize=5,label=r'$R(\tau)$', linewidth=2.5)
plt.plot(f15[:,0],f15[:,4],'green',marker='o',markevery=200,markersize=5,label=r'$N(\tau)$', linewidth=2.5)
plt.tick_params(labelsize='40',labeltop='off',labelright='off', labelbottom='on', labelleft='off')
#xlabels = ['0',r'$\pi$',r'$2\pi$',r'$ 3 \pi $',r'$ 4\pi$']
#x=[0,3.14,2*3.14,3*3.14,4*3.14]
#plt.xticks(x,xlabels)
#plt.ylabel('Modelo 4',fontsize=(40))
plt.xlim(xmax = 5.01, xmin = 0)
plt.xticks(np.arange(0., 15 + 0.01, 5.))
plt.ylim(ymax = 10.1, ymin = -0.1)
plt.yticks(np.arange(0., 10 + 0.1, 5))
#plt.title('Kicks to A and C',fontsize=(30))
letter = '6)'	# letter that identifies the figure (for no letter write '')
letter_color = 'black'	# color of the letter that identifies the figure
plt.text(0.1, 8, letter,fontsize=35, color=letter_color)


plt.suptitle(r'$\beta=$%d$\times 10^{-2}$, $\kappa=$%d$\times 10^{-2}$' %(data[0],data[1]),fontsize=(35))


figure_name = './figure.jpg'	# name of the figure to be saved

plt.savefig(figure_name)
plt.show()



















