from threading import Thread
from time import sleep
from datetime import datetime

time_start = datetime.now()


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100 # колличество врагов
        while enemy > 0:
            enemy -= self.power
            sleep(1) # Прошел день
            time_end = datetime.now()
            time_result = (time_end - time_start)
            print(f'{self.name} сражается {time_result.seconds} день(дня)..., осталось {enemy} воинов.')
        time_end = datetime.now()
        time_result = time_end - time_start
        print(f'{self.name} одержал победу спустя {time_result.seconds} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
