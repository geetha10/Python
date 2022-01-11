from typing import _get_type_hints_obj_allowed_types


def basics():
    for x in range(151):
        print(x)

def mutiples_of_5():
    for x in range(5,1001,5):
        print(x)

def counting_dojo_way():
    for x in range(1,101):
        if x%10 == 0:
            print("Coding Dojo")
        elif x%5 ==0:
            print("Coding")
        else:
            print(x)

def sum_of_odd_numbers():
    sum=0
    for x in range(500001):
        if not x%2==0:
            print(x)
            sum += x
    print("Sum of odd numbers is {}".format(sum))

def count_by_four():
    x =2018
    while x<5000:
        print(x)
        x += 4

def flexible_counter(lowNum,highNum,mult):
    for x in range(lowNum,highNum+1):
        if x%mult == 0:
            print(x)

# basics()
# mutiples_of_5()
# counting_dojo_way()
#sum_of_odd_numbers()
#count_by_four()
flexible_counter(2,9,3)
