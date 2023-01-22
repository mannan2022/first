# person_one=['Moris','male','australia','29th january 1988','morish@jhon.com','01716816874']
# #'morish is born in autralia.his Date of birth 29th jan.He is available at moris@jon.com and phone no is 01716816874'
# gender=person_one[1]
# if gender=='male':
#     relative='his'
#     pronoun='He'
# else:
#     relative='Her'
#     pronoun='She'
# sentence=(f'{person_one[0]} is born in {person_one[2].title()}.{relative.title()} Date of birth {person_one[3]}.{pronoun} is available at {person_one[4]} and phone no is {person_one[-1]}')
# print(sentence)
# person=[
#     ['moris','male','australia','1988','moris@jon.com'],
#     ['vasko','male','ukrain','1956','vasko@jon.com'],
#     ['amni','female','norway','1980','amni@.com'],
#     ['andru','male','india','1971','andu@.com'],
#  ]
# i=0
# while i<len(person):
#     print(person[i])
#     i=i+1
# person=[
#     ['moris','male','australia','1988','moris@jon.com'],
#     ['vasko','male','ukrain','1956','vasko@jon.com'],
#     ['amni','female','norway','1980','amni@.com'],
#     ['andru','male','india','1971','andu@.com'],
# ]
# print(person[-2][2])
# person=[
#     ['Hasmir','Male','1997','Daulotkhan','hasmir@.com'],
#     ['kamal','male','Daulotkhan','1997','juwel2.com'],
#     ['Sagor','male','Daulotkhan','1998','omayer@.com'],
#     ['farzana','female','Daulotkhan','2000','farzana@.com'],
#     ]
# i=0
# while i<len(person):
#     singel_person=person[i]
#     name=singel_person[0]
#     gender=singel_person[1]
#     birth_palace=singel_person[3]
#     Date_of_Birth=singel_person[2]
#     email=singel_person[4]
#     if gender=='male':
#         pronoun='He'
#         relative='His'
#     else:
#         pronoun='She'
#         relative='her'
#     sentence=(f'{name} lives in {birth_palace}.{pronoun} was born in {Date_of_Birth}.{relative} email is {email} ')
#     print(sentence)
#     i=i+1
# import random
# ludu=[1,2,3,4,5,6]
# random_number=random.choice(ludu)
# if random_number==6:
#     print('Yes,you have won the game')
# else:
#     print(random_number,'is not six')
# print(random_number)
# import random
# person=['Moris','chittagong']
# name=person[0]
# location=person[1]
# sentence_one_group=[
#     f'my name is {name}',
#     f'this is {name}',
#     f'{name} is my name',
#     ]
# sentence_two_group=[
#     f'i live in {location}',
#     f'i reside in {location}',
#     f'i was raised in {location}',
#     f'{location } is beautiful palce'
#     ]
# sentence_one=random.choice(sentence_one_group)
# sentence_two=random.choice(sentence_two_group)
# pragraphs=f'{sentence_one}.{sentence_two}'
# print(pragraphs)
# students=[]
# while True:
#     name=input('Enter Your students name:')
#     if name=='sesh':
#         print(students)
#         print('total students',len(students))
#         break
#     else:
#         students.append(name)
# import random
# number=[1,2,3,4,5,6,7,8,9]
# computer_number=random.choice(number)
# while True:
#     numbers=int(input('Enter Your gues number: '))
#     if computer_number==numbers:
#         print('Congratulations ')
#         break
#     else:
#         print('Hoy nai')
# students=['kamal','jamal','rohim','korim','kuddus']
# # i=0
# # while i<len(students):
# #     print(students[i])
# #     i+=1
# for element in students:
#    # print(element)
# bazar_list=['Rice','oil','Dal','fish','Tomato']
# for element in bazar_list:
#     print(element)