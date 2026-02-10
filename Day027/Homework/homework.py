# append() -> სიაში ამატებს ელემენტს ბოლოში
#.insert(index, value) -> სიაში ამატებს ახალ ელემენტს მითითებულ პოზიციაზე
#.pop() -> შლის სიიდან ელემენტს (ნაგულისხმევად ბოლოში არსებულს) და აბრუნებს მას

my_list = [10, 20, 30, 40, 50]
print("სიის სიგრძე არის:", len(my_list)) 

numbers = [] 
for i in range(5):  
    num = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(num)  
print("თქვენი სია:", numbers)

colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop()  
print("განახლებული სია:", colors)

animals = ["dog", "cat", "elephant", "lion"]
animals.insert(1, "monkey")  
print("განახლებული სია:", animals)

students = []  
for i in range(3):
    name = input("შეიყვანეთ სტუდენტის სახელი: ")
    students.append(name)  
students.insert(0, "Teacher")  
students.pop()  
print("სიის სიგრძე:", len(students))
print("საბოლოო სია:", students)
