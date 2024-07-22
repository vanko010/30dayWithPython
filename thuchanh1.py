#If viết tắt
a = 3
print('A is positive') if a > 5 else print('A is negative') # first condition met, 'A is positive' will be printed

#If or
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

#If and
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

#while
count = 1
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

count =6
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

#While if
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

#while if continue
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

#for
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

for number in range(1,11):
    print(number)

for i in range(0,11):
    for j in range(0,11):
        print(f"{i}x{j} = {i*j}")

