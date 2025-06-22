total = 0
for i in range(1, 101):
    total += i

print("1-დან 100-მდე რიცხვების ჯამია:", total)


num = 1
while num <= 50:
    if num % 2 != 0:
        print(num)
    num += 1

total = 0
for i in range(10):
    number = int(input(f"{i+1}) შეიყვანე რიცხვი: "))
    total += number

print("შეყვანილი რიცხვების ჯამი:", total)


import random

secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:
    guess = int(input("გამოიცანი რიცხვი 1-დან 10-მდე "))
    if guess != secret_number:
        print("არასწორია სცადე თავიდან")

print("სწორია გილოცავ")


