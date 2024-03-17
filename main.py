from src.hh_api import HeadHunterAPI
from src.sql_config import config
from src.db_setup import DatabaseSetUp
from src.utils import start_user_interaction, user_interaction

employers_dict = {'Яндекс': '1740',
                  'epam': '29740',
                  'Sber': '3529',
                  'Whoosh': '3536822',
                  'Банк ВТБ (ПАО)': '1440683',
                  'RuTube': '78638',
                  'Cian': '1429999',
                  'RosNeft': '6596',
                  'Gazprom': '2159482',
                  'SeverStal': '6041'}
params = config()


def sql_setup():
    api_connect = HeadHunterAPI(employers_dict)
    vacancies = api_connect.get_vacancies()

    db_setup = DatabaseSetUp('hh_parser', params)
    db_setup.create_database()
    db_setup.create_table()
    db_setup.employers_to_db(employers_dict)
    db_setup.vacancies_to_db(vacancies)


def main():
    params.update({'dbname': 'hh_parser'})

    start_user_interaction(employers_dict)
    user_interaction(params)


if __name__ == "__main__":
    sql_setup()
    main()
