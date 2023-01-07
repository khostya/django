import os
from reader import get_vacancies_by_names, get_vacancies
from collections import defaultdict
import matplotlib.pyplot as plt


def show(x, y, title, ylabel, xlabel='Год'):
    fig, ax = plt.subplots(figsize=(16, 10), facecolor='white', dpi=80)
    ax.bar(x, y, width=0.5, linewidth=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def average_salary(vacancies):
    s = sum([(vacancy.salary.salary_from + vacancy.salary.salary_to) / 2 for vacancy in vacancies])
    return int(s / len(vacancies))


def by_salary(vacancies, title):
    year_dict = defaultdict(list)
    for vacancy in vacancies:
        year = int(vacancy.published_at.split('-')[0])
        year_dict[year].append(vacancy)

    years = list(year_dict.keys())
    years.sort()
    salaries = [average_salary(year_dict[year]) for year in years]
    show(years, salaries, title, 'Средняя зарплата')


def by_count(vacancies, title):
    year_dict = defaultdict(int)
    for vacancy in vacancies:
        year = int(vacancy.published_at.split('-')[0])
        year_dict[year] += 1
    years = list(year_dict.keys())
    years.sort()
    count = [year_dict[year] for year in years]
    show(years, count, title, 'Количество')


def main():
    names = ['engineer', 'инженер программист', 'інженер', 'it инженер', 'инженер разработчик']
    filename = os.path.join("data", "vacancies_with_skills.csv")

    vacancies = get_vacancies(filename)
    vacancies_by_names = [x for x in vacancies if any([name in x.name for name in names])]

    by_count(vacancies, 'Динамика количества вакансий по годам.')
    by_count(vacancies_by_names, 'Динамика количества вакансий по годам для профессии Инженер-программист')

    by_salary(vacancies, 'Динамика уровня зарплат по годам')
    by_salary(vacancies_by_names, 'Динамика уровня зарплат по годам для профессии Инженер-программист')


if __name__ == '__main__':
    main()
