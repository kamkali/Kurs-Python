def say_hello(first_name, last_name="",age = 0):
    print(f'Hi {first_name} {last_name}')
    print(f'You have {age} years old')

say_hello('Kamil','Kalis',21)
say_hello("Jan",age=30)


def polygon(a,b):
    print(f"Polygon areay is {a*b}, and circumference is {a+b}")
    return a*b, a+b

polygon(2,2)

x = polygon(20,34)

print(x)
print(x[0])
print(x[1])

pole, obwod = polygon(10,10)
print(pole)
print(obwod)

print()
##lipa - objekt mutowalny
def my_append(value,my_list=[]):
    my_list.append(value)
    return my_list

##sposob z krotka - malo uzywany
def my_append2(value,my_list=()):
    my_list = list(my_list)
    my_list.append(value)
    return my_list

##Czesciej uzywany
def my_append3(value,my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


##Przekazanie przez referencje
def my_append4(value,my_list):
    my_list.append(value)


def my_append5(value,my_list):
    my_list = [3,4]
    my_list.append(value)


print(my_append(2,[3,4]))
print(my_append(3))
print(my_append(4))

#my_append2
print('my_append2')
print(my_append2(2,[3,4]))
print(my_append2(3))
print(my_append2(4))


#my_append3
print('my_append3')
print(my_append3(2,[3,4]))
print(my_append3(3))
print(my_append3(4))


#my_append4
#my_append5


##Cw1 - napisz funkcje ktora np rect umozliwia pole kwadratu

def rect(a, b=None):
    if b is None:
        b = a
    return a * b

print()
print("Cw1")
print(rect(4))
print(rect(2,3))


##Cw2 - napisz funkcje ktora sprawdza czy caly string z duzej/malej litery

def is_upper_lower(string):
    if string.upper() == string:
        print("Upper")
    elif string.lower() == string:
        print("Lower")
    else:
        print("None")


is_upper_lower("HAHA")
is_upper_lower('haha')
is_upper_lower("HaHa")
