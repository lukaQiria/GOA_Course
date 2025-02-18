hobby = " My hobby is soccer. I've been playing soccer for 2 months and I think it's the best sport. I play in central defense and I want to become a professional soccer player. I don't have any other hobbies yet."
print(hobby)

#int (მთელი რიცხვი) – მხოლოდ რიცხვებს ინახავს და მათზე შესაძლებელია მათემატიკური მოქმედებების შესრულება.
#str (სტრიქონი, ტექსტი) – ინახავს სიმბოლოებს (მათ შორის, ციფრებსაც), მაგრამ როგორც ტექსტს.
#int-ზე შეგიძლია მათემატიკური მოქმედებები:
#num = 5
#print(num + 2)  # 7
#str კი მხოლოდ ტექსტური ოპერაციების საშუალებას იძლევა (მაგალითად, შეერთება):
#text = "5"
#print(text + "2")
#სტრინგის int-ად გადაყვანა
#text = "5"
#number = int(text)  # გადაყავს სტრინგი int-ად
#print(number + 2)   # 7
#int-ის str-ად გადაყვანა:
#num = 5
#text = str(num)
#print(text + "2")  # "52"
#თუ str არ არის რიცხვი, მისი int-ად გარდაქმნა შეცდომას გამოიწვევს:
#text = "hello"
#number = int(text)
