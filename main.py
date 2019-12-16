
from game import Game, Character, Group

if __name__ == '__main__':

    hero = Character(
        name="主人公",
        group=Group.PLAYER,
        attack_power=1,
        hp=100,
        next_level_exp=10
    )
    enemy1 = Character(
        name="エネミー1",
        group=Group.ENEMY,
        attack_power=1,
        hp=3
    )
    enemy2 = Character(
        name="エネミー2",
        group=Group.ENEMY,
        attack_power=1,
        hp=5
    )

    game = Game([hero, enemy1, enemy2])
    game.run()
    game.status()
