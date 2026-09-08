#identity operator
a = None

print(a is None)  
print(a is not None)


#bit wise operators
a = 5
b = 3

print(a & b)  
print(a | b) 
print(a ^ b)  


#electric city bill calculator
units =int(input("Enter electricity units:1000"))

rate = 6

bill = units * rate

print("Electricity bill: ", bill)


#travel expense calculator
travel = float(input("travel expense:1200 "))
food = float(input("food expense:500 "))
hotel = float(input("hotel expense:1800 "))

total = travel + food + hotel

print("Total expense: ", total)