#Taking input
n=int(input())

#Creating a list to store no of doubts
Doubts=[]

#Counting
count=0

#Usinf for loop to get number of doubts
for i in range(n):
    doubts=int(input())
    Doubts.append(doubts)
    

#Choice of teacheer to solve no. of doubts

que=int(input())

#List to store valuue
o=[0]*n

#Creating logic to calculate time
while sum(Doubts):
    for i in range(n):
        
        count+=que
        Doubts[i]-=que
        
        if Doubts[i]<0:
            count+=Doubts[i]
            Doubts[i]=0
            
        if Doubts[i]==0 and not o[i]:
            o[i]=count
        
        if sum(Doubts)==0:
            break

#RESULT        
for i in o:
    print(i)