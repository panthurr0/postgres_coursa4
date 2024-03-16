import json
import os

from config import DATA


class JSONSaver:
    def save_vacancies(self, vacancies):
        """
        Записывает вакансии в файл
        :param vacancies: вакансии list
        """
        with open(DATA, 'w', encoding='utf-8') as f:
            f.write(json.dumps(vacancies, indent=2, ensure_ascii=False))

    def delete_vacancies(self):
        """
        Удаляет файл с вакансиями
        """
        os.remove(DATA)

    @staticmethod
    def read_file():
        with open(DATA, encoding='utf-8') as f:
            return json.load(f)

    def delete_vacancy(self, vacancy):
        """
        Пересоздает файл без указанной vacancy
        :param vacancy: название вакансии
        """
        new_list = []
        old_list = self.read_file()

        for params in old_list:
            if params['name'] != vacancy:
                new_list.append(params)

        self.save_vacancies(new_list)
