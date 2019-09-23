olympians = [("John Aalberg", 31, "Cross Country Skiing"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv","w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
