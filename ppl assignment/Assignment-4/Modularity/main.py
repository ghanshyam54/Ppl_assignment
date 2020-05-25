import fibo

n = int(input("Enter a number : "))

print("Fibonacci series upto",n,":")
fibo.fib(n)

l = fibo.fib2(n)

print("List of Fibonacci series upto",n,":")
print(l)