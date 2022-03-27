def power(n, p):

    if p == 0:
        return 1

    return (n*power(n, p-1))


a = int(input("Masukan Nilai a : "))
b = int(input("Mas2ukan Nilai b : "))
print(power(a, b))
