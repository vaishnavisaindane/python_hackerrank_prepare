# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab=int(input())
bc=int(input())
ac=math.sqrt(ab**2+bc**2)
theta=math.acos(bc/ac)
print(str(round(math.degrees(theta)))+"\N{DEGREE SIGN}")
