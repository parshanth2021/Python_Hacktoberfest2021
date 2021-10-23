rows = int(input("Enter the number of rows = "))     
print("Triangular Pattern ")    

for i in range(0, rows):
    al= 65                                          
    for j in range(rows, i, -1):                     
        print(end = ' ')                             
    for k in range(0, i + 1):                       
        print('%c' %(al + k), end = ' ')
    print()                                          
