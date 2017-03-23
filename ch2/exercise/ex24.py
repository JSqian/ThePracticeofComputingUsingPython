for i in range(1,1000000):
    pl4 = (i % 10 == i % 10000 / 1000 and i % 100 / 10 == i % 1000 / 100)
    if pl4:
        distance = i + 1
        pl5 = (distance % 10 == distance % 100000 / 10000 and distance % 100 / 10 == distance % 10000 / 1000)
        if pl5:
            #print 'pl5',distance
            distance = i + 2
            pm4 = (distance % 100 / 10 == distance % 100000 / 10000 \
                      and distance % 1000 / 100 == distance % 10000 / 1000)
            if pm4:
                #print 'pm4',distance
                distance = distance + 3
                p6 = (distance % 10 == distance / 100000 \
                      and distance % 100 / 10 == distance % 100000 / 10000 \
                      and distance % 1000 / 100 == distance % 10000 / 1000)
                if p6:
                    #print 'p6',distance
                    print 'origin',distance - 5
            else:
                continue
        else:
            continue
    else:
        continue
