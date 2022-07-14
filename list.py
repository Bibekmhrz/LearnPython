fav_places=[]  #empty list created

fav_places.append('tilicho') #added value to the list
print(fav_places)
fav_places.append('phokshunda') #again added
fav_places.append('mustang')
fav_places.append('manang')

fav_places.insert(2, 'west_nepal')   #inserting the value at second index(third position)
print(fav_places)

fav_places.sort()           #sorted list in ascending order
print(fav_places)

fav_places.sort(reverse=True)  #reverse the sorted list
print(fav_places) 

fav_places[0]='darchula'    #change the value of zero position 
print(fav_places)

del fav_places[4]    #removed a value at forth index
print(fav_places)

popped_places=fav_places.pop(2)   #pop out the value from 2nd index
print(fav_places)
print(popped_places)  #print the value of pop element

print(f"lets visit {popped_places.title()}")

print(sorted(fav_places))  #can be sorted temporary
print(fav_places)

#working with for loop in list

cars=['audi', 'tesla', 'ford', 'bmw']
for car in cars:
    print(car)
    print(f"{car} is a wonderful car awesome.")
print('\tDriving a car can make you feel enjoyable')    