#tuple acts as a list but cannot modify the value in each index
#creating tuple
food=('momo', 'chowmein', 'pizza', 'thukpa', 'mushroom')
for each in food:
    print(each)  #printing each value in tuple

# food[0]='hawa'   #this will give an error as a tuple error
# print(food)

#but we can reassign the tuple value
food=('hawa','pizza')
print(food)   