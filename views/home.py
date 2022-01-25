from flask import render_template
from config import app
from models.category import Category


class HomeViews(object):

    @staticmethod
    @app.route('/')
    def index():
        return render_template('home/index.html', context={
            'page_title': 'Главная',
            'test_message': 'Проверка транзита данных',
            'categories_list': Category.get_all_categories()
        })
