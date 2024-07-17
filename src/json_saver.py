from src.abstract_classes import AbstractJson
import json


class JsonSaver(AbstractJson):

    """Класс сохранения вакансий в файл"""

    def save_vacancies(self, vacancies):

        """Метод для записи списка вакансий в файл"""
        with open("./data/vacancies.json", "w", encoding="utf8") as f:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False)
            f.write(vacancies_json)

    def get_data(self, criterion):

        """Метод получения данных из файла по указанным критериям"""

        with open("./data/vacancies.json", "r", encoding="utf8") as f:
            vacancies = json.load(f)
            criterion_vac = []
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:  # требования
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac

    def delete_vacancy(self):

        """Метод удаления данных из файла"""

        list_vacancies_del = []
        list_ = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open("./data/vacancies.json", "w", encoding="utf8") as f:
            f.write(list_)
