from datetime import datetime

class Animal:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = self.get_valid_date(date_of_birth)
        self.commands = []

    def get_valid_date(self, date_str):
        while True:
            try:
                if isinstance(date_str, str):
                    return datetime.strptime(date_str, "%Y-%m-%d")
                else:
                    return date_str
            except ValueError:
                print("Ошибка: Неправильный формат даты. Используйте гггг-мм-дд.")
                date_str = input("Введите дату рождения животного заново: ")

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Дата рождения: {self.date_of_birth.strftime('%Y-%m-%d')}")
        print("Команды:", ', '.join(self.commands))
        print()


class Dog(Animal):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)


class Cat(Animal):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)


class Hamster(Animal):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)


class Horse(Animal):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)


class Camel(Animal):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)


class Donkey(Animal):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)


def add_animal():
    name = input("Введите имя животного: ")
    date_of_birth = input("Введите дату рождения животного (гггг-мм-дд): ")

    return Animal(name, date_of_birth)


def main():
    animals_registry = []

    while True:
        print("\n=== Реестр домашних животных ===")
        print("1. Добавить животное")
        print("2. Увидеть информацию о животном")
        print("3. Обучить животное новым командам")
        print("4. Показать список всех животных")
        print("0. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            print("Выберите класс животного:")
            print("1. Собака")
            print("2. Кошка")
            print("3. Хомяк")
            print("4. Лошадь")
            print("5. Верблюд")
            print("6. Осел")

            animal_type_choice = input("Ваш выбор: ")
            animal = None

            new_animal = add_animal()

            if animal_type_choice == "1":
                animal = Dog(new_animal.name, new_animal.date_of_birth)
            elif animal_type_choice == "2":
                animal = Cat(new_animal.name, new_animal.date_of_birth)
            elif animal_type_choice == "3":
                animal = Hamster(new_animal.name, new_animal.date_of_birth)
            elif animal_type_choice == "4":
                animal = Horse(new_animal.name, new_animal.date_of_birth)
            elif animal_type_choice == "5":
                animal = Camel(new_animal.name, new_animal.date_of_birth)
            elif animal_type_choice == "6":
                animal = Donkey(new_animal.name, new_animal.date_of_birth)
            else:
                print("Неверный выбор. Пожалуйста, выберите класс.")
                continue

            animals_registry.append(animal)
            print(f"Животное {animal.name} успешно добавлено в реестр.")

        elif choice == "2":
            name = input("Введите имя животного: ")
            for animal in animals_registry:
                if animal.name == name:
                    animal.show_info()
                    break
            else:
                print(f"Животное с именем {name} не найдено в реестре.")

        elif choice == "3":
            print("Список всех животных:")
            for animal in animals_registry:
                print(animal.name)
            name = input("Введите имя животного: ")

            for animal in animals_registry:
                if animal.name == name:
                    command = input("Введите новую команду для животного: ")
                    animal.commands.append(command)
                    print(f"Команда {command} успешно добавлена для животного {animal.name}.")
                    break
            else:
                print(f"Животное с именем {name} не найдено в реестре.")

        elif choice == "4":
            print("Список всех зарегистрированных животных:")
            for animal in animals_registry:
                animal.show_info()

        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
