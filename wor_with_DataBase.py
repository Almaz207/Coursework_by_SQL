import psycopg2
from work_with_vacancy import JodHandler
from connection_by_api import HHintegration


# list_key = ['id', 'name', 'area', 'salary', 'employer', 'experience', 'alternate_url']
# rewriting_vacancy = {}
# for key in list_key:
#     if record[key]:
#         rewriting_vacancy[key] = record[key]
#     else:
#         rewriting_vacancy[key] = 'пусто'
# print(rewriting_vacancy)
"""Кусок выше помог мне переписать список так, чтобы все занчения не были пустыми"""

hh_url = "https://api.hh.ru/vacancies"
employer_id = ['8550', '241845', '3095', '78638', '665470', '154832', '1440117', '1440117']
first_request = HHintegration(hh_url,employer_id).request_vacancy()
jobsi = JodHandler().rewrite_vacancys(first_request)
# for i in jobsi:
#     print(i)
#{'id', 'name', 'area', 'salary_from','salary_to', 'employer_id''employer_name' 'experience', 'requirement', 'responsibility', 'alternate_url'}
# list_key = ['id', 'name', 'area', 'salary', 'employer', 'experience', 'alternate_url']
conn_params={
    'host': 'localhost',
    'database': 'vacancyfromhhru',
    'user': 'PostgreSQL',
    'password': '234567'}

with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        create_table = """CREATE TABLE VACANCY_INFORMATION(
        ID_VACANCY INT PRIMARY KEY,
        NAME VARCHAR(100) NOT NULL,
        AREA VARCHAR(150),
        SALARY_FROM INT2,
        SALARY_TO INT2,
        EMPLOYER_ID INT,
        EMPLOYER_NAME VARCHAR(100),
        EXPERIENCE VARCHAR(30),
        REQUIREMENT TEXT,
        RESPONSIBILITY TEXT,
        ALTERNATE_URL TEXT
        );
        """
        cur.execute(create_table)
        cur.close()
    conn.commit()
conn.close()
# conn = psycopg2.connect( **conn_params)
# conn.autocommit = True
# with conn.cursor() as cur:
#     cur.execute("DROP DATABASE IF EXISTS VACANCY_INFORMATION")
#     cur.execute("""CREATE DATABASE VACANCY_INFORMATION
#                         WITH OWNER "PostgreSQL"
#                         ENCODING 'UTF8'
#                         LC_COLLATE = 'ru_RU.UTF-8'
#                         LC_CTYPE = 'ru_RU.UTF-8'
#                         TEMPLATE = template0;""")
#
# conn.close()
