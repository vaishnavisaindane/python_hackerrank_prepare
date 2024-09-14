#solution 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
data=namedtuple('data',input().split())
total_marks=0
for i in range(n):
    total_marks += int(data(*input().split()).MARKS)
print('{:.2f}'.format(total_marks/n))






https://youtu.be/npEECAsseyE?si=0mXUBlqnplTUQSNc
#solution 2
from collections import namedtuple
n=int(input())
fields=input().split()
total_marks=0
for i in range(n):
    students=namedtuple('student','fields')
    MARKS,CLASS,NAME,ID=input().split()
    student= students(MARKS,CLASS,NAME,ID)
    total_marks+=student.MARKS
print('{:.2f}'.format(total_marks/n))
