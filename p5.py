#Fibonacci Series
fib_series = [0,1]
i=2
a=fib_series[0]
b=fib_series[1]
n=int(input("Enter the limit :"))
while i<n :
    c=a+b
    fib_series.append(c)
    a=b
    b=c
    i=i+1
print("Fibonacci series")
print(fib_series)
