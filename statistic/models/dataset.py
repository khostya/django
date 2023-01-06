import csv
from statistic.models.vacancy import Vacancy


class DataSet:

    @staticmethod
    def csv_reader(file_name):
        f = open(file_name, encoding='utf-8-sig')
        vacancies = [row for row in csv.reader(f)]
        f.close()
        title = vacancies.pop(0)
        vacancies_dict = []
        for vacancy in vacancies:
            if len(vacancy) != len(title):
                continue
            if '' in vacancy:
                continue
            vacancy_dict = {}
            for index, param in enumerate(vacancy):
                vacancy_dict[title[index]] = param
            vacancies_dict.append(vacancy_dict)
        return vacancies_dict

    def __init__(self, file_name):
        self.file_name = file_name
        data_vacancies = DataSet.csv_reader(file_name)
        self.vacancies = []
        for data in data_vacancies:
            self.vacancies.append(Vacancy.parce(data))
