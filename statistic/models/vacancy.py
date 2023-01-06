from statistic.models.salary import Salary


class Vacancy:
    @staticmethod
    def parce(data: dict):
        name = data["name"]
        salary = Salary.parce(data)
        area_name = data["area_name"]
        published_at = data["published_at"]
        skills = data["key_skills"].split("\n")
        return Vacancy(name, salary, area_name, published_at, skills)

    def __init__(self, name, salary: Salary, area_name, published_at, skills):
        self.name = name
        self.salary = salary
        self.area_name = area_name
        self.published_at = published_at
        self.skills = skills
