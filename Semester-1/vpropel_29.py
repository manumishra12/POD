#No Common Fraction (NCF)
'''
If a and b are positive integers, b not equal to 1, b>a, the representation a/b is called as a fraction of a to b.
If the factors common to both a and b is the number 1 only, (That is, the greatest common divisor of a and b is 1), 
we call a/b as the `No Common Fraction’ (NCF).

Given an integer `upper’ called upper limit, an integer `lower’ called the lower limit, we can write the NCFs 
that can be formed with the integers that lie between u and l (lower<= integer <= upper) . For example, if upper=3, lower=1, 
the NCFs that can be formed, are 1/2, 1/3, 2/3.

Given the integers upper and lower, Write the pseudocode and the subsequent code to compute the number of NCFs that 
can be formed with the given limits and print the number of pairs whose a/b value is greater than 0.2 and less than 0.6.

For example, if upper = 3 and lower = 1 then there are two NCFs 1/3 and 1/2, satisfying the conditions.

Input Format
First line contains the value of upper limit, upper
Second line contains the value of lower limit, lower

Output Format
Print the count of NCFs that can be formed with the given upper and lower limits
'''

#////////////////////////////////////////////////////////////

#<---MANU--->

#<--- Without hcf test case --->
upper,lower=int(input()),int(input())
o=[]
for i in range(lower,upper):
    for j in range(i+1,upper+1):
        if i!=j and j!=1:
            if (i/j) not in o:
                o.append((i/j))
c=0
for i in o:
    if 0.2<i<0.6:
        c+=1
print(c)  


#<--- With hcf test case --->
upper,lower,o=int(input()),int(input()),[]

if upper > lower:
    s= lower
else:
    s= upper
for i in range(1, s+1):
    if((upper % i == 0) and (lower % i == 0)):
        hcf = i
    
if hcf==1:
    print(1)
else:
    for i in range(lower,upper):
        for j in range(i+1,upper+1):
            if i!=j and j!=1:
                if (i/j) not in o:
                    o.append((i/j))
    c=0
    for i in o:
        if 0.2<i<0.6:
            c+=1
    print(c)
#////////////////////////////////////////////////////////////

#<---Khushi Edited--->
upper,lower=int(input()),int(input())
x=[]
for i in range(lower,upper):
    for j in range(i+1,upper+1):
        if i!=j and j!=1 and 0.2<i/j<0.6 and [i/j] not in x:
            x.append([i/j])
print(len(x))