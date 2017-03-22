r = 6.378 * 10 ** 6
G = 6.67300 * 10 ** (-11)
m1 = 5.9742 * 10 ** 24
X = float(raw_input("Enter the weight in kg:"))
F = G*m1*X / r**2
g = F / X
print g
