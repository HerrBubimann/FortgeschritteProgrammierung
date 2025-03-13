end_preis = 711

for a in range(1,end_preis):
    for b in range(a, end_preis-a):
        for c in range(b, end_preis-a-b):
            d = end_preis - a - b - c

            if a*b*c*d == 711000000:
                print(a,b,c,d)
                break