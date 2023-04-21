# импорт пайтоновских либ
import logging
import random

# импорт Flask
from flask import Flask, jsonify
from flask_cors import CORS

# создаём logger для приложения
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("application")

# инициализируем приложение
app = Flask(__name__)
CORS(app)

# создаём генератор рандома, читаем цитаты из файла
random.seed()
quotes = []
with open("quotes.csv", "r", encoding="utf-8") as F:
    quotes = F.readlines()


# роутинг маршрута /api
@app.route('/api', methods=['GET'])
def api():
    try:
        data = random.choice(quotes).split(";") # выбираем случайную цитату (строчку), сплитим по ;
        return jsonify({
            "text": data[0],
            "author": data[1]
        })
    except Exception as e:  # обрабатываем любые ошибки, возращаем как JSON
        logger.error("/api:" + f'"{str(e)}"')
        return jsonify(error=str(e)), 500
