import fibo
fibo.fib(1000)
fibo.fib2(100)
fibo.__name__


from fibo import fib, fib2
fib(100)

print(fibo.__name__)