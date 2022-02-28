#Special Numbers in different bases
'''
A number in a base is said to be a special number if it is equal to the sum of its
own digits each raised to the power of the number of digits. A number in base
‘b’ can have digits from 0 to b-1. By default the numbers used by humans is to
base 10 and called as decimal number system. A number ‘n’ from decimal
number system can be converted to any base ‘b’ by repeated division of ‘n’ by ‘b’
and writing reminder of each division in reverse order. For example, number 24
is converted to base 3 as shown below:
Given a number ‘n’ and a base ‘b’, write a code to check if n is a special with
respect to base ‘b’. If any digit of ‘n’ is greater than ‘b-1’ then print ‘Invalid’

---------------
Example 1:
Input
122
3
Output
Yes
Explanation
122 -> number of digits - 3
1^3 + 2^3 + 2^3 -> 17
17 to base 10 is 122 to base 3

--------------
Example 2:
Input
433
5
Output
Yes

---------------
Example 3:
Input
121
3
Output
No

--------------
Example 4:
Input
125
3
Output
Invalid

Input Format
First line contains the number, n
Next line contains the base of the number,b
Output Format
Print Invalid or Yes or No
'''

def check_valid(num,b):
    #logic -> num ka every digit < b ->> True / False
    #extract every digit
    while num!=0: #ends when n=0
        rem = num%10
        if rem>=b:
            return False
        num = num//10
    return True

#########################################

def convert_to_decimal(num,b):
    decimal=0
    ulti_counting = 0
    while num!=0: #ends when n=0
        rem = num%10
        decimal = decimal + (b**ulti_counting)*rem
        ulti_counting+=1
        num = num//10
    return decimal

#########################################

def power(num):
    l = len(str(num))
    summ = 0
    while num!=0:
        rem = num%10
        summ = summ + (rem**l)
        num = num//10
    return summ

######---------Driver Code---------######

number = int(input())
base = int(input())
valid = check_valid(number,base)
if valid == True:
    if convert_to_decimal(number,base) == power(number):
        print('Yes')
    else:
        print('No')
else:
    print('Invalid')
