percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []
for i in percent_rain:
    if i > 90:
        resps.append('Bring an umbrella.')
    elif i > 80:
        resps.append('Good for the flowers?')
    elif i > 50:
        resps.append('Watch out for clouds!')
    else:
        resps.append('Nice day!')
        
print(resps)

        
