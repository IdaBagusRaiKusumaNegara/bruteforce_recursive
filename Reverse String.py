def reverseString(s):

    if len(s) == 1:
        print(s[0])
        exit()
    else:

        print(s[-1], end="")

        return reverseString(s.replace(s, s[:-1]))


s = input("masukan Kata : ")
reverseString(s)
