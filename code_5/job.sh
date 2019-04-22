#!/bin/bash
b='25' #25
ka='1'
ka2='1'
mu='1'
is='99'
ii='1'
ir='0'
#k='10'         # interval of change the constants c0...c6 
Tr='500'
pyf='pysc'
Ka='Ti'
Ty='Try'
Rn='RgCo'

for k in {1,10,70,310,1825,3650}
do

start=$SECONDS

dir0=`pwd`
ca=$Rn$Ka$k$Ty$Tr
dir1='/home/newtonmarmota/Documentos/SIR/'
dir2='/home/newtonmarmota/Documentos/SIR/Results/code_5Result/'
dir=$dir2$ca
mkdir $dir

gfortran -O3 -o exe my_prec.f95 dp_const.f95 random.f95 eqs.f95 rk.f95 -mcmodel=medium
 cp $dir1/$pyf/fig1.py  $dir
 cp exe $dir
 cd $dir
 printf "$b $ka $ka2 $mu $is $ii $ir $k $Tr" > par.dat
 ./exe
 mv fort.21 In.dat
 mv fort.22 InE2.dat
 mv fort.23 InE3.dat
 mv fort.31 InP.dat
 mv fort.32 InE2P.dat
 mv fort.33 InE3P.dat
 cd $dir0
 
 cd $dir 
# python fig1.py &

duration=$(( SECONDS - start))
echo "$duration"
done
