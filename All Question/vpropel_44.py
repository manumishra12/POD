#Toggle Switch
'''
There are ‘n’ light bulbs lined up in a row in a long room. Each bulb is numbered consecutively 
from 1 to ‘n’ and each bulb is independently connected to a switch which are currently in off state. 
‘n’ people are lined up outside the entry door of the room. Every ‘ith’ person in the line enter 
the room and toggle the state of ‘ith’ switch and exit the room. Given the value of ‘n’ and an 
integer ‘m’, write a C program to find the state of ‘mth’ switch. Print ‘On’ if the switch will 
be in ‘On’ state print ‘Off’ otherwise. For example, if there are 10 switches then status of 5th 
switch will be Off after all ten people toggle the switches.

Input Format
First line contains the value of ‘n’
Next line contains the value of ‘m’

Output Format
Print the status of the ‘mth’ switch
'''

#TAKING INPUT
n=int(input())
m=int(input())

#CREATING COUNT TO COUNT THE FACTOR
count=0

#USING LOOP TO COUNT AND STATE THE STATE OG NULN
for i in range(1,m+1):
    if m%i==0:
        count+=1

#Checking if series /count is odd or even
#ODD = ON
#EVEN = OFF

if count%2==0:
    print("Off")
else:
    print("On")
    