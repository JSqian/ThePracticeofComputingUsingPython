x = "acegikmoqsuwy"
y = "+bdfhjlnprtvxz"
z = ""
for i in range(len(x)):
    z += x[i]
    z += y[i+1]
print z
