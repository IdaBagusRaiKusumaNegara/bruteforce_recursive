def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


a = int(input("Masukan Nilai Fibonacci ke : "))

print(fibonacci(a))
