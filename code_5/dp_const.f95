!                                                                    8.07.2009
! MyMod basic constants module
!------------------------------------------------------------------------------

module dp_const
   use my_prec, only: wp => dp   ! for double precision constants
   implicit none
 
   real(wp), parameter :: po= 0.0_wp, zo= 0.0_wp

   real(wp), parameter :: beta = 0.05_wp, D = 3.5_wp, om= sqrt(1.0_wp-beta**2/4.0_wp)
                          
   real(wp), parameter :: rero= 0.0_wp, one= 1.0_wp, two= 2.0_wp,             &
                          three= 3.0_wp, four= 4.0_wp, five= 5.0_wp,          &
                          six= 6.0_wp

   real(wp), parameter :: pi= two*two*atan(one)
   real(wp), parameter :: twopi= two*pi, pio2= pi/two
   real(wp), parameter :: sq2= sqrt(two)

   complex(wp), parameter :: zero= (rero,rero), zone= (one,rero),             &
                             zi= (rero,one)
end module dp_const
