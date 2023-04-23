# импорт pure Python библиотек
import random

# импорт Flask
from flask import Flask, jsonify
# импорт Flask-Cors
from flask_cors import CORS

# инициализируем приложение
APP = Flask(__name__)
CORS(APP)

# создаём генератор рандома, читаем цитаты из файла
random.seed()
with open('quotes.csv', 'r', encoding='utf-8') as F:
    quotes = F.readlines()


# роутинг маршрута /api
@APP.route('/api', methods=['GET'])
def send_quote():
    try:
        data = random.choice(quotes).split(';')  # выбираем случайную цитату (строчку), сплитим по ;
        return jsonify({
            'text': data[0],
            'author': data[1]
        })
    except Exception as e:  # обрабатываем любые ошибки, возвращаем как JSON
        APP.logger.error('route /api - ' + '"{}"'.format(e))
        return jsonify(error=str(e)), 500
