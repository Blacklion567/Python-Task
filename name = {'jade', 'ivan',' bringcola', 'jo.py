#cebico bills

print("\n\t CEBICO BILLS ")

input("\tName: ")
input("\tAddress: ")
a = int(input("\tPresent Reading: "))
b = float(input("\tPrevious Reading: "))
bills = (a-b)*15.45

print("\tBills: ", bills)