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
            self.__level = 3
            self.add_skill()

        elif self.get_exp() >= 500:
            self.__level = 2
            self.add_skill()

        elif self.get_exp() >= 200:
            self.__level = 1
            self.add_skill()
        else:
            self.__level = 0
        return f"Герой {self.get_name()}, теперь {self.get_level()} уровня, навыки: {', '.join(self.get_my_hero_skills())}"

    def add_exp(self, exp):
        self.__exp += exp
        new_level = self.get_new_level()
        return new_level

    def add_skill(self):
        pass


class MyHero(Hero):
    def __init__(self, name, character_class):
        super().__init__(name)
        self.__character_class = character_class
        self.__skill_list = super().get_skills(character_class)
        self.__my_hero_skills = []


    def get_character_class(self):
        return self.__character_class

    def get_skill_list(self):
        return self.__skill_list

    def get_my_hero_skills(self):
        return self.__my_hero_skills

    def add_skill(self):
        if super().get_level() > 0:
            while True:
                if len(self.get_my_hero_skills()) == super().get_level():
                    break
                else:
                    choisen_skill = input(f"\nВыберите навык: {self.get_skill_list()}")
                    if choisen_skill.lower() in self.get_skill_list():
                        self.__my_hero_skills.append(choisen_skill)
                        self.__skill_list.remove(choisen_skill)
                        print(f"\nТекущие навыки: {self.get_my_hero_skills()}")
                    else:
                        print "\nНекорректный ввод!"
        else:
            return "Ошибка: уровень вашего героя равен 0"
