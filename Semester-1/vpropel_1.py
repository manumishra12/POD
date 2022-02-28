#Picnic Group
'''
Picnic Groups
After solving yesterday's problem, Adarsh is now enjoying and decides to go on
a picnic.
All of his classmates are divided into 'N' groups. Cabs are going to be ordered
depending on the number of students.
The classmates which belong to the same group have to travel together. Each
cab can carry at most 4 students. What is the minimum
the number of cabs needed if all classmates of each group should travel in the
same car and one car can take more than one group.
Input Format:
The first line of the input contains N, the number of groups
The second line contains N space-separated integers, ith of them denoting the
size of the ith group
Output Format:
Print one line containing a single integer denoting the minimum number of
cabs required.
Constraints:
1 <= N <= 50
1 <= size of each group <= 4
Examples:
Input:
5
1 2 4 3 3
Output:
4
one cab will be required by the group having 4 people
one cab will be required by a group of people having 3 and 1 person(s).
Now we are left with two groups of size 2 and 3.
Both of them cannot travel in the same cab because the size will become 3 + 2 =
5, and since each cab can carry only 4 people at max
we will be requiring a new cab for both these groups. Hence the minimum
number is 4

'''

n=int(input())
arr= list(map(int,input().split()))
print("")

s=0
for i in arr:
    print(i)
    print("")
    s+=i
print(s)
print("")

q = divmod(s, 4)
print(q)

if q[1]==0:
    print("Number of cars= ",q[0])

elif q[1]!=0:
    print("Numbers of cars=",q[0]+1)

else:
    print("Invalid format")    


##############################################################
#CORRECT CODE
n=int(input())
b=0
import math
l,y,t,z,s=[],[],[],[],0
k=input()
k=k.split()
for i in k:
    l.append(int(i))
d=l.count(4)
s=s+d
for i in l:
    if i==3:
        y.append(i)
    elif i==1:
        t.append(i)
    elif i==2:
        z.append(i)
m=(2*len(z))//4
s=s+m
h=len(z)-(2*m)
z=[]
for i in range(0,h):
    z.append(2)
v=min(len(y),len(t))
s+=v
if v==0:
    k=max(len(y),len(t))
    if k==len(t):
        y=t
else:
    if len(y)==v:
        for i in range(v):
            t.pop()
            b=5
    elif len(t)==v:
        for i in range(v):
            y.pop()
            b=6
    if b==5:
        y=t
if len(y)>0:
    if y[0]==3:
        s=s+len(y)
        s=s+h
    else:
        u=((len(z)+len(y))/4)
        if u-int(u)==0:
            s+=u
        else:
            s+=int(u)+1
    print(int(s))
else:
    u=(len(z)/2)
    if u==0:
        print(int(s))
    else:
        if u-int(u)==0:
            s+=u
        else:
            s+=u+1
        print(int(s))
