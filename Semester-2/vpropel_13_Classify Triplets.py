#Classify Triplets
'''
Given two integers ‘l’ and ‘u’, write a C program to identify the triplet (a, b, c) 
where a <= b <= c and a, b, c >= l and a, b, c <= u, that are Exactly Pythagorean, 
Very Close to Pythagorean or Close to Pythagorean. A triplet (a, b, c) is said to be 
Exactly Pythagorean if c2 – a2+b2 = 0, Very Close to Pythagorean if c2 – a2+b2 = +1 or -1 
and Close to Pythagorean if c2 – a2+b2 = +2 or -2. For example, if l = 5 and u = 20 then the program should print

5 5 7 Very Close to Pythagorean
5 11 12 Close to Pythagorean
5 12 13 Exactly Pythagorean
5 13 14 Close to Pythagorean
6 8 10 Exactly Pythagorean
6 17 18 Very Close to Pythagorean
6 18 19 Very Close to Pythagorean
7 7 10 Close to Pythagorean
7 11 13 Very Close to Pythagorean
8 9 12 Very Close to Pythagorean
8 15 17 Exactly Pythagorean
9 12 15 Exactly Pythagorean
10 15 18 Very Close to Pythagorean
11 13 17 Very Close to Pythagorean
12 12 17 Very Close to Pythagorean
12 16 20 Exactly Pythagorean

Input Format
First line contains the value of ‘l’
Next line contains the value of ‘u’

Output Format
Print all the triplets that are Exactly, Very Close to or Close to Pythagorean triplets

'''

#SOLUTION

#Taking input
l,u = int(input()), int(input())

#Nested loop to create triplets
for a in range(l,u+1):
    for b in range(l,u+1):
        for c in range(l,u+1):
            
            #Checking the given conditions
            if ((a <= b <=c) and (a and b and c >= l) and (a and b and c <= u)):
                
                #Storing the exponential value in variable
                A = pow(a,2); B = pow(b,2); C = pow(c,2)
                
                #Checking & printing result on specified condition
                if (C - (A + B)==0) : 
                    print(a,b,c,"Exactly Pythagorean")

                elif (C - ( A + B ))== 1 or (C - ( A + B ) == -1) : 
                    print(a,b,c,"Very Close to Pythagorean")

                elif (C - ( A + B )) == 2 or (C - (A + B )== -2) : 
                    print(a,b,c,"Close to Pythagorean")
        
