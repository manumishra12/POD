#Shuffled Rows Matrix
'''
A matrix is said to be shuffled rows matrix if the elements in all the rows are same but may be in a shuffled order.
 Given nxm matrix, write a C program to check if the matrix is a Shuffled Rows Matrix. 
 For example, a 3x4 matrix M as shown below is a Shuffled rows matrix:

4 5 1 7
7 1 4 5
1 7 5 4

Whereas the matrix M1 shown below is not a Shuffled row matrix

3 1 2
3 3 1
1 2 3

Boundary conditions
0<r,c<20

Input Format
First line contains the number of rows in the matrix, m
Next line contains the number of columns in the matrix, n
Next ‘m’ lines contain the elements in each row of the matrix separated by a space

Output Format
Print Shuffled Row Martix or Not Shuffled Row Martix

'''


#Taking input
m=int(input())
n=int(input())

#list to store values
matrix=[]

#Taking matrix usinf for loop
for i in range(m):
    a=(sorted(input().split()))
    matrix.append(a)

#Creating another list to join
o=[]
for i in matrix:
    o.append("".join(i))

#checking whether lal elements are equal or not
count=0

for i in sorted(o):
    if i==o[0]:
        count+=1

#Result
if len(o)==count:
    print("Shuffled Row Matrix")
else:
    print("Not Shuffled Row Matrix")