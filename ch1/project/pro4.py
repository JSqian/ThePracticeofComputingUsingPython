
year = int(raw_input("Enter the year:"))
seconds = (year - 2009) * 365 * 24 * 3600
numMan = 307357870

numMan = numMan + seconds / 7 - seconds / 13 + seconds / 35
print numMan
