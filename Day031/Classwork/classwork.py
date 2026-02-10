# ფუნქციები ვიყენებთ იმისთვის რომ კოდი გავხადოთ უფრო მარტივი და მოწესრიგებული
# ფუნქცია საშუალებას გვაძლევს ერთხელ დავწეროთ კოდი და შემდეგ რამდენჯერაც გვინდა გამოვიყენოთ
# ასევე ფუნქციები გვეხმარება კოდის გასაგებად და ორგანიზებულად დაყოფაში


def average_of_three(a, b, c):
    
    total = a + b + c
    
    average = total / 3
    
    return average

print(average_of_three(10, 20, 30)) 



text = "Hello World"


print(text.upper())  


print(text.lower())  


print(text.replace("World", "Python"))  


print(text.split())  


text_with_spaces = "   Hello World   "
print(text_with_spaces.strip())  

# default value ფუნქციაში არის მნიშვნელობა რომელიც ავტომატურად გამოიყენება თუ არგუმენტი ფუნქციის გამოძახებისას არ გადაეცემა