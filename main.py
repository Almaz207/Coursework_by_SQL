import requests
import psycopg2
from work_with_vacancy import JodHandler
from connection_by_api import HHintegration
from work_with_DataBase import DataBase
from DBclass import DBManager

hh_url = "https://api.hh.ru/vacancies"
employer_id = ['8550', '241845', '3095', '78638', '665470', '154832', '1440117', '1440117']
conn_params = {'database': 'vacancyfromhhru',
                   'user': 'postgres',
                   'password': '234567',
                   'host': 'localhost',
                   }
if __name__== '__main__':
    print("Привет, давай посмотрим вакансии интересных тебе компаний")
    DataBase().cerate_database()
    for i in range(4):
        list_vacancy = JodHandler().rewrite_vacancys(HHintegration(hh_url, employer_id, i).request_vacancy())
        DataBase().write_data(list_vacancy)
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
                num +=1
        elif user_input == "3":
            print("Cредняя зарплата по вакансиям:")
            answer = DBManager(conn_params).get_avg_salary()
            print(round(answer))
        elif user_input == "4":
            print(
                "Список всех вакансий, у которых зарплата выше средней по всем вакансиям. Компания, должность, зарплата от, зарплата до, ссылка на вакансию(учитывается только зарплата в рублях):")
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