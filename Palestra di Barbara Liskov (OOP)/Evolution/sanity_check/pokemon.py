


class Pokemon:
    def __init__(self, name, type, level, hp, moves, next_evolve):
        self.name = name
        self.type = type
        self.level = level
        self.hp = hp
        self.moves = moves
        self.next_evolve = next_evolve

    def level_up(self):
        self.level += 1
        print(f'{self.name} levelled up to {self.level}')
        self.evolve()

    def evolve(self):
        if self.level == self.next_evolve:
            print(f'{self.name} evolved!')