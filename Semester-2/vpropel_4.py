#Find Abundant Mineral
'''
Many minerals such as olivine, quartz, feldspar, mica, pyroxene and amphibole are found in rocks.
It has been observed that in Madhya Pradesh, only one of the mineral occurs abundantly. 
Here the mineral that occurs in maximum number of rocks is said to be abundant.
Given the details of minerals found in ‘n’ rocks write a C program to find out the mineral
that has occured maximum number of times. Print only the representation of the mineral that
has occurred maximum number of times. Each mineral is represented by one letter that is 
for example, olivine will be represented as o, quartz as q and so on. 
The minerals found in each rock is given as a string.

For example, given the details of minerals in four rocks as oqm, qfo, mpa and opf the
 representation of the mineral that has occurred abundantly is o.

Boundary Conditions
0<n<20
0<number of minerals<20

Input Format
First line contains the number of rocks, n
Next ‘n’ lines contain the details of minerals in each rock

Output Format
Print the representation of mineral that occur abundant

'''

#Taking nput
n=int(input())
minn, each_min, count = [],[],[]

#Using for loop for rock
for i in range(n):
    minerals=input()
    minn.append(minerals)

#Creating for lop for min
for i in minn:
    for j in i:
        each_min.append(j)
        
#Sorting       
each_min.sort()

#for loop to count occurence
for i in each_min:
    x=each_min.count(i)
    count.append(x)
    
#Taking index position   
index=count.index(max(count))   

#Result
print(each_min[index])