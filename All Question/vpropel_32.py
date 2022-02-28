#Sliding Friction
'''Sliding friction is contact force generated when an object moves over a surface. 
Few wooden blocks of different heights are put in a room. An experiment is to be carried over 
in which a ball has to roll up and down over a steps like structure. The experimenter 
wishes to find the maximum size of the steps structure present in the wooden block and 
he prefers to have a step up operation from left to right. Given the height of the 
wooden blocks arranged in the room, write a code to find the starting and ending p
osition of the wooden blocks that can form a steps structure. When more than one 
steps structure of same maximum size is available consider the one that comes first from left to right.

Example 1
Heights = 5 6 3 5 7 8 9 1 2
Longest step up structure from left to right is
3 5 7 8 9
and positions are from 3 to 7

Heights = 12 13 1 5 4 7 8 10 10 11
Longest step up structure from left to right is
4 7 8 10
and positions are from 5 to 8

Input Format
First line contains the number of wooden blocks, n
Next line contains the height of the wooden blocks separated by a space

Output Format
Print the starting and ending positions of the wooden blocks that can 
form a step structure of maximum size separated by a space'''

#<-- Refer Longest Increasing Subarray in Common Codes -->
n=int(input())
arr=list(map(int,input().split()))
m ,l ,maxIndex = 1,1,0
  
for i in range(1, n) :
    if (arr[i] > arr[i-1]) :
        l =l + 1
    else :
        if (m < l)  :
            m = l
            maxIndex = i - m
        l = 1   
     
if (m < l) :
    m = l
    maxIndex = n - m
    
stop  = m+maxIndex
start = 1+maxIndex    
    
print(start,stop)    



