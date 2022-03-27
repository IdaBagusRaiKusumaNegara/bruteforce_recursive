# 2 c. Print Down
def printdown(n):
    print(n)
    if n == 0:
        return " "

    return printdown(n - 1)


a = int(input("Masukan Angka : "))

print(printdown(a))
