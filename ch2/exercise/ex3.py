N = int(raw_input("Enter the number of N:"))
C = N /29
if(C == 0):
    print N,"Ns"
else:
    N = N % 29
    G = C / 17
    if(G==0):
        print C,"Cs,",N,"Ns"
    else:
        C = C % 17
        print G,"Gs",C,"Cs",N,"Ns"
