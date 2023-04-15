import random

def sift_down(data, p, n):
    c = p * 2 + 1
    while c < n:
        if c < n - 1 and data[c] < data[c + 1]:
            c += 1
        if data[p] >= data[c]:
            break
        data[p], data[c] = data[c], data[p]
        p = c
        c = p * 2 + 1

def build_max_heap(data):
    n = len(data)
    for i in range((n - 1) // 2, -1, -1):
        sift_down(data, i, n)
    return data

def heap_sort(data):
    build_max_heap(data)
    d = len(data) - 1
    while d > 0:
        data[0], data[d] = data[d], data[0]
        sift_down(data, 0, d)
        d = d - 1
    return data

n = 12
data = [0] * n
for i in range(n):
    data[i] = random.randint(1, 99)

print(data, "元のデータ")
sorted_data = heap_sort(data)
print(sorted_data, "ソート後のデータ")
