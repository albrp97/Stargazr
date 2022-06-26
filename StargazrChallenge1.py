f = open("./datasets/P1big.txt")
datos = f.readlines()[1:]
Solutions = []

for dato in datos:  # todo Spark.map could be used here if dataset is big enough to parallelize it in clusters since each leaks are independents
    [P, F, G, I] = map(int, dato.split(" "))
    if G - P == F:
        Solutions.append(F)
    else:
        out = False
        F2 = F
        while (not out):
            if G - F2 - ((F2 - F) * I) == P:
                Solutions.append(F2)
                out = True
            else:
                F2 += 1

for i in Solutions:
    print(i)
