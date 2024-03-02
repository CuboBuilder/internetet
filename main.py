from flask import Flask, send_file, Response
import os

app = Flask(__name__)

# Список допустимых протоколов
VALID_PROTOCOLS = ['amogus', 'debilus']

@app.route('/')
def index():
    return "Добро пожаловать на интернетет!"

@app.route('/iperf/iperf:[<path:url>]')
def iperf(url):
    # Разбиваем URL на протокол и название файла
    parts = url.split('.')
    if len(parts) != 2:
        return "Некорректный формат URL. Используйте /iperf/iperf:[<file_name>.protocol]"

    file_name, protocol = parts[0], parts[1]

    # Проверяем допустимый протокол
    if protocol not in VALID_PROTOCOLS:
        return f"Недопустимый протокол: {protocol}"

    # Формируем путь к файлу
    file_path = os.path.join('iperf', f"{file_name}.{protocol}")

    # Проверяем существование файла
    if os.path.exists(file_path):
        # Открываем файл и считываем его содержимое
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        # Возвращаем содержимое файла как ответ с указанием типа контента
        return Response(file_content, mimetype='text/html')
    else:
        # Если файл не найден, возвращаем соответствующее сообщение
        return f"Файл '{file_name}.{protocol}' не найден для протокола '{protocol}'."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
