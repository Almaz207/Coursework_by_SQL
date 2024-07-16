from connection_by_api import random_requests
from connection_by_api import HHintegration

"""Нужны значения по ключам для записи в таблицу вакансий:
ключ: id  Значение: 103472558 - ид вакансии
ключ: name  Значение: Тестировщик ПО / QA Engineer -название вакансии
ключ: area  Значение: {'id': '78', 'name': 'Самара', 'url': 'https://api.hh.ru/areas/78'} - город вакансии
ключ: salary  Значение: {'from': 60000, 'to': 170000, 'currency': 'RUR', 'gross': False} - зарплата
address  Значение: {'city': 'Самара', 'street': 'улица Степана Разина', 'building': '134А', 'lat': 53.190424, 'lng': 50.
087473, 'description': None, 'raw': 'Самара, улица Степана Разина, 134А', 'metro': None, 'metro_stations': [],
'id': '545364'}  - полный адрес вакансии
ключ: alternate_url  Значение: https://hh.ru/vacancy/103472558 - ссылка на страницу вакансии
employer  Значение: {'id': '154832', 'name': 'VDcom', 'url': 'https://api.hh.ru/employers/154832', 
'alternate_url': 'https://hh.ru/employer/154832', 
'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/707756.png', 
'90': 'https://img.hhcdn.ru/employer-logo/3272140.png', '240': 'https://img.hhcdn.ru/employer-logo/3272141.png'},
 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=154832', 
 'accredited_it_employer': False, 'trusted': True} - описание работодателя
experience  Значение: {'id': 'between1And3', 'name': 'От 1 года до 3 лет'} - требуемый опыт

"""

# random_requests

class JodHandler:
    # random_requests = HHintegration().request_vacancy()
    @staticmethod
    def rewrite_vacancys(requests):
        all_vacancy = []
        for record in requests["items"]:
            rewriting_vacancy = {'id': record['id'], 'name': record['name'], 'area': record['area']['name'],
                                 'salary_from': record.get('salary', 'пустоблять'),
                                 'salary_to': record.get('salary', 'пустоблять'),
                                 'employer_id': record['employer']['id'],
                                 'employer_name': record['employer']['name'],
                                 'experience': record['experience']['name'],
                                 'requirement' : record['snippet']['requirement'],
                                 'responsibility':record['snippet']['responsibility'],
                                 'alternate_url': record['alternate_url']}
            # print(rewriting_vacancy)
            if rewriting_vacancy['salary_from'] != None:
                rewriting_vacancy['salary_from'] = rewriting_vacancy['salary_from']['from']
                rewriting_vacancy['salary_to'] = rewriting_vacancy['salary_to']['to']
            all_vacancy.append(rewriting_vacancy)
        return all_vacancy

jobsi = JodHandler().rewrite_vacancys(random_requests)
# for i in jobsi:
#     print(i)