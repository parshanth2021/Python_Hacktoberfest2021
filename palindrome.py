# Give size of list
n=int(input())

# Give list of numbers having size n
l=list(map(int,input().strip().split(' ')))

print("Palindrome numbers are:")
# check through the list to check 
# number is palindrome or not
for i in l:
    num=str(i)
    if("".join(reversed(num))==num):
        print(i)