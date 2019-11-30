class User:
    users_dict = {}
    user_count = 0

    def __init__(self, first_name, second_name, sex, date_of_birth):
        self.first_name = first_name
        self.second_name = second_name
        try:
            self.__class__.users_dict[f"{self.first_name.lower()}{self.second_name.lower()}"] += 1
        except KeyError:
            self.__class__.users_dict[f"{self.first_name.lower()}{self.second_name.lower()}"] = 1

        self.username = f"{self.first_name.lower()}_{self.second_name.lower()}_" \
                        f"{self.users_dict[f'{self.first_name.lower()}{self.second_name.lower()}']}"
        self.gender = sex
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"User info: Name: {self.first_name}, Surname: {self.second_name} \n" \
               f"Username: {self.username}, gender: {self.gender}, Date of birth: {self.date_of_birth}"


def facebook():
    first_user = User('Kamil', 'Kaliś', 'M', '07.05.1998')
    first_user1 = User('Kamil', 'Kaliś', 'M', '10.03.2011')

    second_user = User('Marek', 'Podlecki', 'M', '10.12.1989')
    print(first_user)
    print(second_user)
    print(first_user1)


if __name__ == '__main__':
    facebook()
