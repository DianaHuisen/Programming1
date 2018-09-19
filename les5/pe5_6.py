s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinker = ('aeiou')
for word in s:
    if word in klinker:
        print(word)
