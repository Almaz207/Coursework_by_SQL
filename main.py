from work_with_vacancy import JodHandler
from connection_by_api import HHintegration
from work_with_DataBase import DataBase
from DBclass import DBManager

hh_url = "https://api.hh.ru/vacancies"
employer_id = ['1272486', '3529', '154832', '665470', '139', '3754394', '817892', '241845', '3095', '8550', '1440117']
conn_params = {'database': 'vacancyfromhhru',
               'user': 'postgres',
               'password': '234567',
               'host': 'localhost',
               }
if __name__ == '__main__':
    print("Привет, давай посмотрим вакансии интересных тебе компаний")
    DataBase().employer_database()
    DataBase().vacancy_database()

    vacancy = []
    list_record_employer = []
    for i in range(6):
        list_employer = JodHandler().writing_employer(HHintegration(hh_url, employer_id, i).request_vacancy())
        list_record_employer.append(list_employer)
        list_vacancy = JodHandler().rewrite_vacancys(HHintegration(hh_url, employer_id, i).request_vacancy())
        vacancy.append(list_vacancy)

    employers = []
    for list_employers in list_record_employer:
        for record in list_employers:
            if (record not in employers) and (type(record) == dict):
                employers.append(record)
            else:
                continue
    DataBase().write_employer(employers)
    DataBase().write_vacancy(vacancy)
    print("""Я могу:
    1 -показать список всех компаний и количество вакансий у каждой компании
    2 -показать список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
    3 -показать среднюю зарплату по вакансиям
    4 -показать список всех вакансий, у которых зарплата выше средней по всем вакансиям
    5 -показать список всех вакансий, в названии которых содержатся переданные в метод слова, например python
    Просто введи номер подходящего варианта
    Для того чтобы завершить работу программы введи слово: "Завершить" 
    """)
    while True:
        user_input = input()
        if user_input == "1":
            answer = DBManager(conn_params).get_companies_and_vacancies_count()
            print("Cписок всех компаний и количество вакансий у каждой компании:")
            for key, value in answer.items():
                print(f" {key} -  {value}")
        elif user_input == "2":
            answer = DBManager(conn_params).get_all_vacancies()
            print("Cписок всех вакансий с указанием названия компании, вакансии, зарплаты и ссылки на вакансию:")
            num = 1
            for i in answer:
                print(f"{num} - {i}")
                num += 1
        elif user_input == "3":
            print("Cредняя зарплата по вакансиям:")
            answer = DBManager(conn_params).get_avg_salary()
            print(round(answer))
        elif user_input == "4":
            print("Список всех вакансий, у которых зарплата выше средней по всем вакансиям. "
                  "Компания, должность, зарплата от, зарплата до, ссылка на вакансию:")
            answer = DBManager(conn_params).get_vacancies_with_higher_salary()
            for i in answer:
                print(i)
        elif user_input == "5":
            keyword = input("Ведите ключевое слово   ")
            answer = DBManager(conn_params).get_vacancies_with_keyword(keyword)
            for i in answer:
                print(i)
        elif user_input == "Завершить":
            break
        else:
            print("Не могу разобрать ответ")
