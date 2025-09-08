grades = []

for i in range(5):
    number = int(input("Please enter a grade 1–10: "))
    if number < 1 or number > 10:
        print("Error")
    else:
        grades.append(number)

print(grades)


numbers = [5, 12, 7, 9, 20, 33, 41, 56, 78, 91, 100, 121, 150]

evens = numbers[::2]


odds = numbers[1::2]

reversed_step2 = numbers[::-2]

print("ლუწი ინდექსები:", evens)
print("კენტი ინდექსები:", odds)
print("შებრუნებული ყოველ მეორე:", reversed_step2)


text = "პითონის სლაისინგი მაგარია"

word1 = text[8:17]

word2 = text[:7] + " " + text[18:]

word3 = text[::-2]

word4 = text[:text.index(" ")]  

