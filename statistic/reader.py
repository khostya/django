from statistic.models.dataset import DataSet


def get_vacancies_by_names(filename, names):
    vacancies = DataSet(filename).vacancies
    return [x for x in vacancies if [name in x.name for name in names]]


def get_vacancies(filename):
    vacancies = DataSet(filename).vacancies
    return vacancies

