#we cannot combine strings like this:
age = 36
txt = "My name is John, I am " + age
print(txt)


#right format
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

#placeholder can include a modifier (fixed point number with 2 decimals:)
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#placeholder can contain Python code, like math operations:
txt = f"The price is {20 * 59} dollars"
print(txt)


