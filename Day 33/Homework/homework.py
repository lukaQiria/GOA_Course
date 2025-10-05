# print():
#დადებითი მარტივად ბეჭდავს ინფორმაციას ეკრანზე გამოიყენება ტესტირებისა და გამოტანისთვის.
#უარყოფითი არ აბრუნებს მნიშვნელობას ამიტომ მის შედეგს ვერ გამოვიყენებთ სხვა გამოთვლებში.

# return:
#დადებითი აბრუნებს მნიშვნელობას რომელიც შეიძლება გამოყენო გამოთვლებში ან შეინახო ცვლადში.
#უარყოფითი არ ბეჭდავს ეკრანზე შედეგს თუ არ გამოვიძახებთ print()ს დამატებით.



def check_age(age):
    if age >= 18:
        print("Access Granted")
    else:
        print("Access Denied")


def user_info(name, surname, address):
    return f"მომხმარებლის სახელი: {name}\nმომხმარებლის გვარი: {surname}\nმომხმარებლის მისამართი: {address}"


def power(num1, num2):
    return num1 ** num2


def arithmetic_average(numbers):
 return sum(numbers) / len(numbers)


check_age(20)  
print(user_info("ლუკა", "ქირია", "თბილისი"))
print(power(2, 3))  
print(arithmetic_average([10, 20, 30, 40, 50])) 
