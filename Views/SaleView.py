from tkinter import *
from tkinter import ttk

from Controllers.GameItemController import *
from Views.SearchView import SaerchView
from Views.GameItemView import GameItemView

class SaleView(Tk):
    def __init__(self, sale_string):
        super().__init__()

        self.sale_string = sale_string

        # Атрибуты окна
        self.title("Продажа")
        self.geometry("1280x800")

        # Фрейм Добавить предмет
        self.add_frame = ttk.Frame(self,
                                   borderwidth=1,  # ширина границы фрейма
                                   relief=SOLID,  # тип линии фрейма - СПЛОШНАЯ
                                   padding=[18],  # внутренние отступы фрейма
                                   )
        self.add_frame.pack(
            anchor=CENTER,  # расположение по центру
            fill=X,  # заполнение
            padx=10,  # расположение по оси x от верней левой точки окна
            pady=10,  # расположение по оси y от верней левой точки окна

        )

        # Фрайм в которм расположен текст Передать Предмет (находится внутри фрейма add_frame)
        self.add_title_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,  # тип линии фрейма - СПЛОШНАЯ
                                         borderwidth=1,  # ширина границы фрейма
                                         padding=[8, 10])
        self.add_title_frame.pack(anchor=CENTER,  # расположение по центру
                                  fill=X,  # заполнение
                                  padx=10,  # расположение по оси x от верней левой точки окна
                                  pady=10,  # расположение по оси y от верней левой точки окна
                                  )
        self.add_title = ttk.Label(self.add_title_frame, text="Передать Предмет")
        self.add_title.pack()

        # Фрейм для таблицы
        self.table_frame = ttk.Frame(
            self,
            padding=20
        )
        self.table_frame.pack(
            anchor=CENTER,
            fill=X,
            padx=10,
            pady=10
        )
        # Создание таблицы
        self.columns = ('id', "name", 'rarity', 'player', 'quantity', 'stats')  # Столбцы
        self.table_data = ttk.Treeview(self, columns=self.columns, show='headings')
        # Заголовки
        self.table_data.heading('id', text="№")
        self.table_data.heading('name', text='Имя')
        self.table_data.heading('rarity', text='Уникальность')
        self.table_data.heading('player', text='Имя Игрока')
        self.table_data.heading('quantity', text='Количество')
        self.table_data.heading('stats', text='Характеристика')

        self.elemnt = []
        for row in GameItemController.search_stats(self.sale_string):
            self.elemnt.append(
                (row.id, row.name, row.rarity, row.player, row.quantity, row.stats)
            )
        # Вывод данных из списка   self.elemnt в таблицу   self.table_data
        for item in self.elemnt:
            self.table_data.insert("", END, values=item)
        self.table_data.pack()

        # Фрейм для окна добавления
        self.sale_frame = ttk.Frame(
            self,
            relief=SOLID,
            borderwidth=1,
            padding=[8, 10]
        )
        self.sale_frame.pack(
            fill=X,  # заполнение
            padx=10,  # расположение по оси x от верней левой точки окна
            pady=10,
        )
        self.label_search = ttk.Label(self.sale_frame, text="Игрок")
        self.label_search.grid(row=0)
        self.text_search = Text(self.sale_frame, height=2, width=20)
        self.text_search.grid(row=1, column=0)
        self.button_search = ttk.Button(self.sale_frame, text="Добавить", command=self.search)
        self.button_search.grid(row=1, column=2, padx=5, sticky="s")

        # # Кнопка закрытия окна / перехода в главное
        # self.button_close = ttk.Button(self, text="Вернуться на главную страницу", command=self.destroy)
        # self.button_close.pack(anchor=CENTER)
        # # Переход на главное окно
        # self.button_move = ttk.Button(self, text="Вернуться на главную страницу 2", command=self.move)
        # self.button_move.pack(anchor=CENTER)

    def move(self):
        from Views.GameItemView import GameItemView
        window_home = GameItemView()
        self.destroy()

# метод передачи значения из строки ввода text_search в окно SaerchView
    def search(self):
        self.string = self.text_search.get("1.0","end") # передачи значения из строки ввода text_search
        self.string = self.string.strip()
        window = SaerchView(search_string=self.string)
        self.destroy()

    # Для обновления данных в таблице создал метод добавления записей из БД
    def table(self):
        # Очистить старые записи
        for item in self.table_data.get_children():
            self.table_data.delete(item)

        self.elemnt =[]
        for el in GameItemController.get():
            self.elemnt.append(
                (el.id,el.name,el.rarity,el.player,el.quantity,el.stats)
            )

        #Вывод данных из БД в таблицу
        for item in self.elemnt:
            self.table_data.insert("",END,values=item)
        self.table_data.pack()

if __name__ == "__main__":
    window = SaleView(sale_string="")
    window.mainloop()
