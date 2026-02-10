
sum = 0
while True:
    num = int(input("რიცხვი (0 = გაჩერება): "))
    if num == 0:
        break
    sum += num
print("ჯამი:", sum)


day = input("კვირის დღე (ინგლისურად): ")

if day == "Monday":
    print("კვირის დასაწყისი")
elif day in ["Tuesday", "Wednesday", "Thursday"]:
    print("შუა კვირა")
elif day == "Friday":
    print("შაბათ-კვირას ახლოს")
elif day in ["Saturday", "Sunday"]:
    print("შაბათ-კვირა!")
else:
    print("არასწორი დღეა")


word = input("სიტყვა: ")
count = 0
for letter in word:
    if letter in "აეიოუ":
        count += 1
print("ხმოვნების რაოდენობა:", count)
