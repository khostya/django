import os
from statistic.reader import get_vacancies_by_names
from statistic.demand import show
from collections import defaultdict


def by_skills(vacancies):
    for year in range(2015, 2023):
        skills_dict = defaultdict(int)
        for vacancy in vacancies:
            if vacancy.published_at.split('-')[0] != str(year):
                continue
            for skill in vacancy.skills:
                skills_dict[skill] += 1
        skills = list(skills_dict.keys())
        skills.sort(key=lambda x: skills_dict[x], reverse=True)
        skills = skills[:10]
        count = [skills_dict[skill] for skill in skills]
        show(skills, count,
             'ТОП-10 навыков по годам для профессии инженер-программист. ' + str(year) + ' год', 'Частотность', 'Навык')


def main():
    names = ['engineer', 'инженер программист', 'інженер', 'it инженер', 'инженер разработчик']
    filename = os.path.join("data", "vacancies_with_skills.csv")
    vacancies = get_vacancies_by_names(filename, names)
    by_skills(vacancies)


if __name__ == '__main__':
    main()
