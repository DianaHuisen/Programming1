def wijzig(lijst):
    if (lijst == ['a', 'b', 'c']):
        lijst.clear()
        lijst.append('d')
        lijst.append('e')
        lijst.append('f')


lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)

#list['d','e','f'] werkt niet, omdat de variabele onder de def staat, en in de def ziet hij het als iets anders.
#string werkt niet, omdat je een string niet kan/mag aanpassen.
#je moet het kunnen veranderen, anders werkt het niet.