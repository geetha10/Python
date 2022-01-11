#1 returns 5
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 function returns 5
def number_of_military_branches():
    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) #first function is not defined yet.


#3 returns 5
def number_of_books_on_hold():
    return 5
    return 10 # unreachable statement
print("Num of books on hold:",number_of_books_on_hold())


#4 returns 5
def number_of_fingers():
    return 5
    print(10) # unreachable statement
print("number_of_fingers: ",number_of_fingers())


#5Function prints 5 to console doesnt return a  value
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes() #x is None as function doesn't return anything
print("number_of_great_lakes:",x)


#6 prints the sum of numbers
def add(b,c):
    print("inside add func")
    print(b+c)


#print(add(1,2) + add(2,3)) #prints 3 , 5 and trows TypeError: unsupported operand type(s) 


#7concats two given parameters
def concatenate(b,c):
    return str(b)+str(c)
print("concatenate:", concatenate(2,5))


#8 returns 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print("number_of_oceans_or_fingers_or_continents:", number_of_oceans_or_fingers_or_continents()) #prints 10



#9 returns 7 if b is less than c else returns 14 
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3 # unreachable statement
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #14 
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #21


#10 returns sum
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) #8


#11
b = 500
print("before func:",b) #500
def foobar():
    b = 300 #updating b t0 300
    print("inside func:",b) # 300
print("After func:",b) #500
foobar() 
print("After func call:",b) #300


#12
b = 500
print(b) #500
def foobar():
    b = 300 #updating b t0 300
    print(b) #300
    return b #return 300
print(b) #500
foobar() #func call, prints 300
print(b) # 500


#13
b = 500
print(b) #500
def foobar():
    b = 300 #updating b t0 300
    print(b) #300
    return b #return 300
print(b) #500
b=foobar() #func call, prints 300
print(b) # 300


#14
def foo():
    print("foo:")
    print(1)#1
    bar() # goes to func and prints 3
    print(2)#2
def bar():
    print(3)
foo() #prints 132


#15
def foo():
    print(1) 
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo() # prints 1 3 5 10
print(y)