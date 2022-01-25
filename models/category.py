from config import db


class Category(object):

    @staticmethod
    def get_all_categories() -> list:
        result = db.categories.find()
        categories = [x for x in result]
        return categories
