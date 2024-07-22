class JodHandler:

    @staticmethod
    def rewrite_vacancys(requests):
        all_vacancy = []
        test = 0
        rewriting_vacancy = {}
        for record in requests['items']:
            rewriting_vacancy = {'id': record['id'], 'name': record['name'], 'area': record['area']['name'],
                                 'salary_from': record.get('salary'),
                                 'salary_to': record.get('salary'),
                                 'employer_id': record['employer']['id'],
                                 'employer_name': record['employer']['name'],
                                 'experience': record['experience']['name'],
                                 'requirement': record['snippet']['requirement'],
                                 'responsibility': record['snippet']['responsibility'],
                                 'alternate_url': record['alternate_url']}

            rewriting_vacancy['salary_from'] = rewriting_vacancy['salary_from']['from'] if rewriting_vacancy[
                'salary_from'] else 0

            rewriting_vacancy['salary_to'] = rewriting_vacancy['salary_to']['to'] if rewriting_vacancy[
                'salary_to'] else 0

            rewriting_vacancy['salary_to'] = 0 if rewriting_vacancy['salary_to'] == None else rewriting_vacancy[
                'salary_to']

            rewriting_vacancy['salary_from'] = 0 if rewriting_vacancy['salary_from'] == None else rewriting_vacancy[
                'salary_from']

            rewriting_vacancy['requirement'] = "Ничегошенки тут нет" if rewriting_vacancy['requirement'] == None else \
                rewriting_vacancy['requirement']

            rewriting_vacancy['responsibility'] = "Ничегошенки тут нет" if rewriting_vacancy['responsibility'] == None else \
                rewriting_vacancy['requirement']

            all_vacancy.append(rewriting_vacancy)
        return all_vacancy
