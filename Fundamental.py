#Example - 0
firstname = ("jade ivan")
lastname = ("bringcola")
fullname = (firstname + lastname)

print(fullname)

#Example - 1
nameOne = "jade ivan"
nameTwo = " bringcola "
nameThree = nameOne + nameTwo
age =  20

print(f"Hi", (nameThree)+ "how old are you" +" " + (nameThree) + str(age) +"?")


name = ("proline")
lastname = (" basmayor")
fullname = (name + lastname)

print(f"{fullname.title()} i like you so much.")
print(f"{fullname.upper()} you so beautyful as always.")
print(f"{fullname.lower()} i have a crush on you since grade 8")

#difference

numbers = {1,2,3,4,5,6,7,8,9,10}
evenNumbers = {2,4,6,8,10}

print(numbers.difference(evenNumbers))

#systematic_difference

evenNumbers = {2,4,6,8,10}
numbers = {1,2,3,4,5,6,7,8,9,10}

print(evenNumbers.symmetric_difference(numbers))

#isdisjoint
#True
numbers = {1,2,3,4,5,6,7,8,9,10}
evenNumbers = {12,14,16,18,20}

print(numbers.isdisjoint(evenNumbers))

#False
numbers = {1,2,3,4,5,6,7,8,9,10}
evenNumbers = {2,4,6,8,10}

print(numbers.isdisjoint(evenNumbers))


#intesection
numbers = {1,2,3,4,5,6,7,8,9,10}
evenNumbers = {2,4,6,8,10}

print(numbers.intersection(evenNumbers))

#issubset
#True
numbers = {1,2,3,4,5,6,7,8,9,10}
evenNumbers = {2,4,6,8,10}

print(evenNumbers.issubset(numbers))

#False
numbers = {1,2,3,4,5,6,7,8,9,10}
evenNumbers = {2,4,6,8,10}

print(evenNumbers.issubset(numbers))

#issuperset
numbers = {1,2,3,4,5,6,7,8,9,10}
evenNumbers = {2,4,6,8,10}

print(numbers.issuperset(evenNumbers))

#list
numbers = {1,2,3,4,5,6,7,8,9,10}
numbers = list(numbers)
numbers[0] = 'hotdog'

print(numbers)

#set
numbers = {1,2,3,4,5,6,7,8,9,10}
numbers = set(numbers)

print(numbers)

#tuple
numbers = {1,2,3,4,5,6,7,8,9,10}
numbers = tuple(numbers)

print(numbers)
