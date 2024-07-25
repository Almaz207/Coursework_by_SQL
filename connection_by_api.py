import requests

hh_url = "https://api.hh.ru/vacancies"
employers_id = ['1272486', '3529', '154832', '665470', '139', '3754394', '817892', '241845', '3095', '8550', '1440117']


class HHintegration:

    def __init__(self, url, employer_id, page=0):
        self.url = url
        self.employer_id = employer_id
        self.page = page

    def request_vacancy(self):
        """Метод для выполнения запроса. При инициализации передаётся список вакансий"""

        params_request = {
            'employer_id': self.employer_id,
            'area': '78',
            'page': self.page,
            'per_page': 90
        }

        response = requests.get(url=self.url, params=params_request)

        return response.json()
