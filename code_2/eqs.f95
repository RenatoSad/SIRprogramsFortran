!                                                                     
! This module provides the matrix elements of the louvillian
! terms of the master equation. It reads the external parameters from the
! module readpar.
module eqs
contains !---------------------------------------------------------------------



!Modelo Sir
subroutine eqs0(s,i,r,so,io,ro,xi,det)
 use my_prec, only: i4b,wp => dp
 use dp_const, only: rero,one,two,three,four,zero,zone,zi,pi
 
     real(wp), intent(out) :: r,s,i
     real(wp), intent(in) :: so,io,ro,xi,det

s = -so * io * det     
i = (so * io - xi * io) * det
r = xi * io * det

return
end subroutine

!Modelo SIR con diferentes distribuciones
subroutine eqs1(s,i,r,so,io,ro,bo,kappa,kappa2,miu,det,j,t0,omo)
 use my_prec, only: i4b,wp => dp
 use dp_const, only: rero,one,two,four,zero,zone,zi,pi
 
     real(wp), intent(out) :: r,s,i
     real(wp), intent(in) :: so,io,ro,det,t0
     real(wp), intent(in) :: bo,kappa,kappa2,miu,omo
     integer(i4b), intent(in) :: j
     real(wp) :: beta
     
 beta = bo * cos( t0* omo)**2     
     
if (j==3) then

s = (- (one/ ( exp( one/(beta * so )) - one ) ) * io + kappa2 * ro )* det     
i = ( (one/ ( exp( one/(beta * so )) - one ) )  * io - kappa * io) * det
r = (kappa * io - kappa2 * ro)* det

else if (j==4) then

s = (- ( exp( beta * so ) - one ) * io + kappa2 * ro )* det     
i = ( ( exp( beta * so ) - one )  * io - kappa * io) * det
r = (kappa * io - kappa2 * ro)* det

else if (j==5) then

s = (- beta * so   * io + kappa2 * ro )* det     
i = ( beta * so   * io - kappa * io) * det
r = (kappa * io - kappa2 * ro)* det

else if (j==6) then

s = (- beta * so   * io + miu - miu * so )* det     
i = ( beta * so   * io - kappa * io - miu * io) * det
r = (kappa * io - miu * ro)* det

endif

return
end subroutine


!Modelo SIR polynomial

subroutine eqs2(s,i,r,so,io,ro,bo,kappa,kappa2,cons0,cons1,cons2,cons3,cons4,cons5,det,t0,omo)
 use my_prec, only: i4b,wp => dp
 use dp_const, only: rero,one,two,three,four,zero,zone,zi,pi
 
     real(wp), intent(out) :: r,s,i
     real(wp), intent(in) :: so,io,ro,bo,kappa,kappa2,cons0,cons1,&
                             cons2,cons3,cons4,cons5,t0,det,omo
     real(wp) :: beta
     
beta = bo * cos( t0* omo)**2     

s = (-(cons0 * beta * so + cons1 * (beta * so)**2 + cons2 * (beta * so)**3&
    + cons4 * (beta * so)**4 + cons5 * (beta * so)**5) * io + kappa2 * ro) * det

i = ((cons0 * beta * so + cons1 * (beta * so)**2 + cons2 * (beta * so)**3&
    + cons4 * (beta * so)**4 + cons5 * (beta * so)**5) * io - kappa * io) * det

r = (kappa * io - kappa2 * ro)* det

return
end subroutine

end module
