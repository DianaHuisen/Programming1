def hello(name):
    line = 'Welcome, '+name+', it is nice to meet you'
    print(line)

def vraag():
    naam = input('Wat is je naam: ')
    return (naam)
mijnnaam = vraag()
hello(mijnnaam)
