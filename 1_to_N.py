# Python program to print numbers from 1 to n

n = int(input("Please Enter any Number: "))

print("The List of Natural Numbers from 1", "to", n) 

for i in range(1, n + 1):
    print (i, end = '  ')
    
    
# Output
# Please Enter any Number: 5
# The List of Natural Numbers from 1 to 5
# 1  2  3  4  5  
