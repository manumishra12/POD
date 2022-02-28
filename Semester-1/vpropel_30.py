#Cicular Game
'''
There are N students in a class. In games period they are made to stand in a circle 
and each one of them is given a unique random number, r. Here r1 is the random number 
assigned for the first student, r2 is the number assigned for the second student and so on. 
In this game, for all students except those at first and last positions the winning condition is , 
if the student is at position ‘i’ then he has won the game if ri-1 < ri < ri+1. For the first student 
to win the game, the winning condition is rn<r1<r2. For the last student to win the game, winning condition is rn-1<rn<r1.

For example, if there are six students and they are assigned numbers 90, 25, 37, 28, 73, 84 then 
the numbers satisfying the conditions are 73, 84 and children winning the game are at positions 5 and 6.

If no one has won the game then print None. If there are six students and the numbers assigned are 
35, 25, 37, 28, 84 and 73 then the output of the code should be None.

Input Format
First line contains the number of students in the class, n
Next n lines contain the numbers assigned for the children in order

Output Format
Print the position of the children who has won the game

Note :Position of the children are 1 to n
'''

#<--- MANU --->
n,l,o=int(input()),[],[]

for i in range(1,n+1):
    m=int(input())
    l.append(m)

if l[-1]<l[0]<l[1]:
    o.append(l.index(l[0])+1)
    
elif l[-2]<l[-1]<l[0]:
    o.append(l.index(l[-1])+1)

for i,j in enumerate(l):
    if (i+1 < len(l) and i - 1 >= 0):
        p = (l[i-1])
        c = (j)
        n = (l[i+1])

        if p<c<n:
            o.append(l.index(c)+1)

for i in sorted(o):
    print(i)
if o==[]:
    print("None")


#<---Khushi --->
n=int(input())
r=[int(input()) for i in range(n)]
w=[]
for i in range(1,n-1):
    if r[i-1]<r[i]<r[i+1]:
        w.append(i+1)
if r[-1]<r[0]<r[1]: w.append(1)
if r[-2]<r[-1]<r[0]: w.append(n)
if len(w)==0: print("None")
for i in sorted(w):
    print(i)