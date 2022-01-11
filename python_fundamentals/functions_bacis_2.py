def countdown(num):
    result =[]
    for i in range(5,-1,-1):
        print(i)
        result.append(i)
    return result

print(countdown(5))

def print_and_return(num1,num2):
    print(num1)
    return num2

print(print_and_return(1,2))

def first_plus_length(numList):
    return numList[0]+len(numList)

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(numList):
    newList=[]
    if len(numList) > 1:
        for x in numList:
            if x > numList[1]:
                newList.append(x)
        return newList
    else:
        return False

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_value(size, value):
    result=[]
    for x in range(size):
        result.append(value)
    return result

print(length_and_value(4,7))
print(length_and_value(6,2))

