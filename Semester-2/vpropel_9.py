#Find Color of Chair
'''
In a game the participants are made to sit on chairs of three colors Green, Orange, Blue in a big
hall. A number of pair of six chairs are arranged opposite to each other and numbered as shown
in the following image. In the image each pair of six chairs are separated by a gap that is chairs
with number 1 to 12 is a pair, 13 to 24 is a pair and so on.
The first chair is Green, second chair is Orange third chair is Blue in color, fourth is Blue, fifth is
Orange and sixth is Green and then the colors of chairs are reversed so that color of chairs on
opposite sides are same. The numbering of chairs are increasing from left to right in the first
pair and is decreasing from left to right in the second pair. In this game a participant is called
and given a chair number, ‘x’. He has to find the number of the chair opposite to ‘x’ and also
find the color of ‘x’. For example, when ‘x’ is 30, print 31 and Green when ‘x’ is 46 print 39 and
Blue.
Input Format
First line contains the chair number, ‘x’
Output Format
First line contain the chair ‘y’ number opposite to ‘x’
Next line contain the color of chair ‘y’ (Green or Orange or Blue)

'''

x=int(input())
arr0=[1,2,3,4,5,6]
arr=[12,11,10,9,8,7]
arr2=[13,14,15,16,17,18]
col=['Green','Orange','Blue','Blue','Orange','Green']
if x%6==0:
 print(x+1)
 print('Green')
else:
 y=x
 x=(x%6+6)
 if (y//6)%2!=0:
    print(-x+arr0[arr.index(x)]+y)
 else:
    print(-x+arr2[arr.index(x)]+y)
 print(col[arr.index(x)])