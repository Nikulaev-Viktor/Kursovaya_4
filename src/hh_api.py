import requests
from src.abstract_classes import Api


class HeadHunter(Api):

    """Класс для работы с сайтом HeadHunter"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        # self.vacancies = []

    def get_vacancies(self, name_vac):

        """Метод для отправки запроса на API и получения списка вакансий в формате json"""

        response = requests.get(self.url, headers=self.headers, params={'text': f'NAME:{name_vac}', 'area': '113', 'per_page': 100})
        vacancies = response.json()['items']
        return vacancies
