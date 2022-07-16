strings="car bus van plane tesla ford"
string=strings.split()
pop_element=string.pop()

print(string)
print(f"{string} and {pop_element}")

element=""
for value in string:
    print(value)
    element=element + value + ", "

print(element)   
print(f"{element.title()}and {pop_element.title()}")
