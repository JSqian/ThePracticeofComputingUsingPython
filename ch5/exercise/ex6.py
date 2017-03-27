def getPrice(price,isMember):
    if isMember:
        price = price * 0.85
    else:
        price = price * 0.95
