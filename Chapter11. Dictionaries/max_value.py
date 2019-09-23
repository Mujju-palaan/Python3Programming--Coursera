product = "iphone and android phones"
lett_d = {}
for char in product:
    if char not in lett_d:
        lett_d[char] = 0
    lett_d[char] = lett_d[char] +1
print(lett_d)
ks = lett_d.keys()

max_value = list(ks)[0]
for k in ks:
    print(k)
    if lett_d[k] > lett_d[max_value]:
        max_value = k
print(max_value)