#ADVANCE DICTIONARY
#a COLLECTION OF KEY PAIRS that is UNORDERED, CHANGEABLE and INDEXED.

#dictionary
studentOne = {
    "name" : "JADE IVAN",
    "course" : "BSIT",
    "age" : 20
}

studentTwo = {
    "name" : "JOVAN",
    "course" : "BSIT",
    "age" : 13
}

#print(studentOne("name"))
#print(studentTwo["name"]) 
studentOne["name"] = "JAIJAI"
studentTwo["name"] = "PROLINE"

print(studentOne.get("age"))
print(studentTwo.get("name"))


#Example - 1
studentOne = {
    "name" : "JADE IVAN",
    "course" : "BSIT",
    "age" : 20
}

studentTwo = {
    "name" : "JOVAN",
    "course" : "BSIT",
    "age" : 13
}

print(len(studentOne))
print(len(studentTwo))


studentOne = {
    "name" : "JOVAN",
    "course" : "BSIT",
    "age" : 13
}

studentThree = studentOne.copy
studentThree["name"] = "Proline"

print(studentThree)

