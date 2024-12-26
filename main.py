arr = []
for n in range(1, 30 + 1):
    n_2 = bin(n)[2:]
    if n % 2 == 0:
        n_2 = '10' + n_2 + '1'
    else:
        n_2 = '10' + n_2 + '0111'
    r = int(n_2, 2)
    arr.append(r)
print(max(arr))