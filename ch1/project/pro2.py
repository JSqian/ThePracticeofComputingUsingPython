import datetime

d1 = datetime.datetime(2009,9,25)
d2 = datetime.datetime.now()
hours = (d2-d1).days * 24
distanceFT = 166.37 * 10 ** 8

distanceNowFT = distanceFT + hours * 38241
distanceNowKM = distanceNowFT * 1.609344
distanceNowAU = distanceNowFT / 92955887.6

timeHour = distanceNowKM * 1000 / 299792458 / 3600
