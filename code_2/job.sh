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


c0='100'
c1='100'
c2='100'
c3='100'
c4='100' 
c5='100'

dir0=`pwd`
ca='Calis2' #$beta$b$kappa$ka$miu$mu$so$is$io$ii$ro$ir
dir1='/home/newtonmarmota/Documentos/SIR/'
dir2='/home/newtonmarmota/Documentos/SIR/code_2/'
dir=$dir2$ca
mkdir $dir

gfortran -O3 -o exe my_prec.f95 dp_const.f95 eqs.f95 rk.f95 -mcmodel=medium
cp $dir1/$pyf/fig10.py  $dir
cp exe $dir
cd $dir
printf "$b $ka $ka2 $mu $is $ii $ir" > par.dat
printf "$c0 $c1 $c2 $c3 $c4 $c5" > cons.dat
./exe
mv fort.10 Infec.dat
cd $dir0


cd $dir
python fig10.py &



# ##for b in {10..100..10}
# ##do
# dir0=`pwd`
# ca=$beta$b$kappa$ka$miu$mu$so$is$io$ii$ro$ir
# dir1='/home/newtonmarmota/Documentos/SIR/'
# dir=$dir1$ca
# mkdir $dir
# gfortran -O3 -o exe my_prec.f95 dp_const.f95 random.f95 eqs.f95 rk.f95 -mcmodel=medium
# cp $dir1/$pyf/*.py  $dir
# cp exe $dir
# cd $dir
# printf "$b $ka $ka2 $mu $is $ii $ir" > par.dat
# ./exe
# python fig9.py &
# #python fig7.py &
# #python fig8.py &
# #python fig6.py &
# #python fig1.py &
# #python fig2.py &
# #python fig3.py &
# #python fig4.py &
# #python fig5.py &
# cd $dir0
##done