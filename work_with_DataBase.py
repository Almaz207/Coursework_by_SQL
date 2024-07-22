import psycopg2
from work_with_vacancy import JodHandler
from connection_by_api import HHintegration

hh_url = "https://api.hh.ru/vacancies"
employer_id = ['8550', '241845', '3095', '78638', '665470', '154832', '1440117', '1440117']
# for employer_id in employer_idiii:
# first_request = HHintegration(hh_url, employer_id,3).request_vacancy()
# jobsi = JodHandler().rewrite_vacancys(first_request)

class DataBase:
    conn_params = {'database': 'vacancyfromhhru',
                   'user': 'postgres',
                   'password': '234567',
                   'host': 'localhost',
                   }
    def cerate_database(self):

        with psycopg2.connect(**DataBase.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("DROP TABLE vacancy_information")
                create_table = """CREATE TABLE vacancy_information
                (
                        id_vacancy int PRIMARY KEY,
                        name text NOT NULL,
                        area text,
                        salary_from int,
                        salary_to int,
                        employer_id int,
                        employer_name text,
                        experience text,
                        requirement text,
                        responsibility text,
                        alternate_url text
                );"""
                cur.execute(create_table)
        conn.close()
    def write_data(self,list_vacancy):
        with psycopg2.connect(**DataBase.conn_params) as conn:
            with conn.cursor() as cur:
                for i in list_vacancy:
                    vacancy_to_db = (
                    int(i['id']), str(i['name']), i['area'], int(i['salary_from']), int(i['salary_to']),
                    int(i['employer_id']), i['employer_name'], i['experience'], i['requirement'],
                    i['responsibility'], i['alternate_url'])
                    cur.execute(f"""INSERT INTO vacancy_information (id_vacancy, name, area, salary_from, salary_to,
                    employer_id, employer_name, experience, requirement, responsibility, alternate_url)
                    VALUES {vacancy_to_db}""")
        conn.close()






