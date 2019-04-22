#!/bin/bash
b='25'
ka='1'
ka2='1'
mu='1'
is='99'
ii='1'
ir='0'
#Rg='4'         # kind of random generator 1 => N, 2 => U, 3 => B, 4=>T
#k='36502'         # interval of change the constants c0...c6 
Tr='500'
pyf='pysc'
Ka='Ti'
Ty='Try'

for Rg in {1,2,3,4}
do

start=$SECONDS

if [ "$Rg" == "1" ]; then
Rn='RgN'
elif [ "$Rg" == "2" ]; then
Rn='RgU'
elif [ "$Rg" == "3" ]; then
Rn='RgB'
elif [ "$Rg" == "4" ]; then
Rn='RgT'
fi

for k in {1,10,70,310,1825,3650}  #,36502}
do
dir0=`pwd`
ca=$Rn$Ka$k$Ty$Tr #$beta$b$kappa$ka$miu$mu$so$is$io$ii$ro$ir
dir1='/home/newtonmarmota/Documentos/SIR/'
dir2='/home/newtonmarmota/Documentos/SIR/Results/code_3Result/'
dir=$dir2$ca
mkdir $dir

gfortran -O3 -o exe my_prec.f95 dp_const.f95 random.f95 eqs.f95 rk.f95 -mcmodel=medium
 cp $dir1/$pyf/fig1.py  $dir
 cp exe $dir
 #cp RPar1.dat RPar2.dat RPar3.dat $dir
 cp RPar2.dat $dir
 cd $dir
 printf "$b $ka $ka2 $mu $is $ii $ir $Rg $k $Tr" > par.dat
 ./exe
 mv fort.21 In.dat
 mv fort.22 InE2.dat
 mv fort.23 InE3.dat
 mv fort.31 InP.dat
 mv fort.32 InE2P.dat
 mv fort.33 InE3P.dat
# cd $dir0
 
#cd $dir
# python fig1.py &

duration=$(( SECONDS - start ))
echo "$duration"

 cd $dir0
done
done