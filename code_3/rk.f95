 program runge
 use my_prec, only: i4b,wp => dp
 use dp_const, only: rero,one,two,three,four,zero,zone,zi,pi
 use eqs
 use random
 
 implicit none

  real(wp) :: su,re,in
  real(wp) :: so,ro,io
  real(wp) :: ks1,ki1,kr1,ks2,ki2,kr2,&
              ks3,ki3,kr3,ks4,ki4,kr4
             
  real(wp) :: t,det,tend,xi,beta,kappa,kappa2,miu,t0,om
  integer(i4b) :: tau,npoint,ic1,ntotal
  
  integer(i4b) :: p1,p2,pp2,p3,p4,p5,p6,p7,Rg,k,si,ii,ri,jq,i,j,ir,Tr,q 
  
  real(wp) :: cons0,cons1,cons2,cons3,cons4,cons5
 
  real(wp), dimension(6) :: mean,std_dev,au,bu,al,be,at,ct,bt
  real(wp), dimension(36501,1001) :: infec
  real(wp), dimension(36501) :: iny, ty, infpx
  real(wp), dimension(36501,2) :: Infpr
  
npoint = 1
tend = 365._wp * 10._wp
det = 0.1_wp
ntotal = int(tend/det)

t = rero
ic1 = 0 

open(unit=8,file='par.dat',status='old')
read(8,*) p1,p2,pp2,p3,p4,p5,p6,Rg,k,Tr
close(unit=8)

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
open(unit=9,file='RPar2.dat',status='old')
do ir = 1,6
   read(9,*) mean(ir),std_dev(ir),bu(ir),au(ir),al(ir),be(ir),&
             bt(ir),ct(ir),at(ir)
enddo
close(unit=9)

beta = dfloat(p1)/(15._wp*10._wp)!tasa de infeccion
!!beta = dfloat(p1)/100._wp !tasa de infeccion
kappa = dfloat(p2)/15._wp !tasa de recuperacion
kappa2 = 10._wp*dfloat(pp2)/(8._wp*365._wp) !tasa de perdida de inmunidad
om = pi / 365._wp 

xi = kappa/beta

do q = 1,3
do p7 = 2,Tr+1

si = p4
ii = p5
ri = p6

!initial cs. assuming standard sri model
so = dfloat(si)/100._wp
io = dfloat(ii)/100._wp
ro = dfloat(ri)/100._wp

t0 = rero
t = rero
ic1 = 0 

iny(1) = io
ty(1) = t

call init_random_seed()   ! change the seed
call randomcoefc(cons0,cons1,cons2,cons3,cons4,cons5,mean,std_dev,au,bu,al,be,at,ct,bt,Rg)

jq = 1
do tau=1,ntotal
   t = t + det
   
if (mod(tau,k)==0) then 
! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
call randomcoefc(cons0,cons1,cons2,cons3,cons4,cons5,mean,std_dev,au,bu,al,be,at,ct,bt,Rg)
endif
   
 !runge-kutta 4th order 
call eqs2(ks1,ki1,kr1,so,io,ro,beta,kappa,kappa2,cons0,cons1,cons2,cons3,cons4,cons5,det,t0,om,q) 

  su = so + ks1/2._wp
  in = io + ki1/2._wp
  re = ro + kr1/2._wp
  
call eqs2(ks2,ki2,kr2,su,in,re,beta,kappa,kappa2,cons0,cons1,cons2,cons3,cons4,cons5,det,t0 + det/two,om,q)

  su = so + ks2/2._wp
  in = io + ki2/2._wp
  re = ro + kr2/2._wp
  
call eqs2(ks3,ki3,kr3,su,in,re,beta,kappa,kappa2,cons0,cons1,cons2,cons3,cons4,cons5,det,t0 + det/two,om,q)

  su = so + ks3
  in = io + ki3
  re = ro + kr3

call eqs2(ks4,ki4,kr4,su,in,re,beta,kappa,kappa2,cons0,cons1,cons2,cons3,cons4,cons5,det,t0,om,q) 

  so = so + (ks1 + 2._wp*ks2 +2._wp*ks3 + ks4)/6._wp
  io = io + (ki1 + 2._wp*ki2 +2._wp*ki3 + ki4)/6._wp
  ro = ro + (kr1 + 2._wp*kr2 +2._wp*kr3 + kr4)/6._wp

jq = jq + 1

iny(jq) = io 
ty(jq) = t

t0 = t
enddo

ty=ty/365_i4b

infec(:,1) = ty
infec(:,p7) = iny
infpx(:) = infpx(:) + iny


enddo

do i = lbound(infec,1), ubound(infec,1)
      write(20 + q,'(1001ES24.13E3)') (infec(i, j), j = lbound(infec,2), ubound(infec,2) )
   end do
   
infpx = infpx/Tr  

Infpr(:,1)=ty
Infpr(:,2)=infpx

do i = lbound(Infpr,1), ubound(Infpr,1)
      write(30 + q,'(2ES24.13E3)') (Infpr(i, j), j = lbound(Infpr,2), ubound(Infpr,2) )
end do

end do
!write(22,'(1ES24.13E3)') ty

stop


end program

