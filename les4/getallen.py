cijferICOR = 6
cijferPROG = 8
cijferCSN = 7

gemiddelde = (cijferICOR+cijferPROG+cijferCSN)/3
beloning = (gemiddelde*30*3)
overzicht = 'mijn cijfer is (gemiddeld een ' + str(gemiddelde)+') leveren een beloning van €' +str(beloning)+' op!'
print(overzicht)