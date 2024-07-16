import requests

hh_url = "https://api.hh.ru/vacancies"
employer_id = ['8550', '241845', '3095', '78638', '665470', '154832', '1440117', '1440117']
class HHintegration:

    def __init__(self, hh_url, employer_id):
        self.hh_url = hh_url
        self.employer_id = employer_id

    def request_vacancy(self):
        """Метод для выполнения запроса. При инициализации передаётся список вакансий"""
        params_request = {
            'employer_id': self.employer_id,
            'area': '78',
            'page': 0,
            'per_page': 90
        }
        response = requests.get(url=self.hh_url, params=params_request)
        return response.json()


random_requests=HHintegration(hh_url, employer_id).request_vacancy()
# print(random_requests)
