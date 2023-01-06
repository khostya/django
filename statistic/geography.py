from statistic.reader import get_vacancies_by_names
from collections import defaultdict
from statistic.demand import show
import os


def by_city(vacancies):
    city_dict = defaultdict(int)
    count = len(vacancies)
    for vacancy in vacancies:
        city_dict[vacancy.area_name] += 1

    cities = list(city_dict.keys())
    cities.sort(key=lambda city: city_dict[city]/count, reverse=True)
    cities = cities[:10]
    city_percentage = [city_dict[city]/count for city in cities]
    show(cities, city_percentage, 'Доля вакансий по городам (в порядке убывания)', 'Доля вакансий')


def average_salary(vacancies):
    s = sum([(vacancy.salary.salary_from + vacancy.salary.salary_to) / 2 for vacancy in vacancies])
    return int(s / len(vacancies))


def by_salary(vacancies):
    city_dict = {}
    count = len(vacancies)
    for vacancy in vacancies:
        if vacancy.area_name not in city_dict:
            city_dict[vacancy.area_name] = []
        city_dict[vacancy.area_name].append(vacancy)
    city_dict = dict(filter(lambda x: len(x[1])/count >= 0.01, city_dict))
    for city in city_dict.keys():
        city_dict[city] = average_salary(city_dict[city])
    cities = list(city_dict.keys())
    cities.sort(key=lambda city: city_dict[city], reverse=True)
    cities = cities[:10]
    salaries = [city_dict[city] for city in cities]
    show(cities, salaries, 'Уровень зарплат по городам (в порядке убывания)', 'Средняя зарплата')


def main():
    names = ['engineer', 'инженер программист', 'інженер', 'it инженер', 'инженер разработчик']
    filename = os.path.join("data", "vacancies_with_skills.csv")
    vacancies = get_vacancies_by_names(filename, names)
    by_salary(vacancies)
    by_city(vacancies)


if __name__ == '__main__':
    main()
