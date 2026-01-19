from tkinter import *
from tkinter import ttk
from Controllers.GameItemController import *
from Views.SearchView import SaerchView


class GameItemView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Инвентарь для игр")
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
        # Фрайм в которм расположен текст Добавить Предмет (находится внутри фрейма add_frame)
        self.add_title_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,  # тип линии фрейма - СПЛОШНАЯ
                                         borderwidth=1,  # ширина границы фрейма
                                         padding=[8, 10])
        self.add_title_frame.pack(anchor=CENTER,  # расположение по центру
                          fill=X,  # заполнение
                          padx=10,  # расположение по оси x от верней левой точки окна
                          pady=10,  # расположение по оси y от верней левой точки окна
                          )
        self.add_title = ttk.Label(self.add_title_frame, text="Добавить Предмет")
        self.add_title.pack()
        # Фрайм в которм расположены окна ввода данных о Предмете (находится внутри фрейма add_frame)
        self.add_input_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,  # тип линии фрейма - СПЛОШНАЯ
                                         borderwidth=1,  # ширина границы фрейма
                                         padding=[8, 10]
                                         )
        self.add_input_frame.pack(fill=X,  # заполнение
                              padx=10,  # расположение по оси x от верней левой точки окна
                              pady=10,  # расположение по оси y от верней левой точки окна
                              )
        # Окна ввода данных предмета для добавленпия в таблицу БД
        self.add_title_name = ttk.Label(self.add_input_frame, text="Название")
        self.add_title_name.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.add_title_rarity = ttk.Label(self.add_input_frame, text="Уникальность")
        self.add_title_rarity.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.add_title_player = ttk.Label(self.add_input_frame, text="Игрок")
        self.add_title_player.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        self.add_title_quantity = ttk.Label(self.add_input_frame, text="Количество")
        self.add_title_quantity.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

        self.add_title_stats = ttk.Label(self.add_input_frame, text="Характерстики")
        self.add_title_stats.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)

        self.add_name = ttk.Entry(self.add_input_frame)
        self.add_name.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.add_rarity = ttk.Entry(self.add_input_frame)
        self.add_rarity.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.add_player = ttk.Entry(self.add_input_frame)
        self.add_player.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        self.add_quantity = ttk.Entry(self.add_input_frame)
        self.add_quantity.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

        self.add_stats = ttk.Entry(self.add_input_frame)
        self.add_stats.grid(row=1, column=4, sticky="nsew", padx=5, pady=5)

        self.add_button = ttk.Button(self.add_input_frame, text="Добавить", command=self.add_data)
        self.add_button.grid(row=1, column=5, sticky="nsew", padx=5, pady=5)

        # Фрейм Вывод предметов
        self.get_data = ttk.Frame(
            self,
            relief="raised",
            borderwidth=3,
            padding=[5]
        )
        self.get_data.pack(
            anchor=CENTER
        )
        # Таблица
        self.columns = ('id',"name",'rarity','player','quantity','stats') # Столбцы
        self.table_data = ttk.Treeview(self.get_data,columns=self.columns,show='headings')
        # Заголовки
        self.table_data.heading('id', text="№")
        self.table_data.heading('name',text='Имя')
        self.table_data.heading('rarity',text='Уникальность')
        self.table_data.heading('player',text='Имя Игрока')
        self.table_data.heading('quantity',text='Количество')
        self.table_data.heading('stats',text='Характеристика')
        # Превращает объекты из БД в список кортежей для таблицы
        self.table()
        # Фрейм для окна поиска
        self.search_frame = ttk.Frame(
            self,
            relief=SOLID,
            borderwidth=1,
            padding=[8,10]
        )
        self.search_frame.pack(
            fill=X,  # заполнение
            padx=10,  # расположение по оси x от верней левой точки окна
            pady=10,
        )
        self.label_search = ttk.Label(self.search_frame, text="Найти предмет по характеристикам")
        self.label_search.grid(row=0)
        self.text_search = Text(self.search_frame, height=5, width=50)
        self.text_search.grid(row=1,column=0)
        self.button_search = ttk.Button(self.search_frame,text="Найти", command=self.search)
        self.button_search.grid(row=1,column=2, padx=5,sticky="s")
    # метод передачи значения из строки ввода text_search в окно SaerchView
    def search(self):
        self.string = self.text_search.get("1.0","end") # передачи значения из строки ввода text_search
        self.string = self.string.strip()
        window = SaerchView(search_string=self.string)

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




    # Методы для кнопок
    def add_data(self):
            self.name = self.add_name.get()
            self.rarity = self.add_rarity.get()
            self.player = self.add_player.get()
            self.quantity = self.add_quantity.get()
            self.stats = self.add_stats.get()
            GameItemController.add(
                self.name,
                self.rarity,
                self.player,
                self.quantity,
                self.stats
            )
            # Обновить данные табли Treeview
            self.table()
            # Очистить поля ввода
            self.clear()
    def clear(self):
        '''
        Метод очистит окна Treeview

        :return:
        '''
        self.add_name.delete(0,END) # c 0-го идекса до конца
        self.add_rarity.delete(0,END) # c 0-го идекса до конца
        self.add_player.delete(0,END) # c 0-го идекса до конца
        self.add_quantity.delete(0,END) # c 0-го идекса до конца
        self.add_stats.delete(0,END) # c 0-го идекса до конца


if __name__ == "__main__":
    window = GameItemView()
    window.mainloop()
