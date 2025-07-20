name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
experience = int(input("შეიყვანეთ გამოცდილება (წლებში): "))


if age > 22 and experience > 2:
    print("Hired")
elif age > 25 and experience > 1:
    print("Hired")
elif age > 20 and experience > 3:
    print("Hired")
elif name.lower() == "გურამ":
    print("Hired")
else:
    print("Not hired")


# 1. ვქმნით ლისთს რიცხვებით
numbers = [5, 3, 8, 2, 5]

#2 . append() - ამატებს ახალ რიცხვს ბოლოში
numbers.append(10)
print(numbers)  # [5, 3, 8, 2, 5, 10]

# 3. remove() - შლის მითითებულ რიცხვს (პირველს თუ რამდენიმეა)
numbers.remove(5)
print(numbers)  # [3, 8, 2, 5, 10]

# 4. reverse() - შებრუნება (უკუღმა აკეთებს ლისთს)
numbers.reverse()
print(numbers)  # [99, 8, 5, 3, 2]

# len()  ითვლის რამდენი ელემენტია ლისთში
print("ელემენტების რაოდენობა:", len(numbers))  

# sum()  ჯამს გამოჰყავს (ყველა რიცხვი ერთად)
print("რიცხვების ჯამი:", sum(numbers))  

# max()  პოულობს ყველაზე დიდ რიცხვს
print("ყველაზე დიდი რიცხვი:", max(numbers))  

# min()  პოულობს ყველაზე პატარა რიცხვს
print("ყველაზე პატარა რიცხვი:", min(numbers))  
