def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


#Main
n=int(input("Enter the number of terms for the fibonacci series:\t"))
for i in range(n):
    print(fib(i))

    
