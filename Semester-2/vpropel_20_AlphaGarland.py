#Alpha garland
'''
Given an alphanumeric string S, develop pseudocode and C code for printing the alpha 
garland by processing S character by character based on the following rules:

> If the current character is an alphabet, add it to the garland.
> If the current character is a number, then the garland is 
  extended by adding the alphabets present so far in the garland in reverse form and then its original form alternatively.
> The process is repeated till the end of the string.

For example, if the S= “ab3c1” ,then the garland is “ab baabba c cabbaabba”

Note: The white space in the garland is given for understanding the process. 
Actually the garland formed for this string is “abbaabbaccabbaabba”

Input Format
An alphanumeric string, S

Output Format
A string forming the alpha garland

'''

# ================  SOLUTION  ======================== #

#Taking In put
String,Previous,Final = input(), "", ""

for i in String:
    #Checking if numeric or alphabet
    if (i.isalpha()==True):
        #Adding to string if they are characters
        Previous += i
        Final += i
        
    else:
        #Addinf strings if they are numeric
        for j in range(1,(int(i)+1)):
            #Adding the elemnts
            if (j%2==0):
                Final +=Previous
                
            else:
                Final+=Previous[::-1]  
        #Updating        
        Previous = Final    
#Result        
print(Final)


#========== SHORT CODE =================#


String,Previous,Final = input(), "", ""
for i in String: 
    if (i.isalpha()==True): Previous += i;Final += i
    else:
        for j in range(1,(int(i)+1)):
            if (j%2==0): Final +=Previous     
            else: Final+=Previous[::-1]
        Previous = Final    
print(Final)