import time
start = time.time()


def towerOfHanoi(n, source, helper, target):
    print(f"tower of hanoi {n, source, helper, target} ")
    if n > 0:

        towerOfHanoi(n - 1, source, target, helper)

        if source[0]:
            disk = source[0].pop()
            print(
                f"pindahkan disk {str(disk)} dari {source[1]}  ke {target[1]}")
            target[0].append(disk)

        towerOfHanoi(n - 1, helper, source, target)


n = [1, 2, 3]
source = (n, "source")
target = ([], "target")
helper = ([], "helper")
towerOfHanoi(len(source[0]), source, helper, target)

print(source, helper, target)

print(f"\n runtime {time.time() - start}")
