from os import path

import psycopg2
from flask import Blueprint, current_app, render_template, request

from database.sql_provvider import SqlProvider
from query_bp.model_route import model_route

blueprint_query = Blueprint('query_bp', __name__, template_folder='template')
provider = SqlProvider(path.join(path.dirname(__file__), 'sql'))


@blueprint_query.route('/', methods=['GET'])
def request_handler():
    return render_template('input_category.html')


@blueprint_query.route('/', methods=['POST'])
def query_handler():
    try:
        res_info = model_route(request.form, provider)
    except (psycopg2.Error, OSError, ValueError):
        current_app.logger.exception('Ошибка запроса товаров по категории')
        return render_template(
            'input_category.html',
            error_message=(
                'Не удалось подключиться к базе данных или выполнить запрос. '
                'Проверьте настройки подключения и наличие таблицы product.'
            ),
        ), 503

    if res_info.status:
        prod_title = 'Результат из БД'
        return render_template(
            'dynamic.html', products=res_info.result, prod_title=prod_title
        )
    return render_template('input_category.html', error_message=res_info.error_message)
