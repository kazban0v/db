import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')  # Создаёт файл базы данных в текущей директории
    cursor = conn.cursor()

    # Создание таблицы, например, для хранения сообщений
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
