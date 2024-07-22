import psycopg2


class DBManager:
    def __init__(self, params):
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        query = """SELECT employer_name, COUNT(*)
FROM vacancy_information
GROUP BY employer_name;
        """
        self.cur.execute(query)

        return {row[0]: row[1] for row in self.cur.fetchall()}

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
        self.cur.execute(query, ('%' + keyword.lower() + '%',))
        return self.cur.fetchall()
