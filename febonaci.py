#this code gives you fibonacci sequence

def febSequ(n):
    ''' It takes n input and give n-th Term of Fiboonacci sequence'''
    if n<=1:
        return 1
    else:
        return(febSequ(n-1) + febSequ(n-2))

for i in range(10):
    print(febSequ(i))