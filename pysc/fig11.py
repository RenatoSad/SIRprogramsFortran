import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib import rc    

with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis1/Infec11.dat','r') as f:
  InfN1=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfN1.append(line)
InfN1 = np.array(InfN1)
InfnT1 = InfN1[:,0]/365
Inf2N1 = InfN1[:,1:1000]
InfmN1 = Inf2N1.mean(axis=1)

with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis5/Infec51.dat','r') as f:
  InfN2=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfN2.append(line)
InfN2 = np.array(InfN2)
InfnT2 = InfN2[:,0]/365
Inf2N2 = InfN2[:,1:1000]
InfmN2 = Inf2N2.mean(axis=1)

with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis2/Infec21.dat','r') as f:
  InfU1=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfU1.append(line)
InfU1 = np.array(InfU1)
InfuT1 = InfU1[:,0]/365
Inf2U1 = InfU1[:,1:1000]
InfmU1 = Inf2U1.mean(axis=1)

with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis6/Infec61.dat','r') as f:
  InfU2=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfU2.append(line)
InfU2 = np.array(InfU2)
InfuT2 = InfU2[:,0]/365
Inf2U2 = InfU2[:,1:1000]
InfmU2 = Inf2U2.mean(axis=1)

with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis3/Infec31.dat','r') as f:
  InfB1=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfB1.append(line)
InfB1 = np.array(InfB1)
InfbT1 = InfB1[:,0]/365
Inf2B1 = InfB1[:,1:1000]
InfmB1 = Inf2B1.mean(axis=1)

with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis7/Infec71.dat','r') as f:
  InfB2=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfB2.append(line)
InfB2 = np.array(InfB2)
InfbT2 = InfB2[:,0]/365
Inf2B2 = InfB2[:,1:1000]
InfmB2 = Inf2B2.mean(axis=1)

with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis4/Infec41.dat','r') as f:
  InfT1=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfT1.append(line)
InfT1 = np.array(InfT1)
InftT1 = InfT1[:,0]/365
Inf2T1 = InfT1[:,1:1000]
InfmT1 = Inf2T1.mean(axis=1)


with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis8/Infec81.dat','r') as f:
  InfT2=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfT2.append(line)
InfT2 = np.array(InfT2)
InftT2 = InfT2[:,0]/365
Inf2T2 = InfT2[:,1:1000]
InfmT2 = Inf2T2.mean(axis=1)

plt.rcParams['axes.linewidth'] = 3.5 
plt.rcParams['xtick.major.width'] = 3.5
plt.rcParams['ytick.major.width'] = 3.5
plt.rcParams['xtick.major.size'] = 15
plt.rcParams['ytick.major.size'] = 15


rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

#########################################################################
#########################################################################

fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.51, 0.01, r'$Time \ (years)$', ha='center',fontsize=(30))
fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))

plt.subplot(111)
plt.plot(InfnT1,InfmN1,'fucshia',label=r'$AvNormRanPoly$',linewidth=2.0)   
plt.plot(InfnT2,InfmN2,'palevioletred',label=r'$AvNormPoly$',linewidth=2.0)

plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(.97, 1.10), shadow = True, loc='upper left', ncol=1,fontsize=(14))
    
figure_name = './fig1compN.jpg'	# name of the figure to be saved
plt.savefig(figure_name)
plt.show()

#########################################################################
#########################################################################

fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.51, 0.01, r'$Time \ (years)$', ha='center',fontsize=(30))
fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))

plt.subplot(111)
plt.plot(InfuT1,InfmU1,'salmon',label=r'$AvUnifRanPoly$',linewidth=2.0)   
plt.plot(InfuT2,InfmU2,'darked',label=r'$AvUnifPoly$',linewidth=2.0)

plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(.97, 1.10), shadow = True, loc='upper left', ncol=1,fontsize=(14))
    
figure_name = './fig2compU.jpg'	# name of the figure to be saved
plt.savefig(figure_name)
plt.show()

#########################################################################
#########################################################################

fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.51, 0.01, r'$Time \ (years)$', ha='center',fontsize=(30))
fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))

plt.subplot(111)
plt.plot(InfbT1,InfmB1,'deepskyblue',label=r'$AvBetaRanPoly$',linewidth=2.0)   
plt.plot(InfbT2,InfmB2,'slategray',label=r'$AvBetaPoly$',linewidth=2.0)

plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(.97, 1.10), shadow = True, loc='upper left', ncol=1,fontsize=(14))
    
figure_name = './fig2compB.jpg'	# name of the figure to be saved
plt.savefig(figure_name)
plt.show()

#########################################################################
#########################################################################

fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.51, 0.01, r'$Time \ (years)$', ha='center',fontsize=(30))
fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))

plt.subplot(111)
plt.plot(InftT1,InfmT1,'steelblue',label=r'$AvTrianRanPoly$',linewidth=2.0)   
plt.plot(InftT2,InfmT2,'indigo',label=r'$AvTrianPoly$',linewidth=2.0)

plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(.97, 1.10), shadow = True, loc='upper left', ncol=1,fontsize=(14))
    
figure_name = './fig2compB.jpg'	# name of the figure to be saved
plt.savefig(figure_name)
plt.show()

#########################################################################
#########################################################################