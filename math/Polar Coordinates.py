# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
def polar_coordinates(z):
    r=abs(z)
    p=cmath.phase(z)
    return r, p
if __name__=='__main__':
    z=complex(input().strip())
    r, p= polar_coordinates(z)
    print(r)
    print(p)
    
