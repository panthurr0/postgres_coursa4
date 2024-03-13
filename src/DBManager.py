from config import config
import psycopg2


class DBManager:
    def __init__(self, params, name):
        self.params = params
        self.name: str = name

    def create_database(self):
        conn = psycopg2.connect(dbname='postgres', **self.params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f'DROP DATABASE {self.name}')
        cur.execute(f'CREATE DATABASE {self.name}')

        cur.close()
        conn.close()

    def create_table(self, cur):
        cur.execute(f'CREATE TABLE {self.name}('
                    f'vacancy_id serial PRIMARY KEY,'
                    f'vacancy_name text,'
                    f'description text,'
                    f'salary_from int,'
                    f'salary_to int,'
                    f'currency text,'
                    f'alternative_url text'
                    f')')

    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass
