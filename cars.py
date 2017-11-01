# -*- coding: utf-8 -*-
import csv
import os

class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except ValueError:
            pass    

    def get_photo_file_ext(self):
        split_path = os.path.splitext(self.photo_file_name)
        return split_path[1]

class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        CarBase.__init__(self, car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        CarBase.__init__(self, car_type, brand, photo_file_name, carrying)
        self.body_whl = body_whl
        if self.body_whl == '':
            self.body_length, self.body_width, self.body_height = 0, 0, 0
        else:
            try:
                self.params = body_whl.split('x')
                self.body_length = float(self.params[0])
                self.body_width = float(self.params[1])
                self.body_height = float(self.params[2])
            except ValueError:
                print 'not correct volume'
                self.body_length, self.body_width, self.body_height = 0, 0, 0
                
    def get_body_volume(self):

        if 0 not in self.params:
            return self.body_length*self.body_width*self.body_height
        return 0

class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        CarBase.__init__(self, car_type, brand, photo_file_name, carrying)
        self.extra = extra.decode("utf-8")

d = {'car': Car, 'truck': Truck, 'spec_machine': SpecMachine}
attrs = 'car_type;brand;passenger_seats_count;photo_file_name;body_whl;carrying;extra'

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row[0] == 'car':
                    car_list.append(d[row[0]](row[0], row[1], row[3], row[5], row[2]))
                elif row[0] == 'truck':
                    car_list.append(d[row[0]](row[0], row[1], row[3], row[5], row[4]))
                elif row[0] == 'spec_machine':
                    car_list.append(d[row[0]](row[0], row[1], row[3], row[5], row[6]))
            except IndexError:
                continue

    return car_list

#car_list = get_car_list('_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv')
#print car_list


