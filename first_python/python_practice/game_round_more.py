def game():
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 201
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        if my_hp <= 0:
            print('你赢了')
            break
        elif enemy_hp <= 0:
            print('我赢了')
            break

game()
