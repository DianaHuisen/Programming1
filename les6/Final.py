def standaardprijs(afstandKM):
    if afstandKM > 50:
        bedrag=15+afstandKM*0.60
    else:
        if afstandKM<0:
            afstandKM==0
        bedrag = afstandKM*0.80
    return bedrag

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == 'zaterdag' or weekendrit =='zondag':
        print("True")
        if leeftijd < 12 or leeftijd > 64:
            print(standaardprijs(afstandKM) - (standaardprijs(afstandKM) / 100 * 35))
        else:
            print(standaardprijs(afstandKM)-(standaardprijs(afstandKM) / 100 * 40))
    else:
        print("False")
        if leeftijd <12 or leeftijd >64:
            print(standaardprijs(afstandKM)-(standaardprijs(afstandKM)/100*30))
        else:
            print(standaardprijs(afstandKM))
    return


afstandKM=eval(input("Hoeveel kilometer is de reis: "))
print(standaardprijs(afstandKM))
leeftijd=24
weekendrit=input("op welke dag ga je (schrijf zonder hoofdletter): ")
ritprijs(leeftijd, weekendrit, afstandKM)
