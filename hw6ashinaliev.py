numbers = [2, 7, 11, 15]


def summary(alist, targetnum):
    for i, j in enumerate(alist):
        k = i + 1
        if alist[k:].count(targetnum - j) > 0:
            for n in range(alist[k:].count(targetnum - j)):
                b = alist.index(targetnum - j, k)
                print(i, b)
                k = b + 1


summary(numbers, 9)