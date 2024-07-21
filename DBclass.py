import requests
import psycopg2
from work_with_vacancy import JodHandler
from connection_by_api import HHintegration
from work_with_DataBase import DataBase

hh_url = "https://api.hh.ru/vacancies"
employer_id = ['8550', '241845', '3095', '78638', '665470', '154832', '1440117', '1440117']

first_request = HHintegration(hh_url, employer_id,3).request_vacancy()
jobsi = JodHandler().rewrite_vacancys(first_request)

"""id_vacancy int PRIMARY KEY,
                        name text NOT NULL,
                        area text,
                        salary_from int,
                        salary_to int,
                        employer_id int,
                        employer_name text,
                        experience text,
                        requirement text,
                        responsibility text,
                        alternate_url text"""

class DBManager:
    def __init__(self,params):
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        query = """SELECT employer_name, COUNT(*)
FROM vacancy_information
GROUP BY employer_name;
        """
        self.cur.execute(query)

        return {row[0] : row[1] for row in self.cur.fetchall()}


    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        query = """SELECT employer_name, name, salary_from, salary_to,alternate_url
        FROM vacancy_information
                """
        self.cur.execute(query)
        return self.cur.fetchall()


    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        query = """SELECT AVG(salary_from) FROM vacancy_information"""
        self.cur.execute(query)
        return self.cur.fetchone()[0]

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        query = """SELECT employer_name, name, salary_from, salary_to,alternate_url
                FROM vacancy_information
                WHERE salary_from > (SELECT AVG(salary_from) FROM vacancy_information)"""
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""
        query = """SELECT employer_name, name, salary_from, salary_to,alternate_url
                    FROM vacancy_information
                    WHERE LOWER(name) LIKE %s"""
        self.cur.execute(query,('%'+keyword.lower()+'%',))
        return self.cur.fetchall()

conn_params = {'database': 'vacancyfromhhru',
                   'user': 'postgres',
                   'password': '234567',
                   'host': 'localhost',
                   }
# DB_request = DBManager(conn_params).get_vacancies_with_keyword('')
# print(DB_request)