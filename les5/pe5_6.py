s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinker = ('aeiou')
for char in s:
    if char in klinker:
        print(char)
