class Hero:
    """Добавлен базовый класс Hero"""

    def __init__(self, name):
        """Написан конструктор для класса"""
        self.__name = name
        self.__my_hero_skills = []
        self.__level = 0
        self.__exp = 0
        self.__mage_skills = ["огненный шар", "ледяная стрела", "удар молнии"]
        self.__warrior_skills = ["удар в прыжке", "вой", "берсерк"]
        self.__ranger_skills = ["быстрая стрельба", "двойной выстрел", "скрытность"]

    def get_name(self):
        return self.__name

    def get_my_hero_skills(self):
        return self.__my_hero_skills

    def get_level(self):
        return self.__level

    def get_exp(self):
        return self.__exp

    def get_skills(self, character_class):
        """Добавлен геттер для навыков, результат зависит от выбранного класса"""
        if character_class == 'воин':
            return self.__warrior_skills
        elif character_class == 'маг':
            return self.__mage_skills
        elif character_class == 'рейнджер':
            return self.__ranger_skills
        else:
            exit("Ошибка: перезапустите программу!")

    def get_new_level(self):
        if self.get_exp() >= 1000:
            self.level = 3
            self.add_skill()

        elif self.get_exp() >= 500:
            self.level = 2
            self.add_skill()

        elif self.get_exp() >= 200:
            self.level = 1
            self.add_skill()
        else:
            self.__level = 0
        return f"Герой {self.name}, теперь {self.level} уровня, навыки: {', '.join(self.get_my_hero_skills())}"

    def add_exp(self, exp):
        self.exp += exp
        new_level = self.get_new_level()
        return new_level

    def add_skill(self):
        pass


class MyHero(Hero):
    pass
