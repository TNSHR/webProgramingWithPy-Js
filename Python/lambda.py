people =[
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"cho", "house":"ravenclaw"},
    {"name":"Draco","house":"Slytherin"}
]

# def f(person):
#    return person["name"] 
# people.sort(key=f)
# print(people)

people.sort(key=lambda person: person["name"])
print(people)