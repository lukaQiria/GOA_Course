def number_to_string(num):
    return str(num)
print(number_to_string(123))  
print(number_to_string(999))   
print(number_to_string(-100))  


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(2))  
print(even_or_odd(7))   
print(even_or_odd(0))   
print(even_or_odd(-5))  


def make_negative(number):
    if number > 0:
        return -number
    else:
        return number
print(make_negative(1))   
print(make_negative(-5))  
print(make_negative(0))   


def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2 == 1
print(lovefunc(1, 4)) 
print(lovefunc(2, 2))  
print(lovefunc(0, 1))  
print(lovefunc(5, 5))  


def double_integer(i):
    return i * 2
print(double_integer(2))   
print(double_integer(-3)) 
print(double_integer(0))   

