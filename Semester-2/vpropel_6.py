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