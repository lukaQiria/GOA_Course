# ==  ტოლია
# !=  არ არის ტოლი
# >   მეტია
# <   ნაკლებია
# >=  მეტია ან ტოლი
# <=  ნაკლებია ან ტოლი


# and (ორივე  უნდა იყოს True)
# or  (ერთ-ერთი მაინც უნდა იყოს True)
# not არ არის (აბრუნებს საპირისპიროს)

x = 10
y = 5

# შედარებითი და ლოგიკური ოპერაციები ერთად
if (x > y and y != 0) or not (x < y):
    print("პირობა შესრულდა")
else:
    print("პირობა არ შესრულდა")


print(True and not False and (False or True) and True or not False and False and not True and (True or False) or (True and False))

True or False or False = True
#გამოიტანს true-ს
