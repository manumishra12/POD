#Factor Indexed Numbers
'''
A number ‘n’ in a list at index ‘i’ (human indexing) is said to be a factor indexed number if ‘i’ is a factor ‘n’. 
Given two lists of numbers l1 and l2 form a list l3 by inserting factor indexed numbers of l1 and l2. 
Intialize index to ‘0’ visit elements of l1 and l2 at index, 
if one of them is factored indexed insert and increment index and go till end of the list. 
If both of them are factor indexed then insert element of l1 at index and then element of l2 at index and increment index. 
If end of one of the list is reached then add elements of other list to l3 if they are factor indexed. After construction of l3, 
Print the numbers which continues to be factor indexed in l3.

For example, 
if l1 contains 15, 12, 17, 32, 26, 42 
and l2 contains 45, 34, 64, 80 
then l3 will be 15, 45, 12, 34, 32, 80, 42 
then print 15, 12, 42.

Input Format
First line contains the number of elements in l1, n1
Next ‘n1’ lines contain the elements of l1
Next line contains the number of elements in l2, n2
Next ‘n2’ lines contain the elements of l2

Output Format
Print good numbers of l3 one number in a line

'''
l1,l2,l3=[],[],[]

n1 =int(input("enter n1 "))
for i in range(n1):
    a=int(input("enter list values "))
    l1.append(a)

n2 =int(input("enter n2 "))
for i in range(n2):
    b=int(input("enter list 2 values "))
    l2.append(b)  

for j in range(max(n1,n1)):
    if j< len(l1):
        if l1[j]%(j+1)==0:
            l3.append(l1[j])

    if j< len(l2):
        if l2[j]%(j+1)==0:
            l3.append(l2[j])   

for m in range(len(l3)):
    if l3[i]%(m+1)==0:
        print(l3[m])                       

