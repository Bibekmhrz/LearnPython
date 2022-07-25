

# n = int(input("Number:"))

# if n>0:
#     print("n is positive")

# elif n<0:
#     print("n is negative")

# else:
#     print("n is zero")

car = 'audi'
print("Is car == 'audi'? I predict True. ")
print(car == 'audi')
print(car =='bmw')

print(car.title()=='Audi')

food='momo'
if food != 'chowmein':
    print("Don't like food")
if food =='momo':
    print('wow i like it')  

bikes=['suzuki', 'bajaj','yamaha']
if bikes == 'suzuki' and 'yamaha':
    print('there is no bajaj bikes') 
if bikes != 'honda':
    print('there is no honda bike available')     

age0=22
age1=18
if age0>=21 and age1>=21:
    print('true') 


age=int(input('Your age:'))
# if age<4 :
#     print('admission is free for agegroup under 4')
# elif age<18:
#     print('your admission charge is $25')
# else :
#     print('your admission charge is $40')

if age<4 :
    price = 0;
elif age<18:
    price =25;
elif age<60:
    price = 40    
else :
    price =10;
print(f"you admission charge is ${price}")    
print('***********************Thank u for visiting********************')                