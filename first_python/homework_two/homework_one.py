# 定义手机电量的类
class Phone_electricity:
    def __init__(self, electricity):
        self.electricity = electricity

    # 玩游戏
    def playgame(self, playgame_time):
        self.electricity_final = self.electricity - playgame_time * 10
        if self.electricity_final < 0:
            print("电量不足，已关机")
        else:
            print(f"你今天玩了{playgame_time}小时的游戏了,剩余电量{self.electricity_final}")

    # 看电影
    def see_movie(self, movie_time):
        self.electricity_movied = self.electricity_final - movie_time * 5
        if self.electricity_final < 0:
            print("电量不足，已关机")
        else:
            print(f"你看了{movie_time}小时的电影了，还剩电量{self.electricity_movied}")

    # 听音乐
    def listen_music(self, listen_time):
        self.electricity_listend = self.electricity_movied - listen_time * 3
        if self.electricity_final < 0:
            print("电量不足，已关机")
        else:
            print(f"你听了{listen_time}小时的音乐了，还剩电量{self.electricity_movied}")


final = Phone_electricity(100)
final.playgame(50)
final.see_movie(3)
final.listen_music(5)


# 手机充电的类
class phone_charging(Phone_electricity):
    # 快充
    def qucik(self, time):
        self.electricity = self.electricity + time * 3
        if self.electricity >= 100:
            print("充满了")
        else:
            print(f"已经冲到{self.electricity}的电量了")

    # 慢充
    def slow(self, time):
        self.electricity = self.electricity + time * 1
        if self.electricity >= 100:
            print("充满了")
        else:
            print(f"已经冲到{self.electricity}的电量了")


charging_electricity = phone_charging(30)
charging_electricity.qucik(10)
charging_electricity.slow(20)
