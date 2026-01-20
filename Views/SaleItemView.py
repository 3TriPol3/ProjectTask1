from tkinter import *
from tkinter import ttk

from Controllers.GameItemController import *


class SaleItemView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Передать предмет")
        self.geometry("1280x800")

        self.label_frame = ttk.Frame(self,padding=[20])
        self.label_frame.pack(anchor=CENTER,pady=10,padx=10)

        self.label = ttk.Label(self.label_frame, text="Передать предмет")
        self.label.pack()

        # Таблица
        self.table_frame = ttk.Frame(self, padding=[20])
        self.table_frame.pack(anchor=CENTER, pady=10, padx=10)
        # Таблица
        self.columns = ('id', "name", 'rarity', 'player', 'quantity', 'stats')  # Столбцы
        self.table_data = ttk.Treeview(self.table_frame, columns=self.columns, show='headings')
        # Заголовки
        self.table_data.heading('id', text="№")
        self.table_data.heading('name', text='Имя')
        self.table_data.heading('rarity', text='Уникальность')
        self.table_data.heading('player', text='Имя Игрока')
        self.table_data.heading('quantity', text='Количество')
        self.table_data.heading('stats', text='Характеристика')
        # Превращает объекты из БД в список кортежей для таблицы
        self.table()
        # Для события выбора строки из таблицы вызову метод row_selected
        self.table_data.bind("<<TreeviewSelect>>", self.row_selected)
        # Передача предмета
        self.sale_frame = ttk.Frame(self,padding=[20])
        self.sale_frame.pack(anchor=CENTER, padx=10,pady=10)

        self.sale_label = ttk.Label(self.sale_frame,text="Игрок")
        self.sale_label.grid(row=0, column=0)
        self.sale_entry = ttk.Entry(self.sale_frame)
        self.sale_entry.grid(row=1,column=0)

        self.sale_button = ttk.Button(self.sale_frame,text="Передать")
        self.sale_button.grid(row=1,column=1, padx=15)

        # Для обновления данных в таблице создал метод добавления записей из БД

    def table(self):
        # Очистить старые записи
        for item in self.table_data.get_children():
            self.table_data.delete(item)

        self.elemnt = []
        for el in GameItemController.get():
            self.elemnt.append(
                (el.id, el.name, el.rarity, el.player, el.quantity, el.stats)
            )

        # Вывод данных из БД в таблицу
        for item in self.elemnt:
            self.table_data.insert("", END, values=item)
        self.table_data.pack()
    def row_selected(self):
        '''
        Метод передаст данные о выбранной записи - > передаст строку
        :return:
        '''
        # С помощью метода selection() self.row передаётся список из одной строки / [['id,name,...']]
        # Выделить одну строку можно с помощью [0] - индекса
        self.row = self.table_data.selection()[0]
if __name__ == "__main__":
    win = SaleItemView()
    win.mainloop()


