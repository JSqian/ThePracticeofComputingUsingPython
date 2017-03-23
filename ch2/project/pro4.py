ifContinue = 'y'
while ifContinue == 'y':
    A = int(raw_input("Enter integer A: "))
    B = int(raw_input("Enter integer B: "))
    product = 0
    while B > 0:
        if B % 2 == 1:
            product += A
        B /= 2
        A *= 2
    print product
    ifContinue = raw_input("Do you want to calculate another product?Enter y for yes:")
