from Models.GameItem import *

class GameItemController:
    '''
    методы:
        добавить предмет,
        торговать между игроками,
        найти по характеристикам
    '''
    @classmethod
    def add(cls,name,rarity,player,quantity,stats):
        # добавить предмет в Таблицу
        try:
            GameItem.create(
            name = name,
            rarity = rarity,
            player = player,
            quantity = quantity,
            stats = stats
            )
        except:
            print("Ошибка создания игрового предмета")
    @classmethod
    def get(cls):
        # Выводит список записей из таблицы БД
        return GameItem.select()

    @classmethod
    def update(cls, id, player):
        # Обновить запись по id
        GameItem.update({GameItem.player:player}).where(GameItem.id == id).execute()
    @classmethod
    def search_stats(cls,stats):
        # Метод выводит список записей, если встречается характеристика stats
        # list = [] # создание пустого списка
        query = GameItem.select().where(GameItem.stats == stats) # переменной передаём список записей у которых в поле stats есть stats из аргумента метода
        # for item in query:
        #     list.append(item.name)
        return query


if __name__ == "__main__":
    GameItemController.add(
        name="Зелье здоровья",
        rarity="обычный",
        player="Mage456",
        quantity=15,
        stats="восстановление: 100 HP"
    )
    GameItemController.update(2,'Warrior123')
    for item in GameItemController.get():
        print(item.name, item.player)

    print(GameItemController.search_stats("урон: 150, прочность: 200"))
