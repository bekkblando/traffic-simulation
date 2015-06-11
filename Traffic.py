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

    def check_car_pos(self, car):
         
         pass


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
        pass

    def stop(self):
        pass

    def slow(self):
        pass

    def move(self):
        pass

    def check_road(self):
        pass

    def track_progress(self):
        self.track.append(self.position)

road = Road()
print(road.road)
print(road.car_list)
print(road.car_list[0])
