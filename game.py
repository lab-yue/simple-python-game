from typing import List
from character import Character, Group

class Game(object):

    def __init__(self, characters: List['Character']):
        self.__characters = characters
        self.__turn_count = -1

    def run(self):
        self.info('バトル開始')
        while self.is_game_continue:
            self.current_character.attack(self.attackee)
        self.info('バトル終了')

        for character in self.characters:
            if character.is_alive and character.group == Group.PLAYER:
                print(
                    f"[{character.name}] " +
                    f"{character.exp}の経験値を取得した。 " +
                    f"次のレベルまで{character.exp_remain}"
                )

    def status(self):
        for character in self.characters:
            print(character)

    @property
    def characters(self):
        return self.__characters

    @property
    def is_game_continue(self):
        alive_characters_groups = []
        for character in self.characters:
            if character.is_alive:
                alive_characters_groups.append(character.group)
        if len(set(alive_characters_groups)) == 1:
            return False
        self.__turn_count += 1
        return True

    @property
    def attackee(self):
        for character in self.characters:
            if character.is_alive and character.group != self.current_character.group:
                return character
        return None

    @property
    def turn(self):
        return self.__turn_count % len(self.characters)

    @property
    def current_character(self):
        return self.characters[self.turn]

    @staticmethod
    def info(message):
        print(message)
