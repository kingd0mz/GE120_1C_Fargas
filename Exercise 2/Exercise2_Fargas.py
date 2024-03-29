"""
GE 120: Itro to OOP Geomatic Application
Dominic Fagas Jr.
2015-42069

Exercise 2
"""
# CREATE A SENTINEL CONTROLLED LOOP
counter = 1
lines = []

while True:
    print()
    print("LINE NO.", counter)

    bobo_magtype = False
    while not(bobo_magtype):
        distance = input("Distance: ")
        if bobo_magtype:
            print("BOBO KA MAGTYPE")
            continue
        if not(bobo_magtype):
            break
    azimuth = input("Azimuth from the South: ")

    if "-" in azimuth: #in DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
    else:
        azimuth = float(azimuth)%360

    if azimuth > 0 and azimuth < 90:
        bearing = 'S {: ^10} W'.format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {: ^10} W'.format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = 'N {: ^10} E'.format(azimuth-180)
    elif azimuth > 270 and azimuth < 360:
        bearing = 'S {: ^10} E'.format(360 - azimuth)
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    else:
        bearing = "EWAN KO"

    line = (counter, distance, bearing) #create tuple of the line
    lines.append(line)

    # ASK FOR INPUT
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print(lines)

print("\n\n")
print('{: ^10} {: ^10} {: ^10}'.format("LINE NO.", "DISTANCE", "BEARING"))
for line in lines:
    print('{: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2]))

print("----END----")
