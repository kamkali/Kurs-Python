from enum import Enum
from datetime import datetime


class Sex(Enum):
    FEMALE = "F"
    MALE = "M"
    OTHER = "X"
    UNSPECIFIED = "U"


class Date:
    def __init__(self, day, month, year):
        self.day: int = day
        self.month: int = month
        self.year: int = year

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


class User:
    users_dict = {}

    def __init__(self, first_name, second_name, sex: Sex = Sex.UNSPECIFIED, date_of_birth: datetime.date = None):
        self.first_name: str = first_name
        self.second_name: str = second_name
        try:
            self.__class__.users_dict[f"{self.first_name.lower()}{self.second_name.lower()}"] += 1
        except KeyError:
            self.__class__.users_dict[f"{self.first_name.lower()}{self.second_name.lower()}"] = 1

        self.username: str = f"{self.first_name.lower().replace(' ', '-')}_{self.second_name.lower().replace(' ', '-')}_" \
                             f"{self.users_dict[f'{self.first_name.lower()}{self.second_name.lower()}']}"

        self.gender: Sex = sex
        self.date_of_birth = date_of_birth

        self.friends = []
        self.pending_invites = []

    def __str__(self):
        return f"User info:\nName: {self.first_name}, Surname: {self.second_name}, " \
               f"Username: {self.username}\nGender: {self.gender}, Date of birth: {self.date_of_birth}"

    def get_friend_list(self):
        print(f"{self.username} friends list: ")
        return self.friends

    def get_friend_invites(self):
        print("Pending invite from users: ")
        return self.pending_invites


class Invite:
    def __init__(self, from_user: User, to_user: User):
        self.from_user = from_user
        self.to_user = to_user

    def add(self):
        self.to_user.pending_invites.append(self.from_user.username)

    @staticmethod
    def accept(from_user, to_user):
        to_user.friends.append(from_user.username)
        to_user.pending_invites.remove(from_user.username)

    @staticmethod
    def decline(from_user, to_user):
        to_user.pending_invites.remove(from_user.username)


def facebook():
    first_user = User('Kamil', 'Kaliś', Sex.MALE, '07.05.1998')
    first_user1 = User('Kamil', 'Kaliś', Sex.MALE, '10.03.2011')

    second_user = User('Marek', 'Podlecki', Sex.OTHER, '10.12.1989')

    Invite(from_user=first_user, to_user=second_user).add()

    print(second_user.get_friend_invites())

    Invite.accept(from_user=first_user, to_user=second_user)

    print(second_user.get_friend_list())


if __name__ == '__main__':
    facebook()
