#Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse = True)

#Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)

#The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)


#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.
top_three = []
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
def g(k,d):
    return d[k]
ks = medals.keys()
top_three = sorted(ks,key=lambda x : g(x,medals),reverse = True)[:3]   

#We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.
most_needed = []
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
def g(k,d):
    return d[k]
ks = groceries.keys()
most_needed = sorted(ks, key=lambda x:g(x,groceries), reverse = True)

#Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

def last_four(x):
    
    return (str(x)[-4:])
last_four(ids)

sorted_ids = sorted(ids, key=last_four )
print(sorted_ids)

#$Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key=lambda x: str(x)[-4:])

#
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key = lambda x: x[1])
print(lambda_sort)