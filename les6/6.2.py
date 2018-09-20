def berekensom(lijst):
    som = 0
    for getal in lijst:
        som = som + getal
    return(som)

getallenlijst=[1, 2, 3]
print(berekensom(getallenlijst))
