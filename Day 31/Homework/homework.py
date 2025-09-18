def greet(name):
    return f"გამარჯობა, {name}!"
print(greet("გიორგი"))  
def square(n):
    return n ** 2
print(square(5)) 
def is_even(n):
    if n % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"
print(is_even(4))  
print(is_even(7)) 
def maximum(a, b, c):
    return max(a, b, c)
print(maximum(3, 7, 5))  
def reverse_text(txt):
    return txt[::-1]
print(reverse_text("Python"))  
