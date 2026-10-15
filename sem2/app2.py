import json
import sys
from pathlib import Path

import psycopg2
from flask import Flask, render_template, request

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.select import select_list

app = Flask(__name__)
with (PROJECT_ROOT / 'data' / 'db_config.json').open(encoding='utf-8') as f:
    app.config['db_config'] = json.load(f)


@app.route('/', methods=['POST'])
def query_index():
    prod_param = request.form.get('prod_category', '').strip()
    if not prod_param:
        return render_template('input_category.html',
                               error_message='Введите категорию продуктов.'), 400
    _sql = """select prod_name, prod_measure, prod_price from product
              where prod_category = (%s)"""
    try:
        result = select_list(_sql, [prod_param])
    except psycopg2.Error:
        app.logger.exception('Ошибка запроса товаров')
        return render_template(
            'input_category.html',
            error_message='Не удалось подключиться к базе данных или выполнить запрос. '
                          'Проверьте настройки подключения и наличие таблицы product.'
        ), 503
    if result:
        prod_title = 'Результаты из БД'
        return render_template('dynamic.html', products=result, prod_title=prod_title)
    return render_template('input_category.html',
                           error_message='Нет товаров заданной категории')


@app.route('/', methods=['GET'])
def get_param():
    return render_template('input_category.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=True)
