# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, x: int, y: int, speed=1):
        self.field = field
        self.x = x
        self.y = y
        self.speed = speed

    def move_on_direction(self, direction, status):
        self.speed = self._get_speed(status)
        if direction == 'UP':
            self.field.set_unit(y=self.y + self.speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - self.speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - self.speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + self.speed, unit=self)

    def _get_speed(self, status):
        if status == 'fly':
            return self.speed * 1.2
        elif status == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Неверное состояние')

