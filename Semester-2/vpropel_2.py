#Simple String Subtraction
'''
Given two strings S1 and S2, write a C program to perform simple string subtraction. 
Simple string subtraction does character subtraction from last to first characters of the strings. 
Letters in English alphabet are given forward and reverse positions 1 to 26. 
In forward position letter ‘a’ is at 1 and ‘z’ is at 26. In reverse position letter ‘z’ is at 1 and letter ‘a’ is at 26. 
Character subtraction of character C2 from character C1 (C1 - C2) works as follows:

(i) If C1 and C2 are same then C1 – C2 = C1

(ii) Otherwise C1 – C2 = C3 where C3 is the character in forward position ‘d’ 
where d = i – j, i and j are the foward position of C1 and C2 respectively and d>0 and

C1 – C2 = C3 where C3 is the character in reverse position ‘d’ 
where d = positive value of (i – j), i and j are the foward position of C1 and C2 respectively and d<0.

For example, if S1 is elephant and S2 is apple then S3 is eleoslbo and if S1 is ball and S2 is cell then S3 is zwll

Boundary Conditions
The input will be given such that length of S1 is always greater than or equal to length of S2 and all characters in S1 and S2 are in lower case.

Input Format
First line contains the string S1
Next line contains the string S2

Output Format
String obtained after simple string subtraction
'''


#TAKING INPUTS
a = input()
b = input()

#Defining Alphabets and reversed alphabets and its values 
Alphabets = "abcdefghijklmnopqrstuvwxyz"
Rev_Alpha = Alphabets[::-1]

#Crating empty list
l,o = [],[]

#Taking index value of alphabet for string 1
for i in a:
    if i in Alphabets:
        x=int(Alphabets.index(i))
        l.append(x)


#Taking index value of alphabets for string 2
for i in b:
    if i in Alphabets:
        x=int(Alphabets.index(i))
        o.append(x)

#Removing extra elements if length is unequal
rem=[]
if len(l)>len(o):
    while True:
        i=l.pop(0)

        #Appending charcter that are dropped
        rem.append(Alphabets[i])
        if len(l)==len(o):
            break


#Subtraction of the two string index
list1 = l
list2 = o
diff = []

zip_object = zip(list1, list2)
for i, j in zip_object:
    diff.append(i-j)


#Appending the changed string after subtraction
new=[]
for i in range(len(diff)):
    
    if int(diff[i])>0:
        new.append(Alphabets[diff[i]-1])
        
    elif int(diff[i])<0:
        new.append(Rev_Alpha[-diff[i]-1])
        
    else:
        new.append(b[i])

#RESULT
#Joing both the string together
print(''.join(rem)+ "".join(new))