class Ученик:
    def __init__(self, имя, возраст, любимый_предмет):
        self.имя = имя
        self.возраст = возраст
        self.любимый_предмет = любимый_предмет

    def учиться(self):
        print(f"Ученик {self.имя} учится. Его любимый предмет - {self.любимый_предмет}.")

    def отдыхать(self):
        print(f"Ученик {self.имя} отдыхает.")

    def читать(self):
        print(f"Ученик {self.имя} читает.")


class Компьютер:
    def __init__(self, модель, операционная_система):
        self.модель = модель
        self.операционная_система = операционная_система

    def работать(self):
        print(f"Компьютер модели {self.модель} с операционной системой {self.операционная_система} работает.")

    def играть(self):
        print(f"Компьютер модели {self.модель} с операционной системой {self.операционная_система} играет.")


class Пользователь:
    def __init__(self, имя):
        self.имя = имя

    def использовать(self, устройство):
        print(f"Пользователь {self.имя} использует {устройство}.")


# Создание объектов классов
ученик1 = Ученик("Иван", 12, "Математика")
компьютер1 = Компьютер("Dell", "Windows 10")
пользователь1 = Пользователь("Алексей")

# Демонстрация работы объектов
ученик1.учиться()
ученик1.читать()
компьютер1.работать()
компьютер1.играть()
пользователь1.использовать("компьютер")
пользователь1.использовать("смартфон")
