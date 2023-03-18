from random2 import randint

class Die():
    """Класс, моделирующий кубик"""

    def __init__(self, num_sides=6):
        """По умолчанию используется шестигранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        """Возвращает случайное число от 1 до числа граней"""
        return randint(1, self.num_sides)