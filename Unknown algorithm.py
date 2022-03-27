
def Permutasi(a, n):

    if n == 0:
        print("nilai A : 0")

    if n == 1:
        print(a)
        return

    for i in range(n):
        Permutasi(a, n-1)

        if n % 2 == 1:

            a[0], a[n-1] = a[n-1], a[0]
        else:

            a[i], a[n-1] = a[n-1], a[i]


a = [1, 2, 3]
n = len(a)
Permutasi(a, n)
