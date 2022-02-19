from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def root():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    text = """Человечество вырастает из детства.</br>

Человечеству мала одна планета.</br>

Мы сделаем обитаемыми безжизненные пока планеты.</br>

И начнем с Марса!</br>

Присоединяйся!</br>"""
    return text


@app.route('/promotion_image')
def promotion_image():
    img = url_for('static', filename='img/mars.jpg')
    styles = url_for('static', filename='css/style.css')
    return render_template('index.html', img=img, style=styles)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        styles = url_for('static', filename='css/style.css')
        return render_template('form.html', style=styles)
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')