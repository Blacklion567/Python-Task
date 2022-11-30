#Print The Whole Set

numbers = {1,2,3,4,5,6,7,8,9,10}

print(numbers)


#Checking The How Many Values Inside

numbers = {1,2,3,4,5,6,7,8,9,10}

print(len(numbers))



#Add Some Number Inside Of The Set

numbers = {1,2,3,4,5,6,7,8,9,10}
numbers.add(11)

print(numbers)



#Updating The Value Inside Of The Set

numbers = {1,2,3,4,5,6,7,8,9,10}
numbers.update([11,12,13,14,15])

print(numbers) 


#Updating The Value Inside Of The Set Doing This Also

numbers = {1,2,3,4,5,6,7,8,9,10}
a = ([11,12,13,14,15])
numbers.update(a)

print(numbers) 



#Remove The Number That You Want

numbers = {1,2,3,4,5,6,7,8,9,10}

numbers.remove(3)

print(numbers)




#Remove The Number That You Want But Not Going To ERROR

numbers = {1,2,3,4,5,6,7,8,9,10}

numbers.discard(11)

print(numbers)

