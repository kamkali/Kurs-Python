class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'


class Character:
    number_of_alive_characters = 0

    def __init__(self, _name='Postac'):
        self.name = _name
        self.HP = 100
        self.position = Position(0, 0)
        self.level = 1
        # tmp str
        self.str = self.level * 10
        self.defence = self.level * 4
        self.is_alive = True
        Character.number_of_alive_characters += 1

    def set_position(self, pos_x, pos_y):
        self.position = Position(pos_x, pos_y)

    def get_position(self):
        return self.position

    def move_character(self, move_x, move_y):
        current_position = self.get_position()
        current_position.x += move_x
        current_position.y += move_y

        self.set_position(current_position.x, current_position.y)

    def attack(self, other_char):
        def find_distance(char1: Character, char2: Character):
            return ((char2.get_position().x - char1.get_position().x) ** 2 +
                    (char2.get_position().y - char1.get_position().y) ** 2) ** (1 / 2)

        if find_distance(self, other_char) > 1:
            print("Cannot attack, player is to far")
        else:
            print(f"{self.name} attacked {other_char.name} and deal {self.str} damage")
            other_char.HP -= self.str

            if other_char.HP <= 0:
                print(f"{other_char.name} has been killed by {self.name}")
                Character.number_of_alive_characters -= 1
                self.level += 1
                other_char.HP = 0

    def __str__(self):
        return f'Character name: {self.name}, HP: {self.HP}, position: {self.position}, ' \
               f'lvl: {self.level}. He is {"Alive" if self.HP != 0 else "Dead"}'


if __name__ == '__main__':
    first_char = Character("Beast")
    second_char = Character("Andrew")
    print(first_char)
    print(second_char)

    first_char.move_character(1, 0)
    print(first_char)
    print(second_char)
    for attack in range(10):
        first_char.attack(second_char)
    print(first_char)
    print(second_char)
