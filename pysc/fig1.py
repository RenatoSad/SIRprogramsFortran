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

#########################################################################

with open('/home/newtonmarmota/Documentos/SIR/code_1/Calis1/SIRCla.dat','r') as f:
  f13 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f13.append(line)	      
f13 = np.array(f13)

with open('/home/newtonmarmota/Documentos/SIR/code_1/Calis1/SIRExp.dat','r') as f:
  f14 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f14.append(line)
f14 = np.array(f14)

#########################################################################

#with open('Time.dat','r') as f:
  #Time=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #Time.append(line)
#Time = np.array(Time)

with open('Infec.dat','r') as f:
  InfN1=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfN1.append(line)
InfN1 = np.array(InfN1)
CInfN1 = len(InfN1[0])      #print CInfN1
Inf1N1 = InfN1[:,1:CInfN1]  #print Inf1N1.shape

with open('InfecPr.dat','r') as f:       #InfmNT1 = Inf1N1.mean(axis=1)
  InfN1p=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfN1p.append(line)
InfN1p = np.array(InfN1p)

##########################################################################

plt.rcParams['axes.linewidth'] = 3.5 
plt.rcParams['xtick.major.width'] = 3.5
plt.rcParams['ytick.major.width'] = 3.5
plt.rcParams['xtick.major.size'] = 15
plt.rcParams['ytick.major.size'] = 15


rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

##########################################################################

fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.51, 0.01, r'$Time \ (years)$', ha='center',fontsize=(30))
fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))

plt.subplot(111)
for i in range(1,CInfN1-1):
   plt.plot(InfN1p[:,0],Inf1N1[:,i],'black',linewidth=0.6)

plt.plot(InfN1p[:,0],Inf1N1[:,1],'black',label=r'$UnifRand$',linewidth=0.6)   
plt.plot(InfN1p[:,0],InfN1p[:,1],'red',marker='*',markevery=800,markersize=7,label=r'$AvUnifRand$',linewidth=2.0)

plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(.97, 1.10), shadow = True, loc='upper left', ncol=1,fontsize=(14))
    
plt.suptitle(r'$\beta=$%d$/150\cos\bigg(\frac{\pi}{365}  t \bigg)$, $\kappa_1=1/15$, $\kappa_2=1/(0.8*365)$' %(data[0]),fontsize=(30))
   
    
figure_name = './fig1rNPavP.jpg'	# name of the figure to be saved
plt.savefig(figure_name)
plt.show()

###########################################################################
###########################################################################

#fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
#fig.text(0.51, 0.01, r'$Time \ (years)$', ha='center',fontsize=(30))
#fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))

#plt.subplot(111)
#plt.plot(Time,f13[:,2],'navy',marker='X',markevery=800,markersize=7,label=r'$Classic$', linewidth=1.5)
#plt.plot(Time,f14[:,2],'orange',marker='o',markevery=800,markersize=7,label=r'$Exponential$', linewidth=1.5)
#plt.plot(Time,Infp[:,2],'green',marker='h',markevery=800,markersize=7,label=r'$Polinomial$', linewidth=1.5)
#plt.plot(Time,InfN1p ,'red',marker='*',markevery=800,markersize=7,label=r'$AvNormRandPoly$',linewidth=1.5)
##plt.plot(InfuT3,InfmU3,'orangered',label=r'$AvUnifRand2Poly$',linewidth=2.0)
##plt.plot(InfbT3,InfmB3,'darkturquoise',label=r'$AvBetaRand2Poly$',linewidth=2.0)
##plt.plot(InftT3,InfmT3,'cornflowerblue',label=r'$AvTriaRand2Poly$',linewidth=2.0)

#plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')

#plt.legend(borderpad=0.1,bbox_to_anchor=(.97, 1.16), shadow = True, loc='upper left', ncol=1,fontsize=(14))
                     
##plt.suptitle(r'$\beta=\frac{2.5}{15}\cos\bigg(\frac{\pi}{365}  t \bigg)$, $\kappa_1=1/15$, $\kappa_2=1/(0.8*365)$' %(data[0]),fontsize=(30))    
    
#figure_name = './fig1comp.jpg'	# name of the figure to be saved
#plt.savefig(figure_name)
#plt.show()










