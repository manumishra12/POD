#Count Move Up and Down
'''
Ramu makes a travel to one his office in a hilly region by his car. 
Given the height of his current location above sea level every few minutes after he starts the travel, 
write a code to check the number of up moves and down moves. First move is always up move.

For example, if 12 points are given as follows 45, 60, 82, 72, 65, 32, 53, 84, 103, 110, 89, 95 
then there are 3 up moves and 2 down moves as shown below:

 
Input Format
First line contains the number of current locations of Ramu, n
Next line contains ‘n’ height of locations separated by a space

Output Format
Print the number of Up moves and number of Down moves separated by a space

'''
n=int(input())
l=[]
x=list(map(int, input().split()))
for i in range(len(x)-1):
    if x[i]>x[i+1]:
        l.append('down')
    elif x[i]<x[i+1]:
        l.append('up')
print(l)
u,d=0,0
s=l[0]
if s=='up':
    u+=1
elif s=='down':
    d+=1
for i in range(len(l)):
    if l[i]=='up' and l[i]!=s:
        u+=1
    elif l[i]=='down' and l[i]!=s:
        d+=1
    s=l[i]
print(u,d)