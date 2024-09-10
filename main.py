from flask import Flask, render_template, request, jsonify
import sqlite3
import requests

app = Flask(__name__, static_folder='assets')

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Замените на ваш токен бота и чат ID
TELEGRAM_BOT_TOKEN = '7338152653:AAGqu4B1VZU3-JC0WEE9k7axQRIAx2LLSPQ'
CHAT_ID = '855861024'

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=payload)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('полное имя')
    email = request.form.get('электронная почта')
    message = request.form.get('сообщение')

    # Сохранение в базе данных
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)',
                   (name, email, message))
    conn.commit()
    conn.close()

    # Отправка сообщения в Telegram
    telegram_message = f"Новое сообщение:\nИмя: {name}\nEmail: {email}\nСообщение: {message}"
    send_telegram_message(telegram_message)

    return jsonify({'status': 'Сообщение отправлено успешно'})

if __name__ == '__main__':
    app.run(debug=True)
