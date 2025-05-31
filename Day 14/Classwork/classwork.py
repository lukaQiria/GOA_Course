# მომხმარებლისგან ვიღებთ ასაკს, გამოცდილებას და სიმაღლეს
age = int(input("შეიყვანე ასაკი: "))
experience = int(input("შეიყვანე სამუშაო გამოცდილება (წლებში): "))
height = int(input("შეიყვანე სიმაღლე (სმ-ში): "))

# ვამოწმებთ პირობებს და ვინახავთ isHired ცვლადში
isHired = age >= 18 and experience >= 2 and height >= 175

# ვბეჭდავთ შედეგს
print("You are hired:", isHired)



# მომხმარებლისგან ვიღებთ საჭირო მონაცემებს
people = int(input("შეიყვანე ადამიანების რაოდენობა: "))
time = int(input("შეიყვანე დრო (1-დან 12-მდე): "))
turn_on = input("ჩართულია? (true ან false): ").lower()=="true"

# ვამოწმებთ პირობებს და ვინახავთ lightsOn ცვლადში
lightsOn = people > 2 and time >= 7 and turn_on

# ვბეჭდავთ შედეგს
print("lightsOn:", lightsOn)

