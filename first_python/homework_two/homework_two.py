"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
1、see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，
打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
2、fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，
进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""


class TongLao:
    def __init__(self, HP, power):
        self.HP = HP
        self.power = power

    def see_people(self, name):
        if name == "无崖子" or name == 'WYZ':
            print("师弟！！！！")
        elif name == '李秋水':
            print('呸，贱人')
        elif name == '丁春秋':
            print("叛徒！我杀了你")

    # 2、fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，
    # 进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
    def fight_zms(self, your_hp, your_power):
        your_hp = 1000
        your_power = 100
        self.HP_zms = self.HP / 2
        self.power_zms = self.power * 10
        your_final_hp = your_hp - self.power_zms
        my_final_hp = self.HP_zms - your_power
        if your_final_hp > my_final_hp:
            print('惜败')
        else:
            print('输了吧')


# 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
class XuZhu(TongLao):
    def __init__(self, xz_hp, xz_power):
        self.xz_hp = xz_hp
        self.xz_power = xz_power

    def read(self):
        print('罪过罪过')


babu = TongLao(500, 50)
babu.see_people('WYZ')
babu.fight_zms(100, 30)
xz = XuZhu(300, 100)
xz.read()
