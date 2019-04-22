#!/bin/bash
#b='25' #25
ka='1'
ka2='1'
mu='1'
is='99'
ii='1'
ir='0'
#k='10'         # interval of change the constants c0...c6 
Tr='500'
pyf='pysc'
beta='bet'
Ka='Ti'
Ty='Try'
Rn='RgCo'
Rt='RgCobet(25to105)Ti'

for k in {70,310,1825,3650,36502}
do
for b in {25..105..10}
do
dir0=`pwd`
ca=$Rn$beta$b$Ka$k$Ty$Tr
dir1='/home/newtonmarmota/Documentos/SIR/'
ca2=$Rt$k$Ty$Tr
dir2='/home/newtonmarmota/Documentos/SIR/code_4Result/'
dir=$dir2$ca2/$ca
mkdir $dir

gfortran -O3 -o exe my_prec.f95 dp_const.f95 random.f95 eqs.f95 rk.f95 -mcmodel=medium
 cp $dir1/$pyf/fig1.py  $dir
 cp exe $dir
 cd $dir
 printf "$b $ka $ka2 $mu $is $ii $ir $k $Tr" > par.dat
 ./exe
 mv fort.20 Infec.dat
 mv fort.21 InfecPr.dat
 mv fort.22 Time.dat
 cd $dir0
 
 cd $dir 
 python fig1.py &


done
done