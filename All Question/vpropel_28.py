#Ordered-Containment of a String
'''
A String S2 is said to be order-contained in another string S1 if all the letters of S2 
is present in S1 and order of occurrence of letters of S2 in S1 is same as in S2. For example, 
elephant contains ant, hat but not tap.

Given two strings S1 and S2, write a code to Print ‘Yes’ if S2 is order-contained in S1 
and ‘No’ otherwise. All letters in the input will be lowercase in the given string with no spaces

Input Format
First line contains the string, S1
Second line contains the string, S2

Output Format
Print Yes if S2 is order-contained 
in S1 and Print No otherwise
'''


s1,s2,l = list(input()) ,list(input()) ,[]
for i in s2:
    for j in s1:
        if i==j:
            if s2.count(j)!=l.count(j):
                l.append(i)
                s1=s1[s1.index(i)+1:]
if l==s2:
    print("Yes")
else:
    print("No")         



#////////////////////////////////////////

#<----Rijul---->
s1=input()
s2=input()

a=len(s1) 
b=len(s2) 

j=0
i=0

while i<b and j<a:
    if s2[i]==s1[j]:
        i+=1
        j+=1
    else:
        j+=1
        
if i==b:
    print("Yes")
else:
    print('No')

#////////////////////////////////////////////

    