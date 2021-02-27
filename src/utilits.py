def fibonacci_seq(fib1: int = 0, fib2: int = 1):
    f1 = fib1
    f2 = fib2
    while 1:
        yield f1
        f1, f2 = f2, f1 + f2
