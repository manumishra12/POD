#Secondary Factorial
'''
Factorial of an integer n,  denoted as n! is defined as the product of the first n natural numbers

n! = 1*2*3....*n
1! = 1 and
0! = 1

We define a secondary factorial of a number n, denoted by SF(n), as follows:

SF(n) = 1*3*5*....*n, if n is odd and

SF(n) = 2*4*6*....*n if n is even

If n is an odd number, SF(n) is defined as the product of all the odd numbers, 
starting from 1, till the number n. SF(5)= 1*3*5= 15.

If n is an even number, SF(n) is defined as the product of all the even numbers, 
starting from 2, till the number n. SF(6)=2*4*6=48.

Given a number k, write a code to compute SF(n), where k = n!.  
For the given number k, If there is no number n such that  n! = k then, your code should print -1.

Illstration

Given k = 24 then 24 = 4! and
SF(4) = 2* 4 = 8.

Given k=25, there is no number n such that 25 = n!, 
then the out put should be -1.

Given k=6, 6=3!. 
SF(3)=1*3=3

Input Format
First line contains an integer, k

Ouput Format
Print SF(n) if there exists a number  n, such that k = n! and -1 otherwise
'''


k=int(input())
l=[]
o=[]
u=[] 

if (k==1) or (k==0):
    print("1")
else:    
    for i in range(1,k):
        u.append(i)

total=1
t=-1

for i in range(1, len(u)):
    total *= u[i]
    if total==k:
        n=(i+1)
                
        if n%2==0:
            for j in range(2,n+1):
                if j%2==0:
                    l.append(j)
            t=1
            for m in l:
                t=t*m
              
        else:
            for x in range(1,n+1):
                if x%2!=0:
                    o.append(x)
            t=1
            for y  in o:
                t=t*y       
print(t)  


