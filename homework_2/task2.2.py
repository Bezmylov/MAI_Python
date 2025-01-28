class DataBuffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        self.buffer.append(data)
        if len(self.buffer) >= 5:
            print("Переполнение буфера. Буфер будет очищен.")
            self.buffer.clear()

    def get_data(self):
        if not self.buffer:
            print("Буфер пуст. Нет данных для извлечения.")
        else:
            print("Данные в буфере:", self.buffer)
            return self.buffer

# Пример использования
buffer = DataBuffer()

# Добавляем данные
buffer.add_data(1)
buffer.add_data(2)
buffer.add_data(3)
buffer.get_data()  # Должен вывести [1, 2, 3]

buffer.add_data(4)
buffer.add_data(5)  # После добавления 5-го элемента происходит очистка буфера
buffer.get_data()  # Должен вывести сообщение, что буфер пуст

buffer.add_data(6)
buffer.get_data()  # Должен вывести [6]
