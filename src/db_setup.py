import psycopg2


class DatabaseSetUp:

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def create_database(self):
        """
        Создаёт базы данных SQL.
        """
        conn = psycopg2.connect(dbname='postgres', **self.params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f'DROP DATABASE IF EXISTS {self.name}')
        cur.execute(f'CREATE DATABASE {self.name}')

        cur.close()
        conn.close()

    def create_table(self):
        """
        Создаёт таблицы companies и vacancies в базе данных.
        """
        conn = psycopg2.connect(dbname=self.name, **self.params)
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE companies (
                company_id int primary key,
                company_name varchar unique not null,
                foreign key(company_name) references companies(company_name)
                )
                """)

        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE vacancies (
                    vacancy_id serial primary key,
                    vacancy_name text not null,
                    salary int,
                    company_name text not null,
                    vacancy_url varchar not null
                    )
                    """)

        conn.commit()
        conn.close()

    def employers_to_db(self, emp_dict):
        """
        Сохраняет работодателей в БД
        """
        with psycopg2.connect(dbname=self.name, **self.params) as conn:
            with conn.cursor() as cur:
                for employer in emp_dict:
                    cur.execute(
                        f"INSERT INTO companies values ('{int(emp_dict[employer])}', '{employer}')")

        conn.commit()
        conn.close()

    def vacancies_to_db(self, vacancies):
        """
        Сохраняет вакансии в БД
        """
        with psycopg2.connect(dbname=self.name, **self.params) as conn:
            with conn.cursor() as cur:
                for vacancy in vacancies:
                    cur.execute(
                        f"INSERT INTO vacancies(vacancy_name, salary, company_name, vacancy_url) values "
                        f"('{vacancy['vacancy_name']}', '{int(vacancy['salary'])}', "
                        f"'{vacancy['employer']}', '{vacancy['url']}')")
        conn.commit()
        conn.close()