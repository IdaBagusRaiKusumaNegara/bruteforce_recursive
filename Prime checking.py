def cekBilPrima(n, i=2):

    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True

    return cekBilPrima(n, i + 1)


a = int(input("Masukan Angka : "))

if (cekBilPrima(a)):
    print("%i Bilangan Prima" % a)
else:
    print("%i Tidak Bilangan Prima" % a)
