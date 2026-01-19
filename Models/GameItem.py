from Models.Base import *

class GameItem(BaseModel):
    '''
    Данный класс описывает таблицу в БД с игровыми объектами
    '''
    id  = PrimaryKeyField()
    name = CharField(unique=True) # название предмета
    rarity = CharField() # редкость
    player = CharField() # игрок
    quantity = IntegerField()
    stats = CharField()

if __name__ == "__main__":
    mysql_db.create_tables([GameItem])