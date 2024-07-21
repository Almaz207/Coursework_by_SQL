import requests

hh_url = "https://api.hh.ru/vacancies"
employers_id = ['8550', '241845', '3095', '78638', '665470', '154832', '1440117', '1440117']


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

# for i in range(10):
#     print(i)
#     random_requests = HHintegration(hh_url, employers_id,i).request_vacancy()
#     print(random_requests)
#     print(random_requests['items'])
