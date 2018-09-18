s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinker = ('a','e','i','o', 'u')
for word in s:
    if word in klinker:
        print(word)
