import psycopg2


class DataBase:

    conn_params = {'database': 'vacancyfromhhru',
                   'user': 'postgres',
                   'password': '234567',
                   'host': 'localhost'
                   }

    @staticmethod
    def vacancy_database(conn_params):
        try:
            with psycopg2.connect(**conn_params) as conn:
                with conn.cursor() as cur:
                    create_table = """CREATE TABLE vacancy_information
                    (       id_vacancy int PRIMARY KEY,
                            name text NOT NULL,
                            area text,
                            salary_from int,
                            salary_to int,
                            employer_id int REFERENCES employer_information(employer_id),
                            employer_name text,
                            experience text,
                            requirement text,
                            responsibility text,
                            alternate_url text   );"""
                    cur.execute(create_table)
            conn.close()
        except:
            with psycopg2.connect(**conn_params) as conn:
                with conn.cursor() as cur:
                    create_table = """CREATE TABLE vacancy_information
                        (   id_vacancy int PRIMARY KEY,
                            name text NOT NULL,
                            area text,
                            salary_from int,
                            salary_to int,
                            employer_id int REFERENCES employer_information(employer_id),
                            employer_name text,
                            experience text,
                            requirement text,
                            responsibility text,
                            alternate_url text   );"""
                    cur.execute("DROP TABLE vacancy_information CASCADE")
                    cur.execute(create_table)
            conn.close()

    @staticmethod
    def employer_database(conn_params):
        try:
            with psycopg2.connect(**conn_params) as conn:
                with conn.cursor() as cur:
                    create_table = """CREATE TABLE employer_information
                    (   employer_id int PRIMARY KEY,
                        employer_name text NOT NULL   );"""
                    cur.execute(create_table)
            conn.close()
        except:
            with psycopg2.connect(**conn_params) as conn:
                with conn.cursor() as cur:
                    create_table = """CREATE TABLE employer_information
                        (   employer_id int PRIMARY KEY,
                            employer_name text NOT NULL   );"""
                    cur.execute("DROP TABLE employer_information CASCADE")
                    cur.execute(create_table)
            conn.close()

    @staticmethod
    def write_employer(list_employer, conn_params):
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                if type(list_employer) is list:
                    for record in list_employer:
                        try:
                            empl_to_db = (int(record['employer_id']), record['employer_name'])
                            cur.execute(f"""INSERT INTO employer_information (employer_id, employer_name)
                            VALUES {empl_to_db}""")



                        except:
                            print("Какя-то фигня, обратитесь в тех поддержку)")

        conn.close()

    @staticmethod
    def write_vacancy(list_vacancy, conn_params):
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                for vacancy in list_vacancy:
                    if vacancy != None:
                        for record in vacancy:
                            try:
                                vacancy_to_db = (int(record['id']), str(record['name']), record['area'],
                                                 int(record['salary_from']), int(record['salary_to']),
                                                 int(record['employer_id']), record['employer_name'],
                                                 record['experience'],
                                                 record['requirement'],
                                                 record['responsibility'], record['alternate_url'])
                                cur.execute(f"""INSERT INTO vacancy_information (id_vacancy, name, area, salary_from, 
                                salary_to, employer_id, employer_name, experience, requirement, responsibility,
                                alternate_url)
                                VALUES {vacancy_to_db};""")


                            except:
                                print("Какя-то фигня, обратитесь в тех поддержку)")

        conn.close()
