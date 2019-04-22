#!/bin/bash
b='25'
ka='1'
ka2='1'
mu='1'
is='99'
ii='1'
ir='0'
kappa='k'
miu='m'
beta='b'
so='so'
io='io'
ro='ro'
pyf='pysc'

dir0=`pwd`
ca='Calis2' #$beta$b$kappa$ka$miu$mu$so$is$io$ii$ro$ir
dir1='/home/newtonmarmota/Documentos/SIR/'
dir2='/home/newtonmarmota/Documentos/SIR/code_1/'
dir=$dir2$ca
mkdir $dir


##for b in {10..100..10}
##do
gfortran -O3 -o exe my_prec.f95 dp_const.f95 eqs.f95 rk.f95 -mcmodel=medium
cp $dir1/$pyf/fig7.py  $dir
cp exe $dir
cd $dir
printf "$b $ka $ka2 $mu $is $ii $ir" > par.dat
./exe
mv fort.12 SIRCla.dat
mv fort.13 SIRClaIn.dat
mv fort.14 SIRExp1In.dat
mv fort.15 SIRExp2In.dat

cd $dir0 

# cd $dir
# python fig7.py &