import time
start = time.time()


def towerOfHanoi(n, source, target, helper):

    if n >= 1:

        towerOfHanoi(n-1, source, helper, target)

        print(f"pindahkan disk {n} dari {source} ke {target}")

        towerOfHanoi(n-1, helper, target, source)


n = 4
towerOfHanoi(n, "Source", "Target", "Helper")

print(f"\n runtime {time.time() - start}")
