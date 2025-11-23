#3) შექმენით ფუნქცია user_info, რომელსაც გადაეცემა სამი არგუმენტი: name, surname, address. return-ს გამოყენებით დააბრუნეთ მომხმარებლის ინფორმაცია შემდეგ ფორმატში:

#მომხმარებლის სახელი: <name>
#მომხმარებლის გვარი: <surname>
#მომხმარებლის მისამართი: <address>


def user_info(name,surname,adress):
    print(f"მე ვარ ვარ {name} ჩემი გვარია {surname} და მე ვცხოვრობ {adress}")
    
user_info("luka", "qiria", "tbilisi")
user_info("sandro", "burduli", "gori")
