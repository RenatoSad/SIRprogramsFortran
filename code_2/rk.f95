 program runge
 use my_prec, only: i4b,wp => dp
 use dp_const, only: rero,one,two,three,four,zero,zone,zi,pi
 use eqs
 
 implicit none

  real(wp) :: s,r,i
  real(wp) :: so,ro,io
  real(wp) :: ks1,ki1,kr1,ks2,ki2,kr2,&
              ks3,ki3,kr3,ks4,ki4,kr4
             
  real(wp) :: t,det,tend,xi,beta,kappa,kappa2,miu,t0,om
  integer(i4b) :: tau,npoint,ic1,ntotal
  
  integer(i4b) :: p1,p2,pp2,p3,p4,p5,p6,si,ii,ri,&
                  c0,c1,c2,c3,c4,c5
  
  real(wp) :: cons0,cons1,cons2,cons3,cons4,cons5
  
npoint = 1
tend = 365._wp * 10._wp
det = 0.1_wp
ntotal = int(tend/det)

t = rero
ic1 = 0 

 open(unit=8,file='par.dat',status='old')
 read(8,*) p1,p2,pp2,p3,p4,p5,p6
 close(unit=8)
 
 open(unit=8,file='cons.dat',status='old')
 read(8,*) c0,c1,c2,c3,c4,c5
 close(unit=8)

beta = dfloat(p1)/(15._wp*10._wp)!tasa de infeccion
kappa = dfloat(p2)/15._wp !tasa de recuperacion
kappa2 = 10._wp*dfloat(pp2)/(8._wp*365._wp) !tasa de perdida de inmunidad
om = pi / 365._wp 

xi = kappa/beta

si = p4
ii = p5
ri = p6

 cons0 = dfloat(c0)/100._wp
 cons1 = dfloat(c1)/100._wp
 cons2 = dfloat(c2)/100._wp
 cons3 = dfloat(c3)/100._wp
 cons4 = dfloat(c4)/100._wp
 cons5 = dfloat(c5)/100._wp

!initial cs. assuming standard sri model
so = dfloat(si)/100._wp
io = dfloat(ii)/100._wp
ro = dfloat(ri)/100._wp

t0 = rero
t = rero
ic1 = 0 

write(10,'(8ES24.13E3)') t,so,io,ro,so+io+ro       

do tau=1,ntotal
   t = t + det
   
 !runge-kutta 4th order 
call eqs2(ks1,ki1,kr1,so,io,ro,beta,kappa,kappa2,cons0,cons1,cons2,cons3,cons4,cons5,det,t0,om)   

  s = so + ks1/2._wp
  i = io + ki1/2._wp
  r = ro + kr1/2._wp
  
call eqs2(ks2,ki2,kr2,s,i,r,beta,kappa,kappa2,cons0,cons1,cons2,cons3,cons4,cons5,det,t0 + det/two,om)

  s = so + ks2/2._wp
  i = io + ki2/2._wp
  r = ro + kr2/2._wp
  
call eqs2(ks3,ki3,kr3,s,i,r,beta,kappa,kappa2,cons0,cons1,cons2,cons3,cons4,cons5,det,t0 + det/two,om)

  s = so + ks3
  i = io + ki3
  r = ro + kr3

call eqs2(ks4,ki4,kr4,s,i,r,beta,kappa,kappa2,cons0,cons1,cons2,cons3,cons4,cons5,det,t0,om) 

  so = so + (ks1 + 2._wp*ks2 +2._wp*ks3 + ks4)/6._wp
  io = io + (ki1 + 2._wp*ki2 +2._wp*ki3 + ki4)/6._wp
  ro = ro + (kr1 + 2._wp*kr2 +2._wp*kr3 + kr4)/6._wp

  
if(tau == 1.or.mod(tau,npoint) == 0)then
write(10,'(8ES24.13E3)') t,so,io,ro,so+io+ro              
endif


t0 = t
enddo

stop
end program

