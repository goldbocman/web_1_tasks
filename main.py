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


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    styles = url_for('static', filename='css/style.css')
    if request.method == 'GET':
        img = url_for('static', filename='img/loaded_photo.png')
        return render_template('image_form.html', img=img, style=styles)
    elif request.method == 'POST':
        f = request.files['file']
        with open('static//img//loaded_photo.png', 'wb') as photo:
            photo.write(f.read())
        return "Форма отправлена"


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
    <title>Слайды</title>
</head>
<body>
<div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active" data-bs-interval="2000">
      <img src="{url_for('static', filename='img/mars4.jpg')}" class="d-block w-100" alt="марс">
    </div>
    <div class="carousel-item" data-bs-interval="2000">
      <img src="{url_for('static', filename='img/mars5.jpg')}" class="d-block w-100" alt="марс">
    </div>
    <div class="carousel-item" data-bs-interval="2000">
      <img src="{url_for('static', filename='img/mars3.jpg')}" class="d-block w-100" alt="марс">
    </div>
    <div class="carousel-item" data-bs-interval="2000">
      <img src="{url_for('static', filename='img/mars2.jpg')}" class="d-block w-100" alt="марс">
    </div>
    <div class="carousel-item" data-bs-interval="2000">
      <img src="{url_for('static', filename='img/mars.jpg')}" class="d-block w-100" alt="марс">
    </div>
  </div>
</div>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')