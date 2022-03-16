#Code Word Check
'''An agent ‘A’ comes to a secret place to collect some information, the information will be 
disclosed to him if he is able to find one of the code words of the group of agents from a 
given word ‘w’. All the code words are of length four. The agent ‘A’ will say the positions 
of four letters in ‘w’ that may form the code word. Write a C program to check if the letters 
in ‘w’ in the positions mentioned by ‘A’ is a code word. For example, if the valid code words 
are HEAR, BEAR, VEST, MONK and if ‘w’ is ‘RESEARCH’ and position mentioned by the agent 
is 8, 2, 5 and 6 then it is Valid. Position of letters in the word ‘w’ starts from 1. 
Print Valid if the word that can be formed by the positions mentioed by the agent ‘A’ is in 
the list of code words and print Invalid otherwise.

Input Format
First line contains the number of code words among the group of agents, n
Next ‘n’ lines contain the code words
Next line contains the word, ‘w’
Next four lines contain the position of the letters chosen by the agent ‘A’

Output Format
Print either Valid or Invalid'''


#SOLUTION

#Taking input
n = int(input())

#Creating list to store code words
l=[]

#For loop to take the input or code words
for i in range(n):
    cw = input()
    l.append(cw)
   
#Taking word as input
w = input()

#STORING POSITION
o = []

#Taking positions
for i in range(4):
    ind = int(input())
    o.append(w[ind-1])
  
#Joined the word
final = "".join(o)

#Check and result
if final in l:
    print("Valid")
else:
    print("Invalid")
    
#/////////////////////////////////////////////////////////////////////

#SHORT VERSION
n,l,o = int(input()),[],[]
for i in range(n):cw = input();l.append(cw)
w = input()
for i in range(4):ind = int(input());o.append(w[ind-1])
final = "".join(o)
if final in l:print("Valid")
else:print("Invalid")



