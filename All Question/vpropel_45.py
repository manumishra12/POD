#Count Beeps
'''Binary representation of a number ‘n’ are written on a circle which is divided into ‘m’ segments. 

Here the number of bits required to represent ‘n’ is ‘m’. 
A needle is fixed on the top of this circle and the circle rotates in clockwise direction for every ten seconds 
till a complete rotation is made that is the number of rotations is equal to ‘m-1’. 
Let the segment pointed by needle be ‘p’. A beep sound is made when the decimal equivalent of the 
binary digits is even when read from the next segment to the right of ‘p’ to the segment ‘p’.

Given the binary digits written on the segment from the segment next to ‘p’ to ‘p’, 
write a C program to find the number of times beep sound will be made. For example, if the initial 
configuration of binary string given is ‘1001101’ then the binary strings obtained by rotation are

1001101

1100110

0110011

1011001

1101100

0110110

0011011

The binary strings 1100110, 1101100 and 0110110 are even when decimal equivalent is taken. 
Hence beep sound will be made three times.

Boundary Conditions
Length of the binary string < 25

Input Format       
First line contains the binary representation of the number ‘n’

Output Format
Print the number of times beep sound will be made'''




# //////////////------ SOLUTION -----------\\\\\\\\\\\\\\\ #

#Taking Input
n=input()

#Converting to list
l=list(n)

#Creating count variable as 0
count=0

#Creating function to convert Binary to DECIMAL
def check(l):
    value=0
    for i in range(len(l)):
        digit = l.pop()
        if digit == '1':
        	value = value + pow(2, i)

     #Checking for whether Decimal number is even or not    	
    if (value%2==0):
        return True
    else:
        return False

#Updating the vale of n to give the rotation
for i in range(len(l)):
    n = n[-1] + n[:len(l)-1]
    if (check(list(n))==True):
        count+=1
        
#Printing the Result        
print(count)



