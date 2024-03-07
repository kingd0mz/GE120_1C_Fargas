"""
GE 120: IINtro to OOP GEomatic Application
Dominic Fagas Jr.
2015-42069
"""

# dms = -0.00

# dms = dms % 360
# # dms = float(input("Enter a number: "))

# # Kunin si degree part
# degree = int(dms)

# # Kunin si minutes
# minutes = int((dms - degree) * 60)

# seconds = round((dms - degree - minutes/60) * 3600,2)

# print(f"DMS: {degree}-{minutes}-{seconds}")

# MUST BE A STRING INPUT
dms = "118-25-14.48"
degrees, minutes, seconds = dms.split("-")

dd = int(degrees) + (int(minutes)/60) + (float(seconds)/3600)

print("ETO YUNG VALUE:", round(dd,6))
