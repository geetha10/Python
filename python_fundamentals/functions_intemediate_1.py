x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print("Before updating:",x)
x[1][0] =15
print("After updating:",x)

print("Before updating:",students)
students[0]['last_name']='Bryant'
print("After updating:",students)

print("Before updating:",sports_directory)
sports_directory['soccer'][0]='Andres'
print("After updating:",sports_directory)


#2 Iterate Through a List of Dictionaries

def iterateDictionary(students):
    for student in students:
        firstName=""
        lastName=""
        for key in student:
            if key == 'first_name':
                firstName=student[key]
            elif key == 'last_name':
                lastName=student[key]
        print("First Method: first_name - {}, last_name - {}".format(firstName,lastName))

def iterateDictionarySecondWay(students):
    for student in students:
        values = list(student.values())
        print(f"First name: {values[0]}, last name: {values[1]}")

def iterateDictionary2(key_name, some_list):
    new_list=[]
    for student in some_list:
        for key in student:
            if  key == key_name:
                new_list.append(student[key])
    return new_list

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
iterateDictionarySecondWay(students)
print(iterateDictionary2('last_name',students))

def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key}")
        [print(x) for x in some_dict[key]]

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)