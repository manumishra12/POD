#Scanner
'''
A scanner reads an image with 10 lines. Each line is given a value from 0 to 9 based on their width as follows:

0.2 to 0.7 – 0

0.71 to 1.2 - 1

1.21 to 1.7 – 2

1.71 to 2.2 – 3

2.21 to 2.7 – 4

2.71 to 3.2 – 5

3.21 to 3.7 – 6

3.71 to 4.2 – 7

4.21 to 4.7 – 8

4.71 to 5.2 – 9

There may be errors in the value read by the scanner. So always a check digit is given to verify the correctness.
Check digit of the number scanned can be calculated as modulus of sum of product of the digits and weightage by 10.
Weightage of the digits are given alternatively 1 and 3 from left to right. Given width of the ten lines scanned by
the scanner and the cehck digit, write a code to check if it is read correctly. Print Yes if it is correct and No otherwise.

For example,

Width of lines - 4.2 3.5 2.8 1.5 2.2 4.7 5.0 0.5 1.1 3.8

Digits - 7 6 5 2 3 8 9 0 1 7

Weightage - 1 3 1 3 1 3 1 3 1 3

Sum of product digits and the corressponding weights is 94. Modulus of 10 will be 4.
 Check digit is 4 so print Yes

Note:

1) In C language, real constants are internally considered as double values, i.e. 2.5 is a double value
2) So if you want to check if a floating point variable f is equal to 0.5 then you have to write if (f==0.5f), 
add a suffix f to force 0.5 to be float value. Otherwise there will be inconsistency in the output

Input format
First line contains the width of the ten lines read by the scanner
Next line contains the check digit

Output Format
Print Yes if check digit calculated and given are same and No otherwise'''


#Takimg inputs and empty lists
arr=input().split(" ")
n=int(input())
l,o,r=[],[],[]

#Checking and Appending Digit Values
for i in arr:
    if 0.2<float(i)<0.7:
        l.append(0)
        
    elif 0.71<=float(i)<1.2:
        l.append(1)
        
    elif 1.21<=float(i)<=1.7:
        l.append(2)
    
    elif 1.71<=float(i)<=2.2:
        l.append(3)
    
    elif 2.21<=float(i)<=2.7:
        l.append(4)
        
    elif 2.71<=float(i)<=3.2:
        l.append(5)
        
    elif 3.21<=float(i)<=3.7:
        l.append(6)
        
    elif 3.71<=float(i)<=4.2:
        l.append(7)
        
    elif 4.21<=float(i)<=4.7:
        l.append(8)
        
    elif 4.71<=float(i)<=5.2:
        l.append(9)

#Creating Series of 1 and 3
for i in range(round(len(l)/2)):
    if len(l)!=len(o):
        o.append(1)
        o.append(3)

#Multiplying Two lists
for i in range(len(l)):
    r.append(l[i] * o[i])

#Getting the Sum
sum=(int(sum(r)))
check=(sum%10)

#Checking  the check Digit
if n==check:
    print("Yes")
else:
    print("No")


#<--- Khushi --->
arr,y=list(map(float,input().split())),[1,3]*5

for i in range(10): 
    arr[i]=int((arr[i]-0.21)*2)*y[i]

if (sum(arr)%10)==int(input()): 
    print("Yes"); exit(0)
print("No")

        