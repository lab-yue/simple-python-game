class CharacterBase(object):

    character_count = 0

    def __init__(
        self,
        name: str = "",
        hp: int = 0,
        current_hp: int = 0
    ):
        CharacterBase.character_count += 1
        self.__character_id = CharacterBase.character_count
        self.__name = name
        self.__hp = hp
        self.__current_hp = hp

    @property
    def character_id(self):
        return self.__character_id

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @property
    def current_hp(self):
        return self.__current_hp

    @current_hp.setter
    def current_hp(self, hp: int):
        self.__current_hp = hp

    def add_damage(self, damage: int = 0):
        temp_hp = self.current_hp - damage
        if (temp_hp < 0):
            self.current_hp = 0
            return
        self.current_hp = temp_hp


class Group:
    PLAYER = 1
    ENEMY = 2


class Character(CharacterBase):

    def __init__(
        self,
        name: str = "",
        attack_power: int = 0,
        hp: int = 0,
        current_hp: int = 0,
        exp: int = 0,
        next_level_exp: int = 0,
        group: int = Group.PLAYER,
    ):
        super().__init__(name, hp, current_hp)
        self.__attack_power = attack_power
        self.__exp = exp
        self.__next_level_exp = next_level_exp
        self.__expRemian = 0
        self.__group = group

    def __repr__(self):

        return f"""
character_id: {self.character_id}
name: {self.name}
hp: {self.hp}
current_hp: {self.current_hp}
attack_power: {self.attack_power}
exp: {self.exp}
next_level_exp: {self.next_level_exp}
      """

    @property
    def attack_power(self):
        return self.__attack_power

    @property
    def exp(self):
        return self.__exp

    def add_exp(self, exp: int):
        self.__exp += exp

    @property
    def next_level_exp(self):
        return self.__next_level_exp

    @property
    def group(self):
        return self.__group

    @property
    def exp_remain(self):
        exp_remain = self.next_level_exp - self.exp
        if (exp_remain < 0):
            return 0
        return exp_remain

    @property
    def is_alive(self):
        return self.current_hp > 0

    def attack(self, character: 'Character'):
        character.add_damage(self.attack_power)
        print(
            f"[{self.name}のターン] " +
            f"{character.name} に対して攻撃を行った。" +
            f"{self.attack_power} のダメージ"
        )
        if (not character.is_alive):
            print(f"{character.name}は倒れた")
            self.add_exp(self.attack_power)
