import requests
import json


class HeadHunterAPI:

    def __init__(self, name):
        self.all_vacancies: list = []
        self.name: str = name
        self.url: str = f'https://api.hh.ru/employers?{self.name}'

    def get_vacancies(self):
        params = {
            'text': f'NAME:{self.name}',
            'area': 113,
            'per_page': 100
        }
        response = requests.get(self.url, params=params)
        self.all_vacancies = json.loads(response.text)['items']
        return self.all_vacancies


test = HeadHunterAPI('Северсталь')
print(test.get_vacancies())
