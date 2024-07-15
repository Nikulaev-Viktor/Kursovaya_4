import requests
from src.abstract_classes import Api


class HeadHunter(Api):

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.vacancies = []

    def get_vacancies(self, keyword):
        """Метод для отправки запроса на API и получения списка вакансий в формате json"""

        response = requests.get(self.url, params={'text': keyword, 'area': '113', 'per_page': 100})
        vacancies = response.json()['items']
        return vacancies
