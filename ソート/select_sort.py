data = [9, 3, 7, 1, 4, 2, 5, 8, 6, 0]
print(data, "元のデータ")

for i in range(0, 9):
    min = i
    for j in range(i+1, 10):
        if data[j] < data[min]:
            min = j
    data[i], data[min] = data[min], data[i]
    
print(data, "ソート後のデータ")
