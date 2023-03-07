from register.person import Person
from typing import List

people: List[Person] = []

while True:
    id: str = input("Ingrese identificación: ")
    fullname: str = input("Ingrese nombre completo: ")
    email: str = input("Ingrese email: ")
    person = Person(id=id)
    person.setEmail(email)
    person.setFullname(fullname)
    people.append(person)
    stopExecution = input("nueva persona 1 si, 2 no")
    if stopExecution == '2':
        break

for i in people:
    print(i.getId(), i.getFullname(), i.getEmail())