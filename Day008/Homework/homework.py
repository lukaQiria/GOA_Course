a = 10
b = 5

print(a == b)  
print(a != b)   
print(a > b)    
print(a < b)    
print(a >= b)   
print(a <= b)   



print(5 == 5)  # True


print(8 > 3)  # True


print(2 < 7)  # True


print(6 >= 6)  # True


print(4 <= 9)  # True


# ტოლობის შემოწმება 
# 5 და 5 ტოლია, ამიტომ აბრუნებს True-ს
print(5 == 5)  # True

# მეტობა  8 უფრო დიდია 3-ზე, ამიტომ აბრუნებს True-ს
print(8 > 3)  # True

# ნაკლებობა  2 პატარაა 7-ზე, ამიტომ აბრუნებს True-ს
print(2 < 7)  # True

# მეტია ან ტოლია 6 ტოლია 6-ის, ამიტომ True
print(6 >= 6)  # True

# ნაკლებია ან ტოლია  4 ნაკლებია 9-ზე, ამიტომ True
print(4 <= 9)  # True

#პირობა თუ არ არის სწორი:
print(5 > 10)  # False 5 არ არის 10-ზე დიდი
print(3 == 7)  # False 3 არ არის ტოლი 7-ის


num = int(input("შეიყვანეთ რიცხვი: "))
print(num > 10)
