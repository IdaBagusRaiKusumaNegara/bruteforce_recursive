def multiplication(a, b):
    if a < b:
        return multiplication(b, a)

    elif b != 0:
        return (a + multiplication(a, b - 1))

    else:
        return 0


a = int(input("Masukan Nilai a : "))
b = int(input("Masukan Nilai b : "))

print(multiplication(a, b))
