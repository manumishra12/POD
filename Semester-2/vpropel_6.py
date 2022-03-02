#Print the Pattern
'''
Given the value of ‘n’ write a C program to print a special rectangular pattern with dots and starts. 
When the value of n is 5 the rectangle looks as below:

. . . . * . . . .

. . . * . * . . .

. . * . . . * . .

. * . . . . . * .

* . . . . . . . *

Input Format

First line contains the value of ‘n’

Output Format

Print the pattern appropriate to the value of ‘n’

Dots and stars are separated by one space and each row in the pattern is separated only by a new line character.

'''

#Taking n input
n=int(input())

#printing 1st part
print('. '*(n-1)+'*'+' .'*(n-1))

#Printing the 2d part
for i in range(1,n):
    for j in range(0,n-i-1):
        print(".",end=" ")
        
    #Printing 3rd part    
    print("*",end=" ")   
    
    #printing 4th part
    print('. '*(2*i-1), end='')
    
    #printing 5th part
    print('*', end='')
    
    #printing the 6th part
    print(" ."*(n-i-1))