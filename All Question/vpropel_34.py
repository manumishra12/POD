r=int(input())
c=int(input())
l=[]
p=[]
o=0
g=10000



for i in range(r):
    n=list(map(int,input().split()))
    p.append(n)
print(p)    


for i in range(c):
    for j in range(r):
        if p[j][i]<g:
            o=p[j][i]
    l.append(o)
    
    
for i in p:
    for j in range(c):
        print(i[j]+max(i)+l[j],end=' ')
    print()