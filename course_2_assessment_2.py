#At the halfway point during the Rio Olympics, the United States had 70 medals, Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and Germany had 17 medals. Create a dictionary assigned to the variable medal_count with the country names as the keys and the number of medals the country had as each key’s value.
medal_count = {"United States": 70, "Great Britain": 38, "China": 45 ,"Russia":30, "Germany": 17}

#Given the dictionary swimmers, add an additional key-value pair to the dictionary with "Phelps" as the key and the integer 23 as the value. Do not rewrite the entire dictionary.

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4,"Phelps":23}

#Add the string “hockey” as a key to the dictionary sports_periods and assign it the value of 3. Do not rewrite the entire dictionary.

sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2,'hockey':3}

#The dictionary golds contains information about how many gold medals each country won in the 2016 Olympics. But today, Spain won 2 more gold medals. Update golds to reflect this information.

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds['Spain'] = 21

#Create a list of the countries that are in the dictionary golds, and assign that list to the variable name countries. Do not hard code this.

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = []
for i in golds:
    countries.append(i)

#Provided is the dictionary, medal_count, which lists countries and their respective medal count at the halfway point in the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value for "Belarus" to the variable belarus. Do not hardcode this.

medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}

belarus = medal_count['Belarus']


print(belarus)

#The dictionary total_golds contains the total number of gold medals that countries have won over the course of history. Use dictionary mechanics to find the number of golds Chile has won, and assign that number to the variable name chile_golds. Do not hard code this!

total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}
total_golds['Chile']
chile_golds = total_golds['Chile']
print(chile_golds)

#Provided is a dictionary called US_medals which has the first 70 metals that the United States has won in 2016, and in which category they have won it in. Using dictionary mechanics, assign the value of the key "Fencing" to a variable fencing_value. Remember, do not hard code this.

US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}
US_medals["Fencing"]
fencing_value = US_medals["Fencing"]
print(fencing_value)
