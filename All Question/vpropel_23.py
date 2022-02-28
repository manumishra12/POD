#Shortest typing time
'''
There are two typists : A and B. Typist A, who is experienced, can type a word in ‘a’ seconds 
and the Typist B can type a word in ‘b’ seconds. Given a job of typing ‘n’ number of words in a web portal, 
Write an algorithm and the subsequent code to compute the total time taken by both the typists to type the given ‘n’ 
words if they divide the job in such a manner as to complete the job in the shortest time. Assume that all the words 
have equal number of letterst and both the typists type simultaneously.

For example, if 15 words are to be typed, typist A can type a word in 2 seconds and typist B can type a word in 3 seconds 
then the minimum time required to type 15 words is 18 seconds.

Input Format
First line contains, total number of words in the job : n
Second line contains the time taken by typist A to type a word : a seconds
Third line contains the time taken by Typist B to type a word : b seconds

Output Format
Minimum time required to type the words (in seconds)
'''
import math            
n=int(input())
a=int(input())
b=int(input())

#Taking LCM, Using formula (1/T= 1/t1 + 1/t2)
if a > b:
  greater = a
else:
  greater = b

while(True):
  if((greater % a == 0) and (greater % b == 0)):
      lcm = greater
      break
  greater += 1
  
p=((lcm/(a+b))*n)

#Ceil give the smallest integer greater than or equal to entered value.
print(math.ceil(p))
