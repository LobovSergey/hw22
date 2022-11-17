# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self, population, room_number):
        self._population = population
        self._room_number = room_number

    def get_population(self):
        return self._population

    def get_room_number(self):
        return self._room_number


person = Person(100, 1)
person.get_population()
person.get_room_number()
