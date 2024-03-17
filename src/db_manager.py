class DBManager:
    def __init__(self, cur):
        self.cur = cur

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        self.cur.execute('SELECT companies.company_name, COUNT(vacancies.vacancy_id) '
                         'FROM companies '
                         'LEFT JOIN vacancies ON companies.company_name = vacancies.company_name '
                         'GROUP BY companies.company_name'
                         )
        answer = self.cur.fetchall()

        return answer

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии
                    и зарплаты и ссылки на вакансию.
        """
        self.cur.execute('SELECT * from vacancies')
        answer = self.cur.fetchall()

        return answer

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.
        """
        self.cur.execute('SELECT AVG(salary) from vacancies')
        answer = self.cur.fetchall()

        return answer

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        self.cur.execute('SELECT vacancy_name from vacancies WHERE salary > '
                         '(SELECT AVG(salary) from vacancies)')
        answer = self.cur.fetchall()

        return answer

    def get_vacancies_with_keyword(self, string):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например "аналитик".
        """
        self.cur.execute(f"SELECT * FROM vacancies WHERE vacancy_name LIKE '%{string}%'")
        answer = self.cur.fetchall()

        return answer
