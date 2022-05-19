class Road:
    def __init__(self, length: int, width: int):
        """конструктор класса
        :param length: длинна в метрах
        :param width: ширина в метрах
        """
        self.length = length
        self.width = width
    def calculate(self, height: int = 5, mass_m_2: int = 25) -> int:
        """
        считает масу массу асфальта, необходимого для покрытия всей дороги в тоннах
        :param height: высота дорожного полотна в сантиметрах
        :param mass_m_2: масса в кг квадратного метра дороги высотой 1 см
        :return: int значение тонн, дробная часть если есть НЕ учитывается
        """
        result = (self.length * self.width * height * mass_m_2) / 1000
        return int(result)


if __name__ == '__main__':
    road = Road(15, 15)
    print(f'Для изготовления покрытия дороги нужно {road.calculate()} тонн.')