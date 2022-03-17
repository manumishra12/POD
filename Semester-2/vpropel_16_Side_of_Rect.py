#Sides of a Rectangle
'''
Given four points P1, P2, P3 and P4 check whether they can be corners of a 
rectangle with sides A, B, C and D respectively. The naming of the sides of 
the rectangle are shown as below.

For example, if P1 is (2, 12), P2 is (14, 12), 
P3 is (14, 22), P4 is (2, 22) then they can be 
corners A, B, C and D of a rectangle. Whereas 
the points P1 is (5, 12), P2 is (14, 12), P3 
is (14, 22), P4 is (2, 22) cannot be corners 
of a rectangle. Distance between any two points 
P1(x1, y1) and P2(x2, y2) shall be calculated 
using the formula:

Print Yes if the points P1, P2, P3 and P4 can be corners A, B, C and D of a rectangle respectively and No otherwise.

Input Format
First line contains the coordinates of point P1 separated by a space
Next line contains the coordinates of point P2 separated by a space
Next line contains the coordinates of point P3 separated by a space
Next line contains the coordinates of point P4 separated by a space

Output Format
Print Yes or No

'''

#SOLUTION

#TAKING INPUT FOR  POINTS
Points = [list(map(int,input().split())) for i in range(4)]

#ASSIGNING COORDINATES TO POINTS
x1,y1 = Points[0][0] , Points[0][1]
x2,y2 = Points[1][0] , Points[1][1]
x3,y3 = Points[2][0] , Points[2][1]
x4,y4 = Points[3][0] , Points[3][1]

#FORMULA : (((x1-x2)**2 + (y1-y2)**2))**(1/2)

#SIDES
AB = pow((pow((x1-x2),2) + pow((y1-y2),2)),(1/2))
BC = pow((pow((x3-x2),2) + pow((y3-y2),2)),(1/2))
CD = pow((pow((x3-x4),2) + pow((y3-y4),2)),(1/2))
DA = pow((pow((x1-x4),2) + pow((y1-y4),2)),(1/2))

#DIAGONALS
AC = pow((pow((x1-x3),2) + pow((y1-y3),2)),(1/2))
BD = pow((pow((x4-x2),2) + pow((y4-y2),2)),(1/2))


#RESULT
if ((AB == CD) and (BC == DA) and (AC == BD)):
    print("Yes")
else:
    print("No")
    
    