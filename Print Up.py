def printUp(n):

    if n >= 0:
        printUp(n - 1)
        print(n)

    if n >= 0:
        return " "


a = int(input("Masukan Angka : "))

print(printUp(a))
