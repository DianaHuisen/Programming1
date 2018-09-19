age = int(input("Geef je leeftijd: "))
passport = input("Do you have a Dutch passport (yes/no):")
if age >= 18 and passport == 'yes':
    print("Congratulations, you are allowed to vote in the Netherlands.")
else:
    print("Sorry, you're not allowed to vote. \n"
          "You either don't have a Dutch passport, you're younger than 18 years old, or both.")
