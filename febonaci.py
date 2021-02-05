#this code gives you fibonacci sequence

def febSequ(n):
    ''' It takes n input and give n-th Term of Fiboonacci sequence'''
    if n<=1:
        return 1
    else:
        return(febSequ(n-1) + febSequ(n-2))
n=int(input("Enter number of term: "))
# This takes input as an string and convert into int as given input:
for i in range(n):
    print(febSequ(i), end='  ')