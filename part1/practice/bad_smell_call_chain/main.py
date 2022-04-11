# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self):
        self.planet = Planet()

    def get_person_room(self):
        return self.planet.get_contry().get_city().get_street().get_room().get_name()

    def get_city_population(self):
        return self.planet.get_contry().get_city().population()


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.
class Person_1:
    def __init__(self, country, city, street, room, building, city_population):
        self.country = country
        self.city = city
        self.street = street
        self.building = building
        self.room = room
        self.city_population = city_population

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_city_population(self):
        return self.city_population

    def get_room(self):
        return self.room

    def get_full_address(self):
        return f"{self.country}, {self.city}, {self.street}, {self.building}, {self.room}"
