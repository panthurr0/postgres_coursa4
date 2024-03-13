from src.hhapi import HeadHunterAPI
from src.DBManager import DBManager
from src.config import config
import psycopg2


db_list = ('epam', 'Tinkoff', 'Sber', 'Whoosh', 'SkyPro', 'RuTube', 'Циан', 'Роснефть', 'Газпром', 'Северсталь')

user_input = int(input(f'Выберите ДБ из списка: '
                   f'0 - {db_list[0]}'
                   f'1 - {db_list[1]}'
                   f'2 - {db_list[2]}'
                   f'3 - {db_list[3]}'
                   f'4 - {db_list[4]}'
                   f'5 - {db_list[5]}'
                   f'6 - {db_list[6]}'
                   f'7 - {db_list[7]}'
                   f'8 - {db_list[8]}'
                   f'9 - {db_list[9]}'
                   ))

DB = DBManager(db_list[user_input])


# epam = DBManager('epam')
# Tinkoff = DBManager('Tinkoff')
# Sber = DBManager('Sber')
# Whoosh = DBManager('Whoosh')
# SkyPro = DBManager('SkyPro')
# RuTube = DBManager('RuTube')
# Cian = DBManager('Циан')
# RosNeft = DBManager('Роснефть')
# Gazprom = DBManager('Газпром')
# SeverStal = DBManager('Северсталь')


def main():
    params = config()
    conn = None
    DB = DBManager(db_list[user_input])


    DB.create_database()
    print(f"БД {DB.name} успешно создана")

    params.update({'dbname': DB.name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                execute_sql_script(cur, script_file)
                print(f"БД {db_name} найдена")

                create_suppliers_table(cur)
                print(f"Таблица {DB.name} успешно создана")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
        conn.close()