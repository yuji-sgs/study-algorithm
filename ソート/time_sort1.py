import random 
import time

def quick_sort(left, right):
    global cnt
    i = left
    j = right
    p = data[(left + right) // 2]
    while True:
        while data[i] < p:
            i = i + 1
        while data[j] > p:
            j = j - 1
        if i >= j:
            break
        data[i], data[j] = data[j], data[i]
        cnt += 1
        i = i + 1
        j = j - 1
    if left < i-1:
        quick_sort(left, i-1)
    if right > j+1:
        quick_sort(j+1, right)
        
n = 5000
DATA = [0]*n
data = [0]*n
for i in range(n):
    DATA[i] = random.randint(1, 99)
    data[i] = DATA[i]
    
cnt = 0
print("-------------------")
print("クイックソート開始")
ts=time.time()
quick_sort(0, n-1)
te = time.time()
print("クイックソート終了")
print("入れ替え回数", cnt)
print("要した時間", te-ts, "秒")

for i in range(n):
    data[i] = DATA[i]
cnt = 0
print("-------------------")
print("バブルソート開始")
ts=time.time()
for i in range(n-1):
    for j in range(n-1, i, -1):
        if data[j-1] > data[j]:
            data[j], data[j-1] = data[j-1], data[j]
            cnt += 1
te = time.time()
print("バブルソート終了")
print("入れ替え回数", cnt)
print("要した時間", te-ts, "秒")
