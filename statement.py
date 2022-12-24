type = input("Choose What Type Of Function Do You Want?(addition, subtraction, multiplication, division, average): ")

def addition():
    a = int(input("Enter The First Number: "))
    b = int(input("Enter The Second Number: "))
    print("The Result Is: " + str(a + b))
def subtraction():
    a = int(input("Enter The First Number: "))
    b = int(input("Enter The Second Number: "))
    print("The Result Is: " + str(a - b))
def multiplication():
    a = int(input("Enter The First Number: "))
    b = int(input("Enter The Second Number: "))
    print("The Result Is: " + str(a * b))
def division():
    a = int(input("Enter The First Number: "))
    b = int(input("Enter The Second Number: "))
    print("The Result Is: " + str(a / b))
def average():
    a = int(input("Enter The First Average: "))
    b = int(input("Enter The Second Average: "))
    c = int(input("Enter The Third Average: "))
    d = int(input("Enter The Fourth Average: "))
    e = int(input("Enter The Fifth Average: "))
    print("The Result Is: "+ str(a+b+c+d+e /5 ))


# ALL OF THIS IS FOR ADDITION
if ( type == "addition"):
    print("Addition Mode")
    addition()
elif ( type == "subtraction"):
    print("Subtraction Mode")
    average()
elif ( type == "multiplication"):
    print("Multiplication Mode")
    subtraction()
elif ( type == "division"):
    print("Division Mode")
    division()
elif (type == "average"):
    print("Average Mode")
    average()
elif ( type == "subtraction"):
    print("Subtraction Mode")
    average()
elif ( type == "multiplication"):
    print("Multiplication Mode")
    subtraction()
elif ( type == "division"):
    print("Division Mode")
    division()
elif (type == "average"):
    print("Average Mode")
    average()
else:
    print("Function Error Try Again")
