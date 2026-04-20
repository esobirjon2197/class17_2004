# 17-m
class Speed:
    def __init__(self, speed):
        self.speed = speed

    def check(self):
        if self.speed == 100:
            print("Speed is 100")
        else:
            print("Normal")

s1 = Speed(100)
s1.check()
