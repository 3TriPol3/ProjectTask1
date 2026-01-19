from tkinter import *
from tkinter import ttk

from Controllers.GameItemController import GameItemController



class SaerchView(Tk):
    def __init__(self, search_string):
        super().__init__()

        self.search_string = search_string # Из строки поиска в окне GameItemView, занчение предаётся атрибуту self.search_string

        # Атрибуты окна
        self.title("Найденые предметы")
        self.geometry("1280x800")

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
        for row in GameItemController.search_stats(self.search_string):
            self.elemnt.append(
                (row.id,row.name,row.rarity,row.player,row.quantity,row.stats)
            )
        # Вывод данных из списка   self.elemnt в таблицу   self.table_data
        for item in self.elemnt:
            self.table_data.insert("", END,values=item)
        self.table_data.pack()

        #Кнопка закрытия окна / перехода в главное
        self.button_close = ttk.Button(self,text="Вернуться на главную страницу", command=self.destroy)
        self.button_close.pack(anchor=CENTER)
        #Переход на главное окно
        self.button_move = ttk.Button(self, text="Вернуться на главную страницу 2", command=self.move)
        self.button_move.pack(anchor=CENTER)

    def move(self):
        from Views.GameItemView import GameItemView
        window_home = GameItemView()
        self.destroy()

if __name__ == "__main__":
    window = SaerchView(search_string="")
    window.mainloop()