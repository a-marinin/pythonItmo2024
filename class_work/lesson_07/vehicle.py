class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def print_info(self):
        print(f'Марка: {self.make}'
              f'\nМодель: {self.model}'
              f'\nГод выпуска: {self.year}'
              f'\nСтоимость: {self.price} руб.')


class Car(Vehicle):
    def __init__(self, make, model, year, price, num_doors, body_style):
        super().__init__(make, model, year, price)
        self.num_doors = num_doors
        self.body_style = body_style


car = Car(make='Toyota', model='Camry', year=2023, price=29000000, num_doors=5, body_style='седан')
car.print_info()
