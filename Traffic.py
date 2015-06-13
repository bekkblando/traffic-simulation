import numpy as np


class Road:

    def __init__(self, size=101, number_of_cars=50):
        self.size = size
        self.road = self.create_road(size)
        self.car_list = self.place_cars(number_of_cars)

    def place_cars(self, number_of_cars):
        car_list = []
        for num in range(number_of_cars):
            car = Car(num, num)
            car_list.append((car, num))
        return car_list

    def create_road(self, size):
        return np.arange(size)

    def check_car_pos(self, check_car):
        selected_car = [self.car_list[number] for number, item in enumerate(
            self.car_list) if item[1] == check_car]
        return selected_car


class Car:

    def __init__(self, position=0, car_num=0):
        self.position = position
        self.size = 5
        self.accel = 2
        self.car_num = car_num
        self.max_speed = 120
        self.track = []
        self.speed = 0

    def __str__(self):
        return "Car" + str(self.position)

    def accelerate(self):
        self.speed += 2

    def stop(self):
        self.speed = 0

    def slow(self):
        self.speed -= 2

    def move(self):
        self.position += self.speed

    def check_road(self):
        

    def track_progress(self):
        self.track.append(self.position)

road = Road()
print(road.road)
print(road.car_list)
print(road.car_list[5])
print(road.check_car_pos(0))
