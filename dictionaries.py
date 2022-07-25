# # #dictionary is a collection of key value pair.each is connected to a value.
# # locations={"Ram":"Lalitpur", "Shyam":"Kathmandu", "Hari":"Bhaktapur"}
# # #here locations act as dictionaries
# # print(locations["Ram"])  #dictionaries takes the value of Ram

# # locations["Krishna"]="Lalitpur"
# # locations["sita"]="Bhaktapur"
# # print(locations)


# alien_0={}  #empty dictionary created
# alien_0['color']='green'
# print(alien_0)
# alien_0['color']='red'  #modifying a dictionary value
# print(alien_0)

# del alien_0['color']  #removing a dictionary value
# print(alien_0)

# alien_0={'x-pos':0, 'y-pos':25, 'speed':'medium'}
# print(alien_0)
# print(f"original position is {alien_0['x-pos']}")

# if  alien_0['speed'] =='slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x-pos'] = alien_0['x-pos'] + x_increment    
# print(f"New position is {alien_0['x-pos']}")    


#dictionary of similar objects
fav_language = {
    'ram' : 'python',
    'shyam' : 'c',
    'hari' : 'ruby',
    'krishna': 'python',
}
# language = fav_language['ram'].title()
# print(f"Ram's favourite language is {language}. ")

# #using get() to access values

# alien_0 = {'color':'green', 'speed':'medium'}
# point_value = alien_0.get('points','25')
# print(point_value)
# print(alien_0)

# for name, language in fav_language.items():
#     print(f"{name.title()}'s favourite language is {language.title()}")

# #looping through all the keys in dictionary
# for name in fav_language.keys():
#     print(name.title())

# friends = ['ram','rita','gita','hari']
# for name in fav_language.keys():
#     print(name.title())

#     if name in friends:
#         language=fav_language[name].title()
#         print(f"{name.title()}, I see you love {language}")
#     if 'elin' not in fav_language.keys():
#         print(f"Erin please join courses") 
#     if 'shyam' not in fav_language.keys():
#         print(f"Shyam please join courses")


for name in sorted(fav_language.keys()):
    print(f"{name.title()}, thank you for taking a courses.")        

#now looping through values
print('Here are the progamming language lists.')
for languages in fav_language.values():
    print(languages.title());

#to avoid repetition set() can be used like below.
print('\n Available Programming Languages are as follows:')
for languages in set(fav_language.values()):
    print(languages.title())
    
#set() can be built directly using braces{}.
languages = {'python', 'ruby', 'c#', 'c', 'python'}
print(languages)
