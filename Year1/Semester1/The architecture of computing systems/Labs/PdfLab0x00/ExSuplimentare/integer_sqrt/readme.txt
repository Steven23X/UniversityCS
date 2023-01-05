rsqrt din Quake III se bazeaza pe Newton's Method dar mai exact pe Heron's Method 
==>(?digit-by-digit?)

==> x_(n+1) = (x_n + N // x_n) // 2 


fyl2x ? pentru log2x?(nu stiu)



x0=pow(2,(log2n/2)+1) (pt Heron)

dc doar 9 cifre?

//program

if (n<=1) return n

n0=n/2
n1=(n0+n/n0)/2

while(n1<n0)
{
  n0=n1
  n1=(n0+n/n0)/2
}
return n0

