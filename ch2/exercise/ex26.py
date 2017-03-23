for D in range(10):
    for E in range(10):
        Y = (D + E) % 10
        bitAdd1 = (D + E) / 10
        for N in range(10):
            for R in range(10):
                if ((N+R+bitAdd1)%10) != E:
                    continue
                else:
                    bitAdd2 = (N + R+ bitAdd1)/10
                    for O in range(10):
                        if((E + O + bitAdd2)%10)  != N:
                            continue
                        else:
                            bitAdd3 = (E+O+ bitAdd2)/10
                            for S in range(10):
                                for M in range(10):
                                    if((S+M+bitAdd3)%10) != O:
                                        continue
                                    elif (S+M+bitAdd3)/10 != M:
                                        continue
                                    else:
                                        print "S:",S,"E:",E,
                                        print "N:",N,"D:",D,
                                        print "M:",M,"O:",O,
                                        print "R:",R,"Y:",Y
                                            
