import random 
import time
        
n = 5000
cnt = 0
DATA = [0]*n
data = [0]*n
for i in range(n):
    DATA[i] = random.randint(1, 5000)
    data[i] = DATA[i]


print("-------------------")
print("ヒープソート開始")
ts=time.time()

for i in range((n-1)//2, -1, -1):
    p = i
    c = p * 2 + 1
    while c < n:
        if c < n-1 and data[c] < data[c+1]:
            c += 1
        if data[p] >= data[c]:
            break
        data[p], data[c] = data[c], data[p]
        p = c
        c = p * 2 + 1       

# 値を切りヒープを再構成する
d = n - 1
while d > 0:
    data[0], data[d] = data[d], data[0]
    p = 0 
    c = p*2 + 1
    while c < d:
        if c < d-1 and data[c] < data[c+1]:
            c += 1
        if data[p] >= data[c]:
            break
        data[p], data[c] = data[c], data[p]
        cnt += 1
        p = c
        c = p*2 + 1
    d = d - 1

te = time.time()
print("ヒープソート終了")
print("入れ替え回数", cnt)
print("要した時間", te-ts, "秒")

print(data)

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
