import json
import sys
from pathlib import Path

from flask import Flask, render_template

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if __package__ in (None, ''):
    sys.path.insert(0, str(PROJECT_ROOT))

from query_bp.route import blueprint_query

app = Flask(__name__)
app.register_blueprint(blueprint_query, url_prefix='/query')

with (PROJECT_ROOT / 'data' / 'db_config.json').open(encoding='utf-8') as f:
    app.config['db_config'] = json.load(f)


@app.route('/')
def main_menu():
    return render_template('internal_user_menu.html')


@app.route('/exit')
def exit_func():
    return 'До свидания'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5004, debug=True)
