#Fibanocci Increment Mixed String
'''
Increment mixed string is an operation which operates on two strings S1 and S2 of same length to generate a new string S3.
The letters in odd position of S3 is one more than the corressponding letter in S1 and
the letters in even position of S3 is one more than the corressponding letter in S2.
For example, if S1 = ‘amey’ and S2 = ‘dhft’ then S3 = ‘bifu’. For letter ‘z’, letter ‘a’ is one more than it.

Fibanocci increment mixed string is operation which operates on the last two strings in the series.
Given two strings, S1 and S2 write a code to generate the nth element using Fibanocci increment mixed string operation.
The given strings S1 and S2 are the first two elements in the Fibanocci increment mixed string series.
Third element in the series is found by applying increment mixed string operation for first two elements.
 
If S1 = ‘amey’ and S2 = ‘dhft’ then the first five elements in the series are as follows:

amey
dhft
bifu
ejgv
ckgw

#Input Format
First line contains the string S1
Next line contains the string S2
Next line contains the value of n

#Output Format
Print the nth element in the Fibanocci increment mixed string series
'''

# Program to display the Fibonacci sequence up to n-th term
n = int(input("How many terms? "))

# first two terms
s1=input("string1= ")
s2=input("string2= ")

count= 0
l,p,o,e,q,w,h=[],[],[],[],[],[],""

while count < n:
       l,p,o,e,q,w,h=[],[],[],[],[],[],""   
       print(s1)
       

       for m in s1:
           value = ord(m)
           if value >122:
            value=ord("a")

           l.append(value)
           print(value)    
       print(l)
       print("")
       o=l[1::2]
       print(o)
       print("") 


       print(s2)
       for j in s2:
           value2 = ord(j)
           if value2 >122:
            value2=ord("a")


           p.append(value2)
           print(value2)       
             
       print(p)
       print("")
       e=p[::2]  
       print(e)
       print("")


       q.append(o[0]+1)
       q.append(e[0]+1)
       q.append(o[1]+1)
       q.append(e[1]+1)
       print(q)

       print("")

       for ele in q:
            y = chr(ele) 
            w.append(y)
            
       print(w)
       h=h.join(w)
       print(h)
       print("")
       print("")

       print(s1)
       print(s2)
       print(h)

# update values
       f = s2
       s2 = h
       s1 = f
       count += 1
       

 