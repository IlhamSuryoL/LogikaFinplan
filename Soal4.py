def angka_kecil(data):
    data = set(data)  
    n = len(data) + 1  #
    for i in range(2, n+1):
        if i not in data:
            return i
    return n



input1 = [5, 2, 8, 4, 3, 10]
output1 = angka_kecil(input1)
print(output1)

input2 = [2, 3, 4, 6]
output2 = angka_kecil(input2)
print(output2)

input3 = [8, 6, 7, 12]
output3 = angka_kecil(input3)
print(output3)
