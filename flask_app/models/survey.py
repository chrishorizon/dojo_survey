from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_survey(data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s)"

        return connectToMySQL('dojo_survey').query_db(query, data)

    @classmethod
    def get_survey():
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1"
        results = connectToMySQL('dojo_survey').query_db(query)

        return Survey(results[0])

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash('Name minimum of 3 characters')

        if len(survey['location']) < 1:
            is_valid = False
            flash('Must choose location')

        if len(survey['language']) < 1:
            is_valid = False
            flash('Must choose language')

        if len(survey['comments']) < 3:
            is_valid = False
            flash('Comment must be at least 6 characters')
        return is_valid