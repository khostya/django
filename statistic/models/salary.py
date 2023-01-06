currency_to_rub = {
    "AZN": 35.68,
    "BYR": 23.91,
    "EUR": 59.90,
    "GEL": 21.74,
    "KGS": 0.76,
    "KZT": 0.13,
    "RUR": 1,
    "UAH": 1.64,
    "USD": 60.66,
    "UZS": 0.0055,
}


class Salary:
    @staticmethod
    def parce(data: dict):
        salary_currency = data["salary_currency"]
        salary_from = float(data["salary_from"]) * currency_to_rub[salary_currency]
        salary_to = float(data["salary_to"]) * currency_to_rub[salary_currency]
        return Salary(salary_from, salary_to)

    def __init__(self, salary_from, salary_to):
        self.salary_from = salary_from
        self.salary_to = salary_to
