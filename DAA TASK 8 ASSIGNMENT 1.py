
import time

def linear_search(a, key):
    for i, value in enumerate(a):
        if value == key:
            return i
    return -1

def binary_search(a, key):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == key:
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def hash_search(table, key):
    return table.get(key, -1)

sizes = [1000, 10000, 100000, 1000000]

print("Dataset | Linear(s) | Binary(s) | Hash(s)")

for n in sizes:
    records = list(range(1, n + 1))
    key = n

    start = time.perf_counter()
    r1 = linear_search(records, key)
    t1 = time.perf_counter() - start

    start = time.perf_counter()
    r2 = binary_search(records, key)
    t2 = time.perf_counter() - start

    table = {x: x for x in records}

    start = time.perf_counter()
    r3 = hash_search(table, key)
    t3 = time.perf_counter() - start

    print(n, "|", round(t1, 8), "|",
          round(t2, 8), "|", round(t3, 8))

    print("Results:", r1, r2, r3)
