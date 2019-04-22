module random
 contains
 
! return a random seed 
! based on the system_clock

 subroutine init_random_seed()

      INTEGER :: i, n, clock
      INTEGER, DIMENSION(:), ALLOCATABLE :: seed

      CALL RANDOM_SEED(size = n)
      ALLOCATE(seed(n))

      CALL SYSTEM_CLOCK(COUNT=clock)

      seed = clock + 37 * (/ (i - 1, i = 1, n) /)
      CALL RANDOM_SEED(PUT = seed)

      DEALLOCATE(seed)
      
end 

! ####################################################

! return a random sambple from a normal distribution
! based on the marsalgia polar method

subroutine norm_rand(rn, spare, mean, std_dev, has_spare)

use my_prec, only: wp => dp   ! for double precision constants

    real(wp), intent(out) :: rn, spare
    real(wp), intent(in) :: mean, std_dev
    integer :: seedx, seedy
    real(wp) :: x, y, r
    !real(wp), save :: spare
    logical, intent(inout) :: has_spare
    
        ! use a spare saved from a previous run if one exists
    if (has_spare) then
        has_spare = .FALSE.
        !norm_rand = mean + (std_dev * spare)
        rn = mean + (std_dev * spare)
        return
    else
        r = 1.0_wp
        do while ( r >= 1.0_wp )
            ! generate random number pair between 0 and 1
            call random_number(x)
            
            call random_number(y)
            
            ! normalise random numbers to be in square of side-length = R
            x = (x * 2.0_wp) - 1.0_wp
            y = (y * 2.0_wp) - 1.0_wp
            r = x*x + y*y
        end do

        ! calculate the co-efficient to multiply random numbers x and y
        ! by to achieve normal distribution
        r = sqrt((-2.0_wp * log(r)) / r)

        rn = mean + (std_dev * x * r)
        spare = y * r
        has_spare = .TRUE.
        return
    end if
    
    return
end subroutine 

!  ###################################################################

!  Return a random sample from a gamma distribution

recursive function rand_gamma(shapek, scalet) result(ans)

use my_prec, only: wp => dp   ! for double precision constants

real(wp) :: shapek,scalet,u,w,d,c,x,xsq,g,mean,std_dev,spare
logical, save :: has_spare

if (shapek <= 0.0_wp) then
    write(*,*) "Shape parameter must be positive"
end if

if (scalet <= 0.0_wp) then
    write(*,*) "Scale parameter must be positive"
end if

!    ## Implementation based on "A Simple Method for Generating Gamma Variables"
!    ## by George Marsaglia and Wai Wan Tsang.  
!    ## ACM Transactions on Mathematical Software
!    ## Vol 26, No 3, September 2000, pages 363-372.

if (shapek >= 1.0_wp) then
   d = shapek - 1.0_wp/3.0_wp
   c = 1.0_wp/(9.0_wp*d)**0.5
   do while (.TRUE.)
   mean = 0.0_wp
   std_dev = 1.0_wp
   has_spare = .FALSE.
   call norm_rand(x, spare, mean, std_dev, has_spare)
       v = 1.0_wp + c*x
       do while (v <= 0.0_wp) 
          call norm_rand(x, spare, mean, std_dev, has_spare)
          v = 1.0_wp + c*x
       end do
       v = v*v*v
       call random_number(u) 
       xsq = x*x
       if ((u < 1.0_wp -.0331_wp*xsq*xsq) .or. (log(u) < 0.5_wp*xsq + d*(1.0_wp - v + log(v))) )then
         ans=scalet*d*v
         return 
       end if
   end do
else
   g = rand_gamma(shapek+1.0_wp, 1.0_wp)
   call random_number(w)
   ans=scalet*g*(w)**(1.0_wp/shapek)
   return 
end if
end function

! ## return a random sample from a beta distribution
!
function rand_beta(a, b) result(ans)

use my_prec, only: wp => dp   ! for double precision constants

real(wp) :: a,b,ans,u,v

if ((a <= 0.0_wp) .or. (b <= 0.0_wp)) then
   write(*,*) "Beta parameters must be positive"
end if
    
!    ## There are more efficient methods for generating beta samples.
!    ## However such methods are a little more efficient and much more complicated.
!    ## For an explanation of why the following method works, see
!    ## http://www.johndcook.com/distribution_chart.html#gamma_beta

u = rand_gamma(a, 1.0_wp)
v = rand_gamma(b, 1.0_wp)
ans = u / (u + v)
end function!

! ## return a random sample from a triangular distribution with parameters a,b,c

function rand_trian(a,b,c) result(ans)

use my_prec, only:  wp => dp ! for double precission constants

real(wp) :: a,b,c,u,f,ans

if ((a > b) .or. (c > b) .or. (c < a)) then
   write(*,*) "Triangular parameter are wrong"
end if

f = (c - a)/(b - a)

call random_number(u)

if (u > 0.0_wp .and. u < f) then
   ans = a + sqrt(u*(b - a)*(c - a))
end if
if (u >= f .and. u < 1.0_wp) then
   ans = b - sqrt((1.0_wp - u)*(b - a)*(b - a))
end if

end function

! ## return a random sample from uniform distribution with parameters a,b

function rand_unif(a,b) result(ans)

use my_prec, only: wp => dp !for double precission constants

real(wp) :: a,b,y

call random_number(y)

ans = a + y * (b - a)
end function

!! # This subroutine is only for the rk.f95 program
!! # in the SIR model

subroutine randomcoefc(c0,c1,c2,c3,c4,c5,mean,std_dev,au,bu,al,be,at,ct,bt,Rg)

use my_prec, only: i4b,wp => dp ! for double precission constants

real(wp), intent(out) :: c0,c1,c2,c3,c4,c5
real(wp), dimension(6), intent(in)  :: mean,std_dev,au,bu,al,be,at,ct,bt
integer(i4b),  intent(in) :: Rg
real(wp), save :: spare
logical, save :: has_spare

if (Rg == 1) then           !  Normal distribution
    has_spare = .FALSE.
    call norm_rand(c0, spare, mean(1), std_dev(1), has_spare)
    call norm_rand(c1, spare, mean(2), std_dev(2), has_spare)
    call norm_rand(c2, spare, mean(3), std_dev(3), has_spare)
    call norm_rand(c3, spare, mean(4), std_dev(4), has_spare)
    call norm_rand(c4, spare, mean(5), std_dev(5), has_spare)
    call norm_rand(c5, spare, mean(6), std_dev(6), has_spare)
elseif (Rg == 2) then       ! Uniform distribution
    c0 = rand_unif(au(1),bu(1))
    c1 = rand_unif(au(2),bu(2))
    c2 = rand_unif(au(3),bu(3))
    c3 = rand_unif(au(4),bu(4))
    c4 = rand_unif(au(5),bu(5))
    c5 = rand_unif(au(6),bu(6))
elseif (Rg == 3) then      ! Beta distribution
    c0 = rand_beta(al(1), be(1)) + 0.5_wp
    c1 = rand_beta(al(2), be(2)) + 0.5_wp
    c2 = rand_beta(al(3), be(3)) + 0.5_wp
    c3 = rand_beta(al(4), be(4)) + 0.5_wp
    c4 = rand_beta(al(5), be(5)) + 0.5_wp
    c5 = rand_beta(al(6), be(6)) + 0.5_wp
elseif (Rg == 4) then     ! Triangular distribution
    c0 = rand_trian(at(1),bt(1),ct(1))
    c1 = rand_trian(at(2),bt(2),ct(2))
    c3 = rand_trian(at(3),bt(3),ct(3))
    c4 = rand_trian(at(4),bt(4),ct(4))
    c5 = rand_trian(at(5),bt(5),ct(5))
    c6 = rand_trian(at(6),bt(6),ct(6))
endif
return
end subroutine

end module

