mixed_list = [42, "გამარჯობა", 3.14, True, None, [1, 2, 3], {"key": "value"}]

print(mixed_list)

foods = ["ხინკალი", "აჭარული ხაჭაპური", "მწვადი", "ლობიო"]

foods.append("ჩაქაფული")


foods.remove("ლობიო")


print("Foods List:", foods)


print("Length of list:", len(foods))



nums = [10, 25, 3, 42, 17, 8]

print("Maximum:", max(nums))

print("Minimum:", min(nums))

print("Sum:", sum(nums))

average = sum(nums) / len(nums)
print("Average:", average)



words = ["მზე", "სახლი", "კატა", "ავტობუსი", "ძაღლი", "ხე"]

short_words = []

for word in words:
    if len(word) < 5:
        short_words.append(word)

print("Short words:", short_words)


names = ["გიო", "ანა", "ბექა", "დათა", "ელენე", "ზურა"]

names.sort()
print("Sorted names:", names)


names.reverse()
print("Reversed names:", names)


