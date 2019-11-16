class MyClass:
    def __init__(self):
        self.first_param = 10
        self.second_param = 20


class Person:
    def __init__(self, first_name, second_name, age=20):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def print_person_greeting(self):
        print(f"Hello, my name is {self.first_name} {self.second_name} and I am {self.age} years old")

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.age}'


def class_testing():
    print(MyClass)
    my_object = MyClass()
    print(my_object.first_param)

    person = Person('Jan', 'Kowalski', age=32)
    person.print_person_greeting()
    print()
    print("Override '__str__' method which is to_string equivalent:")
    print(person)


if __name__ == '__main__':
    class_testing()
