items = ["ვაშლი", "ბანანი", "მსხალი", "ატამი", "ყურძენი"]

# ინდექსები:
# "ვაშლი" - ინდექსი 0
# "ბანანი" - ინდექსი 1
# "მსხალი" - ინდექსი 2
# "ატამი" - ინდექსი 3
# "ყურძენი" - ინდექსი 4

print(items[0])   

print(items[-1])  


result = []


for i in range(10):
    num = int(input("შეიყვანეთ რიცხვი: "))
    if num % 2 == 0:  
        result.append(num)

print("ლუწი რიცხვები:", result)

names = ["Gurami", "Gio", "Andria", "Mariami", "Dato"]

for name in names:
    if len(name) > 5:
        print(name)
