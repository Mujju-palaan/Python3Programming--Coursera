top_three = []
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
def g(k,d):
    return d[k]
ks = medals.keys()
top_three = sorted(ks,key=lambda x : g(x,medals),reverse = True)[:3]   


###########################

most_needed = []
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
def g(k,d):
    return d[k]
ks = groceries.keys()
most_needed = sorted(ks, key=lambda x:g(x,groceries), reverse = True)
print(most_needed)

####################################

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

def last_four(x):
    
    return (str(x)[-4:])
last_four(ids)

sorted_ids = sorted(ids, key=lambda x: str(x)[-4:])
print(sorted_ids)

#########################################