import random

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


@app.route('/choice/<planet_name>')
def choice(planet_name):
    styles = url_for('static', filename='css/style.css')
    if planet_name.lower() == 'земля':
        return render_template('zemlya.html', planet=planet_name, style=styles)
    elif planet_name.lower() == 'марс':
        return render_template('mars.html', planet=planet_name, style=styles)
    else:
        return render_template('another_planet.html', planet=planet_name, style=styles)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    styles = url_for('static', filename='css/style.css')
    return render_template('results.html', nickname=nickname, level=level, rating=rating, style=styles)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')