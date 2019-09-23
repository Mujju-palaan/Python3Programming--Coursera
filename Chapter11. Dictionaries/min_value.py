placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d ={}
for char in placement:
    if char not in d:
        d[char] = 0
    d[char] = d[char] + 1
print(d)
ks = d.keys()
min_value = list(ks)[0]

for k in ks:
    if d[k] < min_value:
        min_value = k
print("key " + min_value + " has the min_value value, " + str(d[min_value]))
       