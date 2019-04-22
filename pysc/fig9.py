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

with open('/home/newtonmarmota/Documentos/SIR/code_1/Calis1/SIRCla.dat','r') as f:
  f13 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f13.append(line)	      
f13 = np.array(f13)
T13 = f13[:,0]/365

with open('/home/newtonmarmota/Documentos/SIR/code_1/Calis1/SIRExp.dat','r') as f:
  f14 = []
  for line in f:
      line = line.split()
      if line:
	      line = [float(i) for i in line]
	      f14.append(line)
f14 = np.array(f14)
T14 = f14[:,0]/365

with open('/home/newtonmarmota/Documentos/SIR/code_2/Calis1/Infecp.dat','r') as f:
  Infp=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          Infp.append(line)
Infp = np.array(Infp)
InfTp=Infp[:,0]/365

#######################################################################################

with open('Infec121.dat','r') as f:
  InfT3=[]
  for line in f:
      line = line.split()
      if line:
          line = [float(i) for i in line]
          InfT3.append(line)
InfT3 = np.array(InfT3)
InftT3 = InfT3[:,0]/365
Inf2T3 = InfT3[:,1:1000]
InfmT3 = Inf2T3.mean(axis=1)

#with open('/home/newtonmarmota/Documentos/SIR/code_3/Calis11/Infec111.dat','r') as f:
  #InfB3=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #InfB3.append(line)
#InfB3 = np.array(InfB3)
#InfbT3 = InfB3[:,0]/365
#Inf2B3 = InfB3[:,1:1000]
#InfmB3 = Inf2B3.mean(axis=1)

#with open('/home/newtonmarmota/Documentos/SIR/code_3/Calis10/Infec101.dat','r') as f:
  #InfU3=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #InfU3.append(line)
#InfU3 = np.array(InfU3)
#InfuT3 = InfU3[:,0]/365
#Inf2U3 = InfU3[:,1:1000]
#InfmU3 = Inf2U3.mean(axis=1)

#with open('/home/newtonmarmota/Documentos/SIR/code_3/Calis9/Infec91.dat','r') as f:
  #InfN3=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #InfN3.append(line)
#InfN3 = np.array(InfN3)
#InfnT3 = InfN3[:,0]/365
#Inf2N3 = InfN3[:,1:1000]
#InfmN3 = Inf2N3.mean(axis=1)

#with open('/home/newtonmarmota/Documentos/SIR/code_3/Calis4/Infec41.dat','r') as f:
  #InfT1=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #InfT1.append(line)
#InfT1 = np.array(InfT1)
#InftT1 = InfT1[:,0]/365
#Inf2T1 = InfT1[:,1:1000]
#InfmT1 = Inf2T1.mean(axis=1)

#with open('/home/newtonmarmota/Documentos/SIR/code_3/Calis8/Infec81.dat','r') as f:
  #InfT2=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #InfT2.append(line)
#InfT2 = np.array(InfT2)
#InftT2 = InfT2[:,0]/365
#Inf2T2 = InfT2[:,1:1000]
#InfmT2 = Inf2T2.mean(axis=1)

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
for i in range(1,999):
   plt.plot(InftT3,Inf2T3[:,i],'black',linewidth=0.6)

plt.plot(InftT3,Inf2T3[:,1],'black',label=r'$TriaRand2Poly$',linewidth=0.6)   
plt.plot(InftT3,InfmT3,'cornflowerblue',label=r'$AvTriaRand2Poly$',linewidth=2.0)

plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
plt.legend(borderpad=0.1,bbox_to_anchor=(.97, 1.10), shadow = True, loc='upper left', ncol=1,fontsize=(14))
    
figure_name = './fig1rNPavP.jpg'	# name of the figure to be saved
plt.savefig(figure_name)
plt.show()

##########################################################################
##########################################################################

fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
fig.text(0.51, 0.01, r'$Time \ (years)$', ha='center',fontsize=(30))
fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))

plt.subplot(111)
plt.plot(T13,f13[:,2],'navy',label=r'$Classic$', linewidth=2.0)
plt.plot(T14,f14[:,2],'orange',label=r'$Exponential$', linewidth=2.0)
plt.plot(InfTp,Infp[:,2],'green',label=r'$Polinomial$', linewidth=2.0)
plt.plot(InftT3,InfmT3,'violet',label=r'$AvNormRand2Poly$',linewidth=2.0)
#plt.plot(InfuT3,InfmU3,'orangered',label=r'$AvUnifRand2Poly$',linewidth=2.0)
#plt.plot(InfbT3,InfmB3,'darkturquoise',label=r'$AvBetaRand2Poly$',linewidth=2.0)
#plt.plot(InftT3,InfmT3,'cornflowerblue',label=r'$AvTriaRand2Poly$',linewidth=2.0)

plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')

plt.legend(borderpad=0.1,bbox_to_anchor=(.97, 1.16), shadow = True, loc='upper left', ncol=1,fontsize=(14))
                     
#plt.suptitle(r'$\beta=\frac{2.5}{15}\cos\bigg(\frac{\pi}{365}  t \bigg)$, $\kappa_1=1/15$, $\kappa_2=1/(0.8*365)$' %(data[0]),fontsize=(30))    
    
figure_name = './fig1comp.jpg'	# name of the figure to be saved
plt.savefig(figure_name)
plt.show()

#########################################################################
#########################################################################

#fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
#fig.text(0.51, 0.01, r'$Time \ (years)$', ha='center',fontsize=(30))
#fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))

#plt.subplot(111)
#plt.plot(InftT1,InfmT1,'red',marker='o',markevery=1000,markersize=5,label=r'$AvTriaRanPoly$',linewidth=1.8)     # fucshia
#plt.plot(InftT3,InfmT3,'green',marker='x',markevery=1000,markersize=7,label=r'$AvTriaRand2Poly$',linewidth=1.8) # violet
#plt.plot(InftT2,InfmT2,'blue',marker='*',markevery=1000,markersize=7,label=r'$AvTriaPoly$',linewidth=1.8)       # palevioletred

#plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')

#plt.legend(borderpad=0.1,bbox_to_anchor=(.97, 1.16), shadow = True, loc='upper left', ncol=1,fontsize=(14))
                     
##plt.suptitle(r'$\beta=\frac{2.5}{15}\cos\bigg(\frac{\pi}{365}  t \bigg)$, $\kappa_1=1/15$, $\kappa_2=1/(0.8*365)$' %(data[0]),fontsize=(30))    
    
#figure_name = './fig13comp.jpg'	# name of the figure to be saved
#plt.savefig(figure_name)
#plt.show()

#########################################################################
#########################################################################

#fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
#fig.text(0.51, 0.01, r'$Time \ (years)$', ha='center',fontsize=(30))
#fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))
    
#plt.subplot(111)
#plt.plot(InfT,Inf1[:,1],'blue',linewidth=1.0)
#plt.plot(InfT,Inf1[:,100],'green',linewidth=1.0)
#plt.plot(InfT,Inf1[:,1000],'red',linewidth=1.0)

#plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')
#plt.legend(borderpad=0.1,bbox_to_anchor=(.99, 1.15), shadow = True, loc='upper left', ncol=1,fontsize=(16))
    
#figure_name = './fig00rNP.jpg'	# name of the figure to be saved
#plt.savefig(figure_name)
#plt.show()

#########################################################################
#########################################################################

#with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis3/Infec31.dat','r') as f:
  #InfB1=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #InfB1.append(line)
#InfB1 = np.array(InfB1)

#InfbT1 = InfB1[:,0]/365

#Inf2B1 = InfB1[:,1:1000]

#InfmB1 = Inf2B1.mean(axis=1)



#with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis2/Infec21.dat','r') as f:
  #InfU1=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #InfU1.append(line)
#InfU1 = np.array(InfU1)

#InfuT1 = InfU1[:,0]/365

#Inf2U1 = InfU1[:,1:1000]

#InfmU1 = Inf2U1.mean(axis=1)

#plt.plot(InfuT1,InfmU1,'salmon',label=r'$AvUnifRanPoly$',linewidth=2.0)
#plt.plot(InfbT1,InfmB1,'deepskyblue',label=r'$AvBetRanPoly$',linewidth=2.0)
#plt.plot(InftT1,InfmT1,'steelblue',label=r'$AvTriRanPoly$',linewidth=2.0)

#######################################################################################
#######################################################################################

#with open('Infec81.dat','r') as f:
  #InfT2=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #InfT2.append(line)
#InfT2 = np.array(InfT2)

#InftT2 = InfT2[:,0]/365

#Inf2T2 = InfT2[:,1:1000]

#InfmT2 = Inf2T2.mean(axis=1)

#with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis7/Infec71.dat','r') as f:
  #InfB2=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #InfB2.append(line)
#InfB2 = np.array(InfB2)

#InfbT2 = InfB2[:,0]/365

#Inf2B2 = InfB2[:,1:1000]

#InfmB2 = Inf2B2.mean(axis=1)

#with open('/home/euclidesmarmota/Documentos/SIR/code_3/Calis6/Infec61.dat','r') as f:
  #InfU2=[]
  #for line in f:
      #line = line.split()
      #if line:
          #line = [float(i) for i in line]
          #InfU2.append(line)
#InfU2 = np.array(InfU2)

#InfuT2 = InfU2[:,0]/365

#Inf2U2 = InfU2[:,1:1000]

#InfmU2 = Inf2U2.mean(axis=1)

##########################################################################
##########################################################################

#fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True, figsize=(20, 10))
#fig.text(0.51, 0.01, r'$Time \ (years)$', ha='center',fontsize=(30))
#fig.text(0.03, 0.61, r'$Prevalence$', ma='center',rotation='vertical',fontsize=(30))

#plt.subplot(111)
#plt.plot(T13,f13[:,2],'navy',label=r'$Classic$', linewidth=2.0)
#plt.plot(T14,f14[:,2],'orange',label=r'$Exponential$', linewidth=2.0)
#plt.plot(InfTp,Infp[:,2],'green',label=r'$Polinomial$', linewidth=2.0)
#plt.plot(InfnT2,InfmN2,'palevioletred',label=r'$AvNormPoly$',linewidth=2.0)
#plt.plot(InfuT2,InfmU2,'darkred',label=r'$AvUnifPoly$',linewidth=2.0)
#plt.plot(InfbT2,InfmB2,'slategray',label=r'$AvBetaPoly$',linewidth=2.0)
#plt.plot(InftT2,InfmT2,'indigo',label=r'$AvTrianPoly$',linewidth=2.0)

#plt.tick_params(labelsize='25',labeltop='off',labelright='off', labelbottom='on', labelleft='on')

#plt.legend(borderpad=0.1,bbox_to_anchor=(.97, 1.16), shadow = True, loc='upper left', ncol=1,fontsize=(14))
                     
##plt.suptitle(r'$\beta=\frac{2.5}{15}\cos\bigg(\frac{\pi}{365}  t \bigg)$, $\kappa_1=1/15$, $\kappa_2=1/(0.8*365)$' %(data[0]),fontsize=(30))    
    
#figure_name = './fig1comp.jpg'	# name of the figure to be saved
#plt.savefig(figure_name)
#plt.show()
