PLAYER = 1
ENEMY = 2


def use_character():

    __id = 0

    def create_character(
        name: str = "a",
        attack_power: int = 1,
        hp: int = 100,
        group: int = PLAYER
    ):
        nonlocal __id
        __id += 1

        return {
            'name': name,
            'id': __id,
            'attack_power': attack_power,
            'hp': hp,
            'current_hp': hp,
            'group': group
        }
    return create_character


def is_alive(character):
    return character['current_hp'] > 0


def is_enemy(a, b):
    return a['group'] != b['group']


def info(f):
    def wrapper():
        print("start")
        f()
        print("end")
    return wrapper

def game(characters):
    __turn_count = 0

    def current_character():
        return characters[__turn_count % len(characters)]

    def enemy_character():
        current = current_character()
        for maybe_enemy in characters:
            if is_enemy(current, maybe_enemy) and is_alive(maybe_enemy):
                return maybe_enemy
        return None

    def status(f):
        def wrapper():
            f()
            for character in characters:
                print(character)
        return wrapper

    def attack(a, b):
        print(
            f"[{a['name']} のターン] " +
            f"{b['name']} に対して攻撃を行った。" +
            f"{a['attack_power']} のダメージ"
        )
        tmp_hp = b['current_hp'] - a['attack_power']
        if tmp_hp <= 0:
            tmp_hp = 0
            print(f"{b['name']} is dead")
        b.update({'current_hp': tmp_hp})
        nonlocal __turn_count
        __turn_count += 1

    @status
    @info
    def run():
        while (current := current_character()):
            if (enemy := enemy_character()):
                attack(current, enemy)
            else:
                break

    return run

if __name__ == '__main__':
    create_character = use_character()
    hero = create_character(name='hero', hp=100)
    enemy1 = create_character(name='enemy1', hp=5, group=ENEMY)
    enemy2 = create_character(name='enemy2', hp=3, group=ENEMY)

    game([hero, enemy1, enemy2])()
